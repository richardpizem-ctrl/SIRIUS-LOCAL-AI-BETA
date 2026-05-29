# runtime5/reasoning_engine_5.py

from typing import Any, Dict

from runtime5.kg_core import KnowledgeGraph
from runtime5.kg_reasoner import KGReasoner
from runtime5.kg_router import KGRouter
from runtime5.logging_5 import log5

from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class ReasoningEngine5:
    """
    Reasoning Engine 5.x

    Core deterministic reasoning layer for Runtime 5.x.
    Responsibilities:
    - interpret resolved intent
    - route to KG Reasoner / System / Workflow
    - produce structured reasoning payload
    - diagnostics + degraded mode awareness
    """

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.reasoner = KGReasoner(kg)
        self.router = KGRouter(kg)

        log5("[ReasoningEngine5] Initialized reasoning engine.")

    # --------------------------------------------------------
    # MAIN ENTRYPOINT
    # --------------------------------------------------------
    def process(self, intent: Any, entity: str) -> Dict[str, Any]:
        """
        Main reasoning entrypoint.
        """
        log5(f"[ReasoningEngine5] Starting reasoning for intent={intent}, entity={entity!r}")

        def _exec():
            # Normalize entity
            e = entity.strip()

            # 1. Route intent
            route = self.router.route_intent(intent)
            log5(f"[ReasoningEngine5] Routed intent '{intent}' → {route}")

            # 2. KG Reasoning
            if route == "KG_REASONING":
                if not self.router.is_kg_relevant(e):
                    log5(f"[ReasoningEngine5] Entity '{e}' not found in KG.")
                    return {
                        "intent": intent,
                        "entity": e,
                        "route": route,
                        "result": None,
                        "error": f"Entity '{e}' not found in Knowledge Graph.",
                        "degraded": HealthMonitor5.is_degraded()
                    }

                # Parent chain
                parents = self.reasoner.infer_all_parents(e)

                # Direct parent
                parent = self.reasoner.infer_parent(e)

                # Reasoning payload
                payload = {
                    "intent": intent,
                    "entity": e,
                    "route": route,
                    "parent": parent,
                    "parent_chain": parents,
                    "degraded": HealthMonitor5.is_degraded()
                }

                log5(f"[ReasoningEngine5] KG reasoning payload: {payload}")
                return payload

            # 3. Envoy / System / Workflow placeholder
            payload = {
                "intent": intent,
                "entity": e,
                "route": route,
                "notes": "Non-KG reasoning path. Extend with system/automation logic.",
                "degraded": HealthMonitor5.is_degraded()
            }

            log5(f"[ReasoningEngine5] Non-KG reasoning payload: {payload}")
            return payload

        # Safe execution wrapper
        return ErrorHandler5.safe_execute(
            _exec,
            context={"intent": intent, "entity": entity},
            fallback={
                "intent": intent,
                "entity": entity,
                "route": None,
                "result": None,
                "error": "ReasoningEngine5 failed.",
                "degraded": HealthMonitor5.is_degraded()
            }
        )
