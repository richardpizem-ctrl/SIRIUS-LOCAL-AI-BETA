# runtime5/system_agent_5.py

from runtime5 import Runtime5, KnowledgeGraph
from runtime5.kg_loader import KnowledgeGraphLoader
from runtime5.logging_5 import log5


class SystemAgent5:
    """
    Minimal System Agent 5.0
    Wraps Runtime5 and exposes a simple handle_request() API.
    """

    def __init__(self):
        kg = KnowledgeGraph()
        loader = KnowledgeGraphLoader(kg)
        loader.load_minimal_test_data()

        self.runtime = Runtime5(kg)
        log5("[SystemAgent5] Initialized with minimal KG.")

    def handle_request(self, text: str) -> dict:
        log5(f"[SystemAgent5] Handling request: {text}")
        output = self.runtime.process(text)

        return {
            "input": text,
            "reasoning": output.get("reasoning"),
            "workflow": output.get("workflow")
        }
