# household_4_4/home_task_planner_4_4.py
"""
SIRIUS LOCAL AI – Home Task Planner 4.4.0

Účel:
- plánovanie domácich úloh (upratovanie, údržba, nákupy, pripomienky)
- 100 % offline, deterministické
- žiadne AI heuristiky, žiadne dynamické importy
- integrácia s:
    - Household State Manager 4.4
    - Routine Engine 4.4
    - Event Bus 4.4
    - Household Context Memory 4.4

Úlohy sú čisté dict štruktúry:
{
    "id": "task_001",
    "name": "Vyniesť smeti",
    "category": "cleaning",
    "room": "kitchen",
    "priority": "medium",
    "schedule": {"type": "daily", "time": "20:00"},
    "completed": False
}
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

        self.event_bus = event_bus
        self.context_memory = context_memory

        # Úlohy uložené v pamäti
        self.tasks: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------
    def initialize(self) -> Dict[str, Any]:
        if self.initialized:
            return {"status": "already_initialized"}

        try:
            if self.event_bus:
                self.event_bus.initialize()
            if self.context_memory:
                self.context_memory.initialize()

            self.initialized = True
            return {"status": "initialized"}

        except Exception as exc:
            self.degraded_mode = True
            return {"status": "error", "exception": str(exc)}

    # ------------------------------------------------------------------
    # CREATE TASK
    # ------------------------------------------------------------------
    def create_task(
        self,
        name: str,
        category: str,
        room: Optional[str] = None,
        priority: str = "medium",
        schedule: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:

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

        # Event pre Routine Engine
        if self.event_bus:
            self.event_bus.emit("task_created", task)

        return {"status": "ok", "task": task}

    # ------------------------------------------------------------------
    # LIST TASKS
    # ------------------------------------------------------------------
    def list_tasks(self, include_completed: bool = True) -> Dict[str, Any]:
        if include_completed:
            return {"status": "ok", "tasks": list(self.tasks)}

        filtered = [t for t in self.tasks if not t["completed"]]
        return {"status": "ok", "tasks": filtered}

    # ------------------------------------------------------------------
    # MARK COMPLETED
    # ------------------------------------------------------------------
    def complete_task(self, task_id: str) -> Dict[str, Any]:
        for t in self.tasks:
            if t["id"] == task_id:
                t["completed"] = True

                if self.event_bus:
                    self.event_bus.emit("task_completed", t)

                return {"status": "ok", "task": t}

        return {"status": "error", "reason": "task_not_found"}

    # ------------------------------------------------------------------
    # DELETE TASK
    # ------------------------------------------------------------------
    def delete_task(self, task_id: str) -> Dict[str, Any]:
        for t in self.tasks:
            if t["id"] == task_id:
                self.tasks.remove(t)

                if self.event_bus:
                    self.event_bus.emit("task_deleted", t)

                return {"status": "ok"}

        return {"status": "error", "reason": "task_not_found"}

    # ------------------------------------------------------------------
    # FIND TASKS BY ROOM
    # ------------------------------------------------------------------
    def tasks_in_room(self, room: str) -> Dict[str, Any]:
        result = [t for t in self.tasks if t.get("room") == room]
        return {"status": "ok", "tasks": result}

    # ------------------------------------------------------------------
    # FIND TASKS BY CATEGORY
    # ------------------------------------------------------------------
    def tasks_by_category(self, category: str) -> Dict[str, Any]:
        result = [t for t in self.tasks if t.get("category") == category]
        return {"status": "ok", "tasks": result}

    # ------------------------------------------------------------------
    # SCHEDULED TASKS (for Routine Engine)
    # ------------------------------------------------------------------
    def get_scheduled_tasks(self) -> List[Dict[str, Any]]:
        return [t for t in self.tasks if t.get("schedule")]

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
