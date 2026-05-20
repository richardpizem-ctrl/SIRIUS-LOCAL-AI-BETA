"""
SIRIUS LOCAL AI – Home Task Planner 4.4.0 (PRO)

Účel:
- deterministické plánovanie domácich úloh
- 100 % offline, žiadne AI heuristiky

Security Family 4.4:
- safe‑mode kompatibilita
- Self‑Repair 4.4 ready
"""

from typing import Dict, Any, List, Optional
import uuid


class HomeTaskPlanner44:
    """
    Deterministic planner domácich úloh.
    """

    def __init__(self, event_bus=None, context_memory=None):
        self.initialized = False
        self.degraded_mode = False
        self.safe_mode = False

        self.event_bus = event_bus
        self.context_memory = context_memory

        # Úlohy uložené v pamäti
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
        # čas je voliteľný, ale ak existuje, musí byť string
        if "time" in schedule and not self._validate_str(schedule.get("time")):
            return False
        return True

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            modules = [self.event_bus, self.context_memory]
            for m in modules:
                if m:
                    res = m.initialize()
                    if isinstance(res, dict) and res.get("status") == "error":
                        self.degraded_mode = True
                        return {"status": "error", "code": "module_init_failed"}

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

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
            return {"status": "safe_mode", "message": "Task planner disabled in safe-mode."}

        if not self._validate_str(name):
            return {"status": "error", "code": "invalid_name"}

        if not self._validate_str(category):
            return {"status": "error", "code": "invalid_category"}

        if not self._validate_str(priority):
            return {"status": "error", "code": "invalid_priority"}

        if not self._validate_schedule(schedule):
            return {"status": "error", "code": "invalid_schedule"}

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

            return {"status": "ok", "task": dict(task)}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "create_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # LIST TASKS
    # ---------------------------------------------------------
    def list_tasks(self, include_completed: bool = True) -> Dict[str, Any]:
        try:
            if include_completed:
                return {"status": "ok", "tasks": list(self.tasks)}

            filtered = [t for t in self.tasks if not t["completed"]]
            return {"status": "ok", "tasks": filtered}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "list_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # MARK COMPLETED
    # ---------------------------------------------------------
    def complete_task(self, task_id: str) -> Dict[str, Any]:
        if not self._validate_str(task_id):
            return {"status": "error", "code": "invalid_task_id"}

        try:
            for t in self.tasks:
                if t["id"] == task_id:
                    t["completed"] = True

                    if self.event_bus:
                        try:
                            self.event_bus.emit("task_completed", dict(t))
                        except Exception:
                            self.degraded_mode = True

                    return {"status": "ok", "task": dict(t)}

            return {"status": "error", "code": "task_not_found"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "complete_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # DELETE TASK
    # ---------------------------------------------------------
    def delete_task(self, task_id: str) -> Dict[str, Any]:
        if not self._validate_str(task_id):
            return {"status": "error", "code": "invalid_task_id"}

        try:
            for t in self.tasks:
                if t["id"] == task_id:
                    self.tasks.remove(t)

                    if self.event_bus:
                        try:
                            self.event_bus.emit("task_deleted", dict(t))
                        except Exception:
                            self.degraded_mode = True

                    return {"status": "ok"}

            return {"status": "error", "code": "task_not_found"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "delete_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # FIND TASKS BY ROOM
    # ---------------------------------------------------------
    def tasks_in_room(self, room: str) -> Dict[str, Any]:
        if not self._validate_str(room):
            return {"status": "error", "code": "invalid_room"}

        try:
            result = [t for t in self.tasks if t.get("room") == room]
            return {"status": "ok", "tasks": result}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "tasks_in_room_failed", "exception": str(exc)}

    # ---------------------------------------------------------
    # FIND TASKS BY CATEGORY
    # ---------------------------------------------------------
    def tasks_by_category(self, category: str) -> Dict[str, Any]:
        if not self._validate_str(category):
            return {"status": "error", "code": "invalid_category"}

        try:
            result = [t for t in self.tasks if t.get("category") == category]
            return {"status": "ok", "tasks": result}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "code": "tasks_by_category_failed", "exception": str(exc)}

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
        }
