# 🔐 Security.PasswordVault 4.0 — Offline Password Manager

Part of **Security Family 4.x** in **SIRIUS LOCAL AI BETA**.

## Purpose

- Offline, encrypted password manager
- No cloud, no telemetry, no external sync
- Deterministic, identity‑aware, hybrid‑safe

## Features

- AES‑encrypted JSON vault on disk
- Domain + username based lookup
- No raw passwords exposed in listings
- Ready for Windows autofill integration
- Ready for LAN‑offline sync with GAMA

## Files

- `vault_core.py` — core logic (PasswordVault)
- `vault_crypto.py` — crypto helpers (to be wired to real AES)
- `vault_storage.py` — encrypted JSON storage
- `vault_api.py` — high‑level API for other modules
- `vault_events.py` — event names for Security Family
- `vault_storage.json` — encrypted vault file (runtime‑created)
