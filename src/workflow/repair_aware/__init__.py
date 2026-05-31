"""
SIRIUS Runtime 5.1.0 – Workflow Engine 5.1
Repair‑Aware Workflow Layer – Package Initializer

Tento modul poskytuje jednotné API pre všetky komponenty, ktoré umožňujú:
- automatické obnovenie workflow po chybe
- bezpečné opakovanie krokov
- pokračovanie v degradovanom režime
- integráciu so Self‑Repair Layer 1.0
"""

from .workflow_recovery import WorkflowRecovery
from .safe_retry import SafeRetry
from .degraded_continue import DegradedContinue

__all__ = [
    "WorkflowRecovery",
    "SafeRetry",
    "DegradedContinue",
]
