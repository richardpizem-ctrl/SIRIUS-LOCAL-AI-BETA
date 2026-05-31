"""
SIRIUS Runtime 5.1.0
Workflow Engine 5.1

Účel:
- vykonávať workflow úlohy v deterministickom poradí
- poskytovať RuntimeCore informácie o stave workflow
- podporovať Self‑Repair Layer 1.0 (reportovanie chýb, degradácií)
"""

from typing import Dict, Any, List


class WorkflowEngine5:
    """
    WorkflowEngine5 – nový workflow engine pre Runtime5.

    Očakávané závislosti (dependency injection):
        workflow_source – poskytuje zoznam čakajúcich workflow úloh
        executor        – vykonáva jednotlivé workflow kroky (API: execute(task) -> dict)
        logger          – Logging5 / RuntimeLogger
    """

    def __init__(self, workflow_source, executor, logger):
        self.workflow_source = workflow_source
        self.executor = executor
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def run_pending(self) -> Dict[str, Any]:
        """
        Spustí všetky čakajúce workflow úlohy.

        Výstup:
        {
            "status": "OK" | "DEGRADED" | "ERROR",
            "executed": [...],
            "failed": [...],
            "pending_count": int
        }
        """
        self.logger.info("WorkflowEngine5: checking pending workflow tasks")

        tasks = self._safe_get_pending()
        executed_steps: List[Dict[str, Any]] = []
        failed_steps: List[Dict[str, Any]] = []

        for idx, task in enumerate(tasks):
            ok, info = self._safe_execute(task)

            step_info = {
                "index": idx,
                "task": task,
                "ok": ok,
                "details": info,
            }

            if ok:
                executed_steps.append(step_info)
            else:
                failed_steps.append(step_info)

        # určenie statusu
        if failed_steps:
            status = "ERROR"
        elif executed_steps:
            status = "OK"
        else:
            status = "OK"  # nič na vykonanie

        result = {
            "status": status,
            "executed": executed_steps,
            "failed": failed_steps,
            "pending_count": len(tasks),
        }

        self.logger.info(
            "WorkflowEngine5: run_pending completed",
            extra={"status": status, "executed": len(executed_steps), "failed": len(failed_steps)},
        )

        return result

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------

    def _safe_get_pending(self) -> List[Dict[str, Any]]:
        try:
            tasks = self.workflow_source.get_pending()
            return tasks or []
        except Exception as e:
            self.logger.exception(
                "WorkflowEngine5: workflow_source.get_pending() failed",
                extra={"error": str(e)},
            )
            return []

    def _safe_execute(self, task: Dict[str, Any]) -> tuple[bool, Dict[str, Any]]:
        try:
            self.logger.info(
                "WorkflowEngine5: executing task",
                extra={"task": task.get("name", "unknown")},
            )
            result = self.executor.execute(task)
            return True, result or {}
        except Exception as e:
            self.logger.exception(
                "WorkflowEngine5: task execution failed",
                extra={"task": task, "error": str(e)},
            )
            return False, {"error": "execution_failed", "details": str(e)}
