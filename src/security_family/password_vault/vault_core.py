"""
PasswordVault Core – Runtime 4.3.x
----------------------------------
Core logic for the encrypted offline password vault.

Features:
- AES‑256‑GCM encryption (via vault_crypto)
- deterministic, offline-only behavior
- safe-mode and degraded-mode support
- structured error handling
- no dynamic imports, no eval, no reflection
"""

from typing import Optional, Dict, Any

from .vault_crypto import encrypt_data, decrypt_data
from .vault_storage import VaultStorage


class PasswordVault:
    """
    High-level encrypted password vault wrapper.
    Provides safe, deterministic access to VaultStorage.
    """

    def __init__(self, storage_path: str):
        self.storage = VaultStorage(storage_path)

        # Runtime flags
        self.safe_mode = False
        self.degraded_mode = False

    # ------------------------------------------------------------
    # SAVE ENTRY
    # ------------------------------------------------------------
    def save_entry(self, domain: str, username: str, password: str, meta: Optional[dict] = None) -> Dict[str, Any]:
        """
        Store a new password entry for given domain.
        Returns structured result.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "domain": domain,
                "username": username,
                "degraded_mode": self.degraded_mode,
            }

        try:
            encrypted = encrypt_data({"password": password})
            self.storage.save(domain=domain, username=username, password=encrypted, meta=meta or {})

            return {
                "status": "ok",
                "domain": domain,
                "username": username,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "domain": domain,
                "username": username,
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ------------------------------------------------------------
    # GET ENTRY
    # ------------------------------------------------------------
    def get_entry(self, domain: str, username: Optional[str] = None) -> Dict[str, Any]:
        """
        Retrieve password entry for given domain (and optional username).
        Returns structured result.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "entry": None,
                "degraded_mode": self.degraded_mode,
            }

        try:
            raw = self.storage.load(domain=domain, username=username)

            if raw is None:
                return {
                    "status": "not_found",
                    "entry": None,
                    "degraded_mode": self.degraded_mode,
                }

            decrypted = decrypt_data(raw["password"])
            entry = {
                "domain": domain,
                "username": raw["username"],
                "password": decrypted.get("password"),
                "meta": raw.get("meta", {}),
            }

            return {
                "status": "ok",
                "entry": entry,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "entry": None,
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ------------------------------------------------------------
    # LIST ENTRIES
    # ------------------------------------------------------------
    def list_entries(self) -> Dict[str, Any]:
        """
        List all stored entries (domain + username, no raw passwords).
        Returns structured result.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "entries": [],
                "degraded_mode": self.degraded_mode,
            }

        try:
            entries = self.storage.list_entries()
            return {
                "status": "ok",
                "entries": entries,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "entries": [],
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ------------------------------------------------------------
    # DELETE ENTRY
    # ------------------------------------------------------------
    def delete_entry(self, domain: str, username: Optional[str] = None) -> Dict[str, Any]:
        """
        Delete stored entry for given domain (and optional username).
        Returns structured result.
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "degraded_mode": self.degraded_mode,
            }

        try:
            result = self.storage.delete(domain=domain, username=username)

            if not result:
                return {
                    "status": "not_found",
                    "degraded_mode": self.degraded_mode,
                }

            return {
                "status": "ok",
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "exception": str(exc),
                "degraded_mode": True,
            }
