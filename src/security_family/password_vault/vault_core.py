"""
SIRIUS LOCAL AI – PasswordVault Core 4.4.0 (PRO)
------------------------------------------------
Core logic for the encrypted offline password vault.

Features:
- AES‑256‑GCM encryption (via vault_crypto_4_4)
- deterministic, offline‑only behavior
- identity‑aware access control (OWNER / FAMILY / CHILD / STRANGER)
- safe‑mode and degraded‑mode support
- structured error handling
- Security Family 4.4 compliant
- no dynamic imports, no eval, no reflection
"""

from typing import Optional, Dict, Any

from .vault_crypto_4_4 import encrypt_data_44, decrypt_data_44
from .vault_storage_4_4 import VaultStorage44


class PasswordVault44:
    """
    High‑level encrypted password vault wrapper.
    Provides safe, deterministic access to VaultStorage44.
    """

    VALID_IDENTITIES = {"OWNER", "FAMILY", "CHILD", "STRANGER"}

    def __init__(self, storage_path: str):
        self.storage = VaultStorage44(storage_path)

        # Runtime flags
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

    # ------------------------------------------------------------------
    # INTERNAL – IDENTITY VALIDATION
    # ------------------------------------------------------------------
    def _normalize_identity(self, identity: str) -> str:
        identity = (identity or "STRANGER").upper().strip()
        return identity if identity in self.VALID_IDENTITIES else "STRANGER"

    # ------------------------------------------------------------------
    # SAVE ENTRY
    # ------------------------------------------------------------------
    def save_entry(
        self,
        domain: str,
        username: str,
        password: str,
        meta: Optional[dict] = None,
        identity: str = "OWNER",
    ) -> Dict[str, Any]:
        """
        Store a new password entry for given domain.
        Identity‑aware, deterministic, offline‑safe.
        """

        identity = self._normalize_identity(identity)

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "domain": domain,
                "username": username,
                "identity": identity,
                "degraded_mode": self.degraded_mode,
            }

        try:
            encrypted = encrypt_data_44({"password": password})
            self.storage.save(
                domain=domain,
                username=username,
                password=encrypted,
                meta=meta or {},
                identity=identity,
            )

            return {
                "status": "ok",
                "domain": domain,
                "username": username,
                "identity": identity,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "domain": domain,
                "username": username,
                "identity": identity,
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ------------------------------------------------------------------
    # GET ENTRY
    # ------------------------------------------------------------------
    def get_entry(
        self,
        domain: str,
        username: Optional[str] = None,
        identity: str = "OWNER",
    ) -> Dict[str, Any]:
        """
        Retrieve password entry for given domain (and optional username).
        Identity‑aware, deterministic, offline‑safe.
        """

        identity = self._normalize_identity(identity)

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "entry": None,
                "identity": identity,
                "degraded_mode": self.degraded_mode,
            }

        try:
            raw = self.storage.load(domain=domain, username=username, identity=identity)

            if raw is None:
                return {
                    "status": "not_found",
                    "entry": None,
                    "identity": identity,
                    "degraded_mode": self.degraded_mode,
                }

            decrypted = decrypt_data_44(raw["password"])
            entry = {
                "domain": domain,
                "username": raw["username"],
                "password": decrypted.get("password"),
                "meta": raw.get("meta", {}),
            }

            return {
                "status": "ok",
                "entry": entry,
                "identity": identity,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "entry": None,
                "identity": identity,
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ------------------------------------------------------------------
    # LIST ENTRIES
    # ------------------------------------------------------------------
    def list_entries(self, identity: str = "OWNER") -> Dict[str, Any]:
        """
        List all stored entries (domain + username, no raw passwords).
        Identity‑aware, deterministic, offline‑safe.
        """

        identity = self._normalize_identity(identity)

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "entries": [],
                "identity": identity,
                "degraded_mode": self.degraded_mode,
            }

        try:
            entries = self.storage.list_entries(identity=identity)
            return {
                "status": "ok",
                "entries": entries,
                "identity": identity,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "entries": [],
                "identity": identity,
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ------------------------------------------------------------------
    # DELETE ENTRY
    # ------------------------------------------------------------------
    def delete_entry(
        self,
        domain: str,
        username: Optional[str] = None,
        identity: str = "OWNER",
    ) -> Dict[str, Any]:
        """
        Delete stored entry for given domain (and optional username).
        Identity‑aware, deterministic, offline‑safe.
        """

        identity = self._normalize_identity(identity)

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "identity": identity,
                "degraded_mode": self.degraded_mode,
            }

        try:
            result = self.storage.delete(domain=domain, username=username, identity=identity)

            if not result:
                return {
                    "status": "not_found",
                    "identity": identity,
                    "degraded_mode": self.degraded_mode,
                }

            return {
                "status": "ok",
                "identity": identity,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "identity": identity,
                "exception": str(exc),
                "degraded_mode": True,
            }
