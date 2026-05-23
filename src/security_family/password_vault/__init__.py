"""
SIRIUS LOCAL AI – Security.PasswordVault 4.5.0 (PRO)
----------------------------------------------------
Offline, encrypted password manager (part of Security Family 4.5)

This package provides:
- PasswordVault core (AES‑256‑GCM encrypted storage)
- High‑level API (save / retrieve / list / delete)
- Identity‑aware access control (OWNER / FAMILY / STRANGER / CHILD)
- Deterministic, offline‑only behavior
- Safe‑mode and degraded‑mode compatibility
- Fully Security Family 4.5 compliant

Security Notes (4.5.0):
- Only static imports allowed.
- No dynamic imports, no eval, no reflection.
- This file must not contain executable logic.
- All exported modules must be verified and deterministic.
- Self‑Repair Layer 4.5 ready.
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS (Security Family 4.5 requirement)
# ---------------------------------------------------------

from .vault_core_4_5 import PasswordVault45
from .vault_api_4_5 import (
    save_password_45,
    retrieve_password_45,
    list_entries_45,
    delete_entry_45,
)

# ---------------------------------------------------------
# PACKAGE METADATA (Runtime 4.5)
# ---------------------------------------------------------

PASSWORD_VAULT_VERSION: str = "4.5.0"
SECURITY_FAMILY_COMPAT: str = "4.5"
SAFE_MODE_SUPPORTED: bool = True
OFFLINE_ONLY: bool = True

# ---------------------------------------------------------
# SAFE EXPORT LIST (static, verified modules only)
# ---------------------------------------------------------

__all__ = [
    "PasswordVault45",
    "save_password_45",
    "retrieve_password_45",
    "list_entries_45",
    "delete_entry_45",
    "PASSWORD_VAULT_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
    "OFFLINE_ONLY",
]
