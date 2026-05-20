"""
SIRIUS LOCAL AI – Household Core 4.4.0

Hlavné jadro Household Automation 4.4.

Účel:
- centralizované rozhranie pre všetky domáce akcie
- orchestrácia modulov:
    - Device Registry 4.4
    - State Manager 4.4
    - Routine Engine 4.4
    - Room Mapper 4.4
    - Command Parser 4.4
    - Safety Guard 4.4
    - Event Bus 4.4
    - Context Memory 4.4
    - Task Planner 4.4 (voliteľné)
    - Device Diagnostics 4.4 (voliteľné)
    - Multi‑Step Executor 4.4

Vlastnosti:
- 100 % offline, deterministické
- žiadne AI heuristiky
- žiadne dynamické importy, eval, exec
"""

from typing import Dict, Any, Optional


class HouseholdCore44:
    """
    Hlavné jadro Household Automation 4.4.
    Deterministické, offline‑safe, Security Family 4.4 compliant.
    """

    def __init__(
        self,
        device_registry=None,
        state_manager=None,
        routine_engine=None,
        room_mapper=None,
        command_parser=None,
        safety_guard=None,
        event_bus=None,
        context_memory=None,
        task_planner=None,
        device_diagnostics=None,
        multi_step_executor=None,
    ):
        # Základné moduly
        self.device_registry = device_registry
        self.state_manager = state_manager
        self.routine_engine = routine_engine
        self.room_mapper = room_mapper
        self.command_parser = command_parser
        self.safety_guard = safety_guard
        self.event_bus = event_bus
        self.context_memory = context_memory

        # Doplnkové moduly
        self.task_planner = task_planner
        self.device_diagnostics = device_diagnostics
        self.multi_step_executor = multi_step_executor

        self.initialized = False
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # INTERNAL SAFE INITIALIZATION
    # ---------------------------------------------------------
    def _safe_init(self, module, name: str) -> bool:
        if not module:
            return True
        try:
            res = module.initialize()
            if isinstance(res, dict) and res.get("status") == "error":
                self.degraded_mode = True
                return False
            return True
        except Exception:
            self.degraded_mode = True
            return False

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            modules = {
                "device_registry": self.device_registry,
                "state_manager": self.state_manager,
                "routine_engine": self.routine_engine,
                "room_mapper": self.room_mapper,
                "command_parser": self.command_parser,
                "safety_guard": self.safety_guard,
                "event_bus": self.event_bus,
                "context_memory": self.context_memory,
                "task_planner": self.task_planner,
                "device_diagnostics": self.device_diagnostics,
                "multi_step_executor": self.multi_step_executor,
            }

            for name, module in modules.items():
                if not self._safe_init(module, name):
                    return {
                        "status": "error",
                        "code": "module_init_failed",
                        "module": name,
                        "degraded_mode": self.degraded_mode,
                    }

            self.initialized = True
            return {"status": "initialized", "degraded_mode": self.degraded_mode}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ---------------------------------------------------------
    # MAIN ENTRYPOINT – COMMAND
    # ---------------------------------------------------------
    def handle_command(self, command: str, identity: str = "OWNER") -> Dict[str, Any]:
        """
        Hlavný vstupný bod pre domáce príkazy (text).
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Household core disabled in safe-mode.",
                "degraded_mode": self.degraded_mode,
            }

        if not self.initialized:
            init = self.initialize()
            if init.get("status") != "initialized":
                return init

        if not isinstance(command, str):
            return {"status": "error", "code": "invalid_command_type"}

        if not self.multi_step_executor:
            return {
                "status": "error",
                "code": "no_multi_step_executor",
                "degraded_mode": self.degraded_mode,
            }

        try:
            return self.multi_step_executor.execute_command(
                command,
                identity=identity,
            )
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "executor_failure",
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # DEVICE DIAGNOSTICS
    # ---------------------------------------------------------
    def run_device_diagnostics(self) -> Dict[str, Any]:
        if not self.device_diagnostics:
            return {"status": "error", "code": "no_device_diagnostics"}

        try:
            return self.device_diagnostics.run_diagnostics()
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "diagnostics_failure",
                "exception": str(exc),
            }

    # ---------------------------------------------------------
    # TASK SHORTCUTS
    # ---------------------------------------------------------
    def create_task(self, name: str, category: str, room: Optional[str] = None, priority: str = "medium") -> Dict[str, Any]:
        if not self.task_planner:
            return {"status": "error", "code": "no_task_planner"}

        try:
            return self.task_planner.create_task(
                name=name,
                category=category,
                room=room,
                priority=priority,
            )
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "task_create_failed", "exception": str(exc)}

    def list_tasks(self, include_completed: bool = True) -> Dict[str, Any]:
        if not self.task_planner:
            return {"status": "error", "code": "no_task_planner"}

        try:
            return self.task_planner.list_tasks(include_completed=include_completed)
        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "task_list_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "modules": {
                "device_registry": self.device_registry is not None,
                "state_manager": self.state_manager is not None,
                "routine_engine": self.routine_engine is not None,
                "room_mapper": self.room_mapper is not None,
                "command_parser": self.command_parser is not None,
                "safety_guard": self.safety_guard is not None,
                "event_bus": self.event_bus is not None,
                "context_memory": self.context_memory is not None,
                "task_planner": self.task_planner is not None,
                "device_diagnostics": self.device_diagnostics is not None,
                "multi_step_executor": self.multi_step_executor is not None,
            },
        }
