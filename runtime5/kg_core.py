# runtime5/kg_core.py

from runtime5.logging_5 import log5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5
from runtime5.error_handler_5 import ErrorHandler5


class KGEntity:
    def __init__(self, name: str, attributes=None):
        self.name = name
        self.attributes = attributes or {}

    def to_dict(self):
        return {
            "name": self.name,
            "attributes": self.attributes
        }


class KGRelation:
    def __init__(self, source: str, relation: str, target: str):
        self.source = source
        self.relation = relation
        self.target = target

    def to_dict(self):
        return {
            "source": self.source,
            "relation": self.relation,
            "target": self.target
        }


class KnowledgeGraph:
    """
    Knowledge Graph Core for Runtime 5.x
    Provides:
    - safe entity/relationship management
    - diagnostics
    - degraded mode awareness
    - Self‑Repair Layer compatibility
    """

    def __init__(self):
        self.entities = {}
        self.relations = []
        log5("[KnowledgeGraph] Initialized KG Core 5.x")

    # --------------------------------------------------------
    # ENTITY MANAGEMENT
    # --------------------------------------------------------
    def add_entity(self, name: str, attributes=None):
        def _exec():
            key = name.strip().lower()

            if key in self.entities:
                log5(f"[KG] Entity '{name}' already exists. Updating attributes.")
                self.entities[key].attributes.update(attributes or {})
            else:
                self.entities[key] = KGEntity(name, attributes)
                log5(f"[KG] Added entity: {name}")

        return ErrorHandler5.safe_execute(_exec, context=name)

    def get_entity(self, name: str):
        key = name.strip().lower()
        return self.entities.get(key)

    # --------------------------------------------------------
    # RELATION MANAGEMENT
    # --------------------------------------------------------
    def add_relation(self, source: str, relation: str, target: str):
        def _exec():
            if not source or not target:
                raise ValueError("Relation requires both source and target.")

            rel = KGRelation(source, relation, target)
            self.relations.append(rel)

            log5(f"[KG] Added relation: {source} -[{relation}]-> {target}")

        return ErrorHandler5.safe_execute(
            _exec,
            context={"source": source, "relation": relation, "target": target}
        )

    # --------------------------------------------------------
    # QUERY
    # --------------------------------------------------------
    def get_relations(self, entity: str):
        def _exec():
            key = entity.strip().lower()
            results = [
                r for r in self.relations
                if r.source.lower() == key or r.target.lower() == key
            ]

            log5(f"[KG] Query relations for '{entity}': {len(results)} found")
            return [r.to_dict() for r in results]

        return ErrorHandler5.safe_execute(_exec, context=entity, fallback=[])

    # --------------------------------------------------------
    # SNAPSHOT
    # --------------------------------------------------------
    def snapshot(self):
        """
        Returns a structured snapshot of the entire KG.
        Useful for debugging, exporting, or Self‑Repair Layer.
        """
        return {
            "entities": {k: e.to_dict() for k, e in self.entities.items()},
            "relations": [r.to_dict() for r in self.relations],
            "degraded": HealthMonitor5.is_degraded()
        }
