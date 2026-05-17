"""
VaultStorage – Runtime 4.3.x
----------------------------
Encrypted JSON storage layer for Password Vault.

Features:
- deterministic, offline-only behavior
- AES‑256‑GCM encryption/decryption
- PBKDF2-HMAC-SHA256 master key derivation
- safe-mode and degraded-mode support
- structured error handling
- corruption‑tolerant read/write
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .vault_crypto import encrypt_data, decrypt_data, derive_master_key


class VaultStorage:
    """
    Low-level encrypted storage for PasswordVault.
    """

    def __init__(self, storage_path: str, master_secret_env: str = "SIRIUS_VAULT_MASTER"):
        self.path = Path(storage_path)
        self.master_secret_env = master_secret_env

        self.safe_mode = False
        self.degraded_mode = False

        self._ensure_file()

    # ------------------------------------------------------------
    # MASTER KEY
    # ------------------------------------------------------------
    def _get_master_key(self) -> bytes:
        """
        Derives master key from environment variable.
        Deterministic, offline-only.
        """

        if self.safe_mode:
            return b"\x00" * 32

        try:
            from os import getenv
            secret = getenv(self.master_secret_env, "CHANGE_ME_MASTER_SECRET")
            return derive_master_key(secret)
        except Exception:
            self.degraded_mode = True
            return b"\x00" * 32

    # ------------------------------------------------------------
    # FILE INITIALIZATION
    # ------------------------------------------------------------
    def _ensure_file(self):
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
            iv = bytes.fromhex(container.get("iv", ""))
            ciphertext = bytes.fromhex(container.get("ciphertext", ""))

            decrypted = decrypt_data(iv, ciphertext, key)

            if decrypted.get("status") != "ok":
                self.degraded_mode = True
                return {"entries": []}

            return decrypted["data"]

        except Exception:
            self.degraded_mode = True
            return {"entries": []}

    # ------------------------------------------------------------
    # WRITE ENCRYPTED FILE
    # ------------------------------------------------------------
    def _write_encrypted(self, data: Dict[str, Any]):
        if self.safe_mode:
            return

        try:
            key = self._get_master_key()
            encrypted = encrypt_data(data, key)

            if encrypted.get("status") != "ok":
                self.degraded_mode = True
                return

            container = {
                "iv": encrypted["iv"].hex(),
                "ciphertext": encrypted["ciphertext"].hex(),
            }

            self.path.write_text(
                json.dumps(container, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

        except Exception:
            self.degraded_mode = True

    # ------------------------------------------------------------
    # SAVE ENTRY
    # ------------------------------------------------------------
    def save(self, domain: str, username: str, password: Dict[str, Any], meta: Dict[str, Any]):
        data = self._read_encrypted()
        entries: List[Dict[str, Any]] = data.get("entries", [])

        # Remove existing entry
        entries = [
            e for e in entries
            if not (e.get("domain") == domain and e.get("username") == username)
        ]

        entries.append({
            "domain": domain,
            "username": username,
            "password": password,
            "meta": meta,
        })

        data["entries"] = entries
        self._write_encrypted(data)

    # ------------------------------------------------------------
    # LOAD ENTRY
    # ------------------------------------------------------------
    def load(self, domain: str, username: Optional[str] = None) -> Optional[Dict[str, Any]]:
        data = self._read_encrypted()

        for e in data.get("entries", []):
            if e.get("domain") == domain and (username is None or e.get("username") == username):
                return e

        return None

    # ------------------------------------------------------------
    # LIST ENTRIES (NO PASSWORDS)
    # ------------------------------------------------------------
    def list_entries(self) -> List[Dict[str, Any]]:
        data = self._read_encrypted()

        return [
            {
                "domain": e.get("domain"),
                "username": e.get("username"),
                "meta": e.get("meta", {}),
            }
            for e in data.get("entries", [])
        ]

    # ------------------------------------------------------------
    # DELETE ENTRY
    # ------------------------------------------------------------
    def delete(self, domain: str, username: Optional[str] = None) -> bool:
        data = self._read_encrypted()
        before = len(data.get("entries", []))

        data["entries"] = [
            e for e in data.get("entries", [])
            if not (e.get("domain") == domain and (username is None or e.get("username") == username))
        ]

        after = len(data["entries"])
        self._write_encrypted(data)

        return after < before
