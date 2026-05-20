# household_4_4/ha_core_4_4.py
"""
SIRIUS LOCAL AI – Household Core 4.4.0

Hlavné jadro Household Automation 4.4.

Účel:
- centralizované rozhranie pre všetky domáce akcie
- orchestrácia:
    - Device Registry 4.4
    - State Manager 4.4
    - Routine Engine 4.4
    - Room Mapper 4.4
    - Command Parser 4.4
    - Safety Guard 4.4
    - Event Bus 4.4
    - Context Memory 4.4
    - Home Task Planner 4.4 (voliteľne)
    - Home Device Diagnostics 4.4 (voliteľne)
    - Home Multi‑Step Executor 4.4

Vlastnosti:
- 100 % offline, deterministické
- žiadne AI heuristiky
- žiadne dynamické importy, eval, exec
"""

from typing import Dict, Any, Optional


class HouseholdCore44:
    """
    Hlavné jadro Household Automation 4.4.
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
        self.degraded_mode = False

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.device_registry:
                self.device_registry.initialize()
            if self.state_manager:
                self.state_manager.initialize()
            if self.routine_engine:
                self.routine_engine.initialize()
            if self.room_mapper:
                self.room_mapper.initialize()
            if self.command_parser:
                self.command_parser.initialize()
            if self.safety_guard:
                self.safety_guard.initialize()
            if self.event_bus:
                self.event_bus.initialize()
            if self.context_memory:
                self.context_memory.initialize()
            if self.task_planner:
                self.task_planner.initialize()
            if self.device_diagnostics:
                self.device_diagnostics.initialize()
            if self.multi_step_executor:
                self.multi_step_executor.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # MAIN ENTRYPOINT – COMMAND
    # ------------------------------------------------------------------
    def handle_command(self, command: str, identity: str = "OWNER") -> Dict[str, Any]:
        """
        Hlavný vstupný bod pre domáce príkazy (text).
        Ak je k dispozícii HomeMultiStepExecutor44, použije sa.
        Inak sa vráti jednoduchá chyba.
        """

        if not self.initialized:
            init = self.initialize()
            if init.get("status") not in ("initialized", "already_initialized"):
                return init

        if not self.multi_step_executor:
            return {
                "status": "error",
                "reason": "no_multi_step_executor",
            }

        return self.multi_step_executor.execute_command(command, identity=identity)

    # ------------------------------------------------------------------
    # DIAGNOSTICS
    # ------------------------------------------------------------------
    def run_device_diagnostics(self) -> Dict[str, Any]:
        if not self.device_diagnostics:
            return {"status": "error", "reason": "no_device_diagnostics"}

        return self.device_diagnostics.run_diagnostics()

    # ------------------------------------------------------------------
    # TASKS SHORTCUTS
    # ------------------------------------------------------------------
    def create_task(
        self,
        name: str,
        category: str,
        room: Optional[str] = None,
        priority: str = "medium",
    ) -> Dict[str, Any]:
        if not self.task_planner:
            return {"status": "error", "reason": "no_task_planner"}

        return self.task_planner.create_task(
            name=name,
            category=category,
            room=room,
            priority=priority,
        )

    def list_tasks(self, include_completed: bool = True) -> Dict[str, Any]:
        if not self.task_planner:
            return {"status": "error", "reason": "no_task_planner"}

        return self.task_planner.list_tasks(include_completed=include_completed)

    # ------------------------------------------------------------------
    # LOW-LEVEL ACCESSORS
    # ------------------------------------------------------------------
    def get_device_registry(self):
        return self.device_registry

    def get_state_manager(self):
        return self.state_manager

    def get_routine_engine(self):
        return self.routine_engine

    def get_room_mapper(self):
        return self.room_mapper

    def get_command_parser(self):
        return self.command_parser

    def get_safety_guard(self):
        return self.safety_guard

    def get_event_bus(self):
        return self.event_bus

    def get_context_memory(self):
        return self.context_memory

    def get_task_planner(self):
        return self.task_planner

    def get_device_diagnostics(self):
        return self.device_diagnostics

    def get_multi_step_executor(self):
        return self.multi_step_executor

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "has_device_registry": self.device_registry is not None,
            "has_state_manager": self.state_manager is not None,
            "has_routine_engine": self.routine_engine is not None,
            "has_room_mapper": self.room_mapper is not None,
            "has_command_parser": self.command_parser is not None,
            "has_safety_guard": self.safety_guard is not None,
            "has_event_bus": self.event_bus is not None,
            "has_context_memory": self.context_memory is not None,
            "has_task_planner": self.task_planner is not None,
            "has_device_diagnostics": self.device_diagnostics is not None,
            "has_multi_step_executor": self.multi_step_executor is not None,
        }
