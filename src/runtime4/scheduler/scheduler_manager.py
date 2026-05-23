"""
SIRIUS LOCAL AI – Scheduler 4.5 Manager (PRO)

Responsible for:
- integrating SchedulerCore45, SchedulerRouter45, SchedulerQueue45
- providing unified scheduling API
- managing task lifecycle
- coordinating execution with sandbox manager
- supporting safe-mode and degraded-mode behavior

Security Family 4.5 Compliance:
- No eval, exec, reflection, dynamic imports
- Strict input validation
- Deterministic behavior
- Self‑Repair 4.5 ready
"""

from typing import Optional, Dict, Any


class SchedulerManager45:
    """
    High-level orchestrator for Scheduler 4.5 (PRO).
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
        self.version = "4.5"

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def submit(self, task: str, context: Optional[dict] = None):
        """Adds a task to the queue with safety checks."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Task submission disabled in safe-mode.",
                "version": self.version,
            }

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"status": "error", "code": "invalid_task", "version": self.version}

        # Validate context
        if context is not None and not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type", "version": self.version}

        context = context or {}

        # Validate module name if present
        module_name = context.get("module")
        if module_name is not None:
            if not isinstance(module_name, str) or not module_name.strip():
                return {"status": "error", "code": "invalid_module_name", "version": self.version}

        try:
            result = self.queue.push(task, context)
            result["version"] = self.version
            return result
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "queue_push_failed",
                "exception": str(exc),
                "version": self.version,
            }

    def start(self):
        """Activates the scheduler."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Scheduler start disabled in safe-mode.",
                "version": self.version,
            }

        self.active = True
        self.core.start()
        return {"status": "scheduler_started", "version": self.version}

    def stop(self):
        """Stops the scheduler."""
        self.active = False
        self.core.stop()
        return {"status": "scheduler_stopped", "version": self.version}

    # ---------------------------------------------------------
    # EXECUTION
    # ---------------------------------------------------------

    def step(self) -> Optional[Dict[str, Any]]:
        """Executes the next task in the queue."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Scheduler execution disabled in safe-mode.",
                "version": self.version,
            }

        if not self.active:
            return {"status": "error", "code": "scheduler_inactive", "version": self.version}

        entry = self.queue.pop()
        if not entry:
            return None

        # Validate entry structure
        if not isinstance(entry, dict):
            return {"status": "error", "code": "invalid_queue_entry", "version": self.version}

        task = entry.get("task")
        context = entry.get("context", {})

        # Validate task
        if not isinstance(task, str) or not task.strip():
            return {"status": "error", "code": "invalid_task", "version": self.version}

        # Validate context
        if not isinstance(context, dict):
            return {"status": "error", "code": "invalid_context_type", "version": self.version}

        # Validate module name
        module_name = context.get("module")
        if module_name is not None:
            if not isinstance(module_name, str) or not module_name.strip():
                return {"status": "error", "code": "invalid_module_name", "version": self.version}

        try:
            # Route task to correct module
            result = self.router.route(task, context)
            result["version"] = self.version
            return result
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "routing_failed",
                "exception": str(exc),
                "version": self.version,
            }

    def run_all(self):
        """Executes all tasks until the queue is empty."""

        if self.safe_mode:
            return [{
                "status": "safe_mode",
                "message": "Scheduler execution disabled in safe-mode.",
                "version": self.version,
            }]

        if not self.active:
            return [{"status": "error", "code": "scheduler_inactive", "version": self.version}]

        results = []
        while self.queue.size() > 0:
            results.append(self.step())

        return results
