"""
SIRIUS Runtime 5.1.0 – Runtime Integrity Engine 1.0
Checksum Validator

Účel:
- overiť integritu modulov pomocou kontrolných súčtov
- detegovať zmenené / poškodené súbory
- pripraviť podklady pre Self‑Repair Layer
"""

import hashlib
import json
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any


CHECKSUM_ALGO = "sha256"


@dataclass
class ChecksumEntry:
    path: str
    checksum: str


class ChecksumValidator:
    """
    Validator kontrolných súčtov pre runtime moduly.

    Pracuje s referenčným manifestom:
    - manifest obsahuje zoznam súborov a ich checksum
    - validator porovná aktuálny stav s manifestom
    """

    def __init__(self, base_path: str, manifest_path: str, logger):
        """
        base_path     – koreňový priečinok runtime (napr. /src)
        manifest_path – cesta k JSON manifestu s checksumami
        logger        – Logging5 / RepairLogger
        """
        self.base_path = base_path
        self.manifest_path = manifest_path
        self.logger = logger
        self.manifest: Dict[str, str] = {}

        self._load_manifest()

    # ---------------------------------------------------------
    # MANIFEST
    # ---------------------------------------------------------

    def _load_manifest(self) -> None:
        if not os.path.exists(self.manifest_path):
            self.logger.warning(
                "ChecksumValidator: manifest not found",
                extra={"manifest_path": self.manifest_path}
            )
            self.manifest = {}
            return

        try:
            with open(self.manifest_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # očakávame formát: { "relative/path.py": "checksum", ... }
                self.manifest = data
                self.logger.info(
                    "ChecksumValidator: manifest loaded",
                    extra={"entries": len(self.manifest)}
                )
        except Exception as e:
            self.logger.exception(
                "ChecksumValidator: failed to load manifest",
                extra={"error": str(e)}
            )
            self.manifest = {}

    def save_manifest(self) -> None:
        """
        Uloží aktuálny manifest (napr. po regenerácii).
        """
        try:
            with open(self.manifest_path, "w", encoding="utf-8") as f:
                json.dump(self.manifest, f, indent=2, sort_keys=True)
            self.logger.info(
                "ChecksumValidator: manifest saved",
                extra={"entries": len(self.manifest)}
            )
        except Exception as e:
            self.logger.exception(
                "ChecksumValidator: failed to save manifest",
                extra={"error": str(e)}
            )

    # ---------------------------------------------------------
    # CHECKSUM CALCULATION
    # ---------------------------------------------------------

    def _calc_checksum(self, full_path: str) -> Optional[str]:
        """
        Vypočíta checksum súboru.
        """
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            return None

        h = hashlib.new(CHECKSUM_ALGO)
        try:
            with open(full_path, "rb") as f:
                for chunk in iter(lambda: f.read(8192), b""):
                    h.update(chunk)
            return h.hexdigest()
        except Exception as e:
            self.logger.exception(
                "ChecksumValidator: failed to calculate checksum",
                extra={"path": full_path, "error": str(e)}
            )
            return None

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def validate_module(self, module_rel_path: str) -> Dict[str, Any]:
        """
        Overí integritu všetkých súborov v module (relatívna cesta od base_path).

        Výstup:
        {
            "module": "runtime4",
            "ok": bool,
            "missing": [...],
            "modified": [...],
            "unexpected": [...]
        }
        """
        module_path = os.path.join(self.base_path, module_rel_path)

        if not os.path.exists(module_path):
            self.logger.error(
                "ChecksumValidator: module path not found",
                extra={"module": module_rel_path}
            )
            return {
                "module": module_rel_path,
                "ok": False,
                "missing": [],
                "modified": [],
                "unexpected": [],
            }

        expected_files = {
            rel: checksum
            for rel, checksum in self.manifest.items()
            if rel.startswith(module_rel_path)
        }

        missing: List[str] = []
        modified: List[str] = []
        unexpected: List[str] = []

        # 1) skontrolujeme všetky očakávané súbory
        for rel_path, expected_checksum in expected_files.items():
            full_path = os.path.join(self.base_path, rel_path)
            current_checksum = self._calc_checksum(full_path)

            if current_checksum is None:
                missing.append(rel_path)
                continue

            if current_checksum != expected_checksum:
                modified.append(rel_path)

        # 2) nájdeme neočakávané súbory v module
        for root, _, files in os.walk(module_path):
            for name in files:
                full_path = os.path.join(root, name)
                rel_path = os.path.relpath(full_path, self.base_path)

                if rel_path not in self.manifest:
                    unexpected.append(rel_path)

        ok = not missing and not modified

        self.logger.info(
            "ChecksumValidator: module validation finished",
            extra={
                "module": module_rel_path,
                "ok": ok,
                "missing": len(missing),
                "modified": len(modified),
                "unexpected": len(unexpected),
            }
        )

        return {
            "module": module_rel_path,
            "ok": ok,
            "missing": missing,
            "modified": modified,
            "unexpected": unexpected,
        }

    def regenerate_manifest_for_module(self, module_rel_path: str) -> None:
        """
        Vygeneruje/aktualizuje manifest pre daný modul.
        Použiteľné pri:
        - nových verziách
        - po úspešnej oprave
        """
        module_path = os.path.join(self.base_path, module_rel_path)

        if not os.path.exists(module_path):
            self.logger.error(
                "ChecksumValidator: cannot regenerate, module path not found",
                extra={"module": module_rel_path}
            )
            return

        updated_entries = 0

        for root, _, files in os.walk(module_path):
            for name in files:
                full_path = os.path.join(root, name)
                rel_path = os.path.relpath(full_path, self.base_path)
                checksum = self._calc_checksum(full_path)
                if checksum:
                    self.manifest[rel_path] = checksum
                    updated_entries += 1

        self.logger.info(
            "ChecksumValidator: manifest regenerated for module",
            extra={"module": module_rel_path, "entries": updated_entries}
        )
        self.save_manifest()
