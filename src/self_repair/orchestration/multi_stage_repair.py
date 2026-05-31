"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Multi‑Stage Repair 1.0

Účel:
- riadiť viacstupňové opravy (analyzuj → plánuj → vykonaj → over)
- umožniť sekvenčné spúšťanie viacerých typov opráv
- poskytovať deterministický priebeh pre RepairCore / Workflow Engine
"""

from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class StageResult:
    ok: bool
    stage: str
    details: Dict[str, Any]


class MultiStageRepair:
    """
    Viacstupňový orchestrátor opráv.

    Typický priebeh:
        1) ANALYZE      – zozbieranie signálov (integrity, workflow, OS, KG)
        2) PLAN         – vytvorenie RepairPlanu
        3) EXECUTE      – vykonanie plánu (sandbox, KG repair, workflow recovery…)
        4) VERIFY       – opätovná kontrola integrity / stavu
    """

    def __init__(
        self,
        context_provider,
        planner,
        sandbox_executor,
        validator,
        logger,
    ):
        """
        context_provider – komponent, ktorý vie zostaviť repair context (dict)
        planner          – RepairPlanner
        sandbox_executor – komponent, ktorý vie vykonať plán (napr. KGRepairSandbox, WorkflowRecovery, OSValidationRepair)
        validator        – komponent, ktorý vie overiť výsledný stav (Integrity / health)
        logger           – Logging5 / RepairLogger
        """
        self.context_provider = context_provider
        self.planner = planner
        self.sandbox_executor = sandbox_executor
        self.validator = validator
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def run_multi_stage(self) -> List[StageResult]:
        """
        Spustí kompletný viacstupňový proces opravy.
        Vráti zoznam StageResult pre audit a diagnostiku.
        """
        results: List[StageResult] = []

        # 1) ANALYZE
        analyze_result = self._stage_analyze()
        results.append(analyze_result)
        if not analyze_result.ok:
            return results

        # 2) PLAN
        plan_result, plan = self._stage_plan()
        results.append(plan_result)
        if not plan_result.ok or not plan.steps:
            return results

        # 3) EXECUTE
        exec_result = self._stage_execute(plan)
        results.append(exec_result)
        if not exec_result.ok:
            return results

        # 4) VERIFY
        verify_result = self._stage_verify()
        results.append(verify_result)

        return results

    # ---------------------------------------------------------
    # INTERNAL STAGES
    # ---------------------------------------------------------

    def _stage_analyze(self) -> StageResult:
        """
        ANALYZE – zozbiera kontext pre plánovanie opráv.
        """
        try:
            context = self.context_provider.build_context()
            self._last_context = context  # uložíme pre ďalšie kroky

            self.logger.info(
                "MultiStageRepair: ANALYZE completed",
                extra={"context_keys": list(context.keys())}
            )

            return StageResult(
                ok=True,
                stage="ANALYZE",
                details={"context_keys": list(context.keys())},
            )
        except Exception as e:
            self.logger.exception(
                "MultiStageRepair: ANALYZE failed",
                extra={"error": str(e)}
            )
            return StageResult(
                ok=False,
                stage="ANALYZE",
                details={"error": str(e)},
            )

    def _stage_plan(self):
        """
        PLAN – vytvorí RepairPlan na základe kontextu.
        """
        try:
            plan = self.planner.build_plan(self._last_context)

            self.logger.info(
                "MultiStageRepair: PLAN completed",
                extra={"steps": len(plan.steps), "reason": plan.reason, "severity": plan.severity}
            )

            result = StageResult(
                ok=True,
                stage="PLAN",
                details={
                    "steps": len(plan.steps),
                    "reason": plan.reason,
                    "severity": plan.severity,
                },
            )
            return result, plan
        except Exception as e:
            self.logger.exception(
                "MultiStageRepair: PLAN failed",
                extra={"error": str(e)}
            )
            result = StageResult(
                ok=False,
                stage="PLAN",
                details={"error": str(e)},
            )
            return result, None

    def _stage_execute(self, plan) -> StageResult:
        """
        EXECUTE – vykoná plán opráv.
        Očakáva sa, že sandbox_executor vie pracovať s daným typom plánu.
        """
        try:
            exec_result = self.sandbox_executor.execute_plan(plan)

            self.logger.info(
                "MultiStageRepair: EXECUTE completed",
                extra={"ok": exec_result.ok}
            )

            return StageResult(
                ok=exec_result.ok,
                stage="EXECUTE",
                details=getattr(exec_result, "details", {}),
            )
        except Exception as e:
            self.logger.exception(
                "MultiStageRepair: EXECUTE failed",
                extra={"error": str(e)}
            )
            return StageResult(
                ok=False,
                stage="EXECUTE",
                details={"error": str(e)},
            )

    def _stage_verify(self) -> StageResult:
        """
        VERIFY – overí výsledný stav po oprave.
        Typicky spustí Integrity / health check.
        """
        try:
            verify_result = self.validator.validate()

            self.logger.info(
                "MultiStageRepair: VERIFY completed",
                extra={"ok": verify_result.ok}
            )

            return StageResult(
                ok=verify_result.ok,
                stage="VERIFY",
                details=getattr(verify_result, "details", {}),
            )
        except Exception as e:
            self.logger.exception(
                "MultiStageRepair: VERIFY failed",
                extra={"error": str(e)}
            )
            return StageResult(
                ok=False,
                stage="VERIFY",
                details={"error": str(e)},
            )
