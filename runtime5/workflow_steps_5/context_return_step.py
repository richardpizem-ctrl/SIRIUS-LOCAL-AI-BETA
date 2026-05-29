# runtime5/workflow_steps_5/context_return_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5

class ContextReturnStep5(BaseWorkflowStep5):
    """
    Workflow step that returns context from KG reasoning.
    """

    def execute(self, data: dict):
        return {
            "action": "RETURN_CONTEXT",
            "context": data.get("result")
        }
