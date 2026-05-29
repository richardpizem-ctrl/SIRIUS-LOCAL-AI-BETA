# runtime5/workflow_steps_5/envoy_fetch_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5


class EnvoyFetchStep5(BaseWorkflowStep5):
    """
    Workflow step that triggers an Envoy fetch request.
    Safe, diagnostic, and Self‑Repair‑ready.
    """

    def execute(self, data: dict):
        log5("[EnvoyFetchStep5] Executing ENVOY_FETCH step...")

        # ReasoningEngine5 produces for ENVOY route:
        # {
        #   "intent": ...,
        #   "entity": ...,
        #   "route": "ENVOY",
        #   "notes": "...",
        #   "degraded": ...
        # }

        entity = data.get("entity")
        query = entity or data.get("notes") or ""

        output = {
            "action": "ENVOY_FETCH",
            "query": query,
            "entity": entity,
            "degraded": HealthMonitor5.is_degraded()
        }

        log5(f"[EnvoyFetchStep5] Output: {output}")
        return output
