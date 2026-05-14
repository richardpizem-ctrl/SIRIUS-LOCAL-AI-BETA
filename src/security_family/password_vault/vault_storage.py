# Storage layer for Password Vault 4.0
# Handles encrypted JSON file on disk.

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .vault_crypto import encrypt_data, decrypt_data, derive_master_key


class VaultStorage:
    def __init__(self, storage_path: str, master_secret_env: str = "SIRIUS_VAULT_MASTER"):
        self.path = Path(storage_path)
        self.master_secret_env = master_secret_env
        self._ensure_file()

    def _get_master_key(self) -> bytes:
        # In real implementation: read from secure source / prompt / OS keyring
        from os import getenv

        secret = getenv(self.master_secret_env, "CHANGE_ME_MASTER_SECRET")
        return derive_master_key(secret)

    def _ensure_file(self):
        if not self.path.exists():
            self._write_encrypted({"entries": []})

    def _read_encrypted(self) -> Dict[str, Any]:
        if not self.path.exists():
            return {"entries": []}

        raw = self.path.read_bytes()
        if not raw:
            return {"entries": []}

        # Simple container: {"iv": ..., "ciphertext": ...}
        container = json.loads(raw.decode("utf-8"))
        key = self._get_master_key()
        iv = bytes.fromhex(container["iv"])
        ciphertext = bytes.fromhex(container["ciphertext"])
        plaintext = decrypt_data(iv, ciphertext, key)
        return json.loads(plaintext.decode("utf-8"))

    def _write_encrypted(self, data: Dict[str, Any]):
        key = self._get_master_key()
        plaintext = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        iv, ciphertext = encrypt_data(plaintext, key)
        container = {
            "iv": iv.hex(),
            "ciphertext": ciphertext.hex(),
        }
        self.path.write_text(json.dumps(container, ensure_ascii=False, indent=2), encoding="utf-8")

    def save(self, domain: str, username: str, password: str, meta: Dict[str, Any]):
        data = self._read_encrypted()
        entries: List[Dict[str, Any]] = data.get("entries", [])
        # remove existing same domain+username
        entries = [e for e in entries if not (e["domain"] == domain and e["username"] == username)]
        entries.append(
            {
                "domain": domain,
                "username": username,
                "password": password,
                "meta": meta,
            }
        )
        data["entries"] = entries
        self._write_encrypted(data)

    def load(self, domain: str, username: Optional[str] = None) -> Optional[Dict[str, Any]]:
        data = self._read_encrypted()
        for e in data.get("entries", []):
            if e["domain"] == domain and (username is None or e["username"] == username):
                return e
        return None

    def list_entries(self) -> List[Dict[str, Any]]:
        data = self._read_encrypted()
        # do not expose raw passwords
        return [
            {
                "domain": e["domain"],
                "username": e["username"],
                "meta": e.get("meta", {}),
            }
            for e in data.get("entries", [])
        ]

    def delete(self, domain: str, username: Optional[str] = None) -> bool:
        data = self._read_encrypted()
        before = len(data.get("entries", []))
        data["entries"] = [
            e
            for e in data.get("entries", [])
            if not (e["domain"] == domain and (username is None or e["username"] == username))
        ]
        after = len(data["entries"])
        self._write_encrypted(data)
        return after < before
