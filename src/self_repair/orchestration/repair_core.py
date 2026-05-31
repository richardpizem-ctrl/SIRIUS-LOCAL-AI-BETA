"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair Core 1.0

Účel:
- hlavný orchestrátor Self‑Repair vrstvy
- riadi stavový automat, plánovanie, sandbox a multi‑stage opravy
- poskytuje jednotné API: run_repair_cycle()
"""

from dataclasses import dataclass
from typing import Dict, Any, List

from .repair_state_machine import RepairStateMachine
from .repair_planner import RepairPlanner
from .multi_stage_repair import MultiStageRepair
from .repair_context_memory import RepairContextMemory


@dataclass
class RepairCycleResult:
    ok: bool
    stages: List[Dict[str, Any]]
    details: Dict[str, Any]


class RepairCore:
    """
    Hlavný orchestrátor Self‑Repair Layer 1.0.

    Spája:
    - RepairStateMachine
    - RepairPlanner
    - MultiStageRepair
    - RepairContextMemory
    - RepairContext (context_provider)
    - RepairSandbox (sandbox_executor)
    - Validator (integrity / health)
    """

    def __init__(
        self,
        context_provider,
        sandbox_executor,
        validator,
        logger,
    ):
        """
        context_provider – poskytuje repair context (dict) pre plánovanie
        sandbox_executor – vykonáva plán opráv (multi-domain)
        validator        – overuje výsledný stav (integrity / health)
        logger           – Logging5 / RepairLogger
        """
        self.logger = logger

        # základné komponenty
        self.state_machine = RepairStateMachine(logger)
        self.planner = RepairPlanner(logger)
        self.memory = RepairContextMemory(logger)

        # multi‑stage orchestrátor
        self.multi_stage = MultiStageRepair(
            context_provider=context_provider,
            planner=self.planner,
            sandbox_executor=sandbox_executor,
            validator=validator,
            logger=logger,
        )

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def run_repair_cycle(self) -> RepairCycleResult:
        """
        Spustí kompletný cyklus opravy:
        IDLE → ANALYZING → PLANNING → EXECUTING → VERIFY → COMPLETED/FAILED
        """
        self.logger.info("RepairCore: starting repair cycle")

        self.state_machine.reset()
        self.memory.clear()

        stages_info: List[Dict[str, Any]] = []

        # IDLE → ANALYZING
        t1 = self.state_machine.transition("ANALYZING", reason="start_repair_cycle")
        self.memory.update_state(self.state_machine.state)
        stages_info.append(self._transition_to_dict(t1))
        if not t1.ok:
            return self._fail_cycle("transition_to_analyzing_failed", stages_info)

        # Multi‑stage orchestrácia (ANALYZE, PLAN, EXECUTE, VERIFY)
        stage_results = self.multi_stage.run_multi_stage()
        for sr in stage_results:
            stages_info.append(
                {
                    "stage": sr.stage,
                    "ok": sr.ok,
                    "details": sr.details,
                }
            )

        # rozhodnutie podľa posledného stage
        final_ok = all(sr.ok for sr in stage_results) if stage_results else True
        final_state = "COMPLETED" if final_ok else "FAILED"

        # ANALYZING/PLANNING/EXECUTING → COMPLETED/FAILED
        t2 = self.state_machine.transition(final_state, reason="multi_stage_finished")
        self.memory.update_state(self.state_machine.state)
        stages_info.append(self._transition_to_dict(t2))

        # uloženie výsledku do pamäte
        self.memory.store_result(
            {
                "ok": final_ok,
                "final_state": final_state,
                "stages": stages_info,
            }
        )

        self.logger.info(
            "RepairCore: repair cycle finished",
            extra={"ok": final_ok, "final_state": final_state},
        )

        return RepairCycleResult(
            ok=final_ok,
            stages=stages_info,
            details={"final_state": final_state},
        )

    # ---------------------------------------------------------
    # INTERNAL HELPERS
    # ---------------------------------------------------------

    def _fail_cycle(self, reason: str, stages_info: List[Dict[str, Any]]) -> RepairCycleResult:
        self.logger.error("RepairCore: repair cycle failed early", extra={"reason": reason})

        self.memory.store_error({"reason": reason})
        self.state_machine.reset()
        self.memory.update_state(self.state_machine.state)

        return RepairCycleResult(
            ok=False,
            stages=stages_info,
            details={"reason": reason},
        )

    @staticmethod
    def _transition_to_dict(transition_result) -> Dict[str, Any]:
        return {
            "type": "state_transition",
            "ok": transition_result.ok,
            "from": transition_result.from_state,
            "to": transition_result.to_state,
            "reason": transition_result.reason,
            "details": transition_result.details,
        }
