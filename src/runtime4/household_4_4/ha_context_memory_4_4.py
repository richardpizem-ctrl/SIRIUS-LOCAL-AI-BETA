"""
SIRIUS LOCAL AI – Household Context Memory 4.5.0

Účel:
- krátkodobá pamäť pre jeden príkaz/domácu akciu
- drží kontext medzi modulmi (parser → safety → executor → state manager)
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy

Pamäť je vždy malá, resetuje sa po dokončení príkazu:
{
    "command": "zapni svetlo v kuchyni",
    "intent": "device_control",
    "payload": {...},
    "identity": "OWNER",
    "steps": []
}

Security Family 4.5:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, Optional, List


class HouseholdContextMemory45:
    """
    Deterministic context memory pre Household Automation 4.5.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        # Aktuálny kontext jedného príkazu
        self.context: Dict[str, Any] = {}

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            self.context = {}
            self.initialized = True
            return {"status": "initialized", "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_key(self, key: Any) -> bool:
        return isinstance(key, str) and key.strip()

    def _validate_value(self, value: Any) -> bool:
        # Zakázané typy podľa Security Family 4.5
        if isinstance(value, (bytes, bytearray, type(lambda: None))):
            return False
        return True

    # ---------------------------------------------------------
    # SET CONTEXT
    # ---------------------------------------------------------
    def set(self, key: str, value: Any) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Context memory disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_key(key):
            return {"status": "error", "code": "invalid_key", "version": "4.5"}

        if not self._validate_value(value):
            return {"status": "error", "code": "invalid_value", "version": "4.5"}

        try:
            self.context[key] = value
            return {"status": "ok", "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # GET CONTEXT
    # ---------------------------------------------------------
    def get(self, key: str) -> Dict[str, Any]:
        if not self._validate_key(key):
            return {"status": "error", "code": "invalid_key", "version": "4.5"}

        if key not in self.context:
            return {"status": "error", "code": "not_found", "version": "4.5"}

        return {"status": "ok", "value": self.context[key], "version": "4.5"}

    # ---------------------------------------------------------
    # APPEND TO LIST FIELD
    # ---------------------------------------------------------
    def append(self, key: str, value: Any) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Context memory disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_key(key):
            return {"status": "error", "code": "invalid_key", "version": "4.5"}

        if not self._validate_value(value):
            return {"status": "error", "code": "invalid_value", "version": "4.5"}

        try:
            if key not in self.context:
                self.context[key] = []

            if not isinstance(self.context[key], list):
                return {"status": "error", "code": "not_a_list", "version": "4.5"}

            self.context[key].append(value)
            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # RESET CONTEXT
    # ---------------------------------------------------------
    def reset(self) -> Dict[str, Any]:
        try:
            self.context = {}
            return {"status": "ok", "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # EXPORT CONTEXT
    # ---------------------------------------------------------
    def export(self) -> Dict[str, Any]:
        try:
            return {"status": "ok", "context": dict(self.context), "version": "4.5"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "keys": list(self.context.keys()),
            "version": "4.5",
        }
