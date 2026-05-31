"""
SIRIUS Runtime 5.1.0 – KG Repair Layer
KG Repair Sandbox 1.0

Účel:
- bezpečne vykonávať opravné kroky
- izolovať zmeny od hlavného KG
"""

from dataclasses import dataclass
from typing import Dict, Any
import copy


@dataclass
class SandboxResult:
    ok: bool
    details: Dict[str, Any]


class KGRepairSandbox:
    """
    Sandbox pre bezpečné vykonávanie opráv.

    Princípy:
    - pracuje na kópii KG
    - ak všetko prebehne OK → commit
    - ak nie → rollback
    """

    def __init__(self, entity_repair, logger):
        self.entity_repair = entity_repair
        self.logger = logger

    def execute_plan(self, kg, plan):
        sandbox_kg = copy.deepcopy(kg)

        for step in plan.steps:
            if step["action"] == "repair_entity":
                result = self.entity_repair.repair(step["entity"], sandbox_kg)
                if not result.ok:
                    return SandboxResult(
                        ok=False,
                        details={"failed_step": step, "reason": "entity_repair_failed"}
                    )

            elif step["action"] == "remove_relation":
                entity = sandbox_kg.entities.get(step["entity"])
                if entity:
                    entity["relations"] = [
                        r for r in entity["relations"]
                        if r.get("target") != step["target"]
                    ]

        # commit
        kg.entities = sandbox_kg.entities
        return SandboxResult(ok=True, details={"applied_steps": len(plan.steps)})
