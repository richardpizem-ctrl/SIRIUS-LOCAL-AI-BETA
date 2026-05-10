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
        # Validate core
        if core is None or not hasattr(core, "start") or not hasattr(core, "stop"):
            raise ValueError("Invalid core: missing start/stop methods.")

        # Validate router
        if router is None or not hasattr(router, "route"):
            raise ValueError("Invalid router: missing route() method.")

        # Validate queue
        required_queue_methods = ["push", "pop", "size"]
        if queue is None or not all(hasattr(queue, m) for m in required_queue_methods):
            raise ValueError("Invalid queue: missing required queue methods.")

        self.core = core
        self.router = router
        self.queue = queue

        # State
        self.active = False

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def submit(self, task: str, context: Optional[dict] = None):
        """
        Adds a task to the queue with safety checks.
        """

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"error": "invalid_task"}

        # Validate context
        if context is not None and not isinstance(context, dict):
            return {"error": "invalid_context_type"}

        context = context or {}

        # Validate module name if present
        module_name = context.get("module")
        if module_name is not None and (not isinstance(module_name, str) or not module_name.strip()):
            return {"error": "invalid_module_name"}

        return self.queue.push(task, context)

    def start(self):
        """
        Activates the scheduler.
        """
        self.active = True
        self.core.start()
        return {"status": "scheduler_started"}

    def stop(self):
        """
        Stops the scheduler.
        """
        self.active = False
        self.core.stop()
        return {"status": "scheduler_stopped"}

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------

    def step(self) -> Optional[Dict[str, Any]]:
        """
        Executes the next task in the queue.
        """

        # Scheduler must be active
        if not self.active:
            return {"error": "scheduler_inactive"}

        entry = self.queue.pop()
        if not entry:
            return None

        # Validate entry structure
        if not isinstance(entry, dict):
            return {"error": "invalid_queue_entry"}

        task = entry.get("task")
        context = entry.get("context", {})

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"error": "invalid_task"}

        # Validate context
        if not isinstance(context, dict):
            return {"error": "invalid_context_type"}

        # Validate module name
        module_name = context.get("module")
        if module_name is not None and (not isinstance(module_name, str) or not module_name.strip()):
            return {"error": "invalid_module_name"}

        # Route task to correct module
        return self.router.route(task, context)

    def run_all(self):
        """
        Executes all tasks until the queue is empty.
        """

        # Scheduler must be active
        if not self.active:
            return [{"error": "scheduler_inactive"}]

        results = []
        while self.queue.size() > 0:
            results.append(self.step())
        return results
