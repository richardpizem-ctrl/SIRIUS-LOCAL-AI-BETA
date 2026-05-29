# runtime5/workflow_engine_5.py

from runtime5.workflow_step_registry_5 import WorkflowStepRegistry5

class WorkflowEngine5:
    """
    Workflow Engine 5.0
    Decides what action to take based on reasoning output
    and executes the correct workflow step.
    """

    def __init__(self):
        self.registry = WorkflowStepRegistry5()

    def execute(self, reasoning_output: dict):
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

        # Get workflow step
        step = self.registry.get_step(action)

        # Execute workflow step
        return step.execute(reasoning_output)
