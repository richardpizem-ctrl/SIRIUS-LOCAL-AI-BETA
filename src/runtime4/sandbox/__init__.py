"""
SIRIUS LOCAL AI – SANDBOX 4.3 Package

Provides:
- SandboxContext4
- SandboxProcess4

This package implements the isolated execution environment
used by Runtime 4.3 for safe evaluation, controlled execution,
and deterministic behavior under restricted conditions.

Security Notes (Runtime 4.3):
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
# PACKAGE METADATA
# ---------------------------------------------------------

SANDBOX_VERSION = "4.3"
SECURITY_FAMILY_COMPAT = "4.4"
SAFE_MODE_SUPPORTED = True

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
