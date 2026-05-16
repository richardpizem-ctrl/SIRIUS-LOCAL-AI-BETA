# 🔐 SECURITY POLICY – SIRIUS LOCAL AI (v3.0.0 → 4.3.0 EXPANDED)

This document defines the **security rules, guarantees, and responsibilities** for users and contributors of **SIRIUS LOCAL AI**.  
Version **3.0.0** introduced identity‑based protection, Schoolwork Priority Mode, and the SECURITY FAMILY module.  
Versions **4.2.0 and 4.3.0** expand the security model with **UI Sandbox**, **semantic UI safety**, and **OS‑aware action isolation**.

All processing is fully local; no data leaves the user’s PC.

---

# 1. 🛡 Core Security Principles (v3.0.0)
(unchanged)

---

# 2. 🔒 Filesystem Safety Rules (FS‑AGENT 3.0)
(unchanged)

---

# 3. 🪟 Windows System Interaction Rules (WIN‑CAP 3.0)
(unchanged)

---

# 4. 🔍 Input Validation (AITE 3.0)
(unchanged)

---

# 5. 🧠 SECURITY FAMILY (Core Module – v3.0.0)

The SECURITY FAMILY module provides **identity‑based safety**.

### Identity Levels:
- **OWNER** — full access  
- **FAMILY** — restricted mode  
- **STRANGER** — safe‑mode  

### Responsibilities:
- behavior‑based identity recognition  
- offline learning (no biometrics, no cloud)  
- restricted mode for children  
- safe‑mode for unknown users  
- protection of sensitive operations  
- integration with NL Router, AITE, FS‑AGENT, WIN‑CAP  
- **time‑based limits for children**  
- **Schoolwork Priority Mode (schoolwork always allowed)**  
- **Password Vault 4.0 access enforcement**  
  - OWNER: full read/write/delete  
  - FAMILY: read‑only  
  - STRANGER: blocked  

### Security Guarantees:
- identity classification must be deterministic  
- no biometric data, no external services  
- no background training loops  
- time‑limit enforcement must be constant‑time  
- schoolwork bypass must be instant and safe  
- no module may override SECURITY FAMILY decisions  

---

# 6. 🔐 Password Vault 4.0 – Secure Credential Storage (NEW)

Password Vault 4.0 is a **fully offline, encrypted, identity‑aware credential storage module** integrated into the SECURITY FAMILY.

### Security Guarantees:
- AES‑256‑GCM encryption  
- PBKDF2‑HMAC‑SHA256 master key derivation  
- encrypted JSON container  
- no plaintext storage  
- no cloud sync  
- no telemetry  
- deterministic behavior  

### Identity Enforcement:
- OWNER → full access (read/write/delete)  
- FAMILY → read‑only  
- STRANGER → denied  
- all access routed through SECURITY FAMILY  
- NL Router + RuntimeCore enforce identity rules  

### Threat Protections:
- tamper‑resistant encrypted container  
- no direct filesystem access (FS‑AGENT only)  
- no direct crypto access (vault_crypto only)  
- no remote execution  
- no dynamic imports  
- no unsafe code paths  

---

# 7. 🎓 Schoolwork Priority Mode (v3.0.0)
(unchanged)

---

# 8. 🧪 Security Testing Requirements
(unchanged)

---

# 9. 🛠️ Self‑Repair & Health‑Check Layer (Future Module)
(unchanged)

---

# 10. 🛡 NEW SECURITY SURFACE (v4.2.0 → v4.3.0)

Versions **4.2.0 and 4.3.0** introduce the **UI Automation Engine**, which adds a new security layer.  
All UI‑level actions are strictly sandboxed, identity‑aware, and deterministic.

---

## 🔐 10.1 UI Sandbox Security (v4.2.0)

The UI Sandbox enforces identity‑based restrictions for all UI automation tasks.

### Guarantees:
- OWNER / FAMILY / STRANGER / CHILD permission model  
- deterministic allow/deny rules  
- no direct OS UI access  
- no elevated privileges  
- no kernel‑level operations  
- local audit trail for every UI action  

### Threat Protections:
- prevents uncontrolled UI interaction  
- blocks unsafe click/write/select operations  
- prevents UI automation from bypassing SECURITY FAMILY  
- no persistent hooks or global listeners  

---

## 🔐 10.2 Semantic UI Automation Security (v4.3.0)

Version 4.3.0 introduces **semantic UI safety**, ensuring that UI actions are predictable and safe.

### UIParser 4.3.0 (Fuzzy Matching Engine)
- prevents mis‑clicks via confidence scoring  
- semantic alias mapping avoids ambiguous targets  
- deterministic element resolution  

### UIWorkflow 4.3.0 (Retry & Fallback Engine)
- bounded retry logic  
- deterministic fallback behavior  
- no infinite loops  
- no uncontrolled UI sequences  

### UIActions 4.3.0 (OS‑Aware Action Layer)
- routed through WinCapabilities (safe adapter)  
- sandbox‑protected execution  
- extended audit logging  
- no raw Win32/UIA calls  

### WinCapabilities 4.3.0
- safe OS UI control interface  
- deterministic stubs (no real OS interaction yet)  
- unified logging and tracing  

---

## 🔐 10.3 Threat Protections Added in 4.2–4.3

- no direct access to OS automation APIs  
- no uncontrolled input injection  
- no background UI scanning  
- no persistent system hooks  
- no global keyboard/mouse listeners  
- no elevated or privileged UI operations  
- all UI actions must pass identity checks  
- all UI actions must pass sandbox rules  
- all UI actions must be logged  

---

# 11. 📄 Document Status

**Version:** 3.0.0 (Expanded with 4.2.0–4.3.0 security layers)  
This policy now includes the new **Password Vault 4.0**, **UI Sandbox 4.2.0**, and **Semantic UI Automation Security 4.3.0**.
