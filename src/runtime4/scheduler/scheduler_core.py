"""
SIRIUS LOCAL AI – Scheduler 4.0 Core

Responsible for:
- receiving tasks
- managing task queue
- deterministic offline scheduling
- dispatching tasks to sandbox manager
- future support for task graphs

This is the core of Scheduler 4.0.
"""

from typing import Optional, Dict, Any


class SchedulerCore4:
    """
    Deterministic offline task scheduler for Runtime 4.0.
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

    # ---------------------------------------------------------
    # TASK MANAGEMENT
    # ---------------------------------------------------------

    def submit(self, task: str, context: Optional[dict] = None):
        """
        Adds a task to the scheduler queue with full safety checks.
        """

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"error": "invalid_task"}

        # Validate context
        if context is not None and not isinstance(context, dict):
            return {"error": "invalid_context_type"}

        # Ensure context is dict
        context = context or {}

        # Validate module name inside context
        module_name = context.get("module")
        if module_name is not None and (not isinstance(module_name, str) or not module_name.strip()):
            return {"error": "invalid_module_name"}

        # Store task
        self.queue.append({
            "task": task,
            "context": context
        })

        return {"status": "queued", "size": len(self.queue)}

    # ---------------------------------------------------------
    # EXECUTION LOOP
    # ---------------------------------------------------------

    def step(self) -> Optional[Dict[str, Any]]:
        """
        Executes the next task in the queue.
        Returns the result of the executed task.
        """

        # Scheduler must be active
        if not self.active:
            return {"error": "scheduler_inactive"}

        if not self.queue:
            return None

        entry = self.queue.pop(0)

        # Validate entry structure
        if not isinstance(entry, dict):
            return {"error": "invalid_queue_entry"}

        task = entry.get("task")
        context = entry.get("context", {})

        # Validate again before execution
        if not isinstance(task, str) or not task.strip():
            return {"error": "invalid_task"}

        if not isinstance(context, dict):
            return {"error": "invalid_context_type"}

        module_name = context.get("module")
        if module_name is not None and (not isinstance(module_name, str) or not module_name.strip()):
            return {"error": "invalid_module_name"}

        # Dispatch to sandbox manager
        return self.sandbox_manager.execute(
            module_name=module_name,
            task=task,
            context=context
        )

    def run_all(self):
        """
        Executes all tasks in the queue until empty.
        """
        results = []

        # Scheduler must be active
        if not self.active:
            return [{"error": "scheduler_inactive"}]

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
