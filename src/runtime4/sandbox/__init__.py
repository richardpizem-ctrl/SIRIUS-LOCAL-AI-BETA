"""
SIRIUS LOCAL AI – SANDBOX 4.3 Package (PRO)

Provides:
- SandboxContext4
- SandboxProcess4

Účel:
- izolované sandbox prostredie pre Runtime 4.3
- bezpečné, deterministické vykonávanie pod kontrolou
- žiadne dynamické načítavanie, žiadne eval, žiadna reflexia

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

from .sandbox_context import SandboxContext4
from .sandbox_process import SandboxProcess4

# ---------------------------------------------------------
# PACKAGE METADATA (DETERMINISTIC, READ-ONLY)
# ---------------------------------------------------------

SANDBOX_VERSION: str = "4.3"
SECURITY_FAMILY_COMPAT: str = "4.4"
SAFE_MODE_SUPPORTED: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "SandboxContext4",
    "SandboxProcess4",
    "SANDBOX_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
