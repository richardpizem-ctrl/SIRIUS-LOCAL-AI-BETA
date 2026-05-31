"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair State Machine 1.0

Účel:
- formálny stavový automat pre opravný proces
- jasné prechody medzi stavmi
- logika, kedy sa končí ako REPAIRED / DEGRADATED_STABLE / UNRECOVERABLE
"""

from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict, Any, Optional


class RepairState(Enum):
    INIT = auto()
    DETECTING = auto()
    ISOLATING = auto()
    REPAIRING = auto()
    VERIFYING = auto()
    TRANSITIONING = auto()
    COMPLETED = auto()
    FAILED = auto()


class RepairExit(Enum):
    REPAIRED = auto()
    DEGRADATED_STABLE = auto()
    UNRECOVERABLE = auto()


@dataclass
class RepairContext:
    module: str
    error_code: str
    severity: str
    metadata: Dict[str, Any]


class RepairStateMachine:
    """
    Stavový automat pre Self‑Repair proces.

    Nerieši konkrétne opravy – iba:
    - drží stav
    - rozhoduje, čo je ďalší krok
    - určuje finálny exit (REPAIRED / DEGRADATED_STABLE / UNRECOVERABLE)
    """

    def __init__(self, logger):
        self.logger = logger
        self.state: RepairState = RepairState.INIT
        self.exit: Optional[RepairExit] = None

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def start(self, ctx: RepairContext) -> None:
        self.logger.info(
            "RepairStateMachine: start",
            extra={"module": ctx.module, "error_code": ctx.error_code}
        )
        self.state = RepairState.DETECTING

    def on_detection_result(self, success: bool) -> None:
        if not success:
            self.logger.warning("RepairStateMachine: detection failed")
            self.state = RepairState.FAILED
            self.exit = RepairExit.UNRECOVERABLE
            return

        self.state = RepairState.ISOLATING

    def on_isolation_result(self, success: bool) -> None:
        if not success:
            self.logger.error("RepairStateMachine: isolation failed")
            self.state = RepairState.FAILED
            self.exit = RepairExit.UNRECOVERABLE
            return

        self.state = RepairState.REPAIRING

    def on_repair_result(self, success: bool) -> None:
        if not success:
            self.logger.error("RepairStateMachine: repair failed, staying degraded")
            self.state = RepairState.FAILED
            self.exit = RepairExit.DEGRADATED_STABLE
            return

        self.state = RepairState.VERIFYING

    def on_verify_result(self, success: bool) -> None:
        if not success:
            self.logger.error("RepairStateMachine: verification failed, degraded but stable")
            self.state = RepairState.FAILED
            self.exit = RepairExit.DEGRADATED_STABLE
            return

        self.state = RepairState.TRANSITIONING

    def on_transition_result(self, success: bool) -> None:
        if not success:
            self.logger.warning("RepairStateMachine: transition failed, degraded but stable")
            self.state = RepairState.COMPLETED
            self.exit = RepairExit.DEGRADATED_STABLE
            return

        self.state = RepairState.COMPLETED
        self.exit = RepairExit.REPAIRED

    # ---------------------------------------------------------
    # HELPERS
    # ---------------------------------------------------------

    def is_finished(self) -> bool:
        return self.state in {RepairState.COMPLETED, RepairState.FAILED}

    def get_exit(self) -> Optional[RepairExit]:
        return self.exit
