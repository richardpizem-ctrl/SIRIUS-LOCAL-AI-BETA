"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Core repair orchestration entrypoint.

Responsibility:
- prijme error_state z HealthMonitor5 / Runtime / Workflow
- rozhodne: DETECT → ISOLATE → REPAIR → VERIFY → TRANSITION
- vráti jasný RepairResult späť do systému
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Dict, Any


class RepairStage(Enum):
    DETECT = auto()
    ISOLATE = auto()
    REPAIR = auto()
    VERIFY = auto()
    TRANSITION = auto()
    FAILED = auto()
    SKIPPED = auto()


class RepairOutcome(Enum):
    REPAIRED = auto()
    DEGRADATED_STABLE = auto()
    UNRECOVERABLE = auto()


@dataclass
class ErrorState:
    module: str
    error_code: str
    severity: str
    context: Dict[str, Any]


@dataclass
class RepairResult:
    outcome: RepairOutcome
    stage: RepairStage
    details: Dict[str, Any]
    degraded_mode: bool = False


class RepairCore:
    """
    Hlavný koordinátor opráv.
    Nerieši konkrétnu implementáciu (checksum, KG, workflow),
    iba orchestruje volania na nižšie vrstvy.
    """

    def __init__(self,
                 detector,
                 isolator,
                 repair_engine,
                 verifier,
                 transition_manager,
                 logger):
        """
        Vstupy sú abstraktné komponenty (dependency injection):

        detector          – modul, ktorý vie rozpoznať typ poškodenia
        isolator          – modul, ktorý vie modul odizolovať / vypnúť
        repair_engine     – modul, ktorý vie vykonať opravu
        verifier          – modul, ktorý vie overiť integritu po oprave
        transition_manager– modul, ktorý vie prepnúť stav (degraded → repaired)
        logger            – Logging5 / RepairLogs wrapper
        """
        self.detector = detector
        self.isolator = isolator
        self.repair_engine = repair_engine
        self.verifier = verifier
        self.transition_manager = transition_manager
        self.logger = logger

    def process(self, error_state: ErrorState) -> RepairResult:
        """
        Hlavný vstupný bod:
        SelfRepair.process(error_state)

        Toto bude volané z:
        - HealthMonitor5
        - Workflow Engine
        - Runtime Integrity Engine
        - System Agent
        """
        self.logger.info("SelfRepair: starting process", extra={"error_state": error_state.__dict__})

        # 1) DETECT
        detected = self._detect(error_state)
        if not detected:
            self.logger.warning("SelfRepair: detection failed or not applicable")
            return RepairResult(
                outcome=RepairOutcome.UNRECOVERABLE,
                stage=RepairStage.DETECT,
                details={"reason": "no_repair_strategy"},
                degraded_mode=True,
            )

        # 2) ISOLATE
        if not self._isolate(error_state):
            self.logger.error("SelfRepair: isolation failed")
            return RepairResult(
                outcome=RepairOutcome.UNRECOVERABLE,
                stage=RepairStage.ISOLATE,
                details={"reason": "isolation_failed"},
                degraded_mode=True,
            )

        # 3) REPAIR
        repair_ok = self._repair(error_state)
        if not repair_ok:
            self.logger.error("SelfRepair: repair failed")
            return RepairResult(
                outcome=RepairOutcome.DEGRADATED_STABLE,
                stage=RepairStage.REPAIR,
                details={"reason": "repair_failed"},
                degraded_mode=True,
            )

        # 4) VERIFY
        verify_ok = self._verify(error_state)
        if not verify_ok:
            self.logger.error("SelfRepair: verification failed, rolling back")
            self._rollback(error_state)
            return RepairResult(
                outcome=RepairOutcome.DEGRADATED_STABLE,
                stage=RepairStage.VERIFY,
                details={"reason": "verification_failed_rollback_done"},
                degraded_mode=True,
            )

        # 5) TRANSITION
        transitioned = self._transition(error_state)
        if not transitioned:
            self.logger.warning("SelfRepair: transition to repaired state failed, staying degraded")
            return RepairResult(
                outcome=RepairOutcome.DEGRADATED_STABLE,
                stage=RepairStage.TRANSITION,
                details={"reason": "transition_failed"},
                degraded_mode=True,
            )

        self.logger.info("SelfRepair: successfully repaired")
        return RepairResult(
            outcome=RepairOutcome.REPAIRED,
            stage=RepairStage.TRANSITION,
            details={"info": "module_repaired_and_reintegrated"},
            degraded_mode=False,
        )

    # --- Interné kroky ---

    def _detect(self, error_state: ErrorState) -> bool:
        return self.detector.detect(error_state)

    def _isolate(self, error_state: ErrorState) -> bool:
        return self.isolator.isolate(error_state.module)

    def _repair(self, error_state: ErrorState) -> bool:
        return self.repair_engine.repair(error_state)

    def _verify(self, error_state: ErrorState) -> bool:
        return self.verifier.verify(error_state.module)

    def _rollback(self, error_state: ErrorState) -> None:
        try:
            self.repair_engine.rollback(error_state.module)
        except Exception as e:
            self.logger.exception("SelfRepair: rollback failed", extra={"error": str(e)})

    def _transition(self, error_state: ErrorState) -> bool:
        return self.transition_manager.to_repaired(error_state.module)


# 🔗 Toto je hook, ktorý budeš volať z ostatných častí systému:
# from self_repair.repair_core import RepairCore, ErrorState
#
# result = self_repair_core.process(
#     ErrorState(
#         module="workflow_engine",
#         error_code="MISSING_DEPENDENCY",
#         severity="HIGH",
#         context={"workflow_id": "abc123"}
#     )
# )
#
# Podľa result.outcome vie Runtime/Workflow/SystemAgent, čo ďalej.
