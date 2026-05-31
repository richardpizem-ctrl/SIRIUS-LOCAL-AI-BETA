"""
SIRIUS Runtime 5.1.0 – Knowledge Graph Integrity Engine
Integrity Validator 3.1

Účel:
- validovať štruktúru KG entít
- detegovať chýbajúce referencie
- detegovať poškodené alebo neúplné entity
- poskytovať detailné výsledky pre opravné moduly
"""

from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class IntegrityIssue:
    type: str
    entity: str
    details: Dict[str, Any]


@dataclass
class IntegrityResult:
    ok: bool
    issues: List[IntegrityIssue]
    details: Dict[str, Any]


class IntegrityValidator31:
    """
    Validator Integrity 3.1

    Kontroluje:
    - povinné polia entít
    - validitu vzťahov
    - existenciu cieľových entít
    """

    REQUIRED_FIELDS = ["id", "type", "relations"]

    def __init__(self, logger):
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def validate(self, kg) -> IntegrityResult:
        """
        Validuje celý Knowledge Graph.
        """
        issues: List[IntegrityIssue] = []

        self.logger.info("IntegrityValidator31: starting KG validation")

        for entity_id, entity in kg.entities.items():
            # 1) kontrola povinných polí
            for field in self.REQUIRED_FIELDS:
                if field not in entity:
                    issues.append(
                        IntegrityIssue(
                            type="MISSING_FIELD",
                            entity=entity_id,
                            details={"field": field}
                        )
                    )

            # 2) kontrola typu
            if not isinstance(entity.get("type"), str):
                issues.append(
                    IntegrityIssue(
                        type="INVALID_TYPE",
                        entity=entity_id,
                        details={"value": entity.get("type")}
                    )
                )

            # 3) kontrola vzťahov
            relations = entity.get("relations", [])
            if not isinstance(relations, list):
                issues.append(
                    IntegrityIssue(
                        type="INVALID_RELATIONS_FORMAT",
                        entity=entity_id,
                        details={"value": relations}
                    )
                )
                continue

            for rel in relations:
                if not isinstance(rel, dict) or "target" not in rel:
                    issues.append(
                        IntegrityIssue(
                            type="BROKEN_RELATION",
                            entity=entity_id,
                            details={"relation": rel}
                        )
                    )
                    continue

                target = rel["target"]

                # 4) kontrola existencie cieľovej entity
                if target not in kg.entities:
                    issues.append(
                        IntegrityIssue(
                            type="MISSING_REFERENCE",
                            entity=entity_id,
                            details={"target": target}
                        )
                    )

        ok = len(issues) == 0

        self.logger.info(
            "IntegrityValidator31: validation finished",
            extra={"ok": ok, "issues": len(issues)}
        )

        return IntegrityResult(
            ok=ok,
            issues=issues,
            details={"issue_count": len(issues)}
        )
