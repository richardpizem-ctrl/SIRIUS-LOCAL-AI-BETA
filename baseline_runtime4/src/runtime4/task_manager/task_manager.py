# Runtime4 Task Manager
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class TaskManager:
    """
    SIRIUS LOCAL AI — Task Manager (v4.5.0 PRO)

    Responsibilities:
        - Deterministic execution of queued tasks
        - Safe-mode compatible
        - Phase‑5 ready (isolation, no exception leakage)
        - Works with SchedulerCore4, SchedulerQueue4, SchedulerManager4
    """

    def __init__(self, scheduler, queue, logger=None):
        self.scheduler = scheduler
        self.queue = queue
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.last_run_ok: bool = True

        if self.logger:
            self.logger.log("[TaskManager] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # RUN NEXT TASK
    # --------------------------------------------------------
    def run_next(self) -> bool:
        """
        Execute the next task in the queue safely.
        Deterministic, safe-mode aware, no exception leakage.
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[TaskManager] SAFE MODE → run_next() blocked")
                return False

            if self.logger:
                self.logger.log("[TaskManager] Attempting to run next task")

            # Pop next task from queue
            entry = self.queue.pop()
            if not entry:
                if self.logger:
                    self.logger.log("[TaskManager] No tasks in queue")
                self.last_run_ok = True
                return True

            task = entry.get("task")
            context = entry.get("context", {})

            if self.logger:
                self.logger.log(f"[TaskManager] Executing task: {task}")

            # Execute via scheduler
            result = self.scheduler.step() if hasattr(self.scheduler, "step") else None

            if result is None:
                if self.logger:
                    self.logger.log(f"[TaskManager] Task '{task}' returned no result")
                self.last_run_ok = False
                return False

            if self.logger:
                self.logger.log(f"[TaskManager] Task '{task}' completed → {result}")

            self.last_run_ok = True
            return True

        except Exception as exc:
            self.degraded_mode = True
            self.last_run_ok = False

            if self.logger:
                self.logger.log(f"[TaskManager] run_next() error: {exc}")

            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[TaskManager] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[TaskManager] SAFE MODE disabled")
