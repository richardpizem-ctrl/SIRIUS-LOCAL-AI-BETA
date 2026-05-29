# runtime5/workflow_steps_5/workflow_continue_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5

class WorkflowContinueStep5(BaseWorkflowStep5):
    """
    Default workflow step when the workflow should continue.
    """

    def execute(self, data: dict):
        return {
            "action": "WORKFLOW_CONTINUE",
            "payload": data
        }
