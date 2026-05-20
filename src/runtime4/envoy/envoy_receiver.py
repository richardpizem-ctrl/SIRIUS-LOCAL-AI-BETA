"""
SIRIUS LOCAL AI – ENVOY 4.4 Receiver

Responsible for:
- receiving external ENVOY payloads
- performing initial structural checks
- routing payloads to quarantine or validator
- enforcing Security Family 4.4 rules
- preparing data for Knowledge Packs 2.0 conversion
- supporting Self‑Repair 4.4 diagnostics

This is the entry point of ENVOY 4.4.
"""

from typing import Optional, Dict, Any
import json


class EnvoyReceiver4:
    """
    Deterministic ENVOY receiver for Runtime 4.4.
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    - Security Family 4.4 enforcement
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
        """Performs shallow safety validation before intake."""

        if not isinstance(payload, dict):
            return False

        # Size check (deterministic)
        try:
            if len(json.dumps(payload, ensure_ascii=False)) > self.max_payload_size:
                return False
        except Exception:
            return False

        # Validate keys and values
        for key, value in payload.items():
            if not isinstance(key, str) or not key.strip():
                return False

            # Forbidden types
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
                "message": "ENVOY receiver disabled in safe-mode.",
                "degraded_mode": self.degraded_mode,
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
            "size": len(self.incoming),
            "degraded_mode": self.degraded_mode,
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
            return {
                "status": "error",
                "code": "invalid_queue_entry",
                "degraded_mode": True,
            }

        if not self._is_safe_payload(entry):
            return {
                "status": "error",
                "code": "unsafe_payload_in_queue",
                "degraded_mode": self.degraded_mode,
            }

        return {
            "status": "ready",
            "payload": entry,
            "degraded_mode": self.degraded_mode,
        }
