"""
SIRIUS LOCAL AI – SCHEDULER 4.3 Package (PRO)

Provides:
- SchedulerCore4
- SchedulerRouter4
- SchedulerQueue4
- SchedulerManager4

This package implements the task scheduling layer of Runtime 4.3,
including routing, queueing, prioritization and execution control.

Security Notes (Runtime 4.3 / Security Family 4.4):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS
# ---------------------------------------------------------

from .scheduler_core import SchedulerCore4
from .scheduler_router import SchedulerRouter4
from .scheduler_queue import SchedulerQueue4
from .scheduler_manager import SchedulerManager4

# ---------------------------------------------------------
# PACKAGE METADATA (DETERMINISTIC, READ-ONLY)
# ---------------------------------------------------------

SCHEDULER_VERSION: str = "4.3"
SECURITY_FAMILY_COMPAT: str = "4.4"
SAFE_MODE_SUPPORTED: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "SchedulerCore4",
    "SchedulerRouter4",
    "SchedulerQueue4",
    "SchedulerManager4",
    "SCHEDULER_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
