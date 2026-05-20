"""
SIRIUS LOCAL AI – PasswordVault Events 4.4.0 (PRO)
--------------------------------------------------
Static event definitions for Password Vault 4.4.

Used by:
- Security Family Router 4.4
- NL Router v4
- Runtime Manager 4.4
- UI Automation Engine 4.4 (autofill)
- Diagnostics & Self‑Repair 4.4

Security Notes:
- No dynamic imports, no eval, no reflection.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PASSWORD VAULT EVENT CONSTANTS (STATIC, SAFE)
# ---------------------------------------------------------

PASSWORD_SAVE_EVENT_44 = "SECURITY_EVENT_PASSWORD_SAVE_44"
PASSWORD_RETRIEVE_EVENT_44 = "SECURITY_EVENT_PASSWORD_RETRIEVE_44"
PASSWORD_AUTOFILL_EVENT_44 = "SECURITY_EVENT_PASSWORD_AUTOFILL_44"
PASSWORD_DELETE_EVENT_44 = "SECURITY_EVENT_PASSWORD_DELETE_44"
PASSWORD_LIST_EVENT_44 = "SECURITY_EVENT_PASSWORD_LIST_44"
PASSWORD_PHISHING_DETECTED_EVENT_44 = "SECURITY_EVENT_PASSWORD_PHISHING_DETECTED_44"

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

PASSWORD_VAULT_EVENTS_VERSION: str = "4.4.0"
SECURITY_FAMILY_COMPAT: str = "4.4"

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "PASSWORD_SAVE_EVENT_44",
    "PASSWORD_RETRIEVE_EVENT_44",
    "PASSWORD_AUTOFILL_EVENT_44",
    "PASSWORD_DELETE_EVENT_44",
    "PASSWORD_LIST_EVENT_44",
    "PASSWORD_PHISHING_DETECTED_EVENT_44",
    "PASSWORD_VAULT_EVENTS_VERSION",
    "SECURITY_FAMILY_COMPAT",
]
