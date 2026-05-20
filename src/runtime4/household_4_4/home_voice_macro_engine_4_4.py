# household_4_4/home_voice_macro_engine_4_4.py
"""
SIRIUS LOCAL AI – Home Voice Macro Engine 4.4.0

Účel:
- umožňuje vytvárať hlasové makrá (sekvencie akcií)
- makro = názov + zoznam krokov (deterministických)
- 100 % offline, žiadne AI heuristiky, žiadne dynamické importy

Makro:
{
    "name": "good_morning_macro",
    "steps": [
        {"type": "room", "room": "kitchen", "action": "on"},
        {"type": "device", "device_id": "coffee_machine", "action": "on"},
        {"type": "room", "room": "living_room", "action": "set", "value": "bright"}
    ]
}
"""

from typing import Dict, Any, List, Optional


class HomeVoiceMacroEngine44:
    """
    Deterministic voice macro engine pre domácnosť.
    """

    def __init__(self, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.state_manager = state_manager
        self.event_bus = event_bus

        # name → macro
        self.macros: Dict[str, Dict[str, Any]] = {}

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
    # REGISTER MACRO
    # ------------------------------------------------------------------
    def register_macro(self, macro: Dict[str, Any]) -> Dict[str, Any]:
        name = macro.get("name")
        if not name:
            return {"status": "error", "reason": "missing_name"}

        if name in self.macros:
            return {"status": "error", "reason": "macro_exists"}

        self.macros[name] = macro

        if self.event_bus:
            self.event_bus.emit("voice_macro_registered", {"macro": macro})

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # DELETE MACRO
    # ------------------------------------------------------------------
    def delete_macro(self, name: str) -> Dict[str, Any]:
        if name not in self.macros:
            return {"status": "error", "reason": "macro_not_found"}

        removed = self.macros.pop(name)

        if self.event_bus:
            self.event_bus.emit("voice_macro_deleted", {"macro": removed})

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # LIST MACROS
    # ------------------------------------------------------------------
    def list_macros(self) -> Dict[str, Any]:
        return {"status": "ok", "macros": list(self.macros.keys())}

    # ------------------------------------------------------------------
    # RUN MACRO
    # ------------------------------------------------------------------
    def run_macro(self, name: str) -> Dict[str, Any]:
        if name not in self.macros:
            return {"status": "error", "reason": "macro_not_found"}

        macro = self.macros[name]
        steps = macro.get("steps", [])
        results: List[Dict[str, Any]] = []

        if not self.state_manager:
            return {"status": "error", "reason": "no_state_manager"}

        for step in steps:
            t = step.get("type")
            action = step.get("action")
            value = step.get("value")

            if t == "room":
                room = step.get("room")
                if not room:
                    results.append({"status": "error", "reason": "missing_room"})
                    continue
                res = self.state_manager.set_state_for_room(room, action, value)
                results.append(res)

            elif t == "device":
                device_id = step.get("device_id")
                if not device_id:
                    results.append({"status": "error", "reason": "missing_device_id"})
                    continue
                res = self.state_manager.set_state(device_id, action, value)
                results.append(res)

            else:
                results.append({"status": "error", "reason": "invalid_step_type"})

        if self.event_bus:
            self.event_bus.emit("voice_macro_executed", {
                "macro_name": name,
                "results": results,
            })

        return {"status": "ok", "results": results}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "macros_count": len(self.macros),
        }
