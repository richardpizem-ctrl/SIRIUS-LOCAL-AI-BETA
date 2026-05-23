"""
VaultStorage – Runtime 4.5.0 (PRO)
----------------------------------
Encrypted JSON storage layer for Password Vault 4.5.

Features:
- deterministic, offline‑only behavior
- AES‑256‑GCM encryption/decryption (vault_crypto_4_5)
- PBKDF2‑HMAC‑SHA256 master key derivation
- identity‑aware, safe‑mode and degraded‑mode support
- structured error handling
- corruption‑tolerant read/write
- Security Family 4.5 compliant
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .vault_crypto_4_5 import encrypt_data_45, decrypt_data_45, derive_master_key_45


class VaultStorage45:
    """
    Low‑level encrypted storage for PasswordVault45.
    Deterministic, offline, identity‑aware.
    """

    def __init__(
        self,
        storage_path: str,
        master_secret_env: str = "SIRIUS_VAULT_MASTER_4_5",
    ):
        self.version = "4.5.0"
        self.path = Path(storage_path)
        self.master_secret_env = master_secret_env

        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        self._ensure_file()

    # ------------------------------------------------------------
    # MASTER KEY
    # ------------------------------------------------------------
    def _get_master_key(self) -> bytes:
        """
        Derives master key from environment variable.
        Deterministic, offline‑only.
        """

        if self.safe_mode:
            return b"\x00" * 32

        try:
            from os import getenv
            secret = getenv(self.master_secret_env, "CHANGE_ME_MASTER_SECRET_4_5")
            return derive_master_key_45(secret)
        except Exception:
            self.degraded_mode = True
            return b"\x00" * 32

    # ------------------------------------------------------------
    # FILE INITIALIZATION
    # ------------------------------------------------------------
    def _ensure_file(self) -> None:
        if not self.path.exists():
            self._write_encrypted({"entries": []})

    # ------------------------------------------------------------
    # READ ENCRYPTED FILE
    # ------------------------------------------------------------
    def _read_encrypted(self) -> Dict[str, Any]:
        """
        Reads encrypted JSON file and returns decrypted dict.
        Handles corruption gracefully.
        """

        if self.safe_mode:
            return {"entries": []}

        try:
            if not self.path.exists():
                return {"entries": []}

            raw = self.path.read_bytes()
            if not raw:
                return {"entries": []}

            container = json.loads(raw.decode("utf-8"))

            key = self._get_master_key()
            payload = {
                "iv": bytes.fromhex(container.get("iv", "")),
                "ciphertext": bytes.fromhex(container.get("ciphertext", "")),
            }

            decrypted = decrypt_data_45(payload, key)

            if decrypted.get("status") != "ok":
                self.degraded_mode = True
                return {"entries": []}

            return decrypted["data"] or {"entries": []}

        except Exception:
            self.degraded_mode = True
            return {"entries": []}

    # ------------------------------------------------------------
    # WRITE ENCRYPTED FILE
    # ------------------------------------------------------------
    def _write_encrypted(self, data: Dict[str, Any]) -> None:
        if self.safe_mode:
            return

        try:
            key = self._get_master_key()
            encrypted = encrypt_data_45(data, key)

            if encrypted.get("status") != "ok":
                self.degraded_mode = True
                return

            container = {
                "iv": encrypted["iv"].hex(),
                "ciphertext": encrypted["ciphertext"].hex(),
            }

            self.path.write_text(
                json.dumps(container, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )

        except Exception:
            self.degraded_mode = True

    # ------------------------------------------------------------
    # SAVE ENTRY
    # ------------------------------------------------------------
    def save(
        self,
        domain: str,
        username: str,
        password: Dict[str, Any],
        meta: Dict[str, Any],
        identity: str = "OWNER",
    ) -> None:
        data = self._read_encrypted()
        entries: List[Dict[str, Any]] = data.get("entries", [])

        entries = [
            e
            for e in entries
            if not (
                e.get("domain") == domain
                and e.get("username") == username
                and e.get("identity", "OWNER") == identity
            )
        ]

        entries.append(
            {
                "domain": domain,
                "username": username,
                "password": password,
                "meta": meta,
                "identity": identity,
            }
        )

        data["entries"] = entries
        self._write_encrypted(data)

    # ------------------------------------------------------------
    # LOAD ENTRY
    # ------------------------------------------------------------
    def load(
        self,
        domain: str,
        username: Optional[str] = None,
        identity: str = "OWNER",
    ) -> Optional[Dict[str, Any]]:
        data = self._read_encrypted()

        for e in data.get("entries", []):
            if (
                e.get("domain") == domain
                and (username is None or e.get("username") == username)
                and e.get("identity", "OWNER") == identity
            ):
                return e

        return None

    # ------------------------------------------------------------
    # LIST ENTRIES (NO PASSWORDS)
    # ------------------------------------------------------------
    def list_entries(self, identity: str = "OWNER") -> List[Dict[str, Any]]:
        data = self._read_encrypted()

        return [
            {
                "domain": e.get("domain"),
                "username": e.get("username"),
                "meta": e.get("meta", {}),
                "identity": e.get("identity", "OWNER"),
            }
            for e in data.get("entries", [])
            if e.get("identity", "OWNER") == identity
        ]

    # ------------------------------------------------------------
    # DELETE ENTRY
    # ------------------------------------------------------------
    def delete(
        self,
        domain: str,
        username: Optional[str] = None,
        identity: str = "OWNER",
    ) -> bool:
        data = self._read_encrypted()
        before = len(data.get("entries", []))

        data["entries"] = [
            e
            for e in data.get("entries", [])
            if not (
                e.get("domain") == domain
                and (username is None or e.get("username") == username)
                and e.get("identity", "OWNER") == identity
            )
        ]

        after = len(data["entries"])
        self._write_encrypted(data)

        return after < before
