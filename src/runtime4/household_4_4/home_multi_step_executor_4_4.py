"""
SIRIUS LOCAL AI – Home Multi‑Step Executor 4.4.0 (PRO)

Účel:
- deterministické vykonávanie viac‑krokových domácich akcií
- pipeline:
    1. safety check
    2. parse
    3. route podľa intentu
    4. vykonanie akcií
    5. event log

Security Family 4.4:
- žiadne nebezpečné typy
- deterministické správanie
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, List, Optional


class HomeMultiStepExecutor44:
    """
    Deterministic multi‑step executor pre domácnosť.
    """

    def __init__(
        self,
        command_parser=None,
        safety_guard=None,
        state_manager=None,
        routine_engine=None,
        task_planner=None,
        event_bus=None,
    ):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.command_parser = command_parser
        self.safety_guard = safety_guard
        self.state_manager = state_manager
        self.routine_engine = routine_engine
        self.task_planner = task_planner
        self.event_bus = event_bus

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            modules = [
                self.command_parser,
                self.safety_guard,
                self.state_manager,
                self.routine_engine,
                self.task_planner,
                self.event_bus,
            ]

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
    # MAIN ENTRYPOINT
    # ---------------------------------------------------------
    def execute_command(self, command: str, identity: str = "OWNER") -> Dict[str, Any]:
        if self.safe_mode:
            return {"status": "safe_mode", "message": "Executor disabled in safe-mode."}

        if not self._validate_str(command):
            return {"status": "error", "code": "invalid_command"}

        if not self._validate_str(identity):
            return {"status": "error", "code": "invalid_identity"}

        try:
            # 1. Safety
            if self.safety_guard:
                safe = self.safety_guard.check_command(command, identity)
                if safe.get("status") != "ok":
                    return {
                        "status": "blocked",
                        "stage": "safety",
                        "details": safe,
                    }

            # 2. Parse
            if not self.command_parser:
                return {"status": "error", "code": "no_command_parser"}

            parsed = self.command_parser.parse(command)
            if parsed.get("status") != "ok":
                return {"status": "error", "stage": "parse", "details": parsed}

            intent = parsed.get("intent")
            payload = parsed.get("payload", {})

            # 3. Route
            if intent == "device_control":
                result = self._execute_device_control(payload)
            elif intent == "routine_trigger":
                result = self._execute_routine(payload)
            elif intent == "task_create":
                result = self._execute_task_create(payload)
            else:
                result = {"status": "error", "code": "unknown_intent", "intent": intent}

            # 4. Event log
            if self.event_bus:
                try:
                    self.event_bus.emit("home_command_executed", {
                        "command": command,
                        "intent": intent,
                        "result_status": result.get("status"),
                    })
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "intent": intent, "result": result}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "executor_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # DEVICE CONTROL
    # ---------------------------------------------------------
    def _execute_device_control(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self.state_manager:
            return {"status": "error", "code": "no_state_manager"}

        action = payload.get("action")
        target_type = payload.get("target_type")

        if not self._validate_str(action):
            return {"status": "error", "code": "invalid_action"}

        if target_type == "device":
            device_id = payload.get("device_id")
            if not self._validate_str(device_id):
                return {"status": "error", "code": "missing_device_id"}

            res = self.state_manager.set_state(device_id, action, payload.get("value"))
            return {"status": "ok", "details": res}

        if target_type == "room":
            room = payload.get("room")
            if not self._validate_str(room):
                return {"status": "error", "code": "missing_room"}

            res = self.state_manager.set_state_for_room(
                room=room,
                action=action,
                value=payload.get("value"),
            )
            return {"status": "ok", "details": res}

        return {"status": "error", "code": "invalid_target_type"}

    # ---------------------------------------------------------
    # ROUTINE TRIGGER
    # ---------------------------------------------------------
    def _execute_routine(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self.routine_engine:
            return {"status": "error", "code": "no_routine_engine"}

        name = payload.get("routine_name")
        if not self._validate_str(name):
            return {"status": "error", "code": "missing_routine_name"}

        res = self.routine_engine.run_routine(name)
        return {"status": "ok", "details": res}

    # ---------------------------------------------------------
    # TASK CREATE
    # ---------------------------------------------------------
    def _execute_task_create(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        if not self.task_planner:
            return {"status": "error", "code": "no_task_planner"}

        name = payload.get("name")
        category = payload.get("category")

        if not self._validate_str(name) or not self._validate_str(category):
            return {"status": "error", "code": "missing_name_or_category"}

        res = self.task_planner.create_task(
            name=name,
            category=category,
            room=payload.get("room"),
            priority=payload.get("priority", "medium"),
        )
        return {"status": "ok", "details": res}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "has_command_parser": self.command_parser is not None,
            "has_safety_guard": self.safety_guard is not None,
            "has_state_manager": self.state_manager is not None,
            "has_routine_engine": self.routine_engine is not None,
            "has_task_planner": self.task_planner is not None,
            "has_event_bus": self.event_bus is not None,
        }
