"""
SIRIUS LOCAL AI – Security Family 4.4.0 (PRO)

This package contains the full Security Family subsystem for Runtime 4.4.
It provides:

- Identity Engine 4.4 (OWNER / FAMILY / STRANGER)
- Behavior Monitor 4.4
- StrangerMode 4.4 (restricted identity)
- FamilyMode 4.4 (child‑safe identity)
- TimeLimits 4.4 (per‑identity quotas)
- Security Policy Core 4.4
- Audit & Logging 4.4
- Self‑Repair Layer (Security) 4.4

All modules inside this package are deterministic, offline, and fully isolated.

Security Notes (Security Family 4.4.0):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
- Fully compatible with Runtime 4.4 and UI Automation 4.4.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA (DETERMINISTIC, READ‑ONLY)
# -------------------------------------------------------------------------

SECURITY_FAMILY_VERSION_4_4: str = "4.4.0"
SECURITY_FAMILY_RUNTIME: str = "4.4"
SECURITY_FAMILY_OFFLINE: bool = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST (NAMESPACES ONLY)
# -------------------------------------------------------------------------

__all__ = [
    "identity_engine_4_4",
    "security_behavior_monitor_4_4",
    "stranger_mode_4_4",
    "family_mode_4_4",
    "time_limits_4_4",
    "security_policy_core_4_4",
    "security_audit_4_4",
    "security_self_repair_4_4",
    "SECURITY_FAMILY_VERSION_4_4",
    "SECURITY_FAMILY_RUNTIME",
    "SECURITY_FAMILY_OFFLINE",
]
