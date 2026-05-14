"""
SIRIUS LOCAL AI – Security Family Package
-----------------------------------------
This package contains the offline safety and identity protection system
used by SIRIUS LOCAL AI.

Security Family provides:
- behavior‑based identity classification (OWNER / FAMILY / STRANGER)
- time‑limit enforcement for children
- restricted mode for unknown users
- schoolwork priority mode triggered by the triage engine
- safe‑mode for sensitive operations requiring OWNER approval
- full offline operation without biometrics or cloud services

Modules inside this package are dynamically loaded by the runtime.
No imports are performed here to avoid side‑effects during initialization.

New in Security Family 4.0:
---------------------------
Password Vault 4.0 (Security.PasswordVault)
- offline encrypted password manager
- AES‑256 encrypted vault file
- domain‑aware password retrieval
- phishing‑aware autofill protection
- identity‑aware access (OWNER / FAMILY / STRANGER)
- ready for Windows autofill integration
- ready for LAN‑offline sync with SIRIUS GAMA
"""
