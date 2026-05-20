# household_4_4/ha_routine_engine_4_4.py
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
"""

from typing import Dict, Any, List, Optional


class HouseholdRoutineEngine44:
    """
    Deterministic routine engine pre domácnosť.
    """

    def __init__(self, state_manager=None, device_registry=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.state_manager = state_manager
        self.device_registry = device_registry
        self.event_bus = event_bus

        # Zaregistrované rutiny
        self.routines: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.state_manager:
                self.state_manager.initialize()
            if self.device_registry:
                self.device_registry.initialize()
            if self.event_bus:
                self.event_bus.initialize()

            self.initialized = True
            return {"status": "initialized"}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # REGISTER ROUTINE
    # ------------------------------------------------------------------
    def register_routine(self, routine: Dict[str, Any]) -> Dict[str, Any]:
        name = routine.get("name")
        if not name:
            return {"status": "error", "reason": "missing_name"}

        # unikátne meno
        for r in self.routines:
            if r.get("name") == name:
                return {"status": "error", "reason": "routine_exists"}

        self.routines.append(routine)
        return {"status": "ok"}

    # ------------------------------------------------------------------
    # LIST ROUTINES
    # ------------------------------------------------------------------
    def list_routines(self) -> Dict[str, Any]:
        return {"status": "ok", "routines": list(self.routines)}

    # ------------------------------------------------------------------
    # RUN ROUTINE BY NAME
    # ------------------------------------------------------------------
    def run_routine(self, name: str) -> Dict[str, Any]:
        for r in self.routines:
            if r.get("name") == name:
                return self._execute_routine(r)

        return {"status": "error", "reason": "routine_not_found"}

    # ------------------------------------------------------------------
    # EXECUTE ROUTINE
    # ------------------------------------------------------------------
    def _execute_routine(self, routine: Dict[str, Any]) -> Dict[str, Any]:
        if not self.state_manager:
            return {"status": "error", "reason": "no_state_manager"}

        actions = routine.get("actions", [])
        results: List[Dict[str, Any]] = []

        for act in actions:
            target_type = act.get("type")
            action = act.get("action")
            value = act.get("value")

            if target_type == "room":
                room = act.get("room")
                if not room:
                    results.append({"status": "error", "reason": "missing_room"})
                    continue
                res = self.state_manager.set_state_for_room(room, action, value)
                results.append(res)

            elif target_type == "device":
                device_id = act.get("device_id")
                if not device_id:
                    results.append({"status": "error", "reason": "missing_device_id"})
                    continue
                res = self.state_manager.set_state(device_id, action, value)
                results.append(res)

            else:
                results.append({"status": "error", "reason": "invalid_action_type"})

        if self.event_bus:
            self.event_bus.emit("routine_executed", {
                "routine_name": routine.get("name"),
                "results": results,
            })

        return {"status": "ok", "results": results}

    # ------------------------------------------------------------------
    # EVENT HANDLING (for event‑based routines)
    # ------------------------------------------------------------------
    def handle_event(self, event_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Jednoduchý event handler – prejde všetky event‑based rutiny
        a spustí tie, ktorým sedí event + podmienky.
        """

        matched: List[str] = []
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

    def _conditions_match(self, conditions: Dict[str, Any], payload: Dict[str, Any]) -> bool:
        for key, expected in conditions.items():
            if payload.get(key) != expected:
                return False
        return True

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "routines_count": len(self.routines),
        }
