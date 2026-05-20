"""
SIRIUS LOCAL AI – Home Presence Simulator 4.4.0 (PRO)

Účel:
- deterministická simulácia prítomnosti v domácnosti
- žiadne AI heuristiky, žiadne náhodné generovanie
- 100 % offline

Security Family 4.4:
- deterministické správanie
- safe‑mode kompatibilita
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, List, Optional


class HomePresenceSimulator44:
    """
    Deterministic presence simulator pre domácnosť.
    """

    def __init__(self, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.state_manager = state_manager
        self.event_bus = event_bus

        # názov → scenár
        self.scenarios: Dict[str, Dict[str, Any]] = {}

        # aktuálne aktívny scenár
        self.active_scenario: Optional[str] = None

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_steps(self, steps: Any) -> bool:
        if not isinstance(steps, list):
            return False
        for s in steps:
            if not isinstance(s, dict):
                return False
            if not self._validate_str(s.get("time")):
                return False
            if not self._validate_str(s.get("type")):
                return False
            if not self._validate_str(s.get("action")):
                return False
        return True

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            modules = [self.state_manager, self.event_bus]
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
    # REGISTER SCENARIO
    # ---------------------------------------------------------
    def register_scenario(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Presence simulator disabled in safe-mode."}

        name = scenario.get("name")
        steps = scenario.get("steps")

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name"}

        if name in self.scenarios:
            return {"status": "error", "code": "scenario_exists"}

        if not self._validate_steps(steps):
            return {"status": "error", "code": "invalid_steps"}

        try:
            self.scenarios[name] = scenario

            if self.event_bus:
                try:
                    self.event_bus.emit("presence_scenario_registered", {"scenario": scenario})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "register_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # LIST SCENARIOS
    # ---------------------------------------------------------
    def list_scenarios(self) -> Dict[str, Any]:
        try:
            return {"status": "ok", "scenarios": list(self.scenarios.keys())}
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "list_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # ACTIVATE SCENARIO
    # ---------------------------------------------------------
    def activate(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name"}

        if name not in self.scenarios:
            return {"status": "error", "code": "scenario_not_found"}

        try:
            self.active_scenario = name

            if self.event_bus:
                try:
                    self.event_bus.emit("presence_scenario_activated", {"name": name})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "active": name}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "activate_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # DEACTIVATE SCENARIO
    # ---------------------------------------------------------
    def deactivate(self) -> Dict[str, Any]:
        try:
            old = self.active_scenario
            self.active_scenario = None

            if self.event_bus:
                try:
                    self.event_bus.emit("presence_scenario_deactivated", {"old": old})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "deactivate_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # TICK – APPLY ACTIONS FOR GIVEN TIME
    # ---------------------------------------------------------
    def tick(self, time_str: str) -> Dict[str, Any]:
        if not self._validate_str(time_str):
            return {"status": "error", "code": "invalid_time"}

        if not self.active_scenario:
            return {"status": "ok", "applied": []}

        try:
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
                    if not self._validate_str(room):
                        continue
                    res = self.state_manager.set_state_for_room(room, action, value)
                    applied.append(res)

                elif t == "device":
                    dev = step.get("device_id")
                    if not self._validate_str(dev):
                        continue
                    res = self.state_manager.set_state(dev, action, value)
                    applied.append(res)

            if self.event_bus and applied:
                try:
                    self.event_bus.emit("presence_tick_applied", {
                        "scenario": self.active_scenario,
                        "time": time_str,
                        "results": applied,
                    })
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "applied": applied}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "tick_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "active_scenario": self.active_scenario,
            "scenarios_count": len(self.scenarios),
        }
