# runtime5/workflow_steps_5/envoy_fetch_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class EnvoyFetchStep5(BaseWorkflowStep5):
    """
    Workflow step that triggers an Envoy fetch request.
    Safe, diagnostic, and Self‑Repair‑ready.
    """

    def execute(self, data: dict):
        log5("[EnvoyFetchStep5] Executing ENVOY_FETCH step...")

        try:
            query = data.get("result")

            output = {
                "action": "ENVOY_FETCH",
                "query": query,
                "degraded": HealthMonitor5.is_degraded()
            }

            log5(f"[EnvoyFetchStep5] Output: {output}")

            HealthMonitor5.record_success()
            return output

        except Exception as exc:
            log5(f"[EnvoyFetchStep5] ERROR: {exc}")
            HealthMonitor5.record_error(str(exc))
            SystemHooks5.on_error(str(exc))

            return {
                "action": "ENVOY_FETCH",
                "query": None,
                "error": str(exc),
                "degraded": HealthMonitor5.is_degraded()
            }
