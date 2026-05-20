knowledge_packs_4_4/kp_loader_4_4.py
"""
SIRIUS LOCAL AI – Knowledge Pack Loader 4.4.0

KP Loader 4.4 is the deterministic, offline‑safe loader for Knowledge Packs.
It loads packs from JSON files or Python dicts and integrates with:

- KP Core 4.4 (base pack structure)
- KP Validator 4.4 (schema + integrity checks)
- KP Registry 4.4 (pack registration)
- KP Metadata 4.4 (versioning + descriptors)

Security Notes:
- No dynamic imports, no eval, no reflection.
- Packs must be pure JSON or Python dicts.
- Loader never executes code from packs.
- Fully offline, deterministic, isolated.
"""

from typing import Dict, Any, List, Optional


class KnowledgePackLoader44:
    """
    Deterministic loader for Knowledge Packs 4.4.
    """

    def __init__(self, fs_adapter=None, core=None, validator=None, registry=None, metadata=None):
        self.fs = fs_adapter
        self.core = core
        self.validator = validator
        self.registry = registry
        self.metadata = metadata

        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.fs:
                self.fs.initialize()
            if self.core:
                self.core.initialize()
            if self.validator:
                self.validator.initialize()
            if self.registry:
                self.registry.initialize()
            if self.metadata:
                self.metadata.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # LOAD PACK FROM FILE
    # ------------------------------------------------------------------
    def load_from_file(self, path: str) -> Dict[str, Any]:
        """
        Loads a Knowledge Pack from a JSON file.
        """

        if not self.fs:
            return {"status": "error", "reason": "no_fs_adapter"}

        try:
            raw = self.fs.read_json(path)
        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

        return self._process_raw_pack(raw)

    # ------------------------------------------------------------------
    # LOAD PACK FROM DICT
    # ------------------------------------------------------------------
    def load_from_dict(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """
        Loads a Knowledge Pack directly from a Python dict.
        """
        return self._process_raw_pack(raw)

    # ------------------------------------------------------------------
    # INTERNAL PROCESSING PIPELINE
    # ------------------------------------------------------------------
    def _process_raw_pack(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full deterministic pipeline:
        1. Validate structure
        2. Create pack container
        3. Validate pack content
        4. Register pack
        5. Attach metadata
        """

        # 1. Validate raw structure
        if self.validator:
            valid = self.validator.validate(raw)
            if valid.get("status") != "ok":
                return {
                    "status": "error",
                    "reason": "validation_failed",
                    "details": valid,
                }

        # 2. Create pack container
        if self.core:
            created = self.core.create_pack(
                name=raw.get("name"),
                pack_type=raw.get("pack_type"),
                data=raw.get("data", {}),
                metadata=raw.get("metadata", {}),
            )
            if created.get("status") != "ok":
                return {
                    "status": "error",
                    "reason": "pack_creation_failed",
                    "details": created,
                }

            pack = created["pack"]
        else:
            pack = raw  # fallback (should not happen in production)

        # 3. Metadata enrichment
        if self.metadata:
            enriched = self.metadata.attach_metadata(pack)
            if enriched.get("status") != "ok":
                return {
                    "status": "error",
                    "reason": "metadata_failed",
                    "details": enriched,
                }
            pack = enriched["pack"]

        # 4. Register pack
        if self.registry:
            reg = self.registry.register(pack.to_dict())
            if reg.get("status") != "ok":
                return {
                    "status": "error",
                    "reason": "registration_failed",
                    "details": reg,
                }

        return {"status": "ok", "pack": pack}

    # ------------------------------------------------------------------
    # LOAD ALL PACKS FROM DIRECTORY
    # ------------------------------------------------------------------
    def load_all(self, directory: str) -> Dict[str, Any]:
        """
        Loads all JSON packs from a directory.
        """

        if not self.fs:
            return {"status": "error", "reason": "no_fs_adapter"}

        try:
            files = self.fs.list_files(directory)
        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

        loaded = []
        failed = []

        for f in files:
            if not f.endswith(".json"):
                continue

            result = self.load_from_file(f)
            if result.get("status") == "ok":
                loaded.append(f)
            else:
                failed.append({"file": f, "error": result})

        return {
            "status": "ok",
            "loaded": loaded,
            "failed": failed,
        }

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
