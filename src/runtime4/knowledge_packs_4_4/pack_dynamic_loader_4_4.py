"""
SIRIUS LOCAL AI – Pack Dynamic Loader 4.5.0 (PRO)

This module provides a SAFE, deterministic, non‑code‑executing loader
for Knowledge Packs 4.5.

It supports:
- Loading JSON/dict knowledge packs from disk
- Validating pack structure (via KP Validator 4.5)
- Registering packs (via KP Registry 4.5)
- Refreshing pack list without restarting Runtime
- Zero dynamic imports, zero eval, zero code execution

Security Notes (PRO):
- Only static file reads allowed.
- No Python code is ever executed from packs.
- Packs must be pure JSON or pure Python dicts.
- Fully offline, deterministic, isolated.
"""

from typing import Dict, Any, List, Optional


class PackDynamicLoader45:
    """
    Safe deterministic loader for Knowledge Packs 4.5.
    """

    def __init__(self, fs_adapter=None, validator=None, registry=None):
        self.fs = fs_adapter
        self.validator = validator
        self.registry = registry

        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL HELPERS
    # ------------------------------------------------------------------
    def _has_fs(self) -> bool:
        return self.fs is not None

    def _has_validator(self) -> bool:
        return self.validator is not None

    def _has_registry(self) -> bool:
        return self.registry is not None

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            if self._has_fs():
                res = self.fs.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "fs_init_failed",
                        "details": res,
                        "version": "4.5",
                    }

            if self._has_validator():
                res = self.validator.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "validator_init_failed",
                        "details": res,
                        "version": "4.5",
                    }

            if self._has_registry():
                res = self.registry.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "registry_init_failed",
                        "details": res,
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
    def load_pack(self, path: str) -> Dict[str, Any]:
        """
        Loads a knowledge pack from a JSON file.
        Does NOT execute any code.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Dynamic loader disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._has_fs():
            return {"status": "error", "code": "no_fs_adapter", "version": "4.5"}

        try:
            raw = self.fs.read_json(path)
        except Exception as exc:
            return {
                "status": "error",
                "code": "read_failed",
                "exception": str(exc),
                "version": "4.5",
            }

        # Validate structure
        if self._has_validator():
            valid = self.validator.validate(raw)
            if valid.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "validation_failed",
                    "details": valid,
                    "version": "4.5",
                }

        # Register pack
        if self._has_registry():
            reg = self.registry.register(raw)
            if reg.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "registration_failed",
                    "details": reg,
                    "version": "4.5",
                }

        return {"status": "ok", "pack": raw, "version": "4.5"}

    # ------------------------------------------------------------------
    # LOAD ALL PACKS FROM DIRECTORY
    # ------------------------------------------------------------------
    def load_all(self, directory: str) -> Dict[str, Any]:
        """
        Loads all JSON packs from a directory.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Dynamic loader disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._has_fs():
            return {"status": "error", "code": "no_fs_adapter", "version": "4.5"}

        try:
            files: List[str] = self.fs.list_files(directory)
        except Exception as exc:
            return {
                "status": "error",
                "code": "list_failed",
                "exception": str(exc),
                "version": "4.5",
            }

        loaded: List[str] = []
        failed: List[Dict[str, Any]] = []

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
            "version": "4.5",
        }

    # ------------------------------------------------------------------
    # REFRESH PACKS
    # ------------------------------------------------------------------
    def refresh(self, directory: str) -> Dict[str, Any]:
        """
        Clears registry and reloads all packs.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Dynamic loader disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._has_registry():
            return {"status": "error", "code": "no_registry", "version": "4.5"}

        try:
            cleared = self.registry.clear()
            if isinstance(cleared, dict) and cleared.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "clear_failed",
                    "details": cleared,
                    "version": "4.5",
                }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "clear_exception",
                "exception": str(exc),
                "version": "4.5",
            }

        return self.load_all(directory)

    # ------------------------------------------------------------------
    # GET STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "version": "4.5",
        }
