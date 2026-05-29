# runtime5/workflow_steps_5/context_return_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5


class ContextReturnStep5(BaseWorkflowStep5):
    """
    Workflow step that returns context from KG reasoning.
    Safe, diagnostic, and Self‑Repair‑ready.
    """

    def execute(self, data: dict):
        log5("[ContextReturnStep5] Executing RETURN_CONTEXT step...")

        # ReasoningEngine5 produces:
        # {
        #   "intent": ...,
        #   "entity": ...,
        #   "route": "KG_REASONING",
        #   "parent": ...,
        #   "parent_chain": [...],
        #   "degraded": ...
        # }

        parent = data.get("parent")
        parent_chain = data.get("parent_chain", [])

        output = {
            "action": "RETURN_CONTEXT",
            "entity": data.get("entity"),
            "parent": parent,
            "parent_chain": parent_chain,
            "degraded": HealthMonitor5.is_degraded()
        }

        log5(f"[ContextReturnStep5] Output: {output}")
        return output
