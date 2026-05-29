# runtime5/kg_integrity.py

from runtime5.kg_core import KnowledgeGraph
from runtime5.logging_5 import log5
from runtime5.error_handler_5 import ErrorHandler5
from runtime5.health_monitor_5 import HealthMonitor5
from runtime5.system_hooks_5 import SystemHooks5


class KGIntegrity:
    """
    Knowledge Graph Integrity Checker for Runtime 5.x.
    Provides:
    - missing entity detection
    - cycle detection
    - duplicate detection (future)
    - diagnostics
    - degraded mode awareness
    """

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        log5("[KGIntegrity] Initialized integrity checker.")

    # --------------------------------------------------------
    # MISSING ENTITIES
    # --------------------------------------------------------
    def check_missing_entities(self):
        def _exec():
            missing = []
            for r in self.kg.relations:
                if r.source.lower() not in self.kg.entities or r.target.lower() not in self.kg.entities:
                    missing.append(r.to_dict())

            log5(f"[KGIntegrity] Missing entities: {len(missing)}")
            return missing

        return ErrorHandler5.safe_execute(_exec, fallback=[])

    # --------------------------------------------------------
    # DUPLICATES
    # --------------------------------------------------------
    def check_duplicate_entities(self):
        """
        Entities are stored in a dict → duplicates cannot exist.
        But we keep this for future KGLoader validation.
        """
        return []

    # --------------------------------------------------------
    # CYCLE DETECTION
    # --------------------------------------------------------
    def check_cycles(self):
        def _exec():
            cycles = []

            for entity in self.kg.entities:
                visited = set()
                current = entity

                while True:
                    parents = [
                        r.target for r in self.kg.relations
                        if r.source.lower() == current and r.relation == "is_a"
                    ]

                    if not parents:
                        break

                    parent = parents[0].lower()

                    if parent in visited:
                        cycles.append({"entity": entity, "cycle_at": parent})
                        break

                    visited.add(parent)
                    current = parent

            log5(f"[KGIntegrity] Cycles detected: {len(cycles)}")
            return cycles

        return ErrorHandler5.safe_execute(_exec, fallback=[])

    # --------------------------------------------------------
    # VALIDATION SUMMARY
    # --------------------------------------------------------
    def validate(self):
        def _exec():
            result = {
                "missing_entities": self.check_missing_entities(),
                "cycles": self.check_cycles(),
                "duplicate_entities": self.check_duplicate_entities(),
                "degraded": HealthMonitor5.is_degraded()
            }

            if result["missing_entities"] or result["cycles"]:
                SystemHooks5.on_error("KGIntegrity validation failed.")

            log5(f"[KGIntegrity] Validation summary: {result}")
            return result

        return ErrorHandler5.safe_execute(_exec, fallback={})
