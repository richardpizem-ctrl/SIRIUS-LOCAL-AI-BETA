"""
SIRIUS LOCAL AI – Security.PasswordVault 4.3.x
----------------------------------------------
Offline, encrypted password manager (part of Security Family 4.x)

This package provides:
- PasswordVault core (AES-256-GCM encrypted storage)
- High-level API (save/retrieve/list/delete)
- Identity-aware access control (OWNER / FAMILY / STRANGER / CHILD)
- Deterministic, offline-only behavior
- Safe-mode and degraded-mode compatibility

Security Notes (4.3.x):
- No dynamic imports, no eval, no reflection.
- Only static, verified modules may be exported.
- This file must not contain executable logic.
- Fully compatible with Security Family 4.4.
- Self‑Repair 4.4 ready.
"""

# ---------------------------------------------------------
# SAFE STATIC IMPORTS
# ---------------------------------------------------------

from .vault_core import PasswordVault
from .vault_api import (
    save_password,
    retrieve_password,
    list_entries,
    delete_entry,
)

# ---------------------------------------------------------
# PACKAGE METADATA
# ---------------------------------------------------------

PASSWORD_VAULT_VERSION = "4.3.x"
SECURITY_FAMILY_COMPAT = "4.4"
SAFE_MODE_SUPPORTED = True

# ---------------------------------------------------------
# SAFE EXPORT LIST
# ---------------------------------------------------------

__all__ = [
    "PasswordVault",
    "save_password",
    "retrieve_password",
    "list_entries",
    "delete_entry",
    "PASSWORD_VAULT_VERSION",
    "SECURITY_FAMILY_COMPAT",
    "SAFE_MODE_SUPPORTED",
]
