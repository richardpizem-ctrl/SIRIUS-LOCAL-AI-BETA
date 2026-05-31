"""
SIRIUS Runtime 5.1.0 – Self‑Repair Layer 1.0
Repair State Machine 1.0

Účel:
- riadiť životný cyklus opravy
- zabezpečiť deterministické prechody medzi stavmi
- zabrániť chaotickému alebo opakovanému spúšťaniu opráv
"""

from dataclasses import dataclass
from typing import Dict, Any, Literal


RepairState = Literal[
    "IDLE",
    "ANALYZING",
    "PLANNING",
    "EXECUTING",
    "COMPLETED",
    "FAILED",
]


@dataclass
class StateTransitionResult:
    ok: bool
    from_state: RepairState
    to_state: RepairState
    reason: str
    details: Dict[str, Any]


class RepairStateMachine:
    """
    Stavový automat pre Self‑Repair Layer.

    Povolené prechody:
        IDLE → ANALYZING
        ANALYZING → PLANNING
        PLANNING → EXECUTING
        EXECUTING → COMPLETED
        EXECUTING → FAILED
        FAILED → IDLE
        COMPLETED → IDLE
    """

    VALID_TRANSITIONS = {
        "IDLE": {"ANALYZING"},
        "ANALYZING": {"PLANNING"},
        "PLANNING": {"EXECUTING"},
        "EXECUTING": {"COMPLETED", "FAILED"},
        "FAILED": {"IDLE"},
        "COMPLETED": {"IDLE"},
    }

    def __init__(self, logger):
        self.state: RepairState = "IDLE"
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def transition(self, new_state: RepairState, reason: str, details: Dict[str, Any] = None) -> StateTransitionResult:
        """
        Pokúsi sa prejsť do nového stavu.
        """
        details = details or {}
        old_state = self.state

        allowed = self.VALID_TRANSITIONS.get(old_state, set())

        if new_state not in allowed:
            self.logger.error(
                "RepairStateMachine: invalid transition",
                extra={"from": old_state, "to": new_state, "reason": reason}
            )
            return StateTransitionResult(
                ok=False,
                from_state=old_state,
                to_state=new_state,
                reason="invalid_transition",
                details={"requested_reason": reason, **details}
            )

        # prechod je povolený
        self.logger.info(
            "RepairStateMachine: state transition",
            extra={"from": old_state, "to": new_state, "reason": reason}
        )

        self.state = new_state

        return StateTransitionResult(
            ok=True,
            from_state=old_state,
            to_state=new_state,
            reason=reason,
            details=details
        )

    # ---------------------------------------------------------
    # HELPERS
    # ---------------------------------------------------------

    def reset(self):
        """
        Resetuje stav späť do IDLE.
        """
        old = self.state
        self.state = "IDLE"

        self.logger.info(
            "RepairStateMachine: reset",
            extra={"from": old, "to": "IDLE"}
        )
