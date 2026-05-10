# scheduler_queue.py
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
        Adds a task to the end of the queue.
        """
        self._queue.append({
            "task": task,
            "context": context or {}
        })
        return {"status": "queued", "size": len(self._queue)}

    def pop(self) -> Optional[Dict[str, Any]]:
        """
        Removes and returns the next task from the queue.
        """
        if not self._queue:
            return None
        return self._queue.pop(0)

    def peek(self) -> Optional[Dict[str, Any]]:
        """
        Returns the next task without removing it.
        """
        if not self._queue:
            return None
        return self._queue[0]

    # ---------------------------------------------------------
    # STATE
    # ---------------------------------------------------------

    def size(self) -> int:
        """Returns number of tasks in the queue."""
        return len(self._queue)

    def clear(self):
        """Clears all tasks from the queue."""
        self._queue.clear()
