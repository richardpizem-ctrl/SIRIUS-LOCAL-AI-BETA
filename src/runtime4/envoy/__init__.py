"""
SIRIUS LOCAL AI – ENVOY 4.0 Package

Provides:
- EnvoyReceiver4
- EnvoyQuarantine4
- EnvoyValidator4
- EnvoyConverter4

This package handles external data ingestion, validation,
quarantine isolation and safe conversion for Runtime 4.0.

Security Notes (Runtime 4.0):
- Only static imports are allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public symbols.
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS
# ---------------------------------------------------------

from .envoy_receiver import EnvoyReceiver4
from .envoy_quarantine import EnvoyQuarantine4
from .envoy_validator import EnvoyValidator4
from .envoy_converter import EnvoyConverter4

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "EnvoyReceiver4",
    "EnvoyQuarantine4",
    "EnvoyValidator4",
    "EnvoyConverter4",
]
