"""
SIRIUS LOCAL AI – Home Security Bridge 4.5.0 (PRO)

Purpose:
- deterministic bridge between Household Automation 4.5 and security modes
- switches household behavior based on security mode
- 100% offline, no AI heuristics

Security Family 4.5:
- safe‑mode compatible
- stricter rules for STRANGER_MODE and VACATION
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, List, Optional


class HomeSecurityBridge45:
    """
    Deterministic security bridge for household automation 4.5.
    """

    def __init__(self, state_manager=None, safety_guard=None, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.state_manager = state_manager
        self.safety_guard = safety_guard
        self.event_bus = event_bus

        # current security mode
        self.current_mode: str = "HOME"

        # deterministic mapping of modes to actions
        self.mode_actions = {
            "HOME": [],
            "AWAY": [
                {"type": "room", "room": "all", "action": "off"},
            ],
            "NIGHT": [
                {"type": "room", "room": "living_room", "action": "off"},
                {"type": "room", "room": "kitchen", "action": "off"},
            ],
            "VACATION": [
                {"type": "room", "room": "all", "action": "off"},
            ],
            "SCHOOL_MODE": [],
            "STRANGER_MODE": [],
        }

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
            if not self._validate_str(a.get("type")):
                return False
            if not self._validate_str(a.get("action")):
                return False
        return True

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            modules = [self.state_manager, self.safety_guard, self.event_bus]
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
    # SET SECURITY MODE
    # ---------------------------------------------------------
    def set_mode(self, mode: str) -> Dict[str, Any]:
        if not self._validate_str(mode):
            return {"status": "error", "code": "invalid_mode", "version": "4.5"}

        mode = mode.upper().strip()
        if mode not in self.mode_actions:
            return {"status": "error", "code": "unknown_mode", "version": "4.5"}

        try:
            old_mode = self.current_mode
            self.current_mode = mode

            actions = self.mode_actions.get(mode, [])
            results: List[Dict[str, Any]] = []

            if self.state_manager:
                for act in actions:
                    t = act.get("type")
                    action = act.get("action")
                    value = act.get("value")

                    if t == "room":
                        room = act.get("room")
                        if not self._validate_str(room):
                            results.append({"status": "error", "code": "invalid_room"})
                            continue

                        # special case – all rooms
                        if room == "all":
                            res = self.state_manager.set_state_for_room("all", action, value)
                        else:
                            res = self.state_manager.set_state_for_room(room, action, value)

                        results.append(res)

            if self.event_bus:
                try:
                    self.event_bus.emit("security_mode_changed", {
                        "old_mode": old_mode,
                        "new_mode": mode,
                        "results": results,
                    })
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "mode": mode, "results": results, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "set_mode_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # GET CURRENT MODE
    # ---------------------------------------------------------
    def get_mode(self) -> Dict[str, Any]:
        return {"status": "ok", "mode": self.current_mode, "version": "4.5"}

    # ---------------------------------------------------------
    # CHECK COMMAND AGAINST SECURITY MODE
    # ---------------------------------------------------------
    def check_command(self, command: str, identity: str) -> Dict[str, Any]:
        if not self._validate_str(command):
            return {"status": "error", "code": "invalid_command", "version": "4.5"}

        if not self._validate_str(identity):
            return {"status": "error", "code": "invalid_identity", "version": "4.5"}

        try:
            # 1. base safety layer
            if self.safety_guard:
                base = self.safety_guard.check_command(command, identity)
                if base.get("status") == "blocked":
                    return base

            # 2. additional restrictions based on mode
            mode = self.current_mode
            lowered = command.lower()

            if mode == "STRANGER_MODE":
                if identity.upper().strip() != "OWNER":
                    return {
                        "status": "blocked",
                        "code": "stranger_mode_restriction",
                        "mode": mode,
                        "version": "4.5",
                    }

            if mode == "VACATION":
                risky = ["open", "unlock", "otvor", "odomkni"]
                if any(w in lowered for w in risky):
                    return {
                        "status": "blocked",
                        "code": "vacation_mode_restriction",
                        "mode": mode,
                        "version": "4.5",
                    }

            return {"status": "ok", "mode": mode, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "check_failed",
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
            "current_mode": self.current_mode,
            "version": "4.5",
        }
