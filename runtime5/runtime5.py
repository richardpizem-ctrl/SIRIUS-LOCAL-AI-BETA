# runtime5/runtime5.py

from runtime5.kg_core import KnowledgeGraph
from runtime5.re_chain_executor_5 import REChainExecutor5
from runtime5.workflow_engine_5 import WorkflowEngine5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class Runtime5:
    """
    Main orchestrator for Runtime 5.x
    Connects:
    - Reasoning Engine 5.x (via REChainExecutor5)
    - Workflow Engine 5.x
    - Knowledge Graph subsystem 5.x
    """

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.reasoning_chain = REChainExecutor5(kg)
        self.workflow = WorkflowEngine5()
        log5("[Runtime5] Initialized Runtime 5.x orchestrator.")

    # --------------------------------------------------------
    # INTERNAL PIPELINE
    # --------------------------------------------------------
    def _process_internal(self, text: str):
        log5("=== Runtime5 pipeline start ===")

        # Step 1: Reasoning pipeline
        reasoning_output = self.reasoning_chain.execute(text)

        # Step 2: Workflow execution
        workflow_output = self.workflow.execute(reasoning_output)

        log5("=== Runtime5 pipeline end ===")

        return {
            "reasoning": reasoning_output,
            "workflow": workflow_output,
            "degraded": HealthMonitor5.is_degraded()
        }

    # --------------------------------------------------------
    # PUBLIC SAFE ENTRYPOINT
    # --------------------------------------------------------
    def process(self, text: str):
        """
        Public safe entrypoint.
        Entire pipeline is wrapped in ErrorHandler5.
        Includes:
        - Health monitoring
        - System hooks
        - degraded mode awareness
        """
        def _exec():
            result = self._process_internal(text)
            HealthMonitor5.record_success()
            return result

        return ErrorHandler5.safe_execute(
            _exec,
            context={"input": text},
            fallback={
                "reasoning": None,
                "workflow": None,
                "error": "Runtime5 pipeline failed.",
                "degraded": HealthMonitor5.is_degraded()
            }
        )
