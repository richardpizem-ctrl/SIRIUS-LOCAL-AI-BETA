# SIRIUS LOCAL AI BETA — Security.PasswordVault 4.0
# Offline, encrypted password manager (part of Security Family 4.x)

from .vault_core import PasswordVault
from .vault_api import (
    save_password,
    retrieve_password,
    list_entries,
    delete_entry,
)
