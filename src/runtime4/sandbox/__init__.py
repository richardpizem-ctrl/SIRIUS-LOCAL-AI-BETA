"""
SIRIUS LOCAL AI – SANDBOX 4.0 Package

Provides:
- SandboxContext4
- SandboxProcess4

This package implements the isolated execution environment
used by Runtime 4.0 for safe evaluation, controlled execution,
and deterministic behavior under restricted conditions.

Security Notes (Runtime 4.0):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
- This file must not contain executable logic.
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS
# ---------------------------------------------------------

from .sandbox_context import SandboxContext4
from .sandbox_process import SandboxProcess4

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "SandboxContext4",
    "SandboxProcess4",
]
