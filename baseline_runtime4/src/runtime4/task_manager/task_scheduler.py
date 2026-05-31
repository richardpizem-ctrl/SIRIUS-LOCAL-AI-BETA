# Runtime4 Task Scheduler
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class TaskScheduler:
    """
    SIRIUS LOCAL AI — Task Scheduler (v4.5.0 PRO)

    Responsibilities:
        - Deterministic scheduling of tasks into TaskQueue
        - Safe-mode compatible
        - Phase‑5 ready (isolation, no exception leakage)
        - Used by TaskManager, SchedulerManager4, RuntimeManager45
    """

    def __init__(self, queue, logger=None):
        self.queue = queue
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        if self.logger:
            self.logger.log("[TaskScheduler] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # SCHEDULE TASK
    # --------------------------------------------------------
    def schedule(self, task_name: str) -> bool:
        """
        Schedule a task safely.
        Deterministic, safe-mode aware, no exception leakage.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log(f"[TaskScheduler] SAFE MODE → schedule('{task_name}') blocked")
                return False

            if not isinstance(task_name, str) or not task_name.strip():
                if self.logger:
                    self.logger.log(f"[TaskScheduler] ERROR: Invalid task name '{task_name}'")
                return False

            # Add to queue
            self.queue.add(task_name)

            if self.logger:
                self.logger.log(f"[TaskScheduler] Scheduled task: {task_name}")

            return True

        except Exception as exc:
            self.degraded_mode = True
            if self.logger:
                self.logger.log(f"[TaskScheduler] schedule() error: {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[TaskScheduler] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[TaskScheduler] SAFE MODE disabled")
