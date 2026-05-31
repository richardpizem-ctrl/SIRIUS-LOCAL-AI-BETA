# Runtime4 Task Queue
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class TaskQueue:
    """
    SIRIUS LOCAL AI — Task Queue (v4.5.0 PRO)

    Responsibilities:
        - Deterministic FIFO queue for task names
        - Safe-mode compatible
        - Phase‑5 ready (isolation, no exception leakage)
        - Used by TaskManager, SchedulerManager4, RuntimeManager45
    """

    def __init__(self, logger=None):
        self.logger = logger
        self.queue: list[str] = []

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[TaskQueue] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # ADD TASK
    # --------------------------------------------------------
    def add(self, task_name: str) -> None:
        """
        Add a task to the queue safely.
        Deterministic, safe-mode aware, no exception leakage.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[TaskQueue] SAFE MODE → add('{task_name}') blocked")
                return

            if not isinstance(task_name, str) or not task_name.strip():
                if self.logger:
                    self.logger.log(f"[TaskQueue] ERROR: Invalid task name '{task_name}'")
                return

            self.queue.append(task_name)

            if self.logger:
                self.logger.log(f"[TaskQueue] Added task: {task_name}")

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[TaskQueue] add() error: {exc}")

    # --------------------------------------------------------
    # POP TASK
    # --------------------------------------------------------
    def pop(self) -> str | None:
        """
        Pop next task from the queue safely.
        Returns None if queue is empty or on error.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[TaskQueue] SAFE MODE → pop() blocked")
                return None

            if not self.queue:
                if self.logger:
                    self.logger.log("[TaskQueue] pop() → queue empty")
                return None

            task = self.queue.pop(0)

            if self.logger:
                self.logger.log(f"[TaskQueue] Popped task: {task}")

            return task

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[TaskQueue] pop() error: {exc}")
            return None

    # --------------------------------------------------------
    # PEEK TASK
    # --------------------------------------------------------
    def peek(self) -> str | None:
        """Return next task without removing it."""
        try:
            if not self.queue:
                return None
            return self.queue[0]
        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[TaskQueue] peek() error: {exc}")
            return None

    # --------------------------------------------------------
    # SIZE
    # --------------------------------------------------------
    def size(self) -> int:
        """Return number of tasks in queue."""
        try:
            return len(self.queue)
        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[TaskQueue] size() error: {exc}")
            return 0

    # --------------------------------------------------------
    # CLEAR
    # --------------------------------------------------------
    def clear(self):
        """Clear the queue safely."""
        try:
            self.queue.clear()
            if self.logger:
                self.logger.log("[TaskQueue] Queue cleared")
        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[TaskQueue] clear() error: {exc}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[TaskQueue] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[TaskQueue] SAFE MODE disabled")
