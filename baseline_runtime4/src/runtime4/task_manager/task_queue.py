# Baseline version of TaskQueue
# This file is a clean, unmodified reference copy.
# Version: 4.5.0

class TaskQueue:
    def __init__(self, logger):
        self.logger = logger
        self.queue = []

    def add(self, task_name: str) -> None:
        """
        Baseline version:
        Only defines the interface and expected behavior.
        No active queue logic is implemented here.
        """
        self.logger.log(f"[Baseline] TaskQueue.add() called for task: {task_name}")
        self.queue.append(task_name)

    def pop(self) -> str | None:
        """
        Baseline version:
        Returns None instead of performing real queue operations.
        """
        self.logger.log("[Baseline] TaskQueue.pop() called.")
        return None
