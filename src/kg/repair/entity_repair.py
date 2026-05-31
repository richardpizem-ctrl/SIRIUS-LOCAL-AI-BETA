"""
SIRIUS Runtime 5.1.0 – Knowledge Graph Repair Layer 1.0
Entity Repair 1.0

Účel:
- lokálne opravy poškodených KG entít
- doplnenie chýbajúcich polí
- odstránenie neplatných alebo poškodených vzťahov
- normalizácia dát bez generovania obsahu
"""

from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class EntityRepairResult:
    ok: bool
    changed: bool
    removed_relations: int
    details: Dict[str, Any]


class EntityRepair:
    """
    Nízkoúrovňový opravný modul pre jednu entitu KG.

    Používa sa v:
    - KGIntegrityRepair
    - KGRepairPlanner
    - KGRepairValidator
    """

    REQUIRED_FIELDS = ["id", "type", "relations"]

    def __init__(self, logger):
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def repair(self, entity_id: str, kg) -> EntityRepairResult:
        """
        Opraví jednu entitu v KG.

        Kroky:
        1) doplnenie chýbajúcich polí
        2) odstránenie neplatných vzťahov
        3) normalizácia dát
        """
        entity = kg.entities.get(entity_id)

        if not entity:
            return EntityRepairResult(
                ok=False,
                changed=False,
                removed_relations=0,
                details={"reason": "entity_not_found"}
            )

        changed = False
        removed_relations = 0

        # 1) doplnenie chýbajúcich polí
        for field in self.REQUIRED_FIELDS:
            if field not in entity:
                entity[field] = self._default_value(field)
                changed = True

        # 2) odstránenie neplatných vzťahov
        if isinstance(entity.get("relations"), list):
            valid_relations = []
            for rel in entity["relations"]:
                if isinstance(rel, dict) and "target" in rel:
                    valid_relations.append(rel)
                else:
                    removed_relations += 1
                    changed = True
            entity["relations"] = valid_relations

        # 3) normalizácia typu
        if not isinstance(entity.get("type"), str):
            entity["type"] = "unknown"
            changed = True

        # uloženie späť
        kg.entities[entity_id] = entity

        self.logger.info(
            "EntityRepair: entity repaired",
            extra={
                "entity_id": entity_id,
                "changed": changed,
                "removed_relations": removed_relations
            }
        )

        return EntityRepairResult(
            ok=True,
            changed=changed,
            removed_relations=removed_relations,
            details={"entity_id": entity_id}
        )

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------

    def _default_value(self, field: str):
        """
        Default hodnoty pre chýbajúce polia.
        """
        if field == "relations":
            return []
        if field == "type":
            return "unknown"
        return None
