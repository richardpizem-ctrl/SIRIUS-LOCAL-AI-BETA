# runtime5/kg_loader.py

import json
from runtime5.kg_core import KnowledgeGraph

class KGLoader:
    def __init__(self, base_path="knowledge_packs"):
        self.base_path = base_path

    def load_pack(self, filename: str) -> KnowledgeGraph:
        """
        Load a single knowledge pack JSON file into a new KnowledgeGraph.
        Expected format:
        {
            "entities": {
                "Dog": {"type": "animal"},
                "Animal": {}
            },
            "relations": [
                ["Dog", "is_a", "Animal"]
            ]
        }
        """
        kg = KnowledgeGraph()
        path = f"{self.base_path}/{filename}"

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for name, attrs in data.get("entities", {}).items():
            kg.add_entity(name, attrs)

        for src, rel, tgt in data.get("relations", []):
            kg.add_relation(src, rel, tgt)

        return kg
