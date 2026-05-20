"""
SIRIUS LOCAL AI – Knowledge Packs Validator 4.4.0 (PRO)

Responsible for:
- validating pack structure
- checking required fields
- enforcing Security Family 4.4 rules
- ensuring compatibility with Knowledge Packs 4.4
- preparing packs for loader/graph/linker stages
- supporting Self‑Repair 4.4 diagnostics

This is the validation layer for Knowledge Packs 4.4.
"""

from typing import Dict, Any


class PackValidator44:
    """
    Deterministic validator for Knowledge Packs 4.4.
    Provides:
    - strict structural validation
    - metadata validation
    - JSON‑safe type validation
    - safe-mode compatibility
    - degraded-mode detection
    - structured error surface
    """

    REQUIRED_FIELDS = {
        "name",
        "version",
        "pack_type",
        "data",
        "metadata",
    }

    ALLOWED_PACK_TYPES = {
        "general",
        "math",
        "language",
        "science",
        "history",
        "geography",
    }

    VERSION = "4.4"
    SAFE_TYPES = (str, int, float, bool, dict, list)

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False
        self.initialized = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "init_failed", "exception": str(exc)}

    # ------------------------------------------------------------------
    # VALIDATION HELPERS
    # ------------------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_metadata(self, meta: Any) -> bool:
        if not isinstance(meta, dict):
            return False
        for k, v in meta.items():
            if not isinstance(k, str):
                return False
            if not isinstance(v, self.SAFE_TYPES):
                return False
        return True

    # ------------------------------------------------------------------
    # FULL VALIDATION
    # ------------------------------------------------------------------
    def validate(self, pack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Performs full validation of a Knowledge Pack 4.4.
        """

        if self.safe_mode:
            return {"status": "safe_mode", "message": "Validation disabled in safe-mode."}

        # Must be dict
        if not isinstance(pack, dict):
            return {"status": "error", "code": "not_a_dict"}

        # Required fields
        missing = self.REQUIRED_FIELDS - set(pack.keys())
        if missing:
            return {
                "status": "error",
                "code": "missing_fields",
                "missing": sorted(list(missing)),
            }

        # Validate name
        if not self._validate_str(pack["name"]):
            return {"status": "error", "code": "invalid_name"}

        # Validate version
        if pack["version"] != self.VERSION:
            return {
                "status": "error",
                "code": "invalid_version",
                "expected": self.VERSION,
                "found": pack["version"],
            }

        # Validate pack type
        if pack["pack_type"] not in self.ALLOWED_PACK_TYPES:
            return {
                "status": "error",
                "code": "invalid_pack_type",
                "allowed": sorted(self.ALLOWED_PACK_TYPES),
            }

        # Validate data
        if not isinstance(pack["data"], dict):
            return {"status": "error", "code": "data_must_be_dict"}

        # Validate metadata
        if not self._validate_metadata(pack["metadata"]):
            return {"status": "error", "code": "invalid_metadata"}

        # Recursive JSON-safe validation
        safe_check = self._validate_safe_types(pack)
        if safe_check.get("status") != "ok":
            return safe_check

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # RECURSIVE SAFE TYPE CHECK
    # ------------------------------------------------------------------
    def _validate_safe_types(self, value: Any, path: str = "") -> Dict[str, Any]:
        """
        Ensures no executable code or unsafe types exist in the pack.
        """

        if isinstance(value, self.SAFE_TYPES):
            # Dict recursion
            if isinstance(value, dict):
                for k, v in value.items():
                    if not isinstance(k, str):
                        return {
                            "status": "error",
                            "code": "invalid_key_type",
                            "path": path,
                            "key": k,
                            "type": str(type(k)),
                        }
                    result = self._validate_safe_types(v, f"{path}.{k}")
                    if result.get("status") != "ok":
                        return result

            # List recursion
            if isinstance(value, list):
                for i, item in enumerate(value):
                    result = self._validate_safe_types(item, f"{path}[{i}]")
                    if result.get("status") != "ok":
                        return result

            return {"status": "ok"}

        # Unsafe type detected
        return {
            "status": "error",
            "code": "unsafe_type_detected",
            "path": path,
            "type": str(type(value)),
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
        }
