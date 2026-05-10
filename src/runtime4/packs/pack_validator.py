# pack_validator.py
"""
SIRIUS LOCAL AI – Knowledge Packs 2.0 Validator

Responsible for:
- validating pack structure
- checking required fields
- enforcing safety rules
- ensuring compatibility with Runtime 4.0
- preparing packs for graph/linker stages

This is the validation layer for Knowledge Packs 2.0.
"""


class PackValidator4:
    """
    Validates the structure and metadata of Knowledge Packs 2.0.
    """

    def __init__(self):
        # Required fields for every pack
        self.required_fields = ["data", "meta"]

        # Required metadata keys
        self.required_meta = ["version", "type"]

    # ---------------------------------------------------------
    # STRUCTURE VALIDATION
    # ---------------------------------------------------------

    def validate_structure(self, pack: dict):
        """Checks if pack contains required top-level fields."""
        for field in self.required_fields:
            if field not in pack:
                return {
                    "valid": False,
                    "error": "missing_field",
                    "field": field
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
        return {"valid": True}

    # ---------------------------------------------------------
    # FULL VALIDATION
    # ---------------------------------------------------------

    def validate(self, pack: dict):
        """Performs full validation of a pack."""
        struct = self.validate_structure(pack)
        if not struct["valid"]:
            return struct

        meta = self.validate_metadata(pack["meta"])
        if not meta["valid"]:
            return meta

        return {"valid": True}
