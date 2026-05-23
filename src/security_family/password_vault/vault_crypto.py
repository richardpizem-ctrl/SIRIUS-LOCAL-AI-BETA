"""
SIRIUS LOCAL AI – PasswordVault Cryptography 4.5.0 (PRO)
--------------------------------------------------------
AES‑256‑GCM encryption helpers for Password Vault 4.5.0.

Features:
- deterministic, offline‑only cryptography
- PBKDF2‑HMAC‑SHA256 key derivation
- AES‑256‑GCM authenticated encryption
- safe‑mode and degraded‑mode support
- structured error handling
- no dynamic imports, no eval, no reflection
- Security Family 4.5 compliant
"""

import os
import json
from typing import Dict, Any

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


# Runtime flags
SAFE_MODE: bool = False
DEGRADED_MODE: bool = False


# ------------------------------------------------------------
# MASTER KEY DERIVATION (PBKDF2‑HMAC‑SHA256)
# ------------------------------------------------------------
def derive_master_key_45(master_secret: str) -> bytes:
    """
    Derive a stable 256‑bit key from master secret.
    PBKDF2‑HMAC‑SHA256, 200k iterations.
    Deterministic salt for offline vault consistency.
    """

    global DEGRADED_MODE

    if SAFE_MODE:
        return b"\x00" * 32

    try:
        salt = b"SIRIUS_VAULT_SALT_v2_4_5"
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=200_000,
            backend=default_backend(),
        )
        return kdf.derive(master_secret.encode("utf-8"))

    except Exception:
        DEGRADED_MODE = True
        return b"\x00" * 32


# ------------------------------------------------------------
# AES‑256‑GCM ENCRYPTION
# ------------------------------------------------------------
def encrypt_data_45(data: Dict[str, Any], key: bytes) -> Dict[str, Any]:
    """
    Encrypt a Python dict using AES‑256‑GCM.

    Returns structured encrypted payload:
    {
        "iv": bytes,
        "ciphertext": bytes,
        "status": "ok" | "safe_mode" | "error",
        "degraded_mode": bool,
        "version": "4.5.0"
    }
    """

    global DEGRADED_MODE

    if SAFE_MODE:
        return {
            "iv": b"",
            "ciphertext": b"",
            "status": "safe_mode",
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    try:
        aes = AESGCM(key)
        iv = os.urandom(12)
        plaintext = json.dumps(data, separators=(",", ":")).encode("utf-8")
        ciphertext = aes.encrypt(iv, plaintext, None)

        return {
            "iv": iv,
            "ciphertext": ciphertext,
            "status": "ok",
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    except Exception as exc:
        DEGRADED_MODE = True
        return {
            "iv": b"",
            "ciphertext": b"",
            "status": "error",
            "exception": str(exc),
            "degraded_mode": True,
            "version": "4.5.0",
        }


# ------------------------------------------------------------
# AES‑256‑GCM DECRYPTION
# ------------------------------------------------------------
def decrypt_data_45(payload: Dict[str, Any], key: bytes) -> Dict[str, Any]:
    """
    Decrypt AES‑256‑GCM encrypted payload.

    Expects:
    {
        "iv": bytes,
        "ciphertext": bytes,
        ...
    }

    Returns:
    {
        "status": "ok" | "error" | "safe_mode",
        "data": dict | None,
        "degraded_mode": bool,
        "version": "4.5.0"
    }
    """

    global DEGRADED_MODE

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "data": None,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    try:
        iv = payload.get("iv") or b""
        ciphertext = payload.get("ciphertext") or b""

        aes = AESGCM(key)
        plaintext = aes.decrypt(iv, ciphertext, None)
        data = json.loads(plaintext.decode("utf-8"))

        return {
            "status": "ok",
            "data": data,
            "degraded_mode": DEGRADED_MODE,
            "version": "4.5.0",
        }

    except Exception as exc:
        DEGRADED_MODE = True
        return {
            "status": "error",
            "data": None,
            "exception": str(exc),
            "degraded_mode": True,
            "version": "4.5.0",
        }


__all__ = [
    "derive_master_key_45",
    "encrypt_data_45",
    "decrypt_data_45",
    "SAFE_MODE",
    "DEGRADED_MODE",
]
