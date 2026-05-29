# runtime5/kg_query.py

from collections import deque
from runtime5.kg_core import KnowledgeGraph
from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class KGQuery:
    """
    Knowledge Graph Query Engine for Runtime 5.x.
    Provides:
    - safe relation lookup
    - shortest path search
    - diagnostics
    - degraded mode awareness
    """

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        log5("[KGQuery] Initialized query engine.")

    # --------------------------------------------------------
    # RELATED ENTITIES
    # --------------------------------------------------------
    def get_related_entities(self, entity: str):
        """
        Returns all entities directly connected to the given entity.
        """
        def _exec():
            key = entity.strip().lower()

            if key not in self.kg.entities:
                log5(f"[KGQuery] Entity '{entity}' not found.")
                return []

            results = []
            for r in self.kg.relations:
                if r.source.lower() == key:
                    results.append({"relation": r.relation, "entity": r.target})
                elif r.target.lower() == key:
                    results.append({"relation": r.relation, "entity": r.source})

            log5(f"[KGQuery] Related entities for '{entity}': {len(results)} found")
            return results

        return ErrorHandler5.safe_execute(
            _exec,
            context=entity,
            fallback=[]
        )

    # --------------------------------------------------------
    # SHORTEST PATH (BFS)
    # --------------------------------------------------------
    def shortest_path(self, start: str, end: str):
        """
        Breadth‑first search for shortest relation path.
        Returns list of entity names or None.
        """
        def _exec():
            s = start.strip().lower()
            e = end.strip().lower()

            if s not in self.kg.entities or e not in self.kg.entities:
                log5(f"[KGQuery] Path search failed: '{start}' or '{end}' not found.")
                return None

            queue = deque([(s, [s])])
            visited = set()

            while queue:
                current, path = queue.popleft()

                if current == e:
                    log5(f"[KGQuery] Shortest path found: {path}")
                    return path

                visited.add(current)

                for rel in self.get_related_entities(current):
                    neighbor = rel["entity"].lower()
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

            log5(f"[KGQuery] No path found between '{start}' and '{end}'.")
            return None

        return ErrorHandler5.safe_execute(
            _exec,
            context={"start": start, "end": end},
            fallback=None
        )
