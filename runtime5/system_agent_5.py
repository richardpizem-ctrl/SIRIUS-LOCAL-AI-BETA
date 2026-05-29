# runtime5/system_agent_5.py

from runtime5.runtime5 import Runtime5
from runtime5.kg_core import KnowledgeGraph
from runtime5.kg_loader import KGLoader
from runtime5.logging_5 import log5
from runtime5.system_hooks_5 import SystemHooks5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.error_handler_5 import ErrorHandler5


class SystemAgent5:
    """
    System Agent 5.x
    Entry point for the entire Runtime5 system.

    Responsibilities:
    - system startup/shutdown hooks
    - safe initialization of KnowledgeGraph
    - safe request handling
    - degraded mode reporting
    - Self‑Repair Layer compatibility
    """

    def __init__(self):
        # System startup event
        SystemHooks5.on_startup()
        log5("[SystemAgent5] System startup.")

        # Initialize Knowledge Graph safely
        def _init_kg():
            kg = KnowledgeGraph()
            loader = KGLoader()

            # Load all packs (safe, validated)
            packs = loader.load_all()

            log5(f"[SystemAgent5] Loaded {len(packs)} knowledge packs.")
            return kg

        self.kg = ErrorHandler5.safe_execute(
            _init_kg,
            context="KG initialization",
            fallback=KnowledgeGraph()
        )

        # Initialize Runtime5
        self.runtime = Runtime5(self.kg)
        log5("[SystemAgent5] Runtime5 initialized.")

    # --------------------------------------------------------
    # REQUEST HANDLING
    # --------------------------------------------------------
    def handle_request(self, text: str) -> dict:
        log5(f"[SystemAgent5] Handling request: {text}")

        def _exec():
            output = self.runtime.process(text)

            return {
                "input": text,
                "reasoning": output.get("reasoning"),
                "workflow": output.get("workflow"),
                "degraded": HealthMonitor5.is_degraded()
            }

        return ErrorHandler5.safe_execute(
            _exec,
            context={"input": text},
            fallback={
                "input": text,
                "reasoning": None,
                "workflow": None,
                "error": "SystemAgent5 failed.",
                "degraded": HealthMonitor5.is_degraded()
            }
        )

    # --------------------------------------------------------
    # SHUTDOWN
    # --------------------------------------------------------
    def shutdown(self):
        log5("[SystemAgent5] System shutdown.")
        SystemHooks5.on_shutdown()
