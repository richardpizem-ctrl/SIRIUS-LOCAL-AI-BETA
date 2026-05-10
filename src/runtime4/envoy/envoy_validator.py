# envoy_validator.py
"""
SIRIUS LOCAL AI – ENVOY 4.0 Validator

Responsible for:
- validating ENVOY payload structure
- checking required fields
- enforcing safety rules
- ensuring compatibility with Knowledge Packs 2.0
- preparing payloads for conversion

This is the validation layer of ENVOY 4.0.
"""


class EnvoyValidator4:
    """
    Validates ENVOY payloads before they enter the runtime.
    """

    def __init__(self):
        # Required top-level fields
        self.required_fields = ["type", "content", "meta"]

        # Required metadata keys
        self.required_meta = ["source", "version"]

    # ---------------------------------------------------------
    # STRUCTURE VALIDATION
    # ---------------------------------------------------------

    def validate_structure(self, payload: dict):
        """Checks if payload contains required fields."""
        for field in self.required_fields:
            if field not in payload:
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

    def validate(self, payload: dict):
        """Performs full validation of an ENVOY payload."""
        struct = self.validate_structure(payload)
        if not struct["valid"]:
            return struct

        meta = self.validate_metadata(payload["meta"])
        if not meta["valid"]:
            return meta

        return {"valid": True}
