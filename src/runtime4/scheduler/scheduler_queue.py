"""
SIRIUS LOCAL AI – Scheduler 4.0 Queue

Responsible for:
- deterministic FIFO task ordering
- isolated queue management
- future support for priority scheduling
- safe enqueue/dequeue operations

This is the queue layer of Scheduler 4.0.
"""

from typing import Optional, Dict, Any


class SchedulerQueue4:
    """
    Simple deterministic FIFO queue for Scheduler 4.0.
    """

    def __init__(self):
        # Internal FIFO list
        self._queue = []

    # ---------------------------------------------------------
    # QUEUE OPERATIONS
    # ---------------------------------------------------------

    def push(self, task: str, context: Optional[dict] = None):
        """
        Adds a task to the end of the queue with full safety checks.
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

        # Store entry
        self._queue.append({
            "task": task,
            "context": context
        })

        return {"status": "queued", "size": len(self._queue)}

    def pop(self) -> Optional[Dict[str, Any]]:
        """
        Removes and returns the next task from the queue.
        Includes safety checks.
        """
        if not self._queue:
            return None

        entry = self._queue.pop(0)

        # Validate entry
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

        return entry

    def peek(self) -> Optional[Dict[str, Any]]:
        """
        Returns the next task without removing it.
        Includes safety checks.
        """
        if not self._queue:
            return None

        entry = self._queue[0]

        if not isinstance(entry, dict):
            return {"error": "invalid_queue_entry"}

        return entry

    # ---------------------------------------------------------
    # STATE
    # ---------------------------------------------------------

    def size(self) -> int:
        """Returns number of tasks in the queue."""
        return len(self._queue)

    def clear(self):
        """Clears all tasks from the queue."""
        self._queue.clear()
