# household_4_4/ha_context_memory_4_4.py
"""
SIRIUS LOCAL AI – Household Context Memory 4.4.0

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
"""

from typing import Dict, Any, Optional, List


class HouseholdContextMemory44:
    """
    Deterministic context memory pre Household Automation 4.4.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

        # Aktuálny kontext jedného príkazu
        self.context: Dict[str, Any] = {}

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}
        try:
            self.context = {}
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # SET CONTEXT
    # ------------------------------------------------------------------
    def set(self, key: str, value: Any) -> Dict[str, Any]:
        self.context[key] = value
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # GET CONTEXT
    # ------------------------------------------------------------------
    def get(self, key: str) -> Dict[str, Any]:
        if key not in self.context:
            return {"status": "error", "reason": "not_found"}
        return {"status": "ok", "value": self.context[key]}

    # ------------------------------------------------------------------
    # APPEND TO LIST FIELD
    # ------------------------------------------------------------------
    def append(self, key: str, value: Any) -> Dict[str, Any]:
        if key not in self.context:
            self.context[key] = []
        if not isinstance(self.context[key], list):
            return {"status": "error", "reason": "not_a_list"}

        self.context[key].append(value)
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # RESET CONTEXT
    # ------------------------------------------------------------------
    def reset(self) -> Dict[str, Any]:
        self.context = {}
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # EXPORT CONTEXT (napr. pre log alebo diagnostiku)
    # ------------------------------------------------------------------
    def export(self) -> Dict[str, Any]:
        return {"status": "ok", "context": dict(self.context)}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "keys": list(self.context.keys()),
        }
