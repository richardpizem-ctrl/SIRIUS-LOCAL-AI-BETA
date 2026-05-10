# scheduler_manager.py
"""
SIRIUS LOCAL AI – Scheduler 4.0 Manager

Responsible for:
- integrating SchedulerCore4, SchedulerRouter4, SchedulerQueue4
- providing unified scheduling API
- managing task lifecycle
- coordinating execution with sandbox manager

This is the orchestration layer of Scheduler 4.0.
"""

from typing import Optional, Dict, Any


class SchedulerManager4:
    """
    High-level orchestrator for Scheduler 4.0.
    """

    def __init__(self, core, router, queue):
        # Core scheduler (execution engine)
        self.core = core

        # Router (task → module mapping)
        self.router = router

        # FIFO queue
        self.queue = queue

        # State
        self.active = False

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def submit(self, task: str, context: Optional[dict] = None):
        """
        Adds a task to the queue.
        """
        return self.queue.push(task, context)

    def start(self):
        """
        Activates the scheduler.
        """
        self.active = True
        self.core.start()

    def stop(self):
        """
        Stops the scheduler.
        """
        self.active = False
        self.core.stop()

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------

    def step(self) -> Optional[Dict[str, Any]]:
        """
        Executes the next task in the queue.
        """
        entry = self.queue.pop()
        if not entry:
            return None

        task = entry["task"]
        context = entry["context"]

        # Route task to correct module
        return self.router.route(task, context)

    def run_all(self):
        """
        Executes all tasks until the queue is empty.
        """
        results = []
        while self.queue.size() > 0:
            results.append(self.step())
        return results
