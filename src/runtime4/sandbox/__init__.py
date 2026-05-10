"""
SIRIUS LOCAL AI – SANDBOX 4.0 Package

Provides:
- SandboxContext4
- SandboxProcess4

This package implements the isolated execution environment
used by Runtime 4.0 for safe evaluation, controlled execution,
and deterministic behavior under restricted conditions.
"""

from .sandbox_context import SandboxContext4
from .sandbox_process import SandboxProcess4

__all__ = [
    "SandboxContext4",
    "SandboxProcess4",
]

