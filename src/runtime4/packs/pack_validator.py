"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Validator (Runtime 4.3)

Responsible for:
- validating pack structure
- checking required fields
- enforcing Security Family 4.4 rules
- ensuring compatibility with Knowledge Packs 2.0
- preparing packs for graph/linker stages
- supporting Self‑Repair 4.4 diagnostics

This is the validation layer for Knowledge Packs 2.0 (Runtime 4.3).
"""


class PackValidator4:
    """
    Validates the structure and metadata of Knowledge Packs 2.0.
    Provides:
    - strict structural validation
    - metadata validation
    - safe-mode compatibility
    - degraded-mode detection
    - structured error surface
    """

    def __init__(self):
        self.required_fields = ["data", "meta"]
        self.required_meta = ["version", "type"]
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # STRUCTURE VALIDATION
    # ---------------------------------------------------------

    def validate_structure(self, pack: dict):
        """Checks if pack contains required top-level fields."""

        if not isinstance(pack, dict):
            return {
                "valid": False,
                "error": "invalid_pack_type",
                "detail": "Pack must be a dictionary."
            }

        for field in self.required_fields:
            if field not in pack:
                return {
                    "valid": False,
                    "error": "missing_field",
                    "field": field
                }

        if not isinstance(pack["data"], dict):
            return {
                "valid": False,
                "error": "invalid_data_type",
                "detail": "Pack 'data' must be a dictionary."
            }

        if not isinstance(pack["meta"], dict):
            return {
                "valid": False,
                "error": "invalid_meta_type",
                "detail": "Pack 'meta' must be a dictionary."
            }

        return {"valid": True}

    # ---------------------------------------------------------
    # METADATA VALIDATION
    # ---------------------------------------------------------

    def validate_metadata(self, meta: dict):
        """Checks if metadata contains required keys."""

        for key in self.required_meta:
            if key not in meta:
                return {
                    "valid": False,
                    "error": "missing_meta_key",
                    "key": key
                }

        if not isinstance(meta["version"], str) or not meta["version"].strip():
            return {
                "valid": False,
                "error": "invalid_version_type",
                "detail": "Meta 'version' must be a non-empty string."
            }

        if not isinstance(meta["type"], str) or not meta["type"].strip():
            return {
                "valid": False,
                "error": "invalid_type_field",
                "detail": "Meta 'type' must be a non-empty string."
            }

        return {"valid": True}

    # ---------------------------------------------------------
    # FULL VALIDATION
    # ---------------------------------------------------------

    def validate(self, pack: dict):
        """Performs full validation of a pack."""

        # SAFE MODE
        if self.safe_mode:
            return {
                "valid": False,
                "error": "safe_mode",
                "message": "Pack validation disabled in safe-mode."
            }

        struct = self.validate_structure(pack)
        if not struct["valid"]:
            return struct

        meta = self.validate_metadata(pack["meta"])
        if not meta["valid"]:
            return meta

        return {
            "valid": True,
            "degraded_mode": self.degraded_mode
        }
