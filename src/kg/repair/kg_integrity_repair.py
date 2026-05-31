"""
SIRIUS Runtime 5.1.0 – Knowledge Graph Repair Layer 1.0
KG Integrity Repair – Orchestrator 1.0
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class KGIntegrityRepairResult:
    ok: bool
    applied_steps: int
    fallback_used: bool
    details: Dict[str, Any]


class KGIntegrityRepair:
    """
    Hlavný orchestrátor KG opráv.
    """

    def __init__(self, validator, planner, sandbox, fallback, logger):
        self.validator = validator
        self.planner = planner
        self.sandbox = sandbox
        self.fallback = fallback
        self.logger = logger

    # ---------------------------------------------------------

    def repair(self, kg) -> KGIntegrityRepairResult:
        self.logger.info("KGIntegrityRepair: starting repair")

        # 1) VALIDATE
        validation = self.validator.validate(kg)
        if validation.ok:
            return KGIntegrityRepairResult(
                ok=True,
                applied_steps=0,
                fallback_used=False,
                details={"reason": "no_issues"},
            )

        # 2) PLAN
        plan = self.planner.build_plan(validation)

        # fallback?
        if plan.reason == "too_damaged":
            fb = self.fallback.apply_minimal_pack()
            return KGIntegrityRepairResult(
                ok=fb.ok,
                applied_steps=0,
                fallback_used=True,
                details=fb.details,
            )

        # 3) EXECUTE
        exec_result = self.sandbox.execute_plan(kg, plan)

        if not exec_result.ok:
            fb = self.fallback.apply_minimal_pack()
            return KGIntegrityRepairResult(
                ok=False,
                applied_steps=0,
                fallback_used=True,
                details={"sandbox_error": exec_result.details, "fallback": fb.details},
            )

        # 4) VERIFY
        post_validation = self.validator.validate(kg)

        return KGIntegrityRepairResult(
            ok=post_validation.ok,
            applied_steps=len(plan.steps),
            fallback_used=False,
            details={"issues_after": len(post_validation.issues)},
        )
