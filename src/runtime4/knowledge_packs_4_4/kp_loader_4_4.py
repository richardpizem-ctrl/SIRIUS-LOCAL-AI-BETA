"""
SIRIUS LOCAL AI – Knowledge Pack Loader 4.5.0 (PRO)

KP Loader 4.5 is the deterministic, offline‑safe loader for Knowledge Packs.
It loads packs from JSON files or Python dicts and integrates with:

- KP Core 4.5 (base pack structure)
- KP Validator 4.5 (schema + integrity checks)
- KP Registry 4.5 (pack registration)
- KP Metadata 4.5 (versioning + descriptors)

Security Notes (PRO):
- No dynamic imports, no eval, no reflection.
- Packs must be pure JSON or Python dicts.
- Loader never executes code from packs.
- Fully offline, deterministic, isolated.
"""

from typing import Dict, Any, List, Optional


class KnowledgePackLoader45:
    """
    Deterministic loader for Knowledge Packs 4.5.
    """

    def __init__(self, fs_adapter=None, core=None, validator=None, registry=None, metadata=None):
        self.fs = fs_adapter
        self.core = core
        self.validator = validator
        self.registry = registry
        self.metadata = metadata

        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
    # ------------------------------------------------------------------
    def _validate_raw(self, raw: Any) -> bool:
        return isinstance(raw, dict)

    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            modules = [self.fs, self.core, self.validator, self.registry, self.metadata]
            for m in modules:
                if m:
                    res = m.initialize()
                    if isinstance(res, dict) and res.get("status") == "error":
                        self.degraded_mode = True
                        return {
                            "status": "error",
                            "code": "module_init_failed",
                            "version": "4.5",
                        }

            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # LOAD PACK FROM FILE
    # ------------------------------------------------------------------
    def load_from_file(self, path: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Loader disabled in safe-mode.",
                "version": "4.5",
            }

        if not self.fs:
            return {"status": "error", "code": "no_fs_adapter", "version": "4.5"}

        if not self._validate_str(path):
            return {"status": "error", "code": "invalid_path", "version": "4.5"}

        try:
            raw = self.fs.read_json(path)
        except Exception as exc:
            return {
                "status": "error",
                "code": "file_read_failed",
                "exception": str(exc),
                "version": "4.5",
            }

        return self._process_raw_pack(raw)

    # ------------------------------------------------------------------
    # LOAD PACK FROM DICT
    # ------------------------------------------------------------------
    def load_from_dict(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Loader disabled in safe-mode.",
                "version": "4.5",
            }

        return self._process_raw_pack(raw)

    # ------------------------------------------------------------------
    # INTERNAL PROCESSING PIPELINE
    # ------------------------------------------------------------------
    def _process_raw_pack(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full deterministic pipeline:
        1. Validate raw structure
        2. Schema validation (KP Validator)
        3. Create pack container (KP Core)
        4. Metadata enrichment (KP Metadata)
        5. Register pack (KP Registry)
        """

        # 1. Validate raw structure
        if not self._validate_raw(raw):
            return {"status": "error", "code": "invalid_raw_structure", "version": "4.5"}

        # 2. Schema validation
        if self.validator:
            valid = self.validator.validate(raw)
            if valid.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "validation_failed",
                    "details": valid,
                    "version": "4.5",
                }

        # 3. Create pack container
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
                    "code": "pack_creation_failed",
                    "details": created,
                    "version": "4.5",
                }
            pack = created["pack"]
        else:
            return {"status": "error", "code": "core_missing", "version": "4.5"}

        # 4. Metadata enrichment
        if self.metadata:
            enriched = self.metadata.attach_metadata(pack)
            if enriched.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "metadata_failed",
                    "details": enriched,
                    "version": "4.5",
                }
            pack = enriched["pack"]

        # 5. Register pack
        if self.registry:
            reg = self.registry.register(pack.to_dict())
            if reg.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "registration_failed",
                    "details": reg,
                    "version": "4.5",
                }

        return {"status": "ok", "pack": pack, "version": "4.5"}

    # ------------------------------------------------------------------
    # LOAD ALL PACKS FROM DIRECTORY
    # ------------------------------------------------------------------
    def load_all(self, directory: str) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Loader disabled in safe-mode.",
                "version": "4.5",
            }

        if not self.fs:
            return {"status": "error", "code": "no_fs_adapter", "version": "4.5"}

        if not self._validate_str(directory):
            return {"status": "error", "code": "invalid_directory", "version": "4.5"}

        try:
            files = self.fs.list_files(directory)
        except Exception as exc:
            return {
                "status": "error",
                "code": "list_failed",
                "exception": str(exc),
                "version": "4.5",
            }

        loaded = []
        failed = []

        for f in files:
            if not isinstance(f, str) or not f.endswith(".json"):
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
            "version": "4.5",
        }

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "version": "4.5",
        }
