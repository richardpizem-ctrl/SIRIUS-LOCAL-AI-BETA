"""
SIRIUS LOCAL AI – Security Family 4.3.x
---------------------------------------
Offline safety, identity protection, and family‑aware behavior system
used by SIRIUS LOCAL AI.

Security Family provides:
- behavior‑based identity classification (OWNER / FAMILY / CHILD / STRANGER)
- time‑limit enforcement for children
- restricted mode for unknown users
- schoolwork priority mode (triage‑driven)
- safe‑mode for sensitive operations requiring OWNER approval
- offline‑only operation (no biometrics, no cloud)
- integration with PasswordVault 4.3.x
- integration with Health Assistant 4.3.x
- integration with NL Router v4
- deterministic, sandbox‑safe behavior

Security Notes (4.3.x):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

SECURITY_FAMILY_VERSION = "4.3.x"
PASSWORD_VAULT_VERSION = "4.3.x"
HEALTH_ASSISTANT_VERSION = "4.3.x"
SAFE_MODE_SUPPORTED = True

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY)
# ---------------------------------------------------------

__all__ = [
    # Identity & behavior modules
    "identity",
    "rules",
    "time_limits",
    "schoolwork_mode",
    "safe_mode",

    # Health Assistant subsystem
    "health_assistant",
    "health_rules",
    "health_responses",
    "health_context",
    "health_router",

    # Password Vault subsystem
    "password_vault",
    "vault_core",
    "vault_api",
    "vault_storage",
    "vault_crypto",
    "vault_events",

    # Metadata
    "SECURITY_FAMILY_VERSION",
    "PASSWORD_VAULT_VERSION",
    "HEALTH_ASSISTANT_VERSION",
    "SAFE_MODE_SUPPORTED",
]
