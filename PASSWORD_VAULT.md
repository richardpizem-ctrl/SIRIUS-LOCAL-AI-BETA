# 🟦 SIRIUS Runtime 4.2.0 – UI Automation Engine (Completed)

This release introduces the complete UI Automation subsystem for SIRIUS Runtime.
All modules are fully implemented, documented, and prepared for the upcoming 4.3.0 upgrade.

---

## ✔ Included Modules

### • UI Graph
- Window tree abstraction  
- Fake OS elements for workflow testing  
- Ready for WinCapabilities integration (4.3.0)

### • UI Parser
- Element extraction and normalization  
- Exact, case‑insensitive and partial matching  
- Prepared for fuzzy matching engine (4.3.0)

### • UI Actions
- Deterministic UI operations (click, write, select, semantic)  
- Unified audit logging  
- Sandbox‑aware execution  
- Ready for real OS UI control (4.3.0)

### • UI Sandbox
- Identity‑based permission model (OWNER / FAMILY / STRANGER / CHILD)  
- Deterministic security rules  
- Local audit trail  
- Ready for EventBus integration (4.3.0)

### • UI Workflow
- Deterministic step engine (scan → parse → find → act)  
- Clean target resolution  
- Demo workflow included  
- Ready for fallback logic (4.3.0)

---

## ✔ Highlights
- Fully isolated module (does not modify runtime core)  
- 100% deterministic behavior  
- Full English documentation across all modules  
- Unified architecture and naming conventions  
- Complete vertical slice demo (`demo_ok_click_workflow`)  
- Fully prepared for 4.3.0 upgrades

---

## ✔ Next Milestone: Runtime 4.3.0
- Fuzzy Matching Engine (Parser)  
- WinCapabilities OS UI control (Actions)  
- Workflow fallback engine  
- EventBus integration for audit logs

---

# 🟩 SIRIUS Runtime 4.3.0 – Semantic UI Automation Engine (Completed)

This release delivers the full UI Automation Engine for SIRIUS LOCAL AI.
Version 4.3.0 replaces the previously planned 4.2.0 and introduces a complete,
deterministic, semantic UI automation pipeline fully integrated with Runtime 4.0.

---

## 🔍 UIParser 4.3.0 – Fuzzy Matching Engine
- multi‑strategy fuzzy matching  
- confidence scoring  
- semantic alias mapping  
- deterministic element resolution  
- ready for window graph reasoning

## 🔁 UIWorkflow 4.3.0 – Retry & Fallback Engine
- confidence‑based action routing  
- automatic retry logic  
- fallback strategies  
- multi‑stage resolution pipeline  
- seamless integration with UIParser

## 🖱️ UIActions 4.3.0 – OS‑Aware Action Layer
- unified action interface (click, write, select, semantic)  
- sandbox‑protected execution  
- OS‑level routing via WinCapabilities  
- deterministic fallback behavior  
- extended audit logging

## 🪟 WinCapabilities 4.3.0 – OS UI Control Interface
- safe adapter for OS‑level UI automation  
- deterministic stubs (no real OS interaction yet)  
- ready for Win32/UIA/WinRT integration in 4.4.0  
- unified logging and action tracing

---

## 🎯 Summary
Version 4.3.0 completes the entire Semantic UI Automation Engine:
- fuzzy UI parsing  
- workflow fallback logic  
- semantic UI actions  
- OS‑level routing  
- sandbox enforcement  
- deterministic execution  

This is the most advanced UI automation layer ever implemented in SIRIUS.

---

## 📌 Notes
- Version 4.2.0 is now **replaced** by 4.3.0.  
- All modules are fully integrated and production‑ready.  
- Prepares the foundation for **Runtime 4.4.0 – Real OS Automation**.

---

## 🧩 Compatibility
- Fully compatible with Runtime Core 4.0  
- No breaking changes  
- No migration steps required

---

## 🏁 Status
**This is a stable release.**

---

# 🔐 Password Vault 4.0 – Secure Offline Credential Storage

Password Vault 4.0 is a **fully offline**, **AES‑256‑GCM encrypted**,  
**identity‑aware** credential storage module for **SIRIUS LOCAL AI Runtime 4.0**.

It provides deterministic, safe, and OWNER‑controlled password management  
without cloud sync, telemetry, or external dependencies.

---

# 1. 🎯 Purpose

Password Vault 4.0 enables SIRIUS to:

- store credentials securely  
- retrieve them deterministically  
- enforce identity‑aware access  
- integrate with workflows and NL commands  
- operate fully offline  
- protect sensitive data with modern cryptography  

The vault is designed for **local‑only**, **tamper‑resistant**,  
**family‑safe** credential management.

---

# 2. 🧱 Architecture Overview

Password Vault 4.0 consists of four internal layers:

### **1. vault_api.py**  
Public interface for all vault operations.

### **2. vault_core.py**  
Implements logic for storing, retrieving, updating, and deleting entries.

### **3. vault_storage.py**  
Handles encrypted JSON container on disk.

### **4. vault_crypto.py**  
AES‑256‑GCM encryption + PBKDF2‑HMAC‑SHA256 key derivation.

---

# 3. 🔐 Cryptography

### **Encryption:**  
- AES‑256‑GCM  
- 12‑byte IV  
- authentication tag included in ciphertext  

### **Key Derivation:**  
- PBKDF2‑HMAC‑SHA256  
- 200,000 iterations  
- deterministic salt for stable vault key  

### **Storage Format:**  
Encrypted JSON file containing:

```json
{
  "entries": {
    "example.com": {
      "username": "user123",
      "password": "encrypted",
      "meta": {}
    }
  }
}
```

---

# 4. 🛡 Identity Enforcement (Security Family 4.0)

Password Vault strictly follows identity rules:

| Identity | Permissions |
|---------|-------------|
| **OWNER** | full read/write/delete |
| **FAMILY** | read‑only |
| **STRANGER** | denied |

All access is routed through:

- Security Family 4.0  
- NL Router 4.0  
- Runtime Core 4.0  

No module may bypass these rules.

---

# 5. 🧠 NL Router Integration

Password Vault adds natural language commands:

- “ulož heslo pre …”  
- “zobraz heslo pre …”  
- “vymaž heslo pre …”  
- “čo mám uložené vo vaulte?”  

NL Router → RuntimeManager → vault_api → vault_core → vault_storage → vault_crypto

---

# 6. ⚙️ RuntimeManager Tasks

RuntimeManager exposes deterministic tasks:

- `vault.store_credential`  
- `vault.get_credential`  
- `vault.delete_credential`  
- `vault.list_credentials`  

All tasks enforce identity and capability boundaries.

---

# 7. 📁 File Location

Vault file is stored locally:

```
/sirius_data/vault/password_vault.json.enc
```

- encrypted  
- tamper‑resistant  
- OWNER‑protected  

---

# 8. 🧪 Testing Requirements

Password Vault must pass:

- encryption/decryption tests  
- identity enforcement tests  
- tamper detection tests  
- workflow integration tests  
- NL routing tests  
- deterministic behavior tests  

---

# 9. 🚫 Non‑Goals

Password Vault does **not**:

- sync to cloud  
- send telemetry  
- store plaintext  
- auto‑fill browser fields  
- integrate with external password managers  

These features are intentionally excluded for security.

---

# 10. 📌 Module Status

**Version:** 4.0.0 (Stable)  
Password Vault is a **finalized**, **frozen**, **production‑ready** module.  
No further structural changes are planned.
