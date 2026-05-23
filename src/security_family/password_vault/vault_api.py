"""
SIRIUS LOCAL AI – PasswordVault API 4.5.0 (PRO)
-----------------------------------------------
High‑level API for Password Vault 4.5.0.
Used by Security Family 4.5 modules.

Features:
- deterministic, offline‑only behavior
- safe‑mode and degraded‑mode support
- structured return values
- identity‑aware access (OWNER / FAMILY / STRANGER / CHILD)
- no dynamic imports, no eval, no reflection
- Security Family 4.5 compliant
"""

from pathlib import Path
from typing import Optional, Dict, Any

from .vault_core_4_5 import PasswordVault45


# ---------------------------------------------------------
# DEFAULT STORAGE PATH (DETERMINISTIC)
# ---------------------------------------------------------

_DEFAULT_VAULT_PATH = str(Path.home() / ".sirius_local_ai" / "password_vault_4_5.json")
_vault_instance: Optional[PasswordVault45] = None

# Runtime flags
SAFE_MODE: bool = True
DEGRADED_MODE: bool = False


# ---------------------------------------------------------
# INTERNAL VAULT ACCESSOR (SAFE, DETERMINISTIC)
# ---------------------------------------------------------

def _get_vault() -> PasswordVault45:
    global _vault_instance, DEGRADED_MODE

    if SAFE_MODE:
        raise RuntimeError("PasswordVault45 is in safe‑mode.")

    try:
        if _vault_instance is None:
            Path(_DEFAULT_VAULT_PATH).parent.mkdir(parents=True, exist_ok=True)
            _vault_instance = PasswordVault45(storage_path=_DEFAULT_VAULT_PATH)
        return _vault_instance

    except Exception:
        DEGRADED_MODE = True
        raise


# ---------------------------------------------------------
# HIGH‑LEVEL API (STRUCTURED, SAFE, 4.5 PRO)
# ---------------------------------------------------------

def save_password_45(
    domain: str,
    username: str,
    password: str,
    meta: Optional[dict] = None,
    identity: str = "OWNER",
) -> Dict[str, Any]:
    """
    Saves a password entry.
    Identity‑aware, deterministic, offline‑safe.
    """

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "domain": domain,
            "username": username,
            "identity": identity,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    try:
        vault = _get_vault()
        result = vault.save_entry(
            domain=domain,
            username=username,
            password=password,
            meta=meta or {},
            identity=identity,
        )
        return {
            "status": "ok",
            "domain": domain,
            "username": username,
            "identity": identity,
            "result": result,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    except Exception as exc:
        global DEGRADED_MODE
        DEGRADED_MODE = True
        return {
            "status": "error",
            "domain": domain,
            "username": username,
            "identity": identity,
            "exception": str(exc),
            "degraded_mode": True,
            "version": "4.5.0",
        }


def retrieve_password_45(
    domain: str,
    username: Optional[str] = None,
    identity: str = "OWNER",
) -> Dict[str, Any]:
    """
    Retrieves a password entry.
    """

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "entry": None,
            "identity": identity,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    try:
        vault = _get_vault()
        entry = vault.get_entry(domain=domain, username=username, identity=identity)

        if entry is None:
            return {
                "status": "not_found",
                "entry": None,
                "identity": identity,
                "degraded_mode": DEGRADED_MODE,
                "version": "4.5.0",
            }

        return {
            "status": "ok",
            "entry": entry,
            "identity": identity,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    except Exception as exc:
        global DEGRADED_MODE
        DEGRADED_MODE = True
        return {
            "status": "error",
            "entry": None,
            "identity": identity,
            "exception": str(exc),
            "degraded_mode": True,
            "version": "4.5.0",
        }


def list_entries_45(identity: str = "OWNER") -> Dict[str, Any]:
    """
    Lists all stored entries.
    """

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "entries": [],
            "identity": identity,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    try:
        vault = _get_vault()
        entries = vault.list_entries(identity=identity)
        return {
            "status": "ok",
            "entries": entries,
            "identity": identity,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    except Exception as exc:
        global DEGRADED_MODE
        DEGRADED_MODE = True
        return {
            "status": "error",
            "entries": [],
            "identity": identity,
            "exception": str(exc),
            "degraded_mode": True,
            "version": "4.5.0",
        }


def delete_entry_45(
    domain: str,
    username: Optional[str] = None,
    identity: str = "OWNER",
) -> Dict[str, Any]:
    """
    Deletes a password entry.
    """

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "identity": identity,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    try:
        vault = _get_vault()
        result = vault.delete_entry(domain=domain, username=username, identity=identity)

        if not result:
            return {
                "status": "not_found",
                "identity": identity,
                "degraded_mode": DEGRADED_MODE,
                "version": "4.5.0",
            }

        return {
            "status": "ok",
            "identity": identity,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    except Exception as exc:
        global DEGRADED_MODE
        DEGRADED_MODE = True
        return {
            "status": "error",
            "identity": identity,
            "exception": str(exc),
            "degraded_mode": True,
            "version": "4.5.0",
        }
