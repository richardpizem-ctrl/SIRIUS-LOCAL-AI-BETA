# scheduler_router.py
"""
SIRIUS LOCAL AI – Scheduler 4.0 Router

Responsible for:
- routing tasks to correct modules
- mapping task names to module handlers
- preparing execution context
- integrating scheduler with sandbox manager

This is the routing layer of Scheduler 4.0.
"""

from typing import Optional, Dict, Any


class SchedulerRouter4:
    """
    Decides which module should execute a given task.
    """

    def __init__(self, module_loader, sandbox_manager):
        # Module loader is used to resolve module names
        self.module_loader = module_loader

        # Sandbox manager executes the actual module code
        self.sandbox_manager = sandbox_manager

        # Task → module mapping table
        self.routing_table = {}

    # ---------------------------------------------------------
    # ROUTING TABLE MANAGEMENT
    # ---------------------------------------------------------

    def register_route(self, task_name: str, module_name: str):
        """
        Registers a mapping: task_name → module_name.
        """
        self.routing_table[task_name] = module_name

    def resolve_module(self, task_name: str) -> Optional[str]:
        """
        Returns the module responsible for the given task.
        """
        return self.routing_table.get(task_name)

    # ---------------------------------------------------------
    # ROUTING LOGIC
    # ---------------------------------------------------------

    def route(self, task: str, context: Optional[dict] = None) -> Dict[str, Any]:
        """
        Resolves the module and executes the task via sandbox manager.
        """
        module_name = self.resolve_module(task)

        if module_name is None:
            return {
                "error": "no_route_defined",
                "task": task
            }

        # Prepare execution context
        ctx = context or {}
        ctx["module"] = module_name

        # Execute inside sandbox
        return self.sandbox_manager.execute(
            module_name=module_name,
            task=task,
            context=ctx
        )
