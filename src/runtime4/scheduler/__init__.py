"""
SIRIUS LOCAL AI – SCHEDULER 4.5 Package (PRO)

Provides:
- SchedulerCore45
- SchedulerRouter45
- SchedulerQueue45
- SchedulerManager45

This package implements the task scheduling layer of Runtime 4.5,
including routing, queueing, prioritization and execution control.

Security Notes (Runtime 4.5 / Security Family 4.5):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.5.
- Self‑Repair 4.5 ready.
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS
# ---------------------------------------------------------

from .scheduler_core_4_5 import SchedulerCore45
from .scheduler_router_4_5 import SchedulerRouter45
from .scheduler_queue_4_5 import SchedulerQueue45
from .scheduler_manager_4_5 import SchedulerManager45

# ---------------------------------------------------------
# PACKAGE METADATA (DETERMINISTIC, READ-ONLY)
# ---------------------------------------------------------

SCHEDULER_VERSION: str = "4.5"
SECURITY_FAMILY_COMPAT: str = "4.5"
SAFE_MODE_SUPPORTED: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "SchedulerCore45",
    "SchedulerRouter45",
    "SchedulerQueue45",
    "SchedulerManager45",
    "SCHEDULER_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
