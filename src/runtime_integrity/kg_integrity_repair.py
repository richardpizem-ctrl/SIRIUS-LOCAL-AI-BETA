"""
SIRIUS Runtime 5.1.0 – Runtime Integrity Engine 1.0
KG Integrity Repair 1.0

Účel:
- detegovať a opravovať poškodené KG entity
- spolupracovať so Self‑Repair Layer (RepairPlanner / RepairCore)
- poskytovať bezpečné, deterministické opravy nad Knowledge Graphom
"""

from dataclasses import dataclass
from typing import Dict, Any, List, Optional


@dataclass
class KGRepairResult:
    ok: bool
    repaired_entities: List[str]
    removed_entities: List[str]
    fallback_used: bool
    details: Dict[str, Any]


class KGIntegrityRepair:
    """
    Opravný modul pre Knowledge Graph.

    Očakáva abstraktné rozhranie na KG:
    - loader       – načítanie entít / vzťahov
    - validator    – validácia integrity (KGIntegrity 2.0 / 3.1)
    - saver        – uloženie opraveného stavu
    - fallback     – načítanie minimálneho fallback balíka
    """

    def __init__(self, kg_loader, kg_validator, kg_saver, kg_fallback_loader, logger):
        self.kg_loader = kg_loader
        self.kg_validator = kg_validator
        self.kg_saver = kg_saver
        self.kg_fallback_loader = kg_fallback_loader
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def repair_entity(self, entity_id: str, context: Dict[str, Any]) -> KGRepairResult:
        """
        Opraví jednu konkrétnu entitu (ak je to možné).
        Použiteľné pri chybách typu:
        - KG_ENTITY_MISSING
        - KG_ENTITY_BROKEN
        """
        self.logger.info(
            "KGIntegrityRepair: repairing single entity",
            extra={"entity_id": entity_id}
        )

        kg = self.kg_loader.load()

        if entity_id not in kg.entities:
            self.logger.warning(
                "KGIntegrityRepair: entity not found, attempting fallback",
                extra={"entity_id": entity_id}
            )
            return self._fallback_repair(entity_id, context)

        # pokus o lokálnu opravu
        repaired = self._attempt_local_repair(kg, entity_id)

        if not repaired:
            self.logger.warning(
                "KGIntegrityRepair: local repair failed, removing entity",
                extra={"entity_id": entity_id}
            )
            removed = self._remove_entity(kg, entity_id)
            self.kg_saver.save(kg)
            return KGRepairResult(
                ok=True,
                repaired_entities=[],
                removed_entities=[entity_id] if removed else [],
                fallback_used=False,
                details={"mode": "entity_removed"}
            )

        # validácia po oprave
        valid = self.kg_validator.validate(kg)
        if not valid.ok:
            self.logger.error(
                "KGIntegrityRepair: KG invalid after entity repair, rolling back",
                extra={"entity_id": entity_id, "issues": valid.details}
            )
            return KGRepairResult(
                ok=False,
                repaired_entities=[],
                removed_entities=[],
                fallback_used=False,
                details={"reason": "kg_invalid_after_repair", "issues": valid.details}
            )

        self.kg_saver.save(kg)

        return KGRepairResult(
            ok=True,
            repaired_entities=[entity_id],
            removed_entities=[],
            fallback_used=False,
            details={"mode": "entity_repaired"}
        )

    def repair_global(self, context: Dict[str, Any]) -> KGRepairResult:
        """
        Globálna oprava KG – použiteľné pri:
        - rozsiahlych chybách
        - nekonzistentných vzťahoch
        - poškodených balíkoch
        """
        self.logger.info("KGIntegrityRepair: starting global KG repair")

        kg = self.kg_loader.load()
        validation = self.kg_validator.validate(kg)

        if validation.ok:
            self.logger.info("KGIntegrityRepair: KG already valid, nothing to repair")
            return KGRepairResult(
                ok=True,
                repaired_entities=[],
                removed_entities=[],
                fallback_used=False,
                details={"mode": "no_action_needed"}
            )

        # pokus o lokálne opravy podľa validatora
        repaired_entities: List[str] = []
        removed_entities: List[str] = []

        for issue in validation.issues:
            issue_type = issue.get("type")
            entity_id = issue.get("entity")

            if not entity_id:
                continue

            if issue_type == "MISSING_REFERENCE":
                # odstránime neplatný odkaz
                self._remove_invalid_reference(kg, issue)
                repaired_entities.append(entity_id)

            elif issue_type == "BROKEN_ENTITY":
                if self._attempt_local_repair(kg, entity_id):
                    repaired_entities.append(entity_id)
                else:
                    if self._remove_entity(kg, entity_id):
                        removed_entities.append(entity_id)

        # revalidácia
        revalidation = self.kg_validator.validate(kg)
        if not revalidation.ok:
            self.logger.error(
                "KGIntegrityRepair: KG still invalid after global repair, using fallback",
                extra={"issues": revalidation.details}
            )
            return self._fallback_global(context)

        self.kg_saver.save(kg)

        return KGRepairResult(
            ok=True,
            repaired_entities=repaired_entities,
            removed_entities=removed_entities,
            fallback_used=False,
            details={"mode": "global_repair"}
        )

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------

    def _attempt_local_repair(self, kg, entity_id: str) -> bool:
        """
        Pokus o lokálnu opravu entity:
        - doplnenie chýbajúcich polí default hodnotami
        - odstránenie neplatných vzťahov
        """
        entity = kg.entities.get(entity_id)
        if not entity:
            return False

        changed = False

        # príklad: doplnenie chýbajúcich polí
        if "type" not in entity:
            entity["type"] = "unknown"
            changed = True

        if "relations" in entity and isinstance(entity["relations"], list):
            valid_relations = []
            for rel in entity["relations"]:
                if isinstance(rel, dict) and "target" in rel:
                    valid_relations.append(rel)
                else:
                    changed = True
            entity["relations"] = valid_relations

        if changed:
            kg.entities[entity_id] = entity

        return changed

    def _remove_entity(self, kg, entity_id: str) -> bool:
        """
        Bezpečne odstráni entitu z KG a všetky odkazy na ňu.
        """
        if entity_id not in kg.entities:
            return False

        del kg.entities[entity_id]

        # odstránime odkazy z iných entít
        for e_id, e in kg.entities.items():
            if "relations" not in e or not isinstance(e["relations"], list):
                continue
            new_rel = [r for r in e["relations"] if r.get("target") != entity_id]
            if len(new_rel) != len(e["relations"]):
                e["relations"] = new_rel

        return True

    def _remove_invalid_reference(self, kg, issue: Dict[str, Any]) -> None:
        """
        Odstráni konkrétny neplatný odkaz podľa informácií z validatora.
        """
        source = issue.get("source")
        target = issue.get("target")

        if not source or not target:
            return

        entity = kg.entities.get(source)
        if not entity or "relations" not in entity:
            return

        entity["relations"] = [
            r for r in entity["relations"]
            if r.get("target") != target
        ]
        kg.entities[source] = entity

    # ---------------------------------------------------------
    # FALLBACK MODES
    # ---------------------------------------------------------

    def _fallback_repair(self, entity_id: str, context: Dict[str, Any]) -> KGRepairResult:
        """
        Fallback pre prípad, že entita neexistuje alebo je neopraviteľná.
        """
        self.logger.warning(
            "KGIntegrityRepair: using fallback for entity",
            extra={"entity_id": entity_id}
        )

        minimal_kg = self.kg_fallback_loader.load_minimal()
        self.kg_saver.save(minimal_kg)

        return KGRepairResult(
            ok=True,
            repaired_entities=[],
            removed_entities=[],
            fallback_used=True,
            details={"mode": "entity_fallback", "entity_id": entity_id}
        )

    def _fallback_global(self, context: Dict[str, Any]) -> KGRepairResult:
        """
        Globálny fallback – návrat k minimálnemu KG balíku.
        """
        self.logger.warning("KGIntegrityRepair: using global KG fallback")

        minimal_kg = self.kg_fallback_loader.load_minimal()
        self.kg_saver.save(minimal_kg)

        return KGRepairResult(
            ok=True,
            repaired_entities=[],
            removed_entities=[],
            fallback_used=True,
            details={"mode": "global_fallback"}
        )
