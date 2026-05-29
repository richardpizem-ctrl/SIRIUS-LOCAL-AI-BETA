# runtime5/workflow_steps_5/context_return_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class ContextReturnStep5(BaseWorkflowStep5):
    """
    Workflow step that returns context from KG reasoning.
    Safe, diagnostic, and Self‑Repair‑ready.
    """

    def execute(self, data: dict):
        log5("[ContextReturnStep5] Executing RETURN_CONTEXT step...")

        try:
            context = data.get("result")

            output = {
                "action": "RETURN_CONTEXT",
                "context": context,
                "degraded": HealthMonitor5.is_degraded()
            }

            log5(f"[ContextReturnStep5] Output: {output}")

            HealthMonitor5.record_success()
            return output

        except Exception as exc:
            log5(f"[ContextReturnStep5] ERROR: {exc}")
            HealthMonitor5.record_error(str(exc))
            SystemHooks5.on_error(str(exc))

            return {
                "action": "RETURN_CONTEXT",
                "context": None,
                "error": str(exc),
                "degraded": HealthMonitor5.is_degraded()
            }
