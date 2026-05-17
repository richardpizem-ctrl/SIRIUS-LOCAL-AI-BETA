"""
SIRIUS LOCAL AI – Scheduler 4.3 Manager

Responsible for:
- integrating SchedulerCore4, SchedulerRouter4, SchedulerQueue4
- providing unified scheduling API
- managing task lifecycle
- coordinating execution with sandbox manager
- supporting safe-mode and degraded-mode behavior

This is the orchestration layer of Scheduler 4.3.
"""

from typing import Optional, Dict, Any


class SchedulerManager4:
    """
    High-level orchestrator for Scheduler 4.3.
    Provides:
    - unified scheduling API
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
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
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def submit(self, task: str, context: Optional[dict] = None):
        """
        Adds a task to the queue with safety checks.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Task submission disabled in safe-mode."
            }

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"status": "error", "code": "invalid_task"}

        # Validate context
        if context is not None and not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type"}

        context = context or {}

        # Validate module name if present
        module_name = context.get("module")
        if module_name is not None and (not isinstance(module_name, str) or not module_name.strip()):
            return {"status": "error", "code": "invalid_module_name"}

        try:
            return self.queue.push(task, context)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "queue_push_failed",
                "exception": str(exc)
            }

    def start(self):
        """
        Activates the scheduler.
        """
        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Scheduler start disabled in safe-mode."
            }

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

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Scheduler execution disabled in safe-mode."
            }

        # Scheduler must be active
        if not self.active:
            return {"status": "error", "code": "scheduler_inactive"}

        entry = self.queue.pop()
        if not entry:
            return None

        # Validate entry structure
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

        # Validate module name
        module_name = context.get("module")
        if module_name is not None and (not isinstance(module_name, str) or not module_name.strip()):
            return {"status": "error", "code": "invalid_module_name"}

        try:
            # Route task to correct module
            return self.router.route(task, context)
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "routing_failed",
                "exception": str(exc)
            }

    def run_all(self):
        """
        Executes all tasks until the queue is empty.
        """

        if self.safe_mode:
            return [{
                "status": "safe_mode",
                "message": "Scheduler execution disabled in safe-mode."
            }]

        # Scheduler must be active
        if not self.active:
            return [{"status": "error", "code": "scheduler_inactive"}]

        results = []
        while self.queue.size() > 0:
            results.append(self.step())
        return results
