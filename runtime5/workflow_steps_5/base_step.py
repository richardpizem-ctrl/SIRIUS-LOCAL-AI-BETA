# runtime5/workflow_steps_5/base_step.py

from abc import ABC, abstractmethod
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class BaseWorkflowStep5(ABC):
    """
    Base class for all Workflow Steps in Runtime 5.x.
    Provides:
    - unified execute() wrapper
    - diagnostics
    - error handling
    - degraded mode awareness
    - compatibility with Self‑Repair Layer
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
        """
        log5(f"[BaseWorkflowStep5] Running step: {self.__class__.__name__}")

        try:
            output = self.execute(data)

            # Ensure degraded flag is always present
            if isinstance(output, dict) and "degraded" not in output:
                output["degraded"] = HealthMonitor5.is_degraded()

            HealthMonitor5.record_success()
            return output

        except Exception as exc:
            log5(f"[BaseWorkflowStep5] ERROR in {self.__class__.__name__}: {exc}")
            HealthMonitor5.record_error(str(exc))
            SystemHooks5.on_error(str(exc))

            return {
                "action": self.__class__.__name__,
                "payload": None,
                "error": str(exc),
                "degraded": HealthMonitor5.is_degraded()
            }
