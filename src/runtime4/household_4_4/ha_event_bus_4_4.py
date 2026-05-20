# household_4_4/ha_event_bus_4_4.py
"""
SIRIUS LOCAL AI – Household Event Bus 4.4.0

Účel:
- jednoduchý, deterministický event systém pre domácnosť
- žiadne async, žiadne vlákna, žiadne dynamické importy
- 100 % offline
- používaný modulmi:
    - State Manager 4.4
    - Routine Engine 4.4
    - Task Planner 4.4
    - Diagnostics 4.4
    - Multi‑Step Executor 4.4
    - Household Core 4.4

Event:
{
    "name": "device_state_changed",
    "payload": {...}
}

Handler:
callable(event_name, payload)
"""

from typing import Dict, Any, List, Callable


class HouseholdEventBus44:
    """
    Deterministic event bus pre Household Automation 4.4.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False

        # event_name → [handlers]
        self.handlers: Dict[str, List[Callable[[str, Dict[str, Any]], None]]] = {}

        # log posledných eventov (diagnostika)
        self.event_log: List[Dict[str, Any]] = []

        # maximálna veľkosť logu
        self.max_log_size = 200

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}
        try:
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # REGISTER HANDLER
    # ------------------------------------------------------------------
    def on(self, event_name: str, handler: Callable[[str, Dict[str, Any]], None]) -> Dict[str, Any]:
        """
        Registruje handler pre event.
        """
        if event_name not in self.handlers:
            self.handlers[event_name] = []

        self.handlers[event_name].append(handler)
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # EMIT EVENT
    # ------------------------------------------------------------------
    def emit(self, event_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Emituje event a zavolá všetky registrované handlery.
        """

        # Logovanie
        self._log_event(event_name, payload)

        # Zavolanie handlerov
        if event_name in self.handlers:
            for handler in self.handlers[event_name]:
                try:
                    handler(event_name, payload)
                except Exception:
                    # Handler nesmie zabiť event bus
                    pass

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # INTERNAL: LOG EVENT
    # ------------------------------------------------------------------
    def _log_event(self, event_name: str, payload: Dict[str, Any]):
        entry = {"event": event_name, "payload": payload}

        self.event_log.append(entry)
        if len(self.event_log) > self.max_log_size:
            self.event_log.pop(0)

    # ------------------------------------------------------------------
    # GET LOG
    # ------------------------------------------------------------------
    def get_event_log(self) -> Dict[str, Any]:
        return {"status": "ok", "events": list(self.event_log)}

    # ------------------------------------------------------------------
    # CLEAR LOG
    # ------------------------------------------------------------------
    def clear_log(self) -> Dict[str, Any]:
        self.event_log = []
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "registered_event_types": len(self.handlers),
            "log_size": len(self.event_log),
        }
