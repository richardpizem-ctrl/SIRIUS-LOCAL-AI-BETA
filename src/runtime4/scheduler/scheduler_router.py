"""
SIRIUS LOCAL AI – Scheduler 4.5 Router (PRO)

Responsible for:
- routing tasks to correct modules
- mapping task names to module handlers
- preparing execution context
- integrating scheduler with sandbox manager
- safe-mode and degraded-mode behavior

Security Family 4.5 Compliance:
- No eval, exec, reflection, dynamic imports
- Strict input validation
- Deterministic behavior
- Self‑Repair 4.5 ready
"""

from typing import Optional, Dict, Any


class SchedulerRouter45:
    """
    Deterministic routing layer for Scheduler 4.5 (PRO).
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, module_loader, sandbox_manager):
        # Validate module_loader
        if module_loader is None or not hasattr(module_loader, "get_module"):
            raise ValueError("Invalid module_loader: missing get_module() method.")

        # Validate sandbox_manager
        if sandbox_manager is None or not hasattr(sandbox_manager, "execute"):
            raise ValueError("Invalid sandbox_manager: missing execute() method.")

        self.module_loader = module_loader
        self.sandbox_manager = sandbox_manager

        # Task → module mapping table
        self.routing_table: Dict[str, str] = {}

        self.safe_mode = False
        self.degraded_mode = False
        self.version = "4.5"

    # ---------------------------------------------------------
    # ROUTING TABLE MANAGEMENT
    # ---------------------------------------------------------

    def register_route(self, task_name: str, module_name: str):
        """Registers a mapping: task_name → module_name."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Route registration disabled in safe-mode.",
                "version": self.version,
            }

        # Validate task_name
        if not isinstance(task_name, str) or not task_name.strip():
            return {"status": "error", "code": "invalid_task_name", "version": self.version}

        # Validate module_name
        if not isinstance(module_name, str) or not module_name.strip():
            return {"status": "error", "code": "invalid_module_name", "version": self.version}

        # Validate module exists
        if self.module_loader.get_module(module_name) is None:
            return {"status": "error", "code": "unknown_module", "version": self.version}

        try:
            self.routing_table[task_name] = module_name
            return {
                "status": "route_registered",
                "degraded_mode": self.degraded_mode,
                "version": self.version,
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "route_registration_failed",
                "exception": str(exc),
                "version": self.version,
            }

    def resolve_module(self, task_name: str) -> Optional[str]:
        """Returns the module responsible for the given task."""

        if not isinstance(task_name, str) or not task_name.strip():
            return None

        module_name = self.routing_table.get(task_name)

        # Validate module exists
        if module_name and self.module_loader.get_module(module_name) is None:
            return None

        return module_name

    # ---------------------------------------------------------
    # ROUTING LOGIC
    # ---------------------------------------------------------

    def route(self, task: str, context: Optional[dict] = None) -> Dict[str, Any]:
        """
        Resolves the module and executes the task via sandbox manager.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Routing disabled in safe-mode.",
                "version": self.version,
            }

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"status": "error", "code": "invalid_task", "version": self.version}

        # Validate context
        if context is not None and not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type", "version": self.version}

        context = context or {}

        # Resolve module
        module_name = self.resolve_module(task)
        if module_name is None:
            return {
                "status": "error",
                "code": "no_route_defined",
                "task": task,
                "version": self.version,
            }

        # Validate module exists
        if self.module_loader.get_module(module_name) is None:
            return {"status": "error", "code": "unknown_module", "version": self.version}

        # Prepare execution context
        context["module"] = module_name

        try:
            # Execute inside sandbox
            result = self.sandbox_manager.execute(
                module_name=module_name,
                task=task,
                context=context,
            )
            if isinstance(result, dict) and "version" not in result:
                result["version"] = self.version
            return result
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "sandbox_execution_failed",
                "exception": str(exc),
                "version": self.version,
            }
