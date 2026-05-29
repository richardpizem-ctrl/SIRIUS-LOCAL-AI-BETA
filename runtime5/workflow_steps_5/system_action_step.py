# runtime5/workflow_steps_5/system_action_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5


class SystemActionStep5(BaseWorkflowStep5):
    """
    Workflow step for System Agent 5.x actions (UI automation, OS control).
    Safe, diagnostic, and Self‑Repair‑ready.
    """

    def execute(self, data: dict):
        log5("[SystemActionStep5] Executing SYSTEM_ACTION step...")

        # ReasoningEngine5 produces for SYSTEM_AGENT route:
        # {
        #   "intent": ...,
        #   "entity": ...,
        #   "route": "SYSTEM_AGENT",
        #   "notes": "...",
        #   "degraded": ...
        # }

        entity = data.get("entity")
        notes = data.get("notes", "")
        payload = {
            "entity": entity,
            "notes": notes
        }

        output = {
            "action": "SYSTEM_ACTION",
            "payload": payload,
            "degraded": HealthMonitor5.is_degraded()
        }

        log5(f"[SystemActionStep5] Output: {output}")
        return output
