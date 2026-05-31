"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair Planner 1.0

Účel:
- analyzovať vstupné signály (integrity, workflow, OS, KG)
- rozhodnúť, aký typ opravy spustiť
- vytvoriť deterministický plán opráv pre RepairCore
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Literal


RepairActionType = Literal[
    "KG_REPAIR",
    "WORKFLOW_RECOVERY",
    "SAFE_RETRY",
    "DEGRADED_CONTINUE",
    "OS_VALIDATION_REPAIR",
    "APPLY_KG_FALLBACK",
]


@dataclass
class RepairStep:
    action: RepairActionType
    target: str
    details: Dict[str, Any]


@dataclass
class RepairPlan:
    steps: List[RepairStep]
    reason: str
    severity: str  # LOW / MEDIUM / HIGH / CRITICAL


class RepairPlanner:
    """
    Deterministický plánovač opráv.

    Vstupy (context):
    - integrity: výsledky Integrity Engine / KG validatora
    - workflow: informácie o zlyhaní workflow
    - os_state: výsledky OSValidationRepair
    - kg_state: informácie o KG (napr. too_damaged, fallback_applied)
    """

    def __init__(self, logger):
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def build_plan(self, context: Dict[str, Any]) -> RepairPlan:
        """
        Vytvorí plán opráv na základe kontextu.

        Kontext môže obsahovať:
        - context["integrity"]["kg_issues"]
        - context["workflow"]["last_error"]
        - context["os"]["warnings"]
        - context["kg"]["too_damaged"]
        """
        steps: List[RepairStep] = []

        self.logger.info("RepairPlanner: building repair plan", extra={"context_keys": list(context.keys())})

        # 1) OS problémy majú vysokú prioritu
        os_state = context.get("os") or {}
        if os_state.get("warnings"):
            steps.append(
                RepairStep(
                    action="OS_VALIDATION_REPAIR",
                    target="os_environment",
                    details={"warnings": os_state["warnings"]},
                )
            )

        # 2) KG integrita
        integrity = context.get("integrity") or {}
        kg_issues = integrity.get("kg_issues") or []

        if context.get("kg", {}).get("too_damaged"):
            # KG je v kritickom stave → fallback
            steps.append(
                RepairStep(
                    action="APPLY_KG_FALLBACK",
                    target="knowledge_graph",
                    details={"reason": "too_damaged"},
                )
            )
        elif kg_issues:
            steps.append(
                RepairStep(
                    action="KG_REPAIR",
                    target="knowledge_graph",
                    details={"issue_count": len(kg_issues)},
                )
            )

        # 3) Workflow problémy
        workflow = context.get("workflow") or {}
        last_error = workflow.get("last_error")
        if last_error:
            error_type = last_error.get("type")

            if error_type == "TRANSIENT":
                steps.append(
                    RepairStep(
                        action="SAFE_RETRY",
                        target=workflow.get("step_id", "unknown_step"),
                        details={"error": last_error},
                    )
                )
            elif error_type == "STEP_CORRUPTED":
                steps.append(
                    RepairStep(
                        action="WORKFLOW_RECOVERY",
                        target=workflow.get("workflow_id", "unknown_workflow"),
                        details={"error": last_error},
                    )
                )
            elif error_type == "NON_RECOVERABLE":
                steps.append(
                    RepairStep(
                        action="DEGRADED_CONTINUE",
                        target=workflow.get("workflow_id", "unknown_workflow"),
                        details={"error": last_error},
                    )
                )

        # 4) určenie závažnosti
        severity = self._compute_severity(context, steps)

        if not steps:
            return RepairPlan(
                steps=[],
                reason="no_repairs_needed",
                severity="LOW",
            )

        return RepairPlan(
            steps=steps,
            reason="issues_detected",
            severity=severity,
        )

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------

    def _compute_severity(self, context: Dict[str, Any], steps: List[RepairStep]) -> str:
        """
        Jednoduché, deterministické určenie závažnosti.
        """
        if any(s.action in ("APPLY_KG_FALLBACK", "OS_VALIDATION_REPAIR") for s in steps):
            return "CRITICAL"

        integrity = context.get("integrity") or {}
        kg_issues = integrity.get("kg_issues") or []

        if len(kg_issues) > 20:
            return "HIGH"
        if len(kg_issues) > 0:
            return "MEDIUM"

        return "LOW"
