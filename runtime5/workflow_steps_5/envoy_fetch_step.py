# runtime5/workflow_steps_5/envoy_fetch_step.py

from runtime5.workflow_steps_5.base_step import BaseWorkflowStep5

class EnvoyFetchStep5(BaseWorkflowStep5):
    """
    Workflow step that triggers an Envoy fetch request.
    """

    def execute(self, data: dict):
        return {
            "action": "ENVOY_FETCH",
            "query": data.get("result")
        }
