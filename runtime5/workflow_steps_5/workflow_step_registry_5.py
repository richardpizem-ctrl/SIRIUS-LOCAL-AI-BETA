# runtime5/workflow_steps_5/workflow_step_registry_5.py

from runtime5.workflow_steps_5.context_return_step import ContextReturnStep5
from runtime5.workflow_steps_5.envoy_fetch_step import EnvoyFetchStep5
from runtime5.workflow_steps_5.system_action_step import SystemActionStep5
from runtime5.workflow_steps_5.workflow_continue_step import WorkflowContinueStep5

from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5
from runtime5.error_handler_5 import ErrorHandler5


class WorkflowStepRegistry5:
    """
    Registry that maps workflow actions to workflow step classes.
    Provides:
    - safe lookup
    - fallback step
    - diagnostics
    - degraded mode awareness
    """

    def __init__(self):
        self.registry = {
            "RETURN_CONTEXT": ContextReturnStep5,
            "ENVOY_FETCH": EnvoyFetchStep5,
            "SYSTEM_ACTION": SystemActionStep5,
            "WORKFLOW_CONTINUE": WorkflowContinueStep5
        }
        log5("[WorkflowStepRegistry5] Registry initialized.")

    # --------------------------------------------------------
    # SAFE LOOKUP
    # --------------------------------------------------------
    def get_step(self, action: str):
        """
        Returns an instantiated workflow step.
        Includes:
        - logging
        - fallback
        - degraded mode awareness
        - ErrorHandler5 wrapper
        """

        def _exec():
            log5(f"[WorkflowStepRegistry5] Requested action: {action}")

            step_class = self.registry.get(action)

            if not step_class:
                msg = f"Unknown workflow action: {action}"
                log5(f"[WorkflowStepRegistry5] {msg}")
                HealthMonitor5.record_error(msg)
                SystemHooks5.on_error(msg)
                return WorkflowContinueStep5()

            step = step_class()
            log5(f"[WorkflowStepRegistry5] Loaded step: {step_class.__name__}")

            HealthMonitor5.record_success()
            return step

        return ErrorHandler5.safe_execute(
            _exec,
            context={"action": action},
            fallback=WorkflowContinueStep5()
        )
