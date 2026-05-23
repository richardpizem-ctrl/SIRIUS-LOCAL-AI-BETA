"""
SIRIUS LOCAL AI – Security Family 4.5.0 (PRO)

This package contains the full Security Family subsystem for Runtime 4.5.
It provides:

- Identity Engine 4.5 (OWNER / FAMILY / STRANGER)
- Behavior Monitor 4.5
- StrangerMode 4.5 (restricted identity)
- FamilyMode 4.5 (child‑safe identity)
- TimeLimits 4.5 (per‑identity quotas)
- Security Policy Core 4.5
- Audit & Logging 4.5
- Self‑Repair Layer (Security) 4.5

All modules inside this package are deterministic, offline, and fully isolated.

Security Notes (Security Family 4.5.0):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- __all__ must contain only verified public namespaces.
- This file must not contain executable logic.
- Fully compatible with Runtime 4.5 and UI Automation 4.5.
"""

# -------------------------------------------------------------------------
# PACKAGE METADATA (DETERMINISTIC, READ‑ONLY)
# -------------------------------------------------------------------------

SECURITY_FAMILY_VERSION_4_5: str = "4.5.0"
SECURITY_FAMILY_RUNTIME: str = "4.5"
SECURITY_FAMILY_OFFLINE: bool = True

# -------------------------------------------------------------------------
# SAFE EXPORT LIST (NAMESPACES ONLY)
# -------------------------------------------------------------------------

__all__ = [
    "identity_engine_4_5",
    "security_behavior_monitor_4_5",
    "stranger_mode_4_5",
    "family_mode_4_5",
    "time_limits_4_5",
    "security_policy_core_4_5",
    "security_audit_4_5",
    "security_self_repair_4_5",
    "SECURITY_FAMILY_VERSION_4_5",
    "SECURITY_FAMILY_RUNTIME",
    "SECURITY_FAMILY_OFFLINE",
]
