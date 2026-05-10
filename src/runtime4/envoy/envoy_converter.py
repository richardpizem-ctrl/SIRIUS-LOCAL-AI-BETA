"""
SIRIUS LOCAL AI – ENVOY 4.0 Converter

Responsible for:
- converting validated ENVOY payloads into Knowledge Pack 2.0 format
- extracting data and metadata
- preparing packs for loading and linking
- ensuring structural compatibility

This is the conversion layer of ENVOY 4.0.
"""

from typing import Dict, Any


class EnvoyConverter4:
    """
    Converts ENVOY payloads into Knowledge Pack 2.0 structures.
    """

    def __init__(self, max_content_size: int = 500_000):
        self.max_content_size = max_content_size

    # ---------------------------------------------------------
    # INTERNAL SAFETY CHECKS
    # ---------------------------------------------------------

    def _is_safe_content(self, content: Any) -> bool:
        """Validates ENVOY content before conversion."""

        # Content must be dict or string
        if not isinstance(content, (dict, str)):
            return False

        # If dict, validate keys and values
        if isinstance(content, dict):
            for key, value in content.items():

                # Keys must be strings
                if not isinstance(key, str) or not key.strip():
                    return False

                # Values must be safe types
                if isinstance(value, (bytes, bytearray, type(lambda: None))):
                    return False

        # If string, ensure it's not too large
        if isinstance(content, str) and len(content) > self.max_content_size:
            return False

        return True

    def _is_safe_meta(self, meta: Any) -> bool:
        """Validates ENVOY metadata before conversion."""

        if not isinstance(meta, dict):
            return False

        # Validate required fields
        source = meta.get("source")
        version = meta.get("version")

        if not isinstance(source, str) or not source.strip():
            return False

        if not isinstance(version, str) or not version.strip():
            return False

        return True

    # ---------------------------------------------------------
    # CONVERSION
    # ---------------------------------------------------------

    def convert(self, payload: Dict[str, Any]):
        """
        Converts an ENVOY payload into a Knowledge Pack 2.0 structure.
        Includes full Runtime 4.0 security validation.
        """

        # Validate payload type
        if not isinstance(payload, dict):
            return {"error": "invalid_payload_type"}

        # Extract fields
        content = payload.get("content")
        meta = payload.get("meta", {})
        ptype = payload.get("type", "unknown")

        # Validate content
        if not self._is_safe_content(content):
            return {"error": "invalid_or_unsafe_content"}

        # Validate metadata
        if not self._is_safe_meta(meta):
            return {"error": "invalid_or_unsafe_meta"}

        # Build pack
        pack = {
            "data": content if isinstance(content, dict) else {"content": content},
            "meta": {
                "version": meta.get("version", "1.0"),
                "type": ptype if isinstance(ptype, str) else "unknown",
                "source": meta.get("source", "envoy")
            }
        }

        return pack
