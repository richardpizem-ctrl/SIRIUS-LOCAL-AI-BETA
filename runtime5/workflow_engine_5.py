# runtime5/workflow_engine_5.py

from runtime5.workflow_step_registry_5 import WorkflowStepRegistry5
from runtime5.logging_5 import log5

# NEW: diagnostics + system hooks
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class WorkflowEngine5:
    """
    Workflow Engine 5.0
    Decides what action to take based on reasoning output
    and executes the correct workflow step.
    """

    def __init__(self):
        self.registry = WorkflowStepRegistry5()

    def execute(self, reasoning_output: dict):
        log5("[WorkflowEngine5] Executing workflow step...")

        try:
            intent = reasoning_output.get("intent")
            result = reasoning_output.get("result")

            # Determine action
            if intent == "KG_REASONING":
                action = "RETURN_CONTEXT"
            elif intent == "ENVOY":
                action = "ENVOY_FETCH"
            elif intent == "SYSTEM_AGENT":
                action = "SYSTEM_ACTION"
            else:
                action = "WORKFLOW_CONTINUE"

            log5(f"[WorkflowEngine5] Selected action: {action}")

            # Get workflow step
            step = self.registry.get_step(action)
            if not step:
                raise ValueError(f"Unknown workflow step: {action}")

            # Execute workflow step
            output = step.execute(reasoning_output)
            log5(f"[WorkflowEngine5] Step output: {output}")

            # Diagnostics: successful cycle
            HealthMonitor5.record_success()

            return output

        except Exception as exc:
            # Diagnostics: error cycle
            HealthMonitor5.record_error(str(exc))
            SystemHooks5.on_error(str(exc))

            log5(f"[WorkflowEngine5] ERROR: {exc}")

            return {
                "error": str(exc),
                "degraded": HealthMonitor5.is_degraded(),
                "workflow": None
            }
