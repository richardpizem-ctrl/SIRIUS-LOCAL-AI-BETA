"""
SIRIUS LOCAL AI – Household Routine Engine 4.4.0

Účel:
- deterministické IF–THEN rutiny pre domácnosť
- časové rutiny a event‑based rutiny
- 100 % offline, žiadne AI heuristiky, žiadne dynamické importy

Rutiny sú čisté dict štruktúry:

Time‑based:
{
    "name": "good_night",
    "type": "time",
    "schedule": {"hour": 22, "minute": 0},
    "actions": [
        {"type": "room", "room": "living_room", "action": "off"},
        {"type": "room", "room": "kitchen", "action": "off"}
    ]
}

Event‑based:
{
    "name": "hall_light_on_door_open",
    "type": "event",
    "event": "door_open",
    "conditions": {"room": "hall"},
    "actions": [
        {"type": "room", "room": "hall", "action": "on"}
    ]
}

Security Family 4.4:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, List, Optional


class HouseholdRoutineEngine44:
    """
    Deterministic routine engine pre domácnosť.
    """

    def __init__(self, state_manager=None, device_registry=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.state_manager = state_manager
        self.device_registry = device_registry
        self.event_bus = event_bus

        self.routines: List[Dict[str, Any]] = []

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_actions(self, actions: Any) -> bool:
        if not isinstance(actions, list):
            return False
        for a in actions:
            if not isinstance(a, dict):
                return False
            if not self._validate_str(a.get("type", "")):
                return False
            if not self._validate_str(a.get("action", "")):
                return False
        return True

    def _validate_routine(self, routine: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(routine, dict):
            return {"valid": False, "code": "invalid_routine_type"}

        name = routine.get("name")
        if not self._validate_str(name):
            return {"valid": False, "code": "invalid_name"}

        rtype = routine.get("type")
        if rtype not in ("time", "event"):
            return {"valid": False, "code": "invalid_type"}

        if not self._validate_actions(routine.get("actions", [])):
            return {"valid": False, "code": "invalid_actions"}

        if rtype == "time":
            schedule = routine.get("schedule")
            if not isinstance(schedule, dict):
                return {"valid": False, "code": "invalid_schedule"}
            if not isinstance(schedule.get("hour"), int):
                return {"valid": False, "code": "invalid_schedule_hour"}
            if not isinstance(schedule.get("minute"), int):
                return {"valid": False, "code": "invalid_schedule_minute"}

        if rtype == "event":
            if not self._validate_str(routine.get("event", "")):
                return {"valid": False, "code": "invalid_event_name"}

        return {"valid": True}

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            modules = [self.state_manager, self.device_registry, self.event_bus]
            for m in modules:
                if m:
                    res = m.initialize()
                    if isinstance(res, dict) and res.get("status") == "error":
                        self.degraded_mode = True
                        return {"status": "error", "code": "module_init_failed"}

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------
    # REGISTER ROUTINE
    # ---------------------------------------------------------
    def register_routine(self, routine: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Routine engine disabled in safe-mode."}

        check = self._validate_routine(routine)
        if not check["valid"]:
            return {"status": "error", "code": check["code"]}

        name = routine["name"]
        for r in self.routines:
            if r.get("name") == name:
                return {"status": "error", "code": "routine_exists"}

        try:
            self.routines.append(routine)
            return {"status": "ok"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "routine_register_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # LIST ROUTINES
    # ---------------------------------------------------------
    def list_routines(self) -> Dict[str, Any]:
        return {"status": "ok", "routines": list(self.routines)}

    # ---------------------------------------------------------
    # RUN ROUTINE BY NAME
    # ---------------------------------------------------------
    def run_routine(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name"}

        for r in self.routines:
            if r.get("name") == name:
                return self._execute_routine(r)

        return {"status": "error", "code": "routine_not_found"}

    # ---------------------------------------------------------
    # EXECUTE ROUTINE
    # ---------------------------------------------------------
    def _execute_routine(self, routine: Dict[str, Any]) -> Dict[str, Any]:
        if not self.state_manager:
            return {"status": "error", "code": "no_state_manager"}

        results: List[Dict[str, Any]] = []

        try:
            for act in routine.get("actions", []):
                t = act.get("type")
                action = act.get("action")
                value = act.get("value")

                if t == "room":
                    room = act.get("room")
                    if not self._validate_str(room):
                        results.append({"status": "error", "code": "invalid_room"})
                        continue
                    res = self.state_manager.set_state_for_room(room, action, value)
                    results.append(res)

                elif t == "device":
                    device_id = act.get("device_id")
                    if not self._validate_str(device_id):
                        results.append({"status": "error", "code": "invalid_device_id"})
                        continue
                    res = self.state_manager.set_state(device_id, action, value)
                    results.append(res)

                else:
                    results.append({"status": "error", "code": "invalid_action_type"})

            if self.event_bus:
                self.event_bus.emit("routine_executed", {
                    "routine_name": routine.get("name"),
                    "results": results,
                })

            return {"status": "ok", "results": results}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "routine_execute_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # EVENT HANDLING (event‑based routines)
    # ---------------------------------------------------------
    def handle_event(self, event_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self._validate_str(event_name):
            return {"status": "error", "code": "invalid_event_name"}

        matched: List[str] = []

        try:
            for r in self.routines:
                if r.get("type") != "event":
                    continue
                if r.get("event") != event_name:
                    continue

                conditions = r.get("conditions", {})
                if not self._conditions_match(conditions, payload):
                    continue

                self._execute_routine(r)
                matched.append(r.get("name"))

            return {"status": "ok", "matched_routines": matched}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "event_handler_failed", "exception": str(exc)}

    def _conditions_match(self, conditions: Dict[str, Any], payload: Dict[str, Any]) -> bool:
        for key, expected in conditions.items():
            if payload.get(key) != expected:
                return False
        return True

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "routines_count": len(self.routines),
        }
