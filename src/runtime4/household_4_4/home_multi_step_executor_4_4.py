"""
SIRIUS LOCAL AI – Home Maintenance Scheduler 4.5.0

Purpose:
- deterministic household maintenance scheduling
- 100% offline, no AI heuristics, no dynamic imports

Security Family 4.5:
- no dangerous types
- deterministic behavior
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta


class HomeMaintenanceScheduler45:
    """
    Deterministic maintenance scheduler for household tasks 4.5.
    """

    def __init__(self, event_bus=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.event_bus = event_bus

        # name → task structure
        self.tasks: Dict[str, Dict[str, Any]] = {}

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_int(self, value: Any) -> bool:
        return isinstance(value, int) and value > 0

    def _parse_date(self, value: Optional[str]):
        if value is None:
            return datetime.now()

        if not self._validate_str(value):
            return None

        try:
            return datetime.strptime(value, "%Y-%m-%d")
        except Exception:
            return None

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            if self.event_bus:
                res = self.event_bus.initialize()
                if isinstance(res, dict) and res.get("status") == "error":
                    self.degraded_mode = True
                    return {
                        "status": "error",
                        "code": "event_bus_init_failed",
                        "version": "4.5",
                    }

            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc), "version": "4.5"}

    # ---------------------------------------------------------
    # ADD MAINTENANCE TASK
    # ---------------------------------------------------------
    def add_task(
        self,
        name: str,
        category: str,
        interval_days: int,
        last_done: Optional[str] = None
    ) -> Dict[str, Any]:

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Maintenance scheduler disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if not self._validate_str(category):
            return {"status": "error", "code": "invalid_category", "version": "4.5"}

        if not self._validate_int(interval_days):
            return {"status": "error", "code": "invalid_interval", "version": "4.5"}

        last_dt = self._parse_date(last_done)
        if last_dt is None:
            return {"status": "error", "code": "invalid_date_format", "version": "4.5"}

        try:
            next_due = last_dt + timedelta(days=interval_days)

            task = {
                "name": name,
                "category": category,
                "interval_days": interval_days,
                "last_done": last_dt.strftime("%Y-%m-%d"),
                "next_due": next_due.strftime("%Y-%m-%d"),
            }

            self.tasks[name] = task

            if self.event_bus:
                try:
                    self.event_bus.emit("maintenance_task_added", {"task": task})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "task": dict(task), "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "add_task_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # MARK TASK AS DONE
    # ---------------------------------------------------------
    def mark_done(self, name: str, date: Optional[str] = None) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name not in self.tasks:
            return {"status": "error", "code": "task_not_found", "version": "4.5"}

        done_dt = self._parse_date(date)
        if done_dt is None:
            return {"status": "error", "code": "invalid_date_format", "version": "4.5"}

        try:
            task = self.tasks[name]
            task["last_done"] = done_dt.strftime("%Y-%m-%d")
            task["next_due"] = (
                done_dt + timedelta(days=task["interval_days"])
            ).strftime("%Y-%m-%d")

            if self.event_bus:
                try:
                    self.event_bus.emit("maintenance_task_completed", {"task": task})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "task": dict(task), "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "mark_done_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # LIST TASKS
    # ---------------------------------------------------------
    def list_tasks(self) -> Dict[str, Any]:
        try:
            return {
                "status": "ok",
                "tasks": list(self.tasks.values()),
                "version": "4.5",
            }
        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "list_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # LIST DUE TASKS
    # ---------------------------------------------------------
    def list_due(self, date: Optional[str] = None) -> Dict[str, Any]:
        ref_dt = self._parse_date(date)
        if ref_dt is None:
            return {"status": "error", "code": "invalid_date_format", "version": "4.5"}

        try:
            due: List[Dict[str, Any]] = []
            for task in self.tasks.values():
                next_due_dt = datetime.strptime(task["next_due"], "%Y-%m-%d")
                if next_due_dt <= ref_dt:
                    due.append(task)

            return {"status": "ok", "due": due, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "list_due_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # REMOVE TASK
    # ---------------------------------------------------------
    def remove_task(self, name: str) -> Dict[str, Any]:
        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if name not in self.tasks:
            return {"status": "error", "code": "task_not_found", "version": "4.5"}

        try:
            removed = self.tasks.pop(name)

            if self.event_bus:
                try:
                    self.event_bus.emit("maintenance_task_removed", {"task": removed})
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "remove_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "tasks_count": len(self.tasks),
            "version": "4.5",
        }
