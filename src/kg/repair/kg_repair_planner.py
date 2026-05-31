"""
SIRIUS Runtime 5.1.0 – KG Repair Layer
KG Repair Planner 1.0

Účel:
- analyzovať integrity issues
- rozhodnúť, ktoré opravné kroky sú potrebné
"""

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class RepairPlan:
    steps: List[Dict[str, Any]]
    reason: str


class KGRepairPlanner:
    """
    Plánovač opráv pre Knowledge Graph.

    Na základe Integrity 3.1 issues vytvorí:
    - entity_repair kroky
    - fallback kroky
    """

    def __init__(self, logger):
        self.logger = logger

    def build_plan(self, validation_result) -> RepairPlan:
        steps = []

        for issue in validation_result.issues:
            if issue.type in ("MISSING_FIELD", "INVALID_TYPE", "BROKEN_RELATION"):
                steps.append({
                    "action": "repair_entity",
                    "entity": issue.entity,
                    "issue": issue.type
                })

            elif issue.type == "MISSING_REFERENCE":
                steps.append({
                    "action": "remove_relation",
                    "entity": issue.entity,
                    "target": issue.details["target"]
                })

        if not steps:
            return RepairPlan(steps=[], reason="no_repairs_needed")

        return RepairPlan(steps=steps, reason="issues_detected")
