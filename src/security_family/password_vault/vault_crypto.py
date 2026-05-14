# Cryptographic helpers for Password Vault 4.0
# NOTE: Placeholder — integrate with your existing crypto layer.

import os
from typing import Tuple


def derive_master_key(master_secret: str) -> bytes:
    """
    Derive a stable key from master secret (password / phrase).
    Replace with proper KDF (PBKDF2, Argon2, etc.).
    """
    return master_secret.encode("utf-8")[:32].ljust(32, b"\x00")


def encrypt_data(plaintext: bytes, key: bytes) -> Tuple[bytes, bytes]:
    """
    Encrypt data with given key.
    Returns (iv, ciphertext).
    Placeholder — wire to real AES-256-GCM/CTR implementation.
    """
    iv = os.urandom(12)
    # TODO: replace with real AES encryption
    ciphertext = plaintext  # placeholder
    return iv, ciphertext


def decrypt_data(iv: bytes, ciphertext: bytes, key: bytes) -> bytes:
    """
    Decrypt data with given key.
    Placeholder — wire to real AES-256-GCM/CTR implementation.
    """
    # TODO: replace with real AES decryption
    return ciphertext
