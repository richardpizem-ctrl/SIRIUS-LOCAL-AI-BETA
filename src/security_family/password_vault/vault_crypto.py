# Cryptographic helpers for Password Vault 4.0
# AES‑256‑GCM implementation (secure, production‑ready)

import os
from typing import Tuple
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


# ------------------------------------------------------------
# MASTER KEY DERIVATION (PBKDF2‑HMAC‑SHA256)
# ------------------------------------------------------------
def derive_master_key(master_secret: str) -> bytes:
    """
    Derive a stable 256‑bit key from master secret.
    PBKDF2‑HMAC‑SHA256, 200k iterations.
    """
    salt = b"SIRIUS_VAULT_SALT_v1"  # static salt for deterministic vault key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
        backend=default_backend(),
    )
    return kdf.derive(master_secret.encode("utf-8"))


# ------------------------------------------------------------
# AES‑256‑GCM ENCRYPTION
# ------------------------------------------------------------
def encrypt_data(plaintext: bytes, key: bytes) -> Tuple[bytes, bytes]:
    """
    Encrypt data using AES‑256‑GCM.
    Returns (iv, ciphertext_with_tag).
    """
    aes = AESGCM(key)
    iv = os.urandom(12)  # recommended GCM IV size
    ciphertext = aes.encrypt(iv, plaintext, None)
    return iv, ciphertext


# ------------------------------------------------------------
# AES‑256‑GCM DECRYPTION
# ------------------------------------------------------------
def decrypt_data(iv: bytes, ciphertext: bytes, key: bytes) -> bytes:
    """
    Decrypt AES‑256‑GCM data.
    """
    aes = AESGCM(key)
    return aes.decrypt(iv, ciphertext, None)
