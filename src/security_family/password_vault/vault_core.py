# Core logic for Password Vault 4.0 (BETA runtime)

from .vault_crypto import encrypt_data, decrypt_data
from .vault_storage import VaultStorage


class PasswordVault:
    def __init__(self, storage_path: str):
        self.storage = VaultStorage(storage_path)

    def save_entry(self, domain: str, username: str, password: str, meta: dict | None = None):
        """
        Store a new password entry for given domain.
        """
        self.storage.save(domain=domain, username=username, password=password, meta=meta or {})

    def get_entry(self, domain: str, username: str | None = None):
        """
        Retrieve password entry for given domain (and optional username).
        """
        return self.storage.load(domain=domain, username=username)

    def list_entries(self):
        """
        List all stored entries (domain + username, no raw passwords).
        """
        return self.storage.list_entries()

    def delete_entry(self, domain: str, username: str | None = None):
        """
        Delete stored entry for given domain (and optional username).
        """
        return self.storage.delete(domain=domain, username=username)
