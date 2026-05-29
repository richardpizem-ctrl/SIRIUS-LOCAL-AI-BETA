# runtime5/kg_integrity.py

from runtime5.kg_core import KnowledgeGraph

class KGIntegrity:
    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg

    def check_missing_entities(self):
        """Return list of relations that reference non‑existing entities."""
        missing = []
        for r in self.kg.relations:
            if r.source not in self.kg.entities or r.target not in self.kg.entities:
                missing.append((r.source, r.relation, r.target))
        return missing

    def check_duplicate_entities(self):
        """Return list of duplicate entity names (should be none)."""
        # entities are stored in dict → duplicates cannot exist
        return []  # placeholder for future logic

    def check_cycles(self):
        """Detect simple cycles in 'is_a' hierarchy."""
        cycles = []

        for entity in self.kg.entities:
            visited = set()
            current = entity

            while True:
                parents = [
                    r.target for r in self.kg.relations
                    if r.source == current and r.relation == "is_a"
                ]

                if not parents:
                    break

                parent = parents[0]

                if parent in visited:
                    cycles.append((entity, parent))
                    break

                visited.add(parent)
                current = parent

        return cycles

    def validate(self):
        """Return dict with all integrity checks."""
        return {
            "missing_entities": self.check_missing_entities(),
            "cycles": self.check_cycles(),
            "duplicate_entities": self.check_duplicate_entities()
        }
