"""
SIRIUS LOCAL AI – Security.PasswordVault 4.4.0 (PRO)
----------------------------------------------------
Offline, encrypted password manager (part of Security Family 4.4)

This package provides:
- PasswordVault core (AES‑256‑GCM encrypted storage)
- High‑level API (save / retrieve / list / delete)
- Identity‑aware access control (OWNER / FAMILY / STRANGER / CHILD)
- Deterministic, offline‑only behavior
- Safe‑mode and degraded‑mode compatibility
- Fully Security Family 4.4 compliant

Security Notes (4.4.0):
- Only static imports allowed.
- No dynamic imports, no eval, no reflection.
- This file must not contain executable logic.
- All exported modules must be verified and deterministic.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS (Security Family 4.4 requirement)
# ---------------------------------------------------------

from .vault_core_4_4 import PasswordVault44
from .vault_api_4_4 import (
    save_password_44,
    retrieve_password_44,
    list_entries_44,
    delete_entry_44,
)

# ---------------------------------------------------------
# PACKAGE METADATA (Runtime 4.4)
# ---------------------------------------------------------

PASSWORD_VAULT_VERSION: str = "4.4.0"
SECURITY_FAMILY_COMPAT: str = "4.4"
SAFE_MODE_SUPPORTED: bool = True
OFFLINE_ONLY: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST (static, verified modules only)
# ---------------------------------------------------------

__all__ = [
    "PasswordVault44",
    "save_password_44",
    "retrieve_password_44",
    "list_entries_44",
    "delete_entry_44",
    "PASSWORD_VAULT_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
    "OFFLINE_ONLY",
]
