"""
SIRIUS LOCAL AI – Scheduler 4.3 Queue (PRO)

Responsible for:
- deterministic FIFO task ordering
- isolated queue management
- future support for priority scheduling
- safe enqueue/dequeue operations
- safe-mode and degraded-mode behavior

Security Family 4.4 Compliance:
- No eval, exec, reflection, dynamic imports
- Strict input validation
- Deterministic behavior
- Self‑Repair 4.4 ready
"""

from typing import Optional, Dict, Any


class SchedulerQueue4:
    """
    Deterministic FIFO queue for Scheduler 4.3 (PRO).
    Provides:
    - strict validation
    - structured error surface
    - safe-mode compatibility
    - degraded-mode detection
    """

    def __init__(self):
        self._queue = []
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # QUEUE OPERATIONS
    # ---------------------------------------------------------

    def push(self, task: str, context: Optional[dict] = None):
        """Adds a task to the end of the queue with full safety checks."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Queue push disabled in safe-mode.",
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
        if module_name is not None:
            if not isinstance(module_name, str) or not module_name.strip():
                return {"status": "error", "code": "invalid_module_name"}

        try:
            self._queue.append({"task": task, "context": context})
            return {
                "status": "queued",
                "size": len(self._queue),
                "degraded_mode": self.degraded_mode,
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "queue_push_failed",
                "exception": str(exc),
            }

    def pop(self) -> Optional[Dict[str, Any]]:
        """Removes and returns the next task from the queue."""

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Queue pop disabled in safe-mode.",
            }

        if not self._queue:
            return None

        try:
            entry = self._queue.pop(0)
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

        # Validate module name
        module_name = context.get("module")
        if module_name is not None:
            if not isinstance(module_name, str) or not module_name.strip():
                return {"status": "error", "code": "invalid_module_name"}

        return entry

    def peek(self) -> Optional[Dict[str, Any]]:
        """Returns the next task without removing it."""

        if not self._queue:
            return None

        entry = self._queue[0]

        if not isinstance(entry, dict):
            return {"status": "error", "code": "invalid_queue_entry"}

        return entry

    # ---------------------------------------------------------
    # STATE
    # ---------------------------------------------------------

    def size(self) -> int:
        """Returns number of tasks in the queue."""
        return len(self._queue)

    def clear(self):
        """Clears all tasks from the queue."""
        try:
            self._queue.clear()
            return {"status": "ok"}
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "queue_clear_failed",
                "exception": str(exc),
            }
