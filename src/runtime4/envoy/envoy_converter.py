"""
SIRIUS LOCAL AI – ENVOY 4.3 Converter

Responsible for:
- converting validated ENVOY payloads into Knowledge Pack 2.0 format
- extracting data and metadata
- preparing packs for loading and linking
- enforcing Security Family 4.4 rules
- ensuring structural and semantic compatibility
- providing deterministic, safe conversion

This is the conversion layer of ENVOY 4.3.
"""

from typing import Dict, Any


class EnvoyConverter4:
    """
    Converts ENVOY payloads into Knowledge Pack 2.0 structures.
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, max_content_size: int = 500_000):
        self.max_content_size = max_content_size
        self.degraded_mode = False
        self.safe_mode = False

    # ---------------------------------------------------------
    # INTERNAL SAFETY CHECKS
    # ---------------------------------------------------------

    def _is_safe_content(self, content: Any) -> bool:
        """Validates ENVOY content before conversion."""

        if not isinstance(content, (dict, str)):
            return False

        if isinstance(content, dict):
            for key, value in content.items():
                if not isinstance(key, str) or not key.strip():
                    return False
                if isinstance(value, (bytes, bytearray, type(lambda: None))):
                    return False

        if isinstance(content, str) and len(content) > self.max_content_size:
            return False

        return True

    def _is_safe_meta(self, meta: Any) -> bool:
        """Validates ENVOY metadata before conversion."""

        if not isinstance(meta, dict):
            return False

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

    def convert(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Converts an ENVOY payload into a Knowledge Pack 2.0 structure.
        Includes full Runtime 4.3 security validation.
        """

        # SAFE MODE
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "ENVOY conversion disabled in safe-mode."
            }

        # Validate payload
        if not isinstance(payload, dict):
            return {"status": "error", "code": "invalid_payload_type"}

        content = payload.get("content")
        meta = payload.get("meta", {})
        ptype = payload.get("type", "unknown")

        # Validate content
        if not self._is_safe_content(content):
            return {"status": "error", "code": "invalid_or_unsafe_content"}

        # Validate metadata
        if not self._is_safe_meta(meta):
            return {"status": "error", "code": "invalid_or_unsafe_meta"}

        try:
            # Build Knowledge Pack 2.0 structure
            pack = {
                "data": content if isinstance(content, dict) else {"content": content},
                "meta": {
                    "version": meta.get("version", "1.0"),
                    "type": ptype if isinstance(ptype, str) else "unknown",
                    "source": meta.get("source", "envoy")
                }
            }

            return {
                "status": "success",
                "pack": pack,
                "degraded_mode": self.degraded_mode
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "conversion_failed",
                "exception": str(exc)
            }
