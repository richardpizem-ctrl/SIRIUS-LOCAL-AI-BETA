# runtime5/workflow_step_registry_5.py

from runtime5.workflow_steps_5.context_return_step import ContextReturnStep5
from runtime5.workflow_steps_5.envoy_fetch_step import EnvoyFetchStep5
from runtime5.workflow_steps_5.system_action_step import SystemActionStep5
from runtime5.workflow_steps_5.workflow_continue_step import WorkflowContinueStep5

class WorkflowStepRegistry5:
    """
    Registry that maps workflow actions to workflow step classes.
    """

    def __init__(self):
        self.registry = {
            "RETURN_CONTEXT": ContextReturnStep5,
            "ENVOY_FETCH": EnvoyFetchStep5,
            "SYSTEM_ACTION": SystemActionStep5,
            "WORKFLOW_CONTINUE": WorkflowContinueStep5
        }

    def get_step(self, action: str):
        step_class = self.registry.get(action)
        if not step_class:
            return WorkflowContinueStep5  # fallback
        return step_class()
