"""
SIRIUS LOCAL AI – ENVOY 4.0 Receiver

Responsible for:
- receiving external ENVOY payloads
- performing initial structural checks
- routing payloads to quarantine or validator
- preparing data for Knowledge Packs 2.0 conversion

This is the entry point of ENVOY 4.0.
"""

from typing import Optional, Dict, Any


class EnvoyReceiver4:
    """
    Receives and preprocesses ENVOY payloads.
    """

    def __init__(self, max_queue_size: int = 1000, max_payload_size: int = 500_000):
        # Raw incoming payloads before validation
        self.incoming = []

        # Security limits
        self.max_queue_size = max_queue_size
        self.max_payload_size = max_payload_size

    # ---------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
    # ---------------------------------------------------------

    def _is_safe_payload(self, payload: Any) -> bool:
        """Performs shallow safety validation before quarantine."""

        # Must be dict
        if not isinstance(payload, dict):
            return False

        # Payload must not be too large
        try:
            import json
            if len(json.dumps(payload)) > self.max_payload_size:
                return False
        except Exception:
            return False

        # Validate keys and values
        for key, value in payload.items():

            # Keys must be strings
            if not isinstance(key, str) or not key.strip():
                return False

            # Values must be safe types
            if isinstance(value, (bytes, bytearray, type(lambda: None))):
                return False

        return True

    # ---------------------------------------------------------
    # RECEIVING
    # ---------------------------------------------------------

    def receive(self, payload: Dict[str, Any]):
        """
        Receives a raw ENVOY payload with full safety checks.
        """

        # Validate payload type
        if not isinstance(payload, dict):
            return {"error": "invalid_payload_type"}

        # Validate payload safety
        if not self._is_safe_payload(payload):
            return {"error": "unsafe_payload"}

        # Queue size limit
        if len(self.incoming) >= self.max_queue_size:
            return {"error": "queue_overflow"}

        # Store payload
        self.incoming.append(payload)

        return {"status": "received", "size": len(self.incoming)}

    # ---------------------------------------------------------
    # ACCESS
    # ---------------------------------------------------------

    def get_next(self) -> Optional[Dict[str, Any]]:
        """
        Retrieves the next unprocessed payload.
        Includes safety checks.
        """

        if not self.incoming:
            return None

        entry = self.incoming.pop(0)

        # Validate entry again (defense in depth)
        if not isinstance(entry, dict):
            return {"error": "invalid_queue_entry"}

        if not self._is_safe_payload(entry):
            return {"error": "unsafe_payload_in_queue"}

        return entry
