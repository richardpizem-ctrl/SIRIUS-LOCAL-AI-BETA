"""
SIRIUS LOCAL AI – Household Event Bus 4.4.0

Účel:
- deterministický event systém pre domácnosť
- žiadne async, žiadne vlákna, žiadne dynamické importy
- 100 % offline, bezpečné
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

Security Family 4.4:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, List, Callable


class HouseholdEventBus44:
    """
    Deterministic event bus pre Household Automation 4.4.
    """

    def __init__(self):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        # event_name → [handlers]
        self.handlers: Dict[str, List[Callable[[str, Dict[str, Any]], None]]] = {}

        # log posledných eventov (diagnostika)
        self.event_log: List[Dict[str, Any]] = []
        self.max_log_size = 200

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_event_name(self, name: Any) -> bool:
        return isinstance(name, str) and name.strip()

    def _validate_payload(self, payload: Any) -> bool:
        if not isinstance(payload, dict):
            return False
        for k, v in payload.items():
            if not isinstance(k, str) or not k.strip():
                return False
            if isinstance(v, (bytes, bytearray, type(lambda: None))):
                return False
        return True

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            self.handlers = {}
            self.event_log = []
            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------
    # REGISTER HANDLER
    # ---------------------------------------------------------
    def on(self, event_name: str, handler: Callable[[str, Dict[str, Any]], None]) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Event bus disabled in safe-mode."}

        if not self._validate_event_name(event_name):
            return {"status": "error", "code": "invalid_event_name"}

        if not callable(handler):
            return {"status": "error", "code": "invalid_handler"}

        try:
            if event_name not in self.handlers:
                self.handlers[event_name] = []
            self.handlers[event_name].append(handler)
            return {"status": "ok"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "handler_register_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # EMIT EVENT
    # ---------------------------------------------------------
    def emit(self, event_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Event bus disabled in safe-mode."}

        if not self._validate_event_name(event_name):
            return {"status": "error", "code": "invalid_event_name"}

        if not self._validate_payload(payload):
            return {"status": "error", "code": "invalid_payload"}

        # Log event
        self._log_event(event_name, payload)

        # Call handlers
        if event_name in self.handlers:
            for handler in self.handlers[event_name]:
                try:
                    handler(event_name, payload)
                except Exception:
                    # Handler nesmie zabiť event bus
                    self.degraded_mode = True

        return {"status": "ok", "degraded_mode": self.degraded_mode}

    # ---------------------------------------------------------
    # INTERNAL: LOG EVENT
    # ---------------------------------------------------------
    def _log_event(self, event_name: str, payload: Dict[str, Any]):
        try:
            entry = {"event": event_name, "payload": payload}
            self.event_log.append(entry)
            if len(self.event_log) > self.max_log_size:
                self.event_log.pop(0)
        except Exception:
            self.degraded_mode = True

    # ---------------------------------------------------------
    # GET LOG
    # ---------------------------------------------------------
    def get_event_log(self) -> Dict[str, Any]:
        try:
            return {"status": "ok", "events": list(self.event_log)}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "log_read_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # CLEAR LOG
    # ---------------------------------------------------------
    def clear_log(self) -> Dict[str, Any]:
        try:
            self.event_log = []
            return {"status": "ok"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "log_clear_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "registered_event_types": len(self.handlers),
            "log_size": len(self.event_log),
        }
