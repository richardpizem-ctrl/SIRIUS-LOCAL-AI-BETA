"""
SIRIUS LOCAL AI – PasswordVault Events 4.3.x
--------------------------------------------
Static event definitions for Password Vault.

These events are used by:
- Security Family Router
- NL Router v4
- Runtime Manager
- UI Automation Engine (autofill)
- Diagnostics & Self‑Repair

Security Notes:
- No dynamic imports, no eval, no reflection.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# PASSWORD VAULT EVENT CONSTANTS (STATIC, SAFE)
# ---------------------------------------------------------

PASSWORD_SAVE_EVENT = "SECURITY_EVENT_PASSWORD_SAVE"
PASSWORD_RETRIEVE_EVENT = "SECURITY_EVENT_PASSWORD_RETRIEVE"
PASSWORD_AUTOFILL_EVENT = "SECURITY_EVENT_PASSWORD_AUTOFILL"
PASSWORD_DELETE_EVENT = "SECURITY_EVENT_PASSWORD_DELETE"
PASSWORD_LIST_EVENT = "SECURITY_EVENT_PASSWORD_LIST"
PASSWORD_PHISHING_DETECTED_EVENT = "SECURITY_EVENT_PASSWORD_PHISHING_DETECTED"

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

PASSWORD_VAULT_EVENTS_VERSION = "4.3.x"
SECURITY_FAMILY_COMPAT = "4.4"

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "PASSWORD_SAVE_EVENT",
    "PASSWORD_RETRIEVE_EVENT",
    "PASSWORD_AUTOFILL_EVENT",
    "PASSWORD_DELETE_EVENT",
    "PASSWORD_LIST_EVENT",
    "PASSWORD_PHISHING_DETECTED_EVENT",
    "PASSWORD_VAULT_EVENTS_VERSION",
    "SECURITY_FAMILY_COMPAT",
]
