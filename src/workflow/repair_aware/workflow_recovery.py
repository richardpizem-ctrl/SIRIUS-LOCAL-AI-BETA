"""
SIRIUS Runtime 5.1.0 – Workflow Engine 5.1
Workflow Recovery 1.0

Účel:
- automatické obnovenie workflow po chybe
- integrácia so Self‑Repair Layer 1.0
- bezpečné pokračovanie v degradovanom režime
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class RecoveryResult:
    ok: bool
    resumed_step: Optional[str]
    degraded_mode: bool
    details: Dict[str, Any]


class WorkflowRecovery:
    """
    Obnovovací modul pre Workflow Engine 5.1.

    Spolupracuje s:
    - Self‑Repair Layer (RepairCore)
    - SafeRetry
    - DegradedContinue
    """

    def __init__(self, workflow_store, logger):
        """
        workflow_store – abstrakcia nad úložiskom workflow krokov
        logger         – Logging5 / RepairLogger
        """
        self.workflow_store = workflow_store
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def recover(self, workflow_id: str, context: Dict[str, Any]) -> RecoveryResult:
        """
        Pokúsi sa obnoviť workflow po chybe.

        Kroky:
        1) načíta posledný zdravý krok
        2) pokúsi sa obnoviť workflow od tohto kroku
        3) ak sa nedá obnoviť → prejde do degradovaného režimu
        """
        self.logger.info(
            "WorkflowRecovery: starting recovery",
            extra={"workflow_id": workflow_id}
        )

        last_ok_step = self.workflow_store.get_last_ok_step(workflow_id)

        if not last_ok_step:
            self.logger.warning(
                "WorkflowRecovery: no valid checkpoint, entering degraded mode",
                extra={"workflow_id": workflow_id}
            )
            return RecoveryResult(
                ok=False,
                resumed_step=None,
                degraded_mode=True,
                details={"reason": "no_checkpoint"}
            )

        # pokus o obnovu
        try:
            self.logger.info(
                "WorkflowRecovery: resuming workflow",
                extra={"workflow_id": workflow_id, "step": last_ok_step}
            )

            resumed = self.workflow_store.resume_from_step(workflow_id, last_ok_step)

            if not resumed:
                self.logger.warning(
                    "WorkflowRecovery: resume failed, degraded mode",
                    extra={"workflow_id": workflow_id}
                )
                return RecoveryResult(
                    ok=False,
                    resumed_step=last_ok_step,
                    degraded_mode=True,
                    details={"reason": "resume_failed"}
                )

            return RecoveryResult(
                ok=True,
                resumed_step=last_ok_step,
                degraded_mode=False,
                details={"mode": "workflow_resumed"}
            )

        except Exception as e:
            self.logger.exception(
                "WorkflowRecovery: exception during recovery",
                extra={"workflow_id": workflow_id, "error": str(e)}
            )
            return RecoveryResult(
                ok=False,
                resumed_step=last_ok_step,
                degraded_mode=True,
                details={"reason": "exception", "error": str(e)}
            )
