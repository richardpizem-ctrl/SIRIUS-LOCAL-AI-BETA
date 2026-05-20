knowledge_packs_4_4/pack_dynamic_loader_4_4.py
"""
SIRIUS LOCAL AI – Pack Dynamic Loader 4.4.0

This module provides a SAFE, deterministic, non‑code‑executing loader
for Knowledge Packs 4.4.

It supports:
- Loading JSON/dict knowledge packs from disk
- Validating pack structure (via KP Validator 4.4)
- Registering packs (via KP Registry 4.4)
- Refreshing pack list without restarting Runtime
- Zero dynamic imports, zero eval, zero code execution

Security Notes:
- Only static file reads allowed.
- No Python code is ever executed from packs.
- Packs must be pure JSON or pure Python dicts.
- Fully offline, deterministic, isolated.
"""

from typing import Dict, Any, List


class PackDynamicLoader44:
    """
    Safe deterministic loader for Knowledge Packs 4.4.
    """

    def __init__(self, fs_adapter=None, validator=None, registry=None):
        self.fs = fs_adapter
        self.validator = validator
        self.registry = registry

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
            if self.validator:
                self.validator.initialize()
            if self.registry:
                self.registry.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # LOAD PACK FROM FILE
    # ------------------------------------------------------------------
    def load_pack(self, path: str) -> Dict[str, Any]:
        """
        Loads a knowledge pack from a JSON file.
        Does NOT execute any code.
        """

        if not self.fs:
            return {"status": "error", "reason": "no_fs_adapter"}

        try:
            raw = self.fs.read_json(path)

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

        # Validate structure
        if self.validator:
            valid = self.validator.validate(raw)
            if valid.get("status") != "ok":
                return {
                    "status": "error",
                    "reason": "validation_failed",
                    "details": valid,
                }

        # Register pack
        if self.registry:
            reg = self.registry.register(raw)
            if reg.get("status") != "ok":
                return {
                    "status": "error",
                    "reason": "registration_failed",
                    "details": reg,
                }

        return {"status": "ok", "pack": raw}

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

            result = self.load_pack(f)
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
    # REFRESH PACKS
    # ------------------------------------------------------------------
    def refresh(self, directory: str) -> Dict[str, Any]:
        """
        Clears registry and reloads all packs.
        """

        if not self.registry:
            return {"status": "error", "reason": "no_registry"}

        self.registry.clear()

        return self.load_all(directory)

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
        }
