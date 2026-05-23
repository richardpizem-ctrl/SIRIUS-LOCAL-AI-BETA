"""
SIRIUS LOCAL AI – ENVOY 4.5 Validator

Responsible for:
- validating ENVOY payload structure
- checking required fields
- enforcing Security Family 4.5 rules
- ensuring compatibility with Knowledge Packs 2.0
- preparing payloads for conversion
- supporting Self‑Repair 4.5 diagnostics

This is the validation layer of ENVOY 4.5.
"""


class EnvoyValidator4:
    """
    Deterministic ENVOY payload validator for Runtime 4.5.
    Provides:
    - strict structural validation
    - metadata validation
    - content validation
    - safe-mode compatibility
    - degraded-mode detection
    - Security Family 4.5 enforcement
    """

    def __init__(self):
        self.required_fields = ["type", "content", "meta"]
        self.required_meta = ["source", "version"]
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # STRUCTURE VALIDATION
    # ---------------------------------------------------------

    def validate_structure(self, payload: dict):
        """Checks if payload contains required fields."""

        if not isinstance(payload, dict):
            return {"valid": False, "error": "invalid_payload_type", "version": "4.5"}

        for field in self.required_fields:
            if field not in payload:
                return {
                    "valid": False,
                    "error": "missing_field",
                    "field": field,
                    "version": "4.5",
                }

        return {"valid": True, "version": "4.5"}

    # ---------------------------------------------------------
    # METADATA VALIDATION
    # ---------------------------------------------------------

    def validate_metadata(self, meta: dict):
        """Checks if metadata contains required keys."""

        if not isinstance(meta, dict):
            return {"valid": False, "error": "invalid_meta_type", "version": "4.5"}

        for key in self.required_meta:
            if key not in meta:
                return {
                    "valid": False,
                    "error": "missing_meta_key",
                    "key": key,
                    "version": "4.5",
                }

        source = meta.get("source")
        if not isinstance(source, str) or not source.strip():
            return {"valid": False, "error": "invalid_meta_source", "version": "4.5"}

        version = meta.get("version")
        if not isinstance(version, str) or not version.strip():
            return {"valid": False, "error": "invalid_meta_version", "version": "4.5"}

        return {"valid": True, "version": "4.5"}

    # ---------------------------------------------------------
    # CONTENT VALIDATION
    # ---------------------------------------------------------

    def validate_content(self, content):
        """Validates ENVOY content field."""

        if not isinstance(content, (dict, str)):
            return {"valid": False, "error": "invalid_content_type", "version": "4.5"}

        if isinstance(content, dict):
            for key, value in content.items():
                if not isinstance(key, str) or not key.strip():
                    return {"valid": False, "error": "invalid_content_key", "version": "4.5"}
                if isinstance(value, (bytes, bytearray, type(lambda: None))):
                    return {"valid": False, "error": "invalid_content_value", "version": "4.5"}

        return {"valid": True, "version": "4.5"}

    # ---------------------------------------------------------
    # TYPE VALIDATION
    # ---------------------------------------------------------

    def validate_type(self, t):
        """Validates ENVOY type field."""
        if not isinstance(t, str) or not t.strip():
            return {"valid": False, "error": "invalid_type_field", "version": "4.5"}
        return {"valid": True, "version": "4.5"}

    # ---------------------------------------------------------
    # SECURITY FAMILY 4.5 CHECKS
    # ---------------------------------------------------------

    def validate_security(self, payload: dict):
        """Checks forbidden keys and unsafe patterns."""

        forbidden_keys = ["exec", "code", "script", "inject", "malicious"]

        for key in forbidden_keys:
            if key in payload:
                return {
                    "valid": False,
                    "error": "forbidden_key",
                    "key": key,
                    "version": "4.5",
                }

        return {"valid": True, "version": "4.5"}

    # ---------------------------------------------------------
    # FULL VALIDATION
    # ---------------------------------------------------------

    def validate(self, payload: dict):
        """Performs full validation of an ENVOY payload."""

        # SAFE MODE
        if self.safe_mode:
            return {
                "valid": False,
                "error": "safe_mode",
                "message": "Validation disabled in safe-mode.",
                "version": "4.5",
            }

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

        # SECURITY FAMILY 4.5
        sec_check = self.validate_security(payload)
        if not sec_check["valid"]:
            return sec_check

        return {"valid": True, "version": "4.5"}
