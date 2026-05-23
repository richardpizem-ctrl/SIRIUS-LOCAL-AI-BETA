"""
SIRIUS LOCAL AI – SANDBOX 4.5 Package (PRO)

Provides:
- SandboxContext45
- SandboxProcess45

Účel:
- izolované sandbox prostredie pre Runtime 4.5
- bezpečné, deterministické vykonávanie pod kontrolou
- žiadne dynamické načítavanie, žiadne eval, žiadna reflexia

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

from .sandbox_context_4_5 import SandboxContext45
from .sandbox_process_4_5 import SandboxProcess45

# ---------------------------------------------------------
# PACKAGE METADATA (DETERMINISTIC, READ-ONLY)
# ---------------------------------------------------------

SANDBOX_VERSION: str = "4.5"
SECURITY_FAMILY_COMPAT: str = "4.5"
SAFE_MODE_SUPPORTED: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "SandboxContext45",
    "SandboxProcess45",
    "SANDBOX_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
