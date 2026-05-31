"""
SIRIUS Runtime 5.1.0 – Workflow Engine 5.1
Safe Retry 1.0

Účel:
- bezpečné opakovanie workflow krokov po chybe
- ochrana pred nekonečnými retry cyklami
- integrácia so Self‑Repair Layer 1.0
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass
class RetryResult:
    ok: bool
    attempted_step: Optional[str]
    attempts: int
    degraded_mode: bool
    details: Dict[str, Any]


class SafeRetry:
    """
    Bezpečný retry mechanizmus pre Workflow Engine 5.1.

    Funkcie:
    - limitované retry pokusy
    - ochrana pred cyklami
    - spätná väzba pre Self‑Repair Layer
    """

    def __init__(self, workflow_store, max_attempts: int, logger):
        """
        workflow_store – abstrakcia nad workflow krokmi
        max_attempts   – maximálny počet retry pokusov
        logger         – Logging5 / RepairLogger
        """
        self.workflow_store = workflow_store
        self.max_attempts = max_attempts
        self.logger = logger

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def retry(self, workflow_id: str, step: str, context: Dict[str, Any]) -> RetryResult:
        """
        Pokúsi sa zopakovať konkrétny krok workflow.

        Kroky:
        1) načíta počet doterajších pokusov
        2) ak prekročený limit → degradovaný režim
        3) pokus o retry
        """
        attempts = self.workflow_store.get_retry_count(workflow_id, step)

        self.logger.info(
            "SafeRetry: retry requested",
            extra={"workflow_id": workflow_id, "step": step, "attempts": attempts}
        )

        # 1) kontrola limitu
        if attempts >= self.max_attempts:
            self.logger.warning(
                "SafeRetry: retry limit reached, degraded mode",
                extra={"workflow_id": workflow_id, "step": step}
            )
            return RetryResult(
                ok=False,
                attempted_step=step,
                attempts=attempts,
                degraded_mode=True,
                details={"reason": "retry_limit_reached"}
            )

        # 2) pokus o retry
        try:
            self.logger.info(
                "SafeRetry: attempting retry",
                extra={"workflow_id": workflow_id, "step": step}
            )

            success = self.workflow_store.execute_step(workflow_id, step)

            # zvýšime počítadlo pokusov
            self.workflow_store.increment_retry_count(workflow_id, step)

            if not success:
                self.logger.warning(
                    "SafeRetry: retry failed",
                    extra={"workflow_id": workflow_id, "step": step}
                )
                return RetryResult(
                    ok=False,
                    attempted_step=step,
                    attempts=attempts + 1,
                    degraded_mode=False,
                    details={"reason": "retry_failed"}
                )

            # úspech
            return RetryResult(
                ok=True,
                attempted_step=step,
                attempts=attempts + 1,
                degraded_mode=False,
                details={"mode": "retry_success"}
            )

        except Exception as e:
            self.logger.exception(
                "SafeRetry: exception during retry",
                extra={"workflow_id": workflow_id, "step": step, "error": str(e)}
            )
            return RetryResult(
                ok=False,
                attempted_step=step,
                attempts=attempts,
                degraded_mode=True,
                details={"reason": "exception", "error": str(e)}
            )
