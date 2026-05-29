# runtime5/kg_store.py

import json
from runtime5.kg_core import KnowledgeGraph, KGEntity, KGRelation

class KGStore:
    def __init__(self, path="kg_data.json"):
        self.path = path

    def save(self, kg: KnowledgeGraph):
        data = {
            "entities": {
                name: entity.attributes
                for name, entity in kg.entities.items()
            },
            "relations": [
                {
                    "source": r.source,
                    "relation": r.relation,
                    "target": r.target
                }
                for r in kg.relations
            ]
        }

        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load(self) -> KnowledgeGraph:
        kg = KnowledgeGraph()

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return kg

        for name, attributes in data["entities"].items():
            kg.add_entity(name, attributes)

        for rel in data["relations"]:
            kg.add_relation(rel["source"], rel["relation"], rel["target"])

        return kg
