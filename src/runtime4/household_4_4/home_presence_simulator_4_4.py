# household_4_4/home_presence_simulator_4_4.py
"""
SIRIUS LOCAL AI – Home Presence Simulator 4.4.0

Účel:
- simulácia prítomnosti v domácnosti počas neprítomnosti
- deterministické vzory: svetlá, rolety, zásuvky
- žiadne AI heuristiky, žiadne náhodné generovanie
- 100 % offline

Scenár simulácie:
{
    "name": "evening_presence",
    "steps": [
        {"time": "18:00", "type": "room", "room": "living_room", "action": "on"},
        {"time": "20:00", "type": "room", "room": "kitchen", "action": "on"},
        {"time": "22:00", "type": "room", "room": "living_room", "action": "off"}
    ]
}
"""

from typing import Dict, Any, List, Optional


class HomePresenceSimulator44:
    """
    Deterministic presence simulator pre domácnosť.
    """

    def __init__(self, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.state_manager = state_manager
        self.event_bus = event_bus

        # názov → scenár
        self.scenarios: Dict[str, Dict[str, Any]] = {}

        # aktuálne aktívny scenár
        self.active_scenario: Optional[str] = None

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.state_manager:
                self.state_manager.initialize()
            if self.event_bus:
                self.event_bus.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # REGISTER SCENARIO
    # ------------------------------------------------------------------
    def register_scenario(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        name = scenario.get("name")
        if not name:
            return {"status": "error", "reason": "missing_name"}

        if name in self.scenarios:
            return {"status": "error", "reason": "scenario_exists"}

        self.scenarios[name] = scenario

        if self.event_bus:
            self.event_bus.emit("presence_scenario_registered", {"scenario": scenario})

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # LIST SCENARIOS
    # ------------------------------------------------------------------
    def list_scenarios(self) -> Dict[str, Any]:
        return {"status": "ok", "scenarios": list(self.scenarios.keys())}

    # ------------------------------------------------------------------
    # ACTIVATE SCENARIO
    # ------------------------------------------------------------------
    def activate(self, name: str) -> Dict[str, Any]:
        if name not in self.scenarios:
            return {"status": "error", "reason": "scenario_not_found"}

        self.active_scenario = name

        if self.event_bus:
            self.event_bus.emit("presence_scenario_activated", {"name": name})

        return {"status": "ok", "active": name}

    # ------------------------------------------------------------------
    # DEACTIVATE SCENARIO
    # ------------------------------------------------------------------
    def deactivate(self) -> Dict[str, Any]:
        old = self.active_scenario
        self.active_scenario = None

        if self.event_bus:
            self.event_bus.emit("presence_scenario_deactivated", {"old": old})

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # TICK – APPLY ACTIONS FOR GIVEN TIME
    # ------------------------------------------------------------------
    def tick(self, time_str: str) -> Dict[str, Any]:
        """
        time_str = "HH:MM"
        Aplikuje akcie scenára, ktoré majú daný čas.
        """

        if not self.active_scenario:
            return {"status": "ok", "applied": []}

        scenario = self.scenarios[self.active_scenario]
        steps = scenario.get("steps", [])

        applied: List[Dict[str, Any]] = []

        for step in steps:
            if step.get("time") != time_str:
                continue

            t = step.get("type")
            action = step.get("action")
            value = step.get("value")

            if t == "room":
                room = step.get("room")
                res = self.state_manager.set_state_for_room(room, action, value)
                applied.append(res)

            elif t == "device":
                dev = step.get("device_id")
                res = self.state_manager.set_state(dev, action, value)
                applied.append(res)

        if self.event_bus and applied:
            self.event_bus.emit("presence_tick_applied", {
                "scenario": self.active_scenario,
                "time": time_str,
                "results": applied,
            })

        return {"status": "ok", "applied": applied}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "active_scenario": self.active_scenario,
            "scenarios_count": len(self.scenarios),
        }
