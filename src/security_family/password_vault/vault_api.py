# High-level API for Password Vault 4.0
# This is what other BETA modules will call.

from pathlib import Path

from .vault_core import PasswordVault

_DEFAULT_VAULT_PATH = str(Path.home() / ".sirius_beta" / "password_vault.json")

_vault_instance: PasswordVault | None = None


def _get_vault() -> PasswordVault:
    global _vault_instance
    if _vault_instance is None:
        Path(_DEFAULT_VAULT_PATH).parent.mkdir(parents=True, exist_ok=True)
        _vault_instance = PasswordVault(storage_path=_DEFAULT_VAULT_PATH)
    return _vault_instance


def save_password(domain: str, username: str, password: str, meta: dict | None = None):
    vault = _get_vault()
    vault.save_entry(domain=domain, username=username, password=password, meta=meta or {})


def retrieve_password(domain: str, username: str | None = None):
    vault = _get_vault()
    return vault.get_entry(domain=domain, username=username)


def list_entries():
    vault = _get_vault()
    return vault.list_entries()


def delete_entry(domain: str, username: str | None = None):
    vault = _get_vault()
    return vault.delete_entry(domain=domain, username=username)
