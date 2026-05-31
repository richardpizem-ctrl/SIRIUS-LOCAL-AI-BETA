"""
SIRIUS Runtime 5.1.0 – Workflow Engine 5.1
Degraded Continue 1.0

Účel:
- umožniť workflow pokračovať v degradovanom režime
- preskočiť nefunkčné alebo poškodené kroky
- minimalizovať dopad chyby na celý proces
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class DegradedResult:
    ok: bool
    skipped_step: Optional[str]
    next_step: Optional[str]
    details: Dict[str, Any]


class DegradedContinue:
    """
    Mechanizmus pre pokračovanie workflow v degradovanom režime.

    Používa sa keď:
    - oprava zlyhala
    - retry limit bol prekročený
    - workflow krok je nefunkčný
    """

    def __init__(self, workflow_store, logger):
        """
        workflow_store – abstrakcia nad workflow krokmi
        logger         – Logging5 / RepairLogger
        """
        self.workflow_store = workflow_store
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def continue_after_failure(self, workflow_id: str, failed_step: str, context: Dict[str, Any]) -> DegradedResult:
        """
        Pokračuje workflow preskočením poškodeného kroku.

        Kroky:
        1) zistí ďalší krok po failed_step
        2) ak neexistuje → workflow končí
        3) preskočí failed_step a pokračuje
        """
        self.logger.warning(
            "DegradedContinue: entering degraded mode",
            extra={"workflow_id": workflow_id, "failed_step": failed_step}
        )

        next_step = self.workflow_store.get_next_step(workflow_id, failed_step)

        if not next_step:
            self.logger.info(
                "DegradedContinue: no next step, workflow ends",
                extra={"workflow_id": workflow_id}
            )
            return DegradedResult(
                ok=True,
                skipped_step=failed_step,
                next_step=None,
                details={"mode": "workflow_completed_in_degraded_mode"}
            )

        # pokus o pokračovanie
        try:
            self.logger.info(
                "DegradedContinue: continuing workflow",
                extra={"workflow_id": workflow_id, "next_step": next_step}
            )

            success = self.workflow_store.execute_step(workflow_id, next_step)

            if not success:
                self.logger.error(
                    "DegradedContinue: next step failed as well",
                    extra={"workflow_id": workflow_id, "next_step": next_step}
                )
                return DegradedResult(
                    ok=False,
                    skipped_step=failed_step,
                    next_step=next_step,
                    details={"reason": "next_step_failed"}
                )

            return DegradedResult(
                ok=True,
                skipped_step=failed_step,
                next_step=next_step,
                details={"mode": "continued_in_degraded_mode"}
            )

        except Exception as e:
            self.logger.exception(
                "DegradedContinue: exception during degraded continuation",
                extra={"workflow_id": workflow_id, "error": str(e)}
            )
            return DegradedResult(
                ok=False,
                skipped_step=failed_step,
                next_step=None,
                details={"reason": "exception", "error": str(e)}
            )
