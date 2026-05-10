# envoy_receiver.py
"""
SIRIUS LOCAL AI – ENVOY 4.0 Receiver

Responsible for:
- receiving external ENVOY payloads
- performing initial structural checks
- routing payloads to quarantine or validator
- preparing data for Knowledge Packs 2.0 conversion

This is the entry point of ENVOY 4.0.
"""

from typing import Optional


class EnvoyReceiver4:
    """
    Receives and preprocesses ENVOY payloads.
    """

    def __init__(self):
        # Raw incoming payloads before validation
        self.incoming = []

    # ---------------------------------------------------------
    # RECEIVING
    # ---------------------------------------------------------

    def receive(self, payload: dict):
        """
        Receives a raw ENVOY payload.
        """
        self.incoming.append(payload)
        return {"status": "received", "size": len(self.incoming)}

    # ---------------------------------------------------------
    # ACCESS
    # ---------------------------------------------------------

    def get_next(self) -> Optional[dict]:
        """
        Retrieves the next unprocessed payload.
        """
        if not self.incoming:
            return None
        return self.incoming.pop(0)
