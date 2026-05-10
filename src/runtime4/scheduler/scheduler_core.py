# scheduler_core.py
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
        # Sandbox manager is required for task execution
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
        Adds a task to the scheduler queue.
        """
        self.queue.append({
            "task": task,
            "context": context or {}
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
        if not self.queue:
            return None

        entry = self.queue.pop(0)
        task = entry["task"]
        context = entry["context"]

        # Scheduler does NOT decide module_name.
        # That is responsibility of higher-level routing.
        return self.sandbox_manager.execute(
            module_name=context.get("module"),
            task=task,
            context=context
        )

    def run_all(self):
        """
        Executes all tasks in the queue until empty.
        """
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

    def stop(self):
        """Stops scheduler."""
        self.active = False
