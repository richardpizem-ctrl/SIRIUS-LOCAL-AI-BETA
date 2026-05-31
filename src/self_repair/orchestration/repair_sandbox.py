"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair Sandbox 1.0

Účel:
- bezpečne vykonávať plán opráv vytvorený RepairPlanner
- smerovať jednotlivé kroky na špecializované executory (KG, workflow, OS…)
- zabezpečiť deterministický výsledok a auditovateľný priebeh
"""

from dataclasses import dataclass
from typing import Dict, Any, List

from .repair_planner import RepairPlan, RepairStep


@dataclass
class RepairExecutionResult:
    ok: bool
    executed_steps: int
    failed_step: int | None
    details: Dict[str, Any]


class RepairSandbox:
    """
    RepairSandbox – router a exekútor opráv pre Self‑Repair Layer.

    Očakávané závislosti (dependency injection):
        kg_repair_executor          – komponent pre KG_REPAIR
        workflow_recovery_executor  – komponent pre WORKFLOW_RECOVERY
        safe_retry_executor         – komponent pre SAFE_RETRY
        degraded_continue_executor  – komponent pre DEGRADED_CONTINUE
        os_validation_executor      – komponent pre OS_VALIDATION_REPAIR
        kg_fallback_executor        – komponent pre APPLY_KG_FALLBACK (ak sa použije)
    """

    def __init__(
        self,
        kg_repair_executor=None,
        workflow_recovery_executor=None,
        safe_retry_executor=None,
        degraded_continue_executor=None,
        os_validation_executor=None,
        kg_fallback_executor=None,
        logger=None,
    ):
        self.kg_repair_executor = kg_repair_executor
        self.workflow_recovery_executor = workflow_recovery_executor
        self.safe_retry_executor = safe_retry_executor
        self.degraded_continue_executor = degraded_continue_executor
        self.os_validation_executor = os_validation_executor
        self.kg_fallback_executor = kg_fallback_executor
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def execute_plan(self, plan: RepairPlan) -> RepairExecutionResult:
        """
        Vykoná všetky kroky v pláne v deterministickom poradí.
        """
        if self.logger:
            self.logger.info(
                "RepairSandbox: executing repair plan",
                extra={"steps": len(plan.steps), "reason": plan.reason, "severity": plan.severity},
            )

        executed = 0
        step_results: List[Dict[str, Any]] = []

        for idx, step in enumerate(plan.steps):
            ok, info = self._execute_step(step)
            executed += 1

            step_results.append(
                {
                    "index": idx,
                    "action": step.action,
                    "target": step.target,
                    "ok": ok,
                    "details": info,
                }
            )

            if not ok:
                if self.logger:
                    self.logger.error(
                        "RepairSandbox: step failed",
                        extra={"index": idx, "action": step.action, "details": info},
                    )
                return RepairExecutionResult(
                    ok=False,
                    executed_steps=executed,
                    failed_step=idx,
                    details={"steps": step_results},
                )

        if self.logger:
            self.logger.info(
                "RepairSandbox: all steps executed successfully",
                extra={"executed_steps": executed},
            )

        return RepairExecutionResult(
            ok=True,
            executed_steps=executed,
            failed_step=None,
            details={"steps": step_results},
        )

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------

    def _execute_step(self, step: RepairStep) -> tuple[bool, Dict[str, Any]]:
        """
        Vykoná jeden krok plánu podľa typu akcie.
        Vráti (ok, details).
        """
        action = step.action

        if action == "KG_REPAIR" and self.kg_repair_executor:
            return self._safe_call(self.kg_repair_executor, "kg_repair", step)

        if action == "WORKFLOW_RECOVERY" and self.workflow_recovery_executor:
            return self._safe_call(self.workflow_recovery_executor, "workflow_recovery", step)

        if action == "SAFE_RETRY" and self.safe_retry_executor:
            return self._safe_call(self.safe_retry_executor, "safe_retry", step)

        if action == "DEGRADED_CONTINUE" and self.degraded_continue_executor:
            return self._safe_call(self.degraded_continue_executor, "degraded_continue", step)

        if action == "OS_VALIDATION_REPAIR" and self.os_validation_executor:
            return self._safe_call(self.os_validation_executor, "os_validation_repair", step)

        if action == "APPLY_KG_FALLBACK" and self.kg_fallback_executor:
            return self._safe_call(self.kg_fallback_executor, "kg_fallback", step)

        # neznáma alebo nepodporovaná akcia
        if self.logger:
            self.logger.error(
                "RepairSandbox: unsupported action",
                extra={"action": action, "target": step.target},
            )
        return False, {"error": "unsupported_action", "action": action, "target": step.target}

    def _safe_call(self, executor, kind: str, step: RepairStep) -> tuple[bool, Dict[str, Any]]:
        """
        Bezpečné volanie exekútora s ošetrením výnimiek.
        Očakáva sa API typu: executor.execute(step: RepairStep) -> dict | None
        """
        try:
            if self.logger:
                self.logger.info(
                    "RepairSandbox: executing step",
                    extra={"kind": kind, "action": step.action, "target": step.target},
                )

            result = executor.execute(step)
            result = result or {}

            return True, result
        except Exception as e:
            if self.logger:
                self.logger.exception(
                    "RepairSandbox: executor failed",
                    extra={"kind": kind, "action": step.action, "target": step.target, "error": str(e)},
                )
            return False, {"error": "executor_failed", "kind": kind, "details": str(e)}
