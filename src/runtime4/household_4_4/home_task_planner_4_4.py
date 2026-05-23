"""
SIRIUS LOCAL AI – Home Task Planner 4.5.0 (PRO)

Purpose:
- deterministic household task planning
- 100% offline, no AI heuristics

Security Family 4.5:
- safe‑mode compatible
- Self‑Repair 4.5 ready
"""

from typing import Dict, Any, List, Optional
import uuid


class HomeTaskPlanner45:
    """
    Deterministic household task planner 4.5.
    """

    def __init__(self, event_bus=None, context_memory=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.event_bus = event_bus
        self.context_memory = context_memory

        # Tasks stored in memory
        self.tasks: List[Dict[str, Any]] = []

    # ---------------------------------------------------------
    # INTERNAL VALIDATION
    # ---------------------------------------------------------
    def _validate_str(self, value: Any) -> bool:
        return isinstance(value, str) and value.strip()

    def _validate_schedule(self, schedule: Any) -> bool:
        if schedule is None:
            return True
        if not isinstance(schedule, dict):
            return False
        if "type" not in schedule:
            return False
        if not self._validate_str(schedule.get("type")):
            return False
        # time is optional, but if present must be a string
        if "time" in schedule and not self._validate_str(schedule.get("time")):
            return False
        return True

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized", "version": "4.5"}

        try:
            modules = [self.event_bus, self.context_memory]
            for m in modules:
                if m:
                    res = m.initialize()
                    if isinstance(res, dict) and res.get("status") == "error":
                        self.degraded_mode = True
                        return {
                            "status": "error",
                            "code": "module_init_failed",
                            "version": "4.5",
                        }

            self.initialized = True
            return {"status": "initialized", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # CREATE TASK
    # ---------------------------------------------------------
    def create_task(
        self,
        name: str,
        category: str,
        room: Optional[str] = None,
        priority: str = "medium",
        schedule: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "message": "Task planner disabled in safe-mode.",
                "version": "4.5",
            }

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name", "version": "4.5"}

        if not self._validate_str(category):
            return {"status": "error", "code": "invalid_category", "version": "4.5"}

        if not self._validate_str(priority):
            return {"status": "error", "code": "invalid_priority", "version": "4.5"}

        if not self._validate_schedule(schedule):
            return {"status": "error", "code": "invalid_schedule", "version": "4.5"}

        try:
            task = {
                "id": f"task_{uuid.uuid4().hex[:8]}",
                "name": name,
                "category": category,
                "room": room,
                "priority": priority,
                "schedule": schedule or {},
                "completed": False,
            }

            self.tasks.append(task)

            if self.event_bus:
                try:
                    self.event_bus.emit("task_created", dict(task))
                except Exception:
                    self.degraded_mode = True

            return {"status": "ok", "task": dict(task), "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "create_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # LIST TASKS
    # ---------------------------------------------------------
    def list_tasks(self, include_completed: bool = True) -> Dict[str, Any]:
        try:
            if include_completed:
                return {
                    "status": "ok",
                    "tasks": list(self.tasks),
                    "version": "4.5",
                }

            filtered = [t for t in self.tasks if not t["completed"]]
            return {"status": "ok", "tasks": filtered, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "list_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # MARK COMPLETED
    # ---------------------------------------------------------
    def complete_task(self, task_id: str) -> Dict[str, Any]:
        if not self._validate_str(task_id):
            return {"status": "error", "code": "invalid_task_id", "version": "4.5"}

        try:
            for t in self.tasks:
                if t["id"] == task_id:
                    t["completed"] = True

                    if self.event_bus:
                        try:
                            self.event_bus.emit("task_completed", dict(t))
                        except Exception:
                            self.degraded_mode = True

                    return {"status": "ok", "task": dict(t), "version": "4.5"}

            return {"status": "error", "code": "task_not_found", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "complete_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # DELETE TASK
    # ---------------------------------------------------------
    def delete_task(self, task_id: str) -> Dict[str, Any]:
        if not self._validate_str(task_id):
            return {"status": "error", "code": "invalid_task_id", "version": "4.5"}

        try:
            for t in self.tasks:
                if t["id"] == task_id:
                    self.tasks.remove(t)

                    if self.event_bus:
                        try:
                            self.event_bus.emit("task_deleted", dict(t))
                        except Exception:
                            self.degraded_mode = True

                    return {"status": "ok", "version": "4.5"}

            return {"status": "error", "code": "task_not_found", "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "delete_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # FIND TASKS BY ROOM
    # ---------------------------------------------------------
    def tasks_in_room(self, room: str) -> Dict[str, Any]:
        if not self._validate_str(room):
            return {"status": "error", "code": "invalid_room", "version": "4.5"}

        try:
            result = [t for t in self.tasks if t.get("room") == room]
            return {"status": "ok", "tasks": result, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "tasks_in_room_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # FIND TASKS BY CATEGORY
    # ---------------------------------------------------------
    def tasks_by_category(self, category: str) -> Dict[str, Any]:
        if not self._validate_str(category):
            return {"status": "error", "code": "invalid_category", "version": "4.5"}

        try:
            result = [t for t in self.tasks if t.get("category") == category]
            return {"status": "ok", "tasks": result, "version": "4.5"}

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "code": "tasks_by_category_failed",
                "exception": str(exc),
                "version": "4.5",
            }

    # ---------------------------------------------------------
    # SCHEDULED TASKS (for Routine Engine)
    # ---------------------------------------------------------
    def get_scheduled_tasks(self) -> List[Dict[str, Any]]:
        try:
            return [t for t in self.tasks if t.get("schedule")]
        except Exception:
            self.degraded_mode = True
            return []

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
