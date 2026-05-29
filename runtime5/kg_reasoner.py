# runtime5/kg_reasoner.py

from runtime5.kg_query import KGQuery
from runtime5.kg_core import KnowledgeGraph
from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class KGReasoner:
    """
    Knowledge Graph Reasoner for Runtime 5.x.
    Provides:
    - parent inference
    - full ancestry chain
    - relation path inference
    - diagnostics
    - degraded mode awareness
    """

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.query = KGQuery(kg)
        log5("[KGReasoner] Initialized reasoning engine.")

    # --------------------------------------------------------
    # DIRECT PARENT
    # --------------------------------------------------------
    def infer_parent(self, entity: str):
        """
        Returns the first 'is_a' parent of an entity.
        """
        def _exec():
            relations = self.query.get_related_entities(entity)

            for rel in relations:
                if rel["relation"] == "is_a":
                    log5(f"[KGReasoner] Parent of '{entity}' is '{rel['entity']}'")
                    return rel["entity"]

            log5(f"[KGReasoner] No parent found for '{entity}'")
            return None

        return ErrorHandler5.safe_execute(
            _exec,
            context=entity,
            fallback=None
        )

    # --------------------------------------------------------
    # FULL ANCESTRY CHAIN
    # --------------------------------------------------------
    def infer_all_parents(self, entity: str):
        """
        Returns full parent chain: Dog → Animal → LivingThing.
        """
        def _exec():
            parents = []
            current = entity

            visited = set()  # prevent cycles

            while True:
                parent = self.infer_parent(current)
                if not parent:
                    break

                if parent in visited:
                    log5(f"[KGReasoner] Cycle detected at '{parent}'")
                    break

                parents.append(parent)
                visited.add(parent)
                current = parent

            log5(f"[KGReasoner] Full parent chain for '{entity}': {parents}")
            return parents

        return ErrorHandler5.safe_execute(
            _exec,
            context=entity,
            fallback=[]
        )

    # --------------------------------------------------------
    # RELATION PATH
    # --------------------------------------------------------
    def infer_relation_path(self, a: str, b: str):
        """
        Returns shortest path between two entities.
        """
        def _exec():
            path = self.query.shortest_path(a, b)

            if path:
                log5(f"[KGReasoner] Path {a} → {b}: {path}")
            else:
                log5(f"[KGReasoner] No path found between '{a}' and '{b}'")

            return path

        return ErrorHandler5.safe_execute(
            _exec,
            context={"a": a, "b": b},
            fallback=None
        )
