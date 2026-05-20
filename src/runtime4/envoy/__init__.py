"""
SIRIUS LOCAL AI – ENVOY 4.4 Package
-----------------------------------

Provides:
- EnvoyReceiver4      (entry point for external payloads)
- EnvoyQuarantine4    (isolation of untrusted data)
- EnvoyValidator4     (structural + semantic validation)
- EnvoyConverter4     (conversion to Knowledge Pack 2.0 format)

This package handles external data ingestion, validation,
quarantine isolation and safe conversion for Runtime 4.4.

Security Notes (Runtime 4.4):
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

from .envoy_receiver import EnvoyReceiver4
from .envoy_quarantine import EnvoyQuarantine4
from .envoy_validator import EnvoyValidator4
from .envoy_converter import EnvoyConverter4

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

ENVOY_VERSION = "4.4"
ENVOY_SECURITY_FAMILY = "4.4"
ENVOY_SELF_REPAIR_READY = True
ENVOY_OFFLINE_DETERMINISTIC = True
SAFE_MODE_SUPPORTED = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "EnvoyReceiver4",
    "EnvoyQuarantine4",
    "EnvoyValidator4",
    "EnvoyConverter4",
    "ENVOY_VERSION",
    "ENVOY_SECURITY_FAMILY",
    "ENVOY_SELF_REPAIR_READY",
    "ENVOY_OFFLINE_DETERMINISTIC",
    "SAFE_MODE_SUPPORTED",
]
