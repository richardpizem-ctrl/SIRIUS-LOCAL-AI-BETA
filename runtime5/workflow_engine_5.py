# runtime5/workflow_engine_5.py

from runtime5.workflow_step_registry_5 import WorkflowStepRegistry5
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5
from runtime5.error_handler_5 import ErrorHandler5


class WorkflowEngine5:
    """
    Workflow Engine 5.x
    Decides what action to take based on reasoning output
    and executes the correct workflow step.
    """

    def __init__(self):
        self.registry = WorkflowStepRegistry5()
        log5("[WorkflowEngine5] Initialized Workflow Engine 5.x")

    # --------------------------------------------------------
    # EXECUTION
    # --------------------------------------------------------
    def execute(self, reasoning_output: dict):
        log5("[WorkflowEngine5] Executing workflow step...")

        def _exec():
            route = reasoning_output.get("route")
            intent = reasoning_output.get("intent")
            result = reasoning_output.get("result")

            # Determine action based on route (from ReasoningEngine5)
            if route == "KG_REASONING":
                action = "RETURN_CONTEXT"
            elif route == "ENVOY":
                action = "ENVOY_FETCH"
            elif route == "SYSTEM_AGENT":
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

            HealthMonitor5.record_success()

            return {
                "action": action,
                "output": output,
                "degraded": HealthMonitor5.is_degraded()
            }

        return ErrorHandler5.safe_execute(
            _exec,
            context={"reasoning_output": reasoning_output},
            fallback={
                "action": None,
                "output": None,
                "error": "WorkflowEngine5 failed.",
                "degraded": HealthMonitor5.is_degraded()
            }
        )
