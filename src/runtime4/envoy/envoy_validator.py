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

        # Validate payload type
        if not isinstance(payload, dict):
            return {"valid": False, "error": "invalid_payload_type"}

        # Required fields
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

        # Validate meta type
        if not isinstance(meta, dict):
            return {"valid": False, "error": "invalid_meta_type"}

        # Required metadata keys
        for key in self.required_meta:
            if key not in meta:
                return {
                    "valid": False,
                    "error": "missing_meta_key",
                    "key": key
                }

        # Validate meta.source
        source = meta.get("source")
        if not isinstance(source, str) or not source.strip():
            return {"valid": False, "error": "invalid_meta_source"}

        # Validate meta.version
        version = meta.get("version")
        if not isinstance(version, str) or not version.strip():
            return {"valid": False, "error": "invalid_meta_version"}

        return {"valid": True}

    # ---------------------------------------------------------
    # CONTENT VALIDATION
    # ---------------------------------------------------------

    def validate_content(self, content):
        """Validates ENVOY content field."""

        # Content must be dict or string depending on ENVOY type
        if not isinstance(content, (dict, str)):
            return {"valid": False, "error": "invalid_content_type"}

        # If dict, ensure no dangerous types
        if isinstance(content, dict):
            for key, value in content.items():
                if not isinstance(key, str):
                    return {"valid": False, "error": "invalid_content_key"}
                if isinstance(value, (bytes, bytearray, type(lambda: None))):
                    return {"valid": False, "error": "invalid_content_value"}

        return {"valid": True}

    # ---------------------------------------------------------
    # TYPE VALIDATION
    # ---------------------------------------------------------

    def validate_type(self, t):
        """Validates ENVOY type field."""
        if not isinstance(t, str) or not t.strip():
            return {"valid": False, "error": "invalid_type_field"}
        return {"valid": True}

    # ---------------------------------------------------------
    # FULL VALIDATION
    # ---------------------------------------------------------

    def validate(self, payload: dict):
        """Performs full validation of an ENVOY payload."""

        # STRUCTURE
        struct = self.validate_structure(payload)
        if not struct["valid"]:
            return struct

        # TYPE
        type_check = self.validate_type(payload["type"])
        if not type_check["valid"]:
            return type_check

        # CONTENT
        content_check = self.validate_content(payload["content"])
        if not content_check["valid"]:
            return content_check

        # META
        meta_check = self.validate_metadata(payload["meta"])
        if not meta_check["valid"]:
            return meta_check

        return {"valid": True}
