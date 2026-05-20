"""
SIRIUS LOCAL AI – Scheduler 4.3 Core (PRO)

Responsible for:
- receiving tasks
- managing task queue
- deterministic offline scheduling
- dispatching tasks to sandbox manager
- future support for task graphs
- safe-mode and degraded-mode behavior

Security Family 4.4 Compliance:
- No eval, exec, reflection, dynamic imports
- Strict input validation
- Deterministic behavior
- Self‑Repair 4.4 ready
"""

from typing import Optional, Dict, Any


class SchedulerCore4:
    """
    Deterministic offline task scheduler for Runtime 4.3 (PRO).
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self, sandbox_manager):
        # Validate sandbox manager
        if sandbox_manager is None or not hasattr(sandbox_manager, "execute"):
            raise ValueError("Invalid sandbox_manager: missing execute() method.")

        self.sandbox_manager = sandbox_manager

        # FIFO task queue (deterministic)
        self.queue = []

        # Scheduler state
        self.active = False
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # TASK MANAGEMENT
    # ---------------------------------------------------------

    def submit(self, task: str, context: Optional[dict] = None):
        """Adds a task to the scheduler queue with full safety checks."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Task submission disabled in safe-mode.",
            }

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"status": "error", "code": "invalid_task"}

        # Validate context
        if context is not None and not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type"}

        context = context or {}

        # Validate module name inside context
        module_name = context.get("module")
        if module_name is not None:
            if not isinstance(module_name, str) or not module_name.strip():
                return {"status": "error", "code": "invalid_module_name"}

        try:
            self.queue.append({"task": task, "context": context})
            return {
                "status": "queued",
                "size": len(self.queue),
                "degraded_mode": self.degraded_mode,
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "queue_append_failed",
                "exception": str(exc),
            }

    # ---------------------------------------------------------
    # EXECUTION LOOP
    # ---------------------------------------------------------

    def step(self) -> Optional[Dict[str, Any]]:
        """Executes the next task in the queue."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Scheduler execution disabled in safe-mode.",
            }

        if not self.active:
            return {"status": "error", "code": "scheduler_inactive"}

        if not self.queue:
            return None

        try:
            entry = self.queue.pop(0)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "queue_pop_failed",
                "exception": str(exc),
            }

        # Validate entry
        if not isinstance(entry, dict):
            return {"status": "error", "code": "invalid_queue_entry"}

        task = entry.get("task")
        context = entry.get("context", {})

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"status": "error", "code": "invalid_task"}

        # Validate context
        if not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type"}

        module_name = context.get("module")
        if module_name is not None:
            if not isinstance(module_name, str) or not module_name.strip():
                return {"status": "error", "code": "invalid_module_name"}

        # Execute in sandbox
        try:
            return self.sandbox_manager.execute(
                module_name=module_name,
                task=task,
                context=context,
            )
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "sandbox_execution_failed",
                "exception": str(exc),
            }

    # ---------------------------------------------------------
    # RUN ALL
    # ---------------------------------------------------------

    def run_all(self):
        """Executes all tasks in the queue until empty."""

        if self.safe_mode:
            return [{
                "status": "safe_mode",
                "message": "Scheduler execution disabled in safe-mode.",
            }]

        if not self.active:
            return [{"status": "error", "code": "scheduler_inactive"}]

        results = []
        while self.queue:
            results.append(self.step())

        return results

    # ---------------------------------------------------------
    # CONTROL
    # ---------------------------------------------------------

    def start(self):
        """Marks scheduler as active."""
        self.active = True
        return {"status": "scheduler_started"}

    def stop(self):
        """Stops scheduler."""
        self.active = False
        return {"status": "scheduler_stopped"}
