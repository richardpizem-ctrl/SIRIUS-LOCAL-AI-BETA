# runtime5/runtime5.py

from runtime5.kg_core import KnowledgeGraph
from runtime5.re_chain_executor_5 import REChainExecutor5
from runtime5.workflow_engine_5 import WorkflowEngine5

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

    def process(self, text: str):
        # Step 1: Reasoning pipeline
        reasoning_output = self.reasoning_chain.execute(text)

        # Step 2: Workflow execution
        workflow_output = self.workflow.execute(reasoning_output)

        return {
            "reasoning": reasoning_output,
            "workflow": workflow_output
        }
