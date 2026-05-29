# runtime5/system_agent_5.py

from runtime5 import Runtime5, KnowledgeGraph
from runtime5.kg_loader import KnowledgeGraphLoader
from runtime5.logging_5 import log5
from runtime5.system_hooks_5 import SystemHooks5
from runtime5.health_monitor_5 import HealthMonitor5


class SystemAgent5:
    """
    System Agent 5.0
    Wraps Runtime5 and exposes a simple handle_request() API.
    Includes:
    - startup hook
    - error hook
    - shutdown hook
    - degraded mode reporting
    """

    def __init__(self):
        # System startup event
        SystemHooks5.on_startup()

        # Initialize Knowledge Graph
        kg = KnowledgeGraph()
        loader = KnowledgeGraphLoader(kg)
        loader.load_minimal_test_data()

        # Initialize Runtime5
        self.runtime = Runtime5(kg)
        log5("[SystemAgent5] Initialized with minimal KG.")

    def handle_request(self, text: str) -> dict:
        log5(f"[SystemAgent5] Handling request: {text}")

        try:
            output = self.runtime.process(text)
        except Exception as exc:
            # System-level error hook
            SystemHooks5.on_error(str(exc))
            return {
                "input": text,
                "reasoning": None,
                "workflow": None,
                "error": str(exc),
                "degraded": HealthMonitor5.is_degraded()
            }

        return {
            "input": text,
            "reasoning": output.get("reasoning"),
            "workflow": output.get("workflow"),
            "degraded": HealthMonitor5.is_degraded()
        }

    def shutdown(self):
        # System shutdown event
        SystemHooks5.on_shutdown()
