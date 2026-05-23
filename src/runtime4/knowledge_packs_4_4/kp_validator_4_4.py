"""
SIRIUS LOCAL AI – Knowledge Pack Validator 4.5.0 (PRO)

KP Validator 4.5 performs deterministic, offline‑safe validation of
Knowledge Packs. It ensures:

- Correct schema
- Correct version
- Allowed pack types
- Safe data structures
- No executable code
- No invalid metadata
- Compatibility with KP Core 4.5

Security Notes (PRO):
- No dynamic imports, no eval, no reflection.
- Packs must be pure JSON or Python dicts.
- Fully offline, deterministic, isolated.
"""

from typing import Dict, Any


class KnowledgePackValidator45:
    """
    Deterministic validator for Knowledge Packs 4.5.
    """

    ALLOWED_PACK_TYPES = {
        "general",
        "math",
        "language",
        "science",
        "history",
        "geography",
    }

    REQUIRED_FIELDS = {
        "name",
        "version",
        "pack_type",
        "data",
    }

    VERSION = "4.5"

    SAFE_TYPES = (str, int, float, bool, dict, list)

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

    # ------------------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
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
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
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
    # VALIDATE PACK STRUCTURE
    # ------------------------------------------------------------------
    def validate(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates the raw JSON/dict structure of a Knowledge Pack.
        Deterministic, strict, offline-safe.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Validator disabled in safe-mode.",
                "version": "4.5",
            }

        # Must be dict
        if not isinstance(raw, dict):
            return {"status": "error", "code": "not_a_dict", "version": "4.5"}

        # Required fields
        missing = self.REQUIRED_FIELDS - set(raw.keys())
        if missing:
            return {
                "status": "error",
                "code": "missing_fields",
                "missing": sorted(list(missing)),
                "version": "4.5",
            }

        # Validate name
        if not self._validate_str(raw.get("name")):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        # Validate version
        if raw.get("version") != self.VERSION:
            return {
                "status": "error",
                "code": "invalid_version",
                "expected": self.VERSION,
                "found": raw.get("version"),
                "version": "4.5",
            }

        # Validate pack type
        if raw.get("pack_type") not in self.ALLOWED_PACK_TYPES:
            return {
                "status": "error",
                "code": "invalid_pack_type",
                "allowed": sorted(self.ALLOWED_PACK_TYPES),
                "version": "4.5",
            }

        # Validate data
        data = raw.get("data")
        if not isinstance(data, dict):
            return {"status": "error", "code": "data_must_be_dict", "version": "4.5"}

        # Validate metadata
        metadata = raw.get("metadata", {})
        if not self._validate_metadata(metadata):
            return {"status": "error", "code": "invalid_metadata", "version": "4.5"}

        # Recursive safe type check
        safe_check = self._validate_safe_types(raw)
        if safe_check.get("status") != "ok":
            safe_check["version"] = "4.5"
            return safe_check

        return {"status": "ok", "version": "4.5"}

    # ------------------------------------------------------------------
    # RECURSIVE SAFE TYPE CHECK
    # ------------------------------------------------------------------
    def _validate_safe_types(self, value: Any, path: str = "") -> Dict[str, Any]:
        """
        Ensures no executable code or unsafe types exist in the pack.
        Deterministic, recursive, strict.
        """

        # Basic safe types
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

        # Callable or unsafe type detected
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
            "version": "4.5",
        }
