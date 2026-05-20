# household_4_4/home_multi_step_executor_4_4.py
"""
SIRIUS LOCAL AI – Home Multi‑Step Executor 4.4.0

Účel:
- deterministické vykonávanie viac‑krokových domácich akcií
- pipeline typu:
    1. parse príkazu
    2. safety check
    3. výber cieľových zariadení / miestností
    4. vykonanie akcií (state manager / routines / tasks)
    5. log + eventy

Vlastnosti:
- 100 % offline, žiadne AI heuristiky
- žiadne dynamické importy, eval, exec
- integrácia s:
    - HouseholdCommandParser44
    - HouseholdSafetyGuard44
    - HouseholdStateManager44
    - HouseholdRoutineEngine44
    - HomeTaskPlanner44 (voliteľne)
    - HouseholdEventBus44
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

        self.command_parser = command_parser
        self.safety_guard = safety_guard
        self.state_manager = state_manager
        self.routine_engine = routine_engine
        self.task_planner = task_planner
        self.event_bus = event_bus

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.command_parser:
                self.command_parser.initialize()
            if self.safety_guard:
                self.safety_guard.initialize()
            if self.state_manager:
                self.state_manager.initialize()
            if self.routine_engine:
                self.routine_engine.initialize()
            if self.task_planner:
                self.task_planner.initialize()
            if self.event_bus:
                self.event_bus.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # MAIN ENTRYPOINT
    # ------------------------------------------------------------------
    def execute_command(self, command: str, identity: str = "OWNER") -> Dict[str, Any]:
        """
        Hlavný vstup pre domáci príkaz (text).
        Pipeline:
        1. safety check
        2. parse
        3. route podľa typu akcie
        4. vykonanie krokov
        """

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
                return {"status": "error", "reason": "no_command_parser"}

            parsed = self.command_parser.parse(command)
            if parsed.get("status") != "ok":
                return {
                    "status": "error",
                    "stage": "parse",
                    "details": parsed,
                }

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
                result = {
                    "status": "error",
                    "reason": "unknown_intent",
                    "intent": intent,
                }

            # 4. Event log
            if self.event_bus:
                self.event_bus.emit("home_command_executed", {
                    "command": command,
                    "intent": intent,
                    "result_status": result.get("status"),
                })

            return {
                "status": "ok",
                "intent": intent,
                "result": result,
            }

        except Exception as exc:
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # DEVICE CONTROL
    # ------------------------------------------------------------------
    def _execute_device_control(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Očakávaný payload:
        {
            "action": "on" | "off" | "open" | "close" | "set",
            "target_type": "room" | "device",
            "room": "kitchen",
            "device_id": "dev_001",
            "value": any (napr. teplota)
        }
        """

        if not self.state_manager:
            return {"status": "error", "reason": "no_state_manager"}

        action = payload.get("action")
        target_type = payload.get("target_type")

        if target_type == "device":
            device_id = payload.get("device_id")
            if not device_id:
                return {"status": "error", "reason": "missing_device_id"}

            res = self.state_manager.set_state(device_id, action, payload.get("value"))
            return {"status": "ok", "details": res}

        if target_type == "room":
            room = payload.get("room")
            if not room:
                return {"status": "error", "reason": "missing_room"}

            # State manager by mal mať API na hromadné operácie
            res = self.state_manager.set_state_for_room(
                room=room,
                action=action,
                value=payload.get("value"),
            )
            return {"status": "ok", "details": res}

        return {"status": "error", "reason": "invalid_target_type"}

    # ------------------------------------------------------------------
    # ROUTINE TRIGGER
    # ------------------------------------------------------------------
    def _execute_routine(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Očakávaný payload:
        {
            "routine_name": "good_night"
        }
        """

        if not self.routine_engine:
            return {"status": "error", "reason": "no_routine_engine"}

        name = payload.get("routine_name")
        if not name:
            return {"status": "error", "reason": "missing_routine_name"}

        res = self.routine_engine.run_routine(name)
        return {"status": "ok", "details": res}

    # ------------------------------------------------------------------
    # TASK CREATE
    # ------------------------------------------------------------------
    def _execute_task_create(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Očakávaný payload:
        {
            "name": "Vyniesť smeti",
            "category": "cleaning",
            "room": "kitchen",
            "priority": "high"
        }
        """

        if not self.task_planner:
            return {"status": "error", "reason": "no_task_planner"}

        name = payload.get("name")
        category = payload.get("category")
        if not name or not category:
            return {"status": "error", "reason": "missing_name_or_category"}

        res = self.task_planner.create_task(
            name=name,
            category=category,
            room=payload.get("room"),
            priority=payload.get("priority", "medium"),
        )
        return {"status": "ok", "details": res}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "has_command_parser": self.command_parser is not None,
            "has_safety_guard": self.safety_guard is not None,
            "has_state_manager": self.state_manager is not None,
            "has_routine_engine": self.routine_engine is not None,
            "has_task_planner": self.task_planner is not None,
            "has_event_bus": self.event_bus is not None,
        }
