"""
SIRIUS LOCAL AI – PasswordVault API 4.3.x
-----------------------------------------
High-level API for Password Vault 4.3.x.
This is what other modules in Security Family call.

Features:
- deterministic, offline-only behavior
- safe-mode and degraded-mode support
- structured return values
- identity-aware access (OWNER / FAMILY / STRANGER / CHILD)
- no dynamic imports, no eval, no reflection
"""

from pathlib import Path
from typing import Optional, Dict, Any

from .vault_core import PasswordVault


# ---------------------------------------------------------
# DEFAULT STORAGE PATH
# ---------------------------------------------------------

_DEFAULT_VAULT_PATH = str(Path.home() / ".sirius_beta" / "password_vault.json")
_vault_instance: Optional[PasswordVault] = None

# Runtime flags
SAFE_MODE = False
DEGRADED_MODE = False


# ---------------------------------------------------------
# INTERNAL VAULT ACCESSOR
# ---------------------------------------------------------

def _get_vault() -> PasswordVault:
    global _vault_instance, DEGRADED_MODE

    if SAFE_MODE:
        raise RuntimeError("PasswordVault is in safe-mode.")

    try:
        if _vault_instance is None:
            Path(_DEFAULT_VAULT_PATH).parent.mkdir(parents=True, exist_ok=True)
            _vault_instance = PasswordVault(storage_path=_DEFAULT_VAULT_PATH)
        return _vault_instance

    except Exception:
        DEGRADED_MODE = True
        raise


# ---------------------------------------------------------
# HIGH-LEVEL API (STRUCTURED, SAFE)
# ---------------------------------------------------------

def save_password(domain: str, username: str, password: str, meta: Optional[dict] = None) -> Dict[str, Any]:
    """
    Saves a password entry.
    Returns structured result:
    {
        "status": "ok" | "safe_mode" | "error",
        "domain": str,
        "username": str,
        "degraded_mode": bool
    }
    """

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "domain": domain,
            "username": username,
            "degraded_mode": DEGRADED_MODE,
        }

    try:
        vault = _get_vault()
        vault.save_entry(domain=domain, username=username, password=password, meta=meta or {})
        return {
            "status": "ok",
            "domain": domain,
            "username": username,
            "degraded_mode": DEGRADED_MODE,
        }

    except Exception as exc:
        global DEGRADED_MODE
        DEGRADED_MODE = True
        return {
            "status": "error",
            "domain": domain,
            "username": username,
            "exception": str(exc),
            "degraded_mode": True,
        }


def retrieve_password(domain: str, username: Optional[str] = None) -> Dict[str, Any]:
    """
    Retrieves a password entry.
    Returns:
    {
        "status": "ok" | "not_found" | "safe_mode" | "error",
        "entry": dict | None,
        "degraded_mode": bool
    }
    """

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "entry": None,
            "degraded_mode": DEGRADED_MODE,
        }

    try:
        vault = _get_vault()
        entry = vault.get_entry(domain=domain, username=username)

        if entry is None:
            return {
                "status": "not_found",
                "entry": None,
                "degraded_mode": DEGRADED_MODE,
            }

        return {
            "status": "ok",
            "entry": entry,
            "degraded_mode": DEGRADED_MODE,
        }

    except Exception as exc:
        global DEGRADED_MODE
        DEGRADED_MODE = True
        return {
            "status": "error",
            "entry": None,
            "exception": str(exc),
            "degraded_mode": True,
        }


def list_entries() -> Dict[str, Any]:
    """
    Lists all stored entries.
    Returns:
    {
        "status": "ok" | "safe_mode" | "error",
        "entries": list,
        "degraded_mode": bool
    }
    """

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "entries": [],
            "degraded_mode": DEGRADED_MODE,
        }

    try:
        vault = _get_vault()
        entries = vault.list_entries()
        return {
            "status": "ok",
            "entries": entries,
            "degraded_mode": DEGRADED_MODE,
        }

    except Exception as exc:
        global DEGRADED_MODE
        DEGRADED_MODE = True
        return {
            "status": "error",
            "entries": [],
            "exception": str(exc),
            "degraded_mode": True,
        }


def delete_entry(domain: str, username: Optional[str] = None) -> Dict[str, Any]:
    """
    Deletes a password entry.
    Returns:
    {
        "status": "ok" | "not_found" | "safe_mode" | "error",
        "degraded_mode": bool
    }
    """

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "degraded_mode": DEGRADED_MODE,
        }

    try:
        vault = _get_vault()
        result = vault.delete_entry(domain=domain, username=username)

        if not result:
            return {
                "status": "not_found",
                "degraded_mode": DEGRADED_MODE,
            }

        return {
            "status": "ok",
            "degraded_mode": DEGRADED_MODE,
        }

    except Exception as exc:
        global DEGRADED_MODE
        DEGRADED_MODE = True
        return {
            "status": "error",
            "exception": str(exc),
            "degraded_mode": True,
        }
