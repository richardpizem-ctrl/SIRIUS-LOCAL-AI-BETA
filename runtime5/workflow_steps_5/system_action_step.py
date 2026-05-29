# runtime5/workflow_steps_5/system_action_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5

class SystemActionStep5(BaseWorkflowStep5):
    """
    Workflow step for System Agent 5.0 actions (UI automation, OS control).
    """

    def execute(self, data: dict):
        return {
            "action": "SYSTEM_ACTION",
            "payload": data.get("result")
        }
