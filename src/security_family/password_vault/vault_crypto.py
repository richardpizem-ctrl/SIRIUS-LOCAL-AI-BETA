"""
PasswordVault Cryptography – Runtime 4.3.x
------------------------------------------
AES‑256‑GCM encryption helpers for Password Vault.

Features:
- deterministic, offline-only cryptography
- PBKDF2-HMAC-SHA256 key derivation
- AES‑256‑GCM authenticated encryption
- safe-mode and degraded-mode support
- structured error handling
- no dynamic imports, no eval, no reflection
"""

import os
import json
from typing import Tuple, Dict, Any

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


# Runtime flags
SAFE_MODE = False
DEGRADED_MODE = False


# ------------------------------------------------------------
# MASTER KEY DERIVATION (PBKDF2‑HMAC‑SHA256)
# ------------------------------------------------------------
def derive_master_key(master_secret: str) -> bytes:
    """
    Derive a stable 256‑bit key from master secret.
    PBKDF2‑HMAC‑SHA256, 200k iterations.
    Deterministic salt for offline vault consistency.
    """

    global DEGRADED_MODE

    if SAFE_MODE:
        # Return a dummy key in safe-mode (vault operations disabled anyway)
        return b"\x00" * 32

    try:
        salt = b"SIRIUS_VAULT_SALT_v1"
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
def encrypt_data(data: Dict[str, Any], key: bytes) -> Dict[str, Any]:
    """
    Encrypt a Python dict using AES‑256‑GCM.
    Returns structured encrypted payload:
    {
        "iv": bytes,
        "ciphertext": bytes
    }
    """

    global DEGRADED_MODE

    if SAFE_MODE:
        return {
            "iv": b"",
            "ciphertext": b"",
            "status": "safe_mode",
            "degraded_mode": DEGRADED_MODE,
        }

    try:
        aes = AESGCM(key)
        iv = os.urandom(12)
        plaintext = json.dumps(data).encode("utf-8")
        ciphertext = aes.encrypt(iv, plaintext, None)

        return {
            "iv": iv,
            "ciphertext": ciphertext,
            "status": "ok",
            "degraded_mode": DEGRADED_MODE,
        }

    except Exception as exc:
        DEGRADED_MODE = True
        return {
            "iv": b"",
            "ciphertext": b"",
            "status": "error",
            "exception": str(exc),
            "degraded_mode": True,
        }


# ------------------------------------------------------------
# AES‑256‑GCM DECRYPTION
# ------------------------------------------------------------
def decrypt_data(iv: bytes, ciphertext: bytes, key: bytes) -> Dict[str, Any]:
    """
    Decrypt AES‑256‑GCM encrypted payload.
    Returns:
    {
        "status": "ok" | "error" | "safe_mode",
        "data": dict | None,
        "degraded_mode": bool
    }
    """

    global DEGRADED_MODE

    if SAFE_MODE:
        return {
            "status": "safe_mode",
            "data": None,
            "degraded_mode": DEGRADED_MODE,
        }

    try:
        aes = AESGCM(key)
        plaintext = aes.decrypt(iv, ciphertext, None)
        data = json.loads(plaintext.decode("utf-8"))

        return {
            "status": "ok",
            "data": data,
            "degraded_mode": DEGRADED_MODE,
        }

    except Exception as exc:
        DEGRADED_MODE = True
        return {
            "status": "error",
            "data": None,
            "exception": str(exc),
            "degraded_mode": True,
        }
