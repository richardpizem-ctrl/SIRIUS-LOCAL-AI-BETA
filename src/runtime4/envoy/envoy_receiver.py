"""
SIRIUS LOCAL AI – ENVOY 4.3 Receiver

Responsible for:
- receiving external ENVOY payloads
- performing initial structural checks
- routing payloads to quarantine or validator
- enforcing Security Family 4.4 rules
- preparing data for Knowledge Packs 2.0 conversion
- supporting Self‑Repair 4.4 diagnostics

This is the entry point of ENVOY 4.3.
"""

from typing import Optional, Dict, Any
import json


class EnvoyReceiver4:
    """
    Receives and preprocesses ENVOY payloads.
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, max_queue_size: int = 1000, max_payload_size: int = 500_000):
        self.incoming = []
        self.max_queue_size = max_queue_size
        self.max_payload_size = max_payload_size
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # INTERNAL SAFETY CHECKS
    # ---------------------------------------------------------

    def _is_safe_payload(self, payload: Any) -> bool:
        """Performs shallow safety validation before quarantine."""

        if not isinstance(payload, dict):
            return False

        # Size check
        try:
            if len(json.dumps(payload)) > self.max_payload_size:
                return False
        except Exception:
            return False

        # Validate keys and values
        for key, value in payload.items():
            if not isinstance(key, str) or not key.strip():
                return False
            if isinstance(value, (bytes, bytearray, type(lambda: None))):
                return False

        return True

    # ---------------------------------------------------------
    # RECEIVING
    # ---------------------------------------------------------

    def receive(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Receives a raw ENVOY payload with full safety checks.
        """

        # SAFE MODE
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "ENVOY receiver disabled in safe-mode."
            }

        if not isinstance(payload, dict):
            return {"status": "error", "code": "invalid_payload_type"}

        if not self._is_safe_payload(payload):
            return {"status": "error", "code": "unsafe_payload"}

        if len(self.incoming) >= self.max_queue_size:
            return {"status": "error", "code": "queue_overflow"}

        self.incoming.append(payload)

        return {
            "status": "received",
            "size": len(self.incoming)
        }

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

        if not isinstance(entry, dict):
            self.degraded_mode = True
            return {"status": "error", "code": "invalid_queue_entry"}

        if not self._is_safe_payload(entry):
            return {"status": "error", "code": "unsafe_payload_in_queue"}

        return {
            "status": "ready",
            "payload": entry
        }
