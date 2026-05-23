"""
SIRIUS LOCAL AI – Knowledge Packs Loader 4.5.0 (PRO)

Responsible for:
- loading knowledge packs from memory or disk (via fs adapter)
- validating structure (via KP Validator 4.5)
- registering packs (via KP Registry 4.5)
- preparing packs for graph/linker stages
- enforcing Security Family 4.5 rules
- supporting Self‑Repair 4.5 diagnostics

This is the entry point for Knowledge Packs 4.5.
"""

from typing import Dict, Any, Optional


class PackLoader45:
    """
    Loads and registers Knowledge Packs 4.5.
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, validator=None, registry=None, max_packs: int = 1000):
        self.validator = validator
        self.registry = registry

        self.max_packs = max_packs
        self.safe_mode = False
        self.degraded_mode = False
        self.initialized = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            if self.validator:
                res = self.validator.initialize()
                if res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "validator_init_failed",
                        "details": res,
                        "version": "4.5",
                    }

            if self.registry:
                res = self.registry.initialize()
                if res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "registry_init_failed",
                        "details": res,
                        "version": "4.5",
                    }

            self.initialized = True
            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "init_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ------------------------------------------------------------------
    # VALIDATION HELPERS
    # ------------------------------------------------------------------
    def _validate_name(self, name: Any) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_data(self, data: Any) -> bool:
        return isinstance(data, dict)

    def _validate_metadata(self, meta: Any) -> bool:
        return isinstance(meta, dict)

    # ------------------------------------------------------------------
    # LOAD PACK (FROM MEMORY)
    # ------------------------------------------------------------------
    def load_pack(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """
        Loads a pack from a raw dict.
        Validates → registers → returns structured result.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Pack loading disabled in safe-mode.",
                "version": "4.5",
            }

        if not isinstance(raw, dict):
            return {"status": "error", "code": "invalid_raw_type", "version": "4.5"}

        # Validate structure via KP Validator 4.5
        if self.validator:
            valid = self.validator.validate(raw)
            if valid.get("status") != "ok":
                return {
                    "status": "error",
                    "code": "validation_failed",
                    "details": valid,
                    "version": "4.5",
                }

        name = raw.get("name")
        if not self._validate_name(name):
            return {"status": "error", "code": "invalid_pack_name", "version": "4.5"}

        if self.registry:
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
    # LOAD PACK (FROM FILE)
    # ------------------------------------------------------------------
    def load_from_file(self, fs, path: str) -> Dict[str, Any]:
        """
        Loads a pack from a JSON file using fs adapter.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Pack loading disabled in safe-mode.",
                "version": "4.5",
            }

        try:
            raw = fs.read_json(path)
        except Exception as exc:
            return {
                "status": "error",
                "code": "read_failed",
                "exception": str(exc),
                "version": "4.5",
            }

        return self.load_pack(raw)

    # ------------------------------------------------------------------
    # LIST PACKS
    # ------------------------------------------------------------------
    def list_packs(self) -> Dict[str, Any]:
        if not self.registry:
            return {"status": "error", "code": "no_registry", "version": "4.5"}

        return {
            "status": "ok",
            "packs": list(self.registry.get_all().keys()),
            "version": "4.5",
        }

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
