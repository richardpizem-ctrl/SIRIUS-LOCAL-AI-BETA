# runtime5/kg_query.py

from collections import deque
from runtime5.kg_core import KnowledgeGraph

class KGQuery:
    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg

    def get_related_entities(self, entity: str):
        """Return all entities directly connected to the given entity."""
        results = []
        for r in self.kg.relations:
            if r.source == entity:
                results.append((r.relation, r.target))
            elif r.target == entity:
                results.append((r.relation, r.source))
        return results

    def shortest_path(self, start: str, end: str):
        """Breadth‑first search for shortest relation path."""
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current, path = queue.popleft()

            if current == end:
                return path

            visited.add(current)

            for rel, neighbor in self.get_related_entities(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None  # no path found
