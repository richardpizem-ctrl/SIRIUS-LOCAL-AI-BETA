"""
SIRIUS LOCAL AI – Runtime 4.0 Scheduler

The Scheduler is responsible for:
- task queue management
- priority routing
- safe‑mode restrictions
- schoolwork priority bypass
- parallel execution rules
- integration with the dependency graph
- deterministic offline execution

This is the execution engine of Runtime 4.0.
"""

from typing import Optional, Any, Dict


class Scheduler4:
    """
    Task scheduler for Runtime 4.0.
    Handles task dispatching, prioritization, and execution flow.
    """

    def __init__(self, max_queue_size: int = 500):
        self.task_queue = []
        self.running = False
        self.safe_mode = False
        self.schoolwork_priority = True
        self.max_queue_size = max_queue_size

    # ---------------------------------------------------------
    # INTERNAL VALIDATION HELPERS
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

    def add_task(self, task: str, context: Optional[dict] = None, priority: int = 1):
        """
        Adds a task to the queue with full safety checks.
        Priority 0 = highest, 5 = lowest.
        """

        # Validate task
        if not self._validate_task(task):
            return {"error": "invalid_task"}

        # Validate context
        if not self._validate_context(context):
            return {"error": "invalid_context"}

        # Validate priority
        if not self._validate_priority(priority):
            return {"error": "invalid_priority"}

        # Queue size limit
        if len(self.task_queue) >= self.max_queue_size:
            return {"error": "queue_overflow"}

        # Store task
        self.task_queue.append({
            "task": task,
            "context": context or {},
            "priority": priority
        })

        return {"status": "queued", "size": len(self.task_queue)}

    def get_next_task(self) -> Optional[Dict[str, Any]]:
        """
        Retrieves the next task based on priority rules.
        Includes safety checks.
        """

        if not self.task_queue:
            return None

        # Sort by priority (lower = higher priority)
        try:
            self.task_queue.sort(key=lambda t: t["priority"])
        except Exception:
            return {"error": "invalid_queue_structure"}

        entry = self.task_queue.pop(0)

        # Validate entry structure
        if not isinstance(entry, dict):
            return {"error": "invalid_queue_entry"}

        if not self._validate_task(entry.get("task")):
            return {"error": "invalid_task_in_queue"}

        if not self._validate_context(entry.get("context")):
            return {"error": "invalid_context_in_queue"}

        return entry

    # ---------------------------------------------------------
    # EXECUTION LOOP
    # ---------------------------------------------------------

    def start(self):
        """Starts the scheduler loop safely."""
        self.running = True
        return {"status": "scheduler_started"}

    def stop(self):
        """Stops the scheduler loop safely."""
        self.running = False
        return {"status": "scheduler_stopped"}

    def tick(self) -> Optional[Any]:
        """
        Executes a single scheduler cycle.
        Returns the result of the executed task.
        """

        if not self.running:
            return {"error": "scheduler_not_running"}

        task = self.get_next_task()
        if not task:
            return None

        # Safe-mode restrictions
        if self.safe_mode and task["priority"] > 1:
            return {"error": "blocked_by_safe_mode", "task": task["task"]}

        # Schoolwork priority bypass
        if self.schoolwork_priority:
            ctx = task["context"]
            if isinstance(ctx, dict) and ctx.get("type") == "schoolwork":
                task["priority"] = 0

        # Placeholder for integration with RuntimeCore4
        return {
            "status": "scheduled",
            "task": task["task"],
            "context": task["context"]
        }
