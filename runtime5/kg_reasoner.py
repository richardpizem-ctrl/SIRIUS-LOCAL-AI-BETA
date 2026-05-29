# runtime5/kg_reasoner.py

from runtime5.kg_query import KGQuery
from runtime5.kg_core import KnowledgeGraph

class KGReasoner:
    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.query = KGQuery(kg)

    def infer_parent(self, entity: str):
        """Return the first 'is_a' parent of an entity."""
        relations = self.query.get_related_entities(entity)
        for rel, target in relations:
            if rel == "is_a":
                return target
        return None

    def infer_all_parents(self, entity: str):
        """Return full parent chain: Dog → Animal → LivingThing."""
        parents = []
        current = entity

        while True:
            parent = self.infer_parent(current)
            if not parent:
                break
            parents.append(parent)
            current = parent

        return parents

    def infer_relation_path(self, a: str, b: str):
        """Return shortest path between two entities."""
        return self.query.shortest_path(a, b)
