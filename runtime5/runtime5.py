# runtime5/runtime5.py

from runtime5.kg_core import KnowledgeGraph
from runtime5.re_chain_executor_5 import REChainExecutor5
from runtime5.workflow_engine_5 import WorkflowEngine5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.logging_5 import log5

# NEW: Health + System Hooks
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class Runtime5:
    """
    Main orchestrator for Runtime 5.x
    Connects:
    - Reasoning Engine 5.0
    - Workflow Engine 5.0
    - Knowledge Graph Runtime 1.0
    """

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.reasoning_chain = REChainExecutor5(kg)
        self.workflow = WorkflowEngine5()

    def _process_internal(self, text: str):
        log5("=== Runtime5 pipeline start ===")

        # Step 1: Reasoning pipeline
        reasoning_output = self.reasoning_chain.execute(text)

        # Step 2: Workflow execution
        workflow_output = self.workflow.execute(reasoning_output)

        log5("=== Runtime5 pipeline end ===")

        return {
            "reasoning": reasoning_output,
            "workflow": workflow_output
        }

    def process(self, text: str):
        """
        Public safe entrypoint.
        Entire pipeline is wrapped in ErrorHandler5.
        Includes:
        - Health monitoring
        - System hooks
        """
        try:
            result = ErrorHandler5.safe_execute(
                lambda: self._process_internal(text)
            )

            # Successful cycle
            HealthMonitor5.record_success()
            return result

        except Exception as exc:
            # Error cycle
            HealthMonitor5.record_error(str(exc))
            SystemHooks5.on_error(str(exc))

            return {
                "reasoning": None,
                "workflow": None,
                "error": str(exc)
            }
