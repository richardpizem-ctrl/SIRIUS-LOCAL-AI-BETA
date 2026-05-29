# runtime5/workflow_steps_5/system_action_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class SystemActionStep5(BaseWorkflowStep5):
    """
    Workflow step for System Agent 5.0 actions (UI automation, OS control).
    Safe, diagnostic, and Self‑Repair‑ready.
    """

    def execute(self, data: dict):
        log5("[SystemActionStep5] Executing SYSTEM_ACTION step...")

        try:
            payload = data.get("result")

            output = {
                "action": "SYSTEM_ACTION",
                "payload": payload,
                "degraded": HealthMonitor5.is_degraded()
            }

            log5(f"[SystemActionStep5] Output: {output}")

            HealthMonitor5.record_success()
            return output

        except Exception as exc:
            log5(f"[SystemActionStep5] ERROR: {exc}")
            HealthMonitor5.record_error(str(exc))
            SystemHooks5.on_error(str(exc))

            return {
                "action": "SYSTEM_ACTION",
                "payload": None,
                "error": str(exc),
                "degraded": HealthMonitor5.is_degraded()
            }
