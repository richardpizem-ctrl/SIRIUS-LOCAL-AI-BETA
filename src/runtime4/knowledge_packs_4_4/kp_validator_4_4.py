knowledge_packs_4_4/kp_validator_4_4.py
"""
SIRIUS LOCAL AI – Knowledge Pack Validator 4.4.0

KP Validator 4.4 performs deterministic, offline‑safe validation of
Knowledge Packs. It ensures:

- Correct schema
- Correct version
- Allowed pack types
- Safe data structures
- No executable code
- No invalid metadata
- Compatibility with KP Core 4.4

Security Notes:
- No dynamic imports, no eval, no reflection.
- Packs must be pure JSON or Python dicts.
- Fully offline, deterministic, isolated.
"""

from typing import Dict, Any


class KnowledgePackValidator44:
    """
    Deterministic validator for Knowledge Packs 4.4.
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

    VERSION = "4.4"

    SAFE_TYPES = (str, int, float, bool, dict, list)

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self):
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # VALIDATE PACK STRUCTURE
    # ------------------------------------------------------------------
    def validate(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates the raw JSON/dict structure of a Knowledge Pack.
        """

        # Must be dict
        if not isinstance(raw, dict):
            return {"status": "error", "reason": "not_a_dict"}

        # Check required fields
        missing = self.REQUIRED_FIELDS - set(raw.keys())
        if missing:
            return {
                "status": "error",
                "reason": "missing_fields",
                "missing": list(missing),
            }

        # Validate version
        if raw.get("version") != self.VERSION:
            return {
                "status": "error",
                "reason": "invalid_version",
                "expected": self.VERSION,
                "found": raw.get("version"),
            }

        # Validate pack type
        if raw.get("pack_type") not in self.ALLOWED_PACK_TYPES:
            return {
                "status": "error",
                "reason": "invalid_pack_type",
                "allowed": list(self.ALLOWED_PACK_TYPES),
            }

        # Validate data
        if not isinstance(raw.get("data"), dict):
            return {
                "status": "error",
                "reason": "data_must_be_dict",
            }

        # Validate metadata
        metadata = raw.get("metadata", {})
        if not isinstance(metadata, dict):
            return {
                "status": "error",
                "reason": "metadata_must_be_dict",
            }

        # Validate safe types recursively
        safe_check = self._validate_safe_types(raw)
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

        # Basic safe types
        if isinstance(value, self.SAFE_TYPES):
            # Recurse into dict
            if isinstance(value, dict):
                for k, v in value.items():
                    result = self._validate_safe_types(v, f"{path}.{k}")
                    if result.get("status") != "ok":
                        return result

            # Recurse into list
            if isinstance(value, list):
                for i, item in enumerate(value):
                    result = self._validate_safe_types(item, f"{path}[{i}]")
                    if result.get("status") != "ok":
                        return result

            return {"status": "ok"}

        # Unsafe type detected
        return {
            "status": "error",
            "reason": "unsafe_type_detected",
            "path": path,
            "type": str(type(value)),
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
