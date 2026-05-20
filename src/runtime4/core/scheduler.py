"""
SIRIUS LOCAL AI – Runtime 4.4 Scheduler

Responsible for:
- task queue management
- priority routing
- safe‑mode restrictions
- schoolwork priority bypass
- deterministic execution
- structured telemetry
- degraded‑mode detection
- Self‑Repair 4.4 compatibility

This is the execution engine of Runtime 4.4.
"""

from typing import Optional, Any, Dict, List


class Scheduler4:
    """
    Task scheduler for Runtime 4.4.
    Handles task dispatching, prioritization, and execution flow
    with deterministic, structured behavior.
    """

    def __init__(self, max_queue_size: int = 500):
        self.task_queue: List[Dict[str, Any]] = []
        self.running = False
        self.safe_mode = False
        self.schoolwork_priority = True
        self.max_queue_size = max_queue_size
        self.degraded_mode = False

    # ---------------------------------------------------------
    # VALIDATION HELPERS
    # ---------------------------------------------------------

    def _validate_task(self, task: Any) -> bool:
        return isinstance(task, str) and task.strip()

    def _validate_context(self, context: Any) -> bool:
        if context is None:
            return True
        if not isinstance(context, dict):
            return False
        for key, value in context.items():
            if not isinstance(key, str) or not key.strip():
                return False
            if isinstance(value, (bytes, bytearray, type(lambda: None))):
                return False
        return True

    def _validate_priority(self, priority: Any) -> bool:
        return isinstance(priority, int) and 0 <= priority <= 5

    # ---------------------------------------------------------
    # TASK MANAGEMENT
    # ---------------------------------------------------------

    def add_task(
        self,
        task: str,
        context: Optional[dict] = None,
        priority: int = 1
    ) -> Dict[str, Any]:
        """
        Adds a task to the queue with full safety checks.
        Priority 0 = highest, 5 = lowest.
        """

        if not self._validate_task(task):
            return {"status": "error", "code": "invalid_task"}

        if not self._validate_context(context):
            return {"status": "error", "code": "invalid_context"}

        if not self._validate_priority(priority):
            return {"status": "error", "code": "invalid_priority"}

        if len(self.task_queue) >= self.max_queue_size:
            return {"status": "error", "code": "queue_overflow"}

        entry = {
            "task": task,
            "context": context or {},
            "priority": priority,
        }

        self.task_queue.append(entry)

        return {
            "status": "queued",
            "size": len(self.task_queue),
            "task": task,
            "priority": priority,
        }

    def get_next_task(self) -> Optional[Dict[str, Any]]:
        """
        Retrieves the next task based on priority rules.
        Includes safety checks and degraded-mode detection.
        """

        if not self.task_queue:
            return None

        try:
            self.task_queue.sort(key=lambda t: t["priority"])
        except Exception:
            self.degraded_mode = True
            return {"status": "error", "code": "invalid_queue_structure"}

        entry = self.task_queue.pop(0)

        if not isinstance(entry, dict):
            self.degraded_mode = True
            return {"status": "error", "code": "invalid_queue_entry"}

        if not self._validate_task(entry.get("task")):
            self.degraded_mode = True
            return {"status": "error", "code": "invalid_task_in_queue"}

        if not self._validate_context(entry.get("context")):
            self.degraded_mode = True
            return {"status": "error", "code": "invalid_context_in_queue"}

        return entry

    # ---------------------------------------------------------
    # EXECUTION LOOP
    # ---------------------------------------------------------

    def start(self) -> Dict[str, Any]:
        self.running = True
        return {"status": "success", "message": "scheduler_started"}

    def stop(self) -> Dict[str, Any]:
        self.running = False
        return {"status": "success", "message": "scheduler_stopped"}

    def tick(self) -> Optional[Dict[str, Any]]:
        """
        Executes a single scheduler cycle.
        Returns the result of the scheduled task envelope.
        """

        if not self.running:
            return {"status": "error", "code": "scheduler_not_running"}

        task = self.get_next_task()
        if not task:
            return None

        if isinstance(task, dict) and task.get("status") == "error":
            return task

        # SAFE MODE
        if self.safe_mode and task["priority"] > 1:
            return {
                "status": "blocked",
                "code": "blocked_by_safe_mode",
                "task": task["task"],
            }

        # SCHOOLWORK PRIORITY BOOST
        if self.schoolwork_priority:
            ctx = task["context"]
            if isinstance(ctx, dict) and ctx.get("type") == "schoolwork":
                task["priority"] = 0

        return {
            "status": "scheduled",
            "task": task["task"],
            "context": task["context"],
            "priority": task["priority"],
        }
