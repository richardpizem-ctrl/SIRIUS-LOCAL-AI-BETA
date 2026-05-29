# runtime5/kg_router.py

from runtime5.kg_reasoner import KGReasoner
from runtime5.kg_core import KnowledgeGraph

class KGRouter:
    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.reasoner = KGReasoner(kg)

    def route_intent(self, intent: str):
        """
        Decide if the intent should be handled by:
        - KG Reasoner
        - Workflow Engine
        - Envoy
        - System Agent
        """

        # KG‑related intents
        if intent in ["explain", "define", "context", "relation", "parent"]:
            return "KG_REASONING"

        # Envoy‑related intents
        if intent in ["fetch", "online", "lookup", "search"]:
            return "ENVOY"

        # System‑related intents
        if intent in ["open_app", "click", "type", "automation"]:
            return "SYSTEM_AGENT"

        # Workflow‑related intents
        return "WORKFLOW"

    def is_kg_relevant(self, entity: str):
        """Return True if entity exists in KG."""
        return entity in self.kg.entities

    def get_context_chain(self, entity: str):
        """Return full parent chain using KG Reasoner."""
        return self.reasoner.infer_all_parents(entity)
