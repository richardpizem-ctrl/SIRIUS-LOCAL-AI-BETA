# runtime5/re_chain_executor_5.py

from runtime5.intent_resolver_5 import IntentResolver5
from runtime5.context_builder_5 import ContextBuilder5
from runtime5.reasoning_engine_5 import ReasoningEngine5
from runtime5.kg_core import KnowledgeGraph
from runtime5.logging_5 import log5


class REChainExecutor5:
    """
    Main reasoning pipeline for Runtime 5.x.
    Executes:
    1. Intent resolution
    2. Context building
    3. Reasoning Engine execution
    """

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.intent_resolver = IntentResolver5()
        self.context_builder = ContextBuilder5(kg)
        self.reasoning_engine = ReasoningEngine5(kg)

    def execute(self, text: str):
        log5(f"[REChain] Input text: {text}")

        # 1. Intent resolution
        intent = self.intent_resolver.resolve(text)
        log5(f"[REChain] Resolved intent: {intent}")

        # 2. Context building
        context = self.context_builder.build(entity=text)
        log5(f"[REChain] Built context: {context}")

        # 3. Reasoning Engine execution
        result = self.reasoning_engine.process(intent, entity=text)
        log5(f"[REChain] Reasoning result: {result}")

        output = {
            "intent": intent,
            "context": context,
            "result": result
        }

        log5(f"[REChain] Final reasoning output: {output}")
        return output
