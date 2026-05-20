# household_4_4/home_maintenance_scheduler_4_4.py
"""
SIRIUS LOCAL AI – Home Maintenance Scheduler 4.4.0

Účel:
- plánovanie údržby domácnosti (filtre, batérie, servis, čistenie)
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy

Úloha údržby:
{
    "name": "vymenit_filter_klima",
    "category": "air_system",
    "interval_days": 30,
    "last_done": "2026-05-01",
    "next_due": "2026-05-31"
}
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta


class HomeMaintenanceScheduler44:
    """
    Deterministic maintenance scheduler pre domácnosť.
    """

    def __init__(self, event_bus=None):
        self.initialized = False
        self.degraded_mode = False

        self.event_bus = event_bus

        # name → task
        self.tasks: Dict[str, Dict[str, Any]] = {}

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.event_bus:
                self.event_bus.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # ADD MAINTENANCE TASK
    # ------------------------------------------------------------------
    def add_task(
        self,
        name: str,
        category: str,
        interval_days: int,
        last_done: Optional[str] = None
    ) -> Dict[str, Any]:

        if last_done:
            try:
                last_dt = datetime.strptime(last_done, "%Y-%m-%d")
            except ValueError:
                return {"status": "error", "reason": "invalid_date_format"}
        else:
            last_dt = datetime.now()

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
            self.event_bus.emit("maintenance_task_added", {"task": task})

        return {"status": "ok", "task": task}

    # ------------------------------------------------------------------
    # MARK TASK AS DONE
    # ------------------------------------------------------------------
    def mark_done(self, name: str, date: Optional[str] = None) -> Dict[str, Any]:
        if name not in self.tasks:
            return {"status": "error", "reason": "task_not_found"}

        if date:
            try:
                done_dt = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                return {"status": "error", "reason": "invalid_date_format"}
        else:
            done_dt = datetime.now()

        task = self.tasks[name]
        task["last_done"] = done_dt.strftime("%Y-%m-%d")
        task["next_due"] = (done_dt + timedelta(days=task["interval_days"])).strftime("%Y-%m-%d")

        if self.event_bus:
            self.event_bus.emit("maintenance_task_completed", {"task": task})

        return {"status": "ok", "task": dict(task)}

    # ------------------------------------------------------------------
    # LIST TASKS
    # ------------------------------------------------------------------
    def list_tasks(self) -> Dict[str, Any]:
        return {"status": "ok", "tasks": list(self.tasks.values())}

    # ------------------------------------------------------------------
    # LIST DUE TASKS
    # ------------------------------------------------------------------
    def list_due(self, date: Optional[str] = None) -> Dict[str, Any]:
        if date:
            try:
                ref_dt = datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                return {"status": "error", "reason": "invalid_date_format"}
        else:
            ref_dt = datetime.now()

        due = []
        for task in self.tasks.values():
            next_due_dt = datetime.strptime(task["next_due"], "%Y-%m-%d")
            if next_due_dt <= ref_dt:
                due.append(task)

        return {"status": "ok", "due": due}

    # ------------------------------------------------------------------
    # REMOVE TASK
    # ------------------------------------------------------------------
    def remove_task(self, name: str) -> Dict[str, Any]:
        if name not in self.tasks:
            return {"status": "error", "reason": "task_not_found"}

        removed = self.tasks.pop(name)

        if self.event_bus:
            self.event_bus.emit("maintenance_task_removed", {"task": removed})

        return {"status": "ok"}

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "status": "ok",
            "initialized": self.initialized,
            "degraded_mode": self.degraded_mode,
            "tasks_count": len(self.tasks),
        }
