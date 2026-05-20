"""
SIRIUS LOCAL AI – ENVOY 4.4 Quarantine

Responsible for:
- isolating unvalidated ENVOY payloads
- performing safety checks
- blocking suspicious or malformed data
- preparing safe payloads for validation
- enforcing Security Family 4.4 rules
- supporting Self‑Repair 4.4 diagnostics

This is the quarantine layer of ENVOY 4.4.
"""

from typing import Dict, Any, Optional
import json


class EnvoyQuarantine4:
    """
    Deterministic quarantine layer for ENVOY 4.4.
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    - Security Family 4.4 enforcement
    """

    def __init__(self, max_queue_size: int = 500, max_payload_size: int = 500_000):
        self.quarantine = []
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
    # ISOLATION
    # ---------------------------------------------------------

    def isolate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Moves a payload into quarantine with full safety checks."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Quarantine disabled in safe-mode.",
                "degraded_mode": self.degraded_mode,
            }

        if not isinstance(payload, dict):
            return {"status": "error", "code": "invalid_payload_type"}

        if not self._is_safe_payload(payload):
            return {"status": "error", "code": "unsafe_payload"}

        if len(self.quarantine) >= self.max_queue_size:
            return {"status": "error", "code": "quarantine_overflow"}

        self.quarantine.append(payload)

        return {
            "status": "isolated",
            "count": len(self.quarantine),
            "degraded_mode": self.degraded_mode,
        }

    # ---------------------------------------------------------
    # INSPECTION
    # ---------------------------------------------------------

    def inspect(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Performs safety checks before validation."""

        if not self._is_safe_payload(payload):
            return {"safe": False, "reason": "unsafe_payload"}

        # Forbidden keys (Security Family 4.4)
        forbidden_keys = ["exec", "code", "script", "inject"]
        for key in forbidden_keys:
            if key in payload:
                return {"safe": False, "reason": f"forbidden_key:{key}"}

        # Example malicious flag
        if "malicious" in payload:
            return {"safe": False, "reason": "malicious_flag_detected"}

        return {"safe": True}

    # ---------------------------------------------------------
    # RELEASE
    # ---------------------------------------------------------

    def release_next(self) -> Optional[Dict[str, Any]]:
        """Releases the next safe payload from quarantine."""

        if not self.quarantine:
            return None

        entry = self.quarantine.pop(0)

        if not isinstance(entry, dict):
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "invalid_quarantine_entry",
                "degraded_mode": True,
            }

        check = self.inspect(entry)

        if not check.get("safe", False):
            return {
                "status": "error",
                "code": "payload_blocked",
                "reason": check.get("reason"),
                "degraded_mode": self.degraded_mode,
            }

        return {
            "status": "released",
            "payload": entry,
            "degraded_mode": self.degraded_mode,
        }
