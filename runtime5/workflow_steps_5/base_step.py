# runtime5/workflow_steps_5/base_step.py

from abc import ABC, abstractmethod
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5
from runtime5.error_handler_5 import ErrorHandler5


class BaseWorkflowStep5(ABC):
    """
    Base class for all Workflow Steps in Runtime 5.x.
    Provides:
    - unified safe_execute() wrapper
    - diagnostics
    - error isolation
    - degraded mode awareness
    - Self‑Repair Layer compatibility
    """

    @abstractmethod
    def execute(self, data: dict):
        """
        Child classes must implement this.
        Should return a dict with:
        - action
        - payload / context / query
        - degraded flag
        - optional error
        """
        pass

    # --------------------------------------------------------
    # SAFE EXECUTION WRAPPER
    # --------------------------------------------------------
    def safe_execute(self, data: dict):
        """
        Wraps execute() with:
        - logging
        - diagnostics
        - error isolation
        - degraded mode support
        - ErrorHandler5 compatibility
        """
        log5(f"[BaseWorkflowStep5] Running step: {self.__class__.__name__}")

        def _exec():
            output = self.execute(data)

            # Ensure degraded flag is always present
            if isinstance(output, dict) and "degraded" not in output:
                output["degraded"] = HealthMonitor5.is_degraded()

            HealthMonitor5.record_success()
            return output

        return ErrorHandler5.safe_execute(
            _exec,
            context={"step": self.__class__.__name__, "input": data},
            fallback={
                "action": self.__class__.__name__,
                "payload": None,
                "error": f"Workflow step '{self.__class__.__name__}' failed.",
                "degraded": HealthMonitor5.is_degraded()
            }
        )
