"""
SIRIUS LOCAL AI – Security Family 4.4.0 (PRO)
---------------------------------------------
Offline safety, identity protection, and family‑aware behavior system
used by SIRIUS LOCAL AI.

Security Family 4.4.0 provides:
- behavior‑based identity classification (OWNER / FAMILY / CHILD / STRANGER)
- time‑limit enforcement for children
- restricted mode for unknown users (STRANGER)
- schoolwork priority mode (triage‑driven)
- safe‑mode for sensitive operations requiring OWNER approval
- offline‑only operation (no biometrics, no cloud)
- integration with PasswordVault 4.4.0
- integration with Health Assistant 4.4.0
- integration with NL Router v4
- deterministic, sandbox‑safe behavior

Security Notes (4.4.0):
- Only static imports allowed.
- No dynamic loading, no eval, no reflection.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

SECURITY_FAMILY_VERSION: str = "4.4.0"
PASSWORD_VAULT_VERSION: str = "4.4.0"
HEALTH_ASSISTANT_VERSION: str = "4.4.0"
SAFE_MODE_SUPPORTED: bool = True
OFFLINE_ONLY: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST (STATIC ONLY, 4.4 NAMES)
# ---------------------------------------------------------

__all__ = [
    # Identity & behavior modules (4.4)
    "identity_4_4",
    "rules_4_4",
    "time_limits_4_4",
    "schoolwork_mode_4_4",
    "safe_mode_4_4",

    # Health Assistant subsystem (4.4)
    "health_assistant_4_4",
    "health_rules_4_4",
    "health_responses_4_4",
    "health_context_4_4",
    "health_router_4_4",

    # Password Vault subsystem (4.4)
    "password_vault_4_4",
    "vault_core_4_4",
    "vault_api_4_4",
    "vault_storage_4_4",
    "vault_crypto_4_4",
    "vault_events_4_4",

    # Metadata
    "SECURITY_FAMILY_VERSION",
    "PASSWORD_VAULT_VERSION",
    "HEALTH_ASSISTANT_VERSION",
    "SAFE_MODE_SUPPORTED",
    "OFFLINE_ONLY",
]
