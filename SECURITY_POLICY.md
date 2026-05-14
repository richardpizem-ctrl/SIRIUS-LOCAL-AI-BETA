# 🔐 SECURITY POLICY – SIRIUS LOCAL AI (v3.0.0)

This document defines the **security rules, guarantees, and responsibilities** for users and contributors of **SIRIUS LOCAL AI**.  
Version **3.0.0** introduces identity‑based protection, Schoolwork Priority Mode, and the SECURITY FAMILY module.

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
- **Password Vault 4.0 access enforcement** ← *NEW*  
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

# 10. 📄 Supported Versions
(unchanged)

---

# 11. 📌 Document Status

Current version: **3.0.0 (Stable)**  
This policy evolves with new modules and capabilities, including the new **Password Vault 4.0**.
