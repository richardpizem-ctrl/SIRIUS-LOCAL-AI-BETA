# runtime5/kg_router.py

from runtime5.kg_reasoner import KGReasoner
from runtime5.kg_core import KnowledgeGraph
from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class KGRouter:
    """
    Knowledge Graph Router for Runtime 5.x.
    Decides:
    - whether intent belongs to KG Reasoner
    - whether entity exists
    - which reasoning path to use
    Provides:
    - diagnostics
    - degraded mode awareness
    """

    KG_INTENTS = {
        "explain", "define", "context", "relation", "parent",
        "ancestors", "path", "kg", "knowledge"
    }

    ENVOY_INTENTS = {
        "fetch", "online", "lookup", "search", "web"
    }

    SYSTEM_INTENTS = {
        "open_app", "click", "type", "automation", "system"
    }

    WORKFLOW_DEFAULT = "WORKFLOW"

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.reasoner = KGReasoner(kg)
        log5("[KGRouter] Initialized KG Router 5.x")

    # --------------------------------------------------------
    # INTENT ROUTING
    # --------------------------------------------------------
    def route_intent(self, intent: str):
        """
        Decide if the intent should be handled by:
        - KG Reasoner
        - Envoy
        - System Agent
        - Workflow Engine
        """
        def _exec():
            i = intent.strip().lower()

            if i in self.KG_INTENTS:
                log5(f"[KGRouter] Intent '{intent}' → KG_REASONING")
                return "KG_REASONING"

            if i in self.ENVOY_INTENTS:
                log5(f"[KGRouter] Intent '{intent}' → ENVOY")
                return "ENVOY"

            if i in self.SYSTEM_INTENTS:
                log5(f"[KGRouter] Intent '{intent}' → SYSTEM_AGENT")
                return "SYSTEM_AGENT"

            log5(f"[KGRouter] Intent '{intent}' → WORKFLOW")
            return self.WORKFLOW_DEFAULT

        return ErrorHandler5.safe_execute(
            _exec,
            context=intent,
            fallback=self.WORKFLOW_DEFAULT
        )

    # --------------------------------------------------------
    # ENTITY CHECK
    # --------------------------------------------------------
    def is_kg_relevant(self, entity: str):
        """
        Returns True if entity exists in KG.
        """
        def _exec():
            key = entity.strip().lower()
            exists = key in self.kg.entities
            log5(f"[KGRouter] Entity '{entity}' exists: {exists}")
            return exists

        return ErrorHandler5.safe_execute(
            _exec,
            context=entity,
            fallback=False
        )

    # --------------------------------------------------------
    # CONTEXT CHAIN
    # --------------------------------------------------------
    def get_context_chain(self, entity: str):
        """
        Return full parent chain using KG Reasoner.
        """
        def _exec():
            if not self.is_kg_relevant(entity):
                log5(f"[KGRouter] Cannot get context chain: '{entity}' not in KG")
                return []

            chain = self.reasoner.infer_all_parents(entity)
            log5(f"[KGRouter] Context chain for '{entity}': {chain}")
            return chain

        return ErrorHandler5.safe_execute(
            _exec,
            context=entity,
            fallback=[]
        )
