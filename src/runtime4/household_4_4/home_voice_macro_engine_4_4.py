"""
SIRIUS LOCAL AI – Home Voice Macro Engine 4.5.0 (PRO)

Purpose:
- deterministic voice macros (action sequences)
- 100% offline, no AI heuristics

Security Family 4.5:
- safe‑mode compatible
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, List, Optional


class HomeVoiceMacroEngine45:
    """
    Deterministic voice macro engine for household automation 4.5.
    """

    def __init__(self, state_manager=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.state_manager = state_manager
        self.event_bus = event_bus

        # name → macro definition
        self.macros: Dict[str, Dict[str, Any]] = {}

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
            return {"status": "already_initialized", "version": "4.5"}

        try:
            modules = [self.state_manager, self.event_bus]
            for m in modules:
                if m:
                    res = m.initialize()
                    if isinstance(res, dict) and res.get("status") == "error":
                        self.degraded_mode = True
                        return {
                            "status": "error",
                            "code": "module_init_failed",
                            "version": "4.5",
                        }

            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # REGISTER MACRO
    # ---------------------------------------------------------
    def register_macro(self, macro: Dict[str, Any]) -> Dict[str, Any]:
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Voice macro engine disabled in safe-mode.",
                "version": "4.5",
            }

        name = macro.get("name")
        steps = macro.get("steps")

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name in self.macros:
            return {"status": "error", "code": "macro_exists", "version": "4.5"}

        if not self._validate_steps(steps):
            return {"status": "error", "code": "invalid_steps", "version": "4.5"}

        try:
            self.macros[name] = macro

            if self.event_bus:
                try:
                    self.event_bus.emit("voice_macro_registered", {"macro": macro})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "register_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # DELETE MACRO
    # ---------------------------------------------------------
    def delete_macro(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name not in self.macros:
            return {"status": "error", "code": "macro_not_found", "version": "4.5"}

        try:
            removed = self.macros.pop(name)

            if self.event_bus:
                try:
                    self.event_bus.emit("voice_macro_deleted", {"macro": removed})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "delete_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # LIST MACROS
    # ---------------------------------------------------------
    def list_macros(self) -> Dict[str, Any]:
        try:
            return {
                "status": "ok",
                "macros": list(self.macros.keys()),
                "version": "4.5",
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "list_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # RUN MACRO
    # ---------------------------------------------------------
    def run_macro(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name not in self.macros:
            return {"status": "error", "code": "macro_not_found", "version": "4.5"}

        if not self.state_manager:
            return {"status": "error", "code": "no_state_manager", "version": "4.5"}

        try:
            macro = self.macros[name]
            steps = macro.get("steps", [])
            results: List[Dict[str, Any]] = []

            for step in steps:
                t = step.get("type")
                action = step.get("action")
                value = step.get("value")

                if t == "room":
                    room = step.get("room")
                    if not self._validate_str(room):
                        results.append({"status": "error", "code": "invalid_room"})
                        continue
                    res = self.state_manager.set_state_for_room(room, action, value)
                    results.append(res)

                elif t == "device":
                    device_id = step.get("device_id")
                    if not self._validate_str(device_id):
                        results.append({"status": "error", "code": "invalid_device_id"})
                        continue
                    res = self.state_manager.set_state(device_id, action, value)
                    results.append(res)

                else:
                    results.append({"status": "error", "code": "invalid_step_type"})

            if self.event_bus:
                try:
                    self.event_bus.emit("voice_macro_executed", {
                        "macro_name": name,
                        "results": results,
                    })
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "results": results, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "run_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "macros_count": len(self.macros),
            "version": "4.5",
        }
