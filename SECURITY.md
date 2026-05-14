# 🔐 Security – SIRIUS LOCAL AI (v4.0.0)

Thank you for taking the time to help improve the security of **SIRIUS LOCAL AI**.  
This document defines the **official security policy**, **threat model**, and **reporting process** for the **Runtime 4.0 architecture**.

All processing in SIRIUS LOCAL AI is fully local.  
No data leaves the user’s PC.  
No telemetry.  
No cloud.  
No remote execution.

---

# 1. 📢 Reporting a Security Issue
(unchanged)

---

# 2. 🛡 Supported Versions
(unchanged)

---

# 3. 🔍 What Counts as a Security Issue?
(unchanged)

---

# 4. ❌ What Is *Not* a Security Issue?
(unchanged)

---

# 5. 🔐 Security Architecture Summary (v4.0.0)

SIRIUS LOCAL AI Runtime 4.0 includes:

---

## ✔ SECURITY FAMILY (Identity Layer)
- OWNER / FAMILY / STRANGER identity  
- offline behavior‑based recognition  
- restricted mode for children  
- safe‑mode for unknown users  
- time‑limits engine  
- Schoolwork Priority Mode  
- **Password Vault 4.0 access control** ← *NEW*  
  - OWNER: full read/write  
  - FAMILY: read‑only  
  - STRANGER: blocked  
  - identity‑aware routing enforced by Security Family  

---

## ✔ RuntimeCore 4.0 (Deterministic Engine)
(unchanged)

---

## ✔ Scheduler 4.0 (Task Safety)
(unchanged)

---

## ✔ Sandbox 4.0 (Execution Isolation)
(unchanged)

---

## ✔ DependencyGraph 4.0
(unchanged)

---

## ✔ ModuleLoader 4.0
(unchanged)

---

## ✔ Filesystem Safety
(unchanged)

---

# 🔐 5.2 Password Vault 4.0 — Secure Credential Storage (NEW)

Password Vault 4.0 is a **fully offline, encrypted, identity‑aware credential storage module** integrated into the Security Family.

### **Security Guarantees**
- AES‑256‑GCM encryption  
- PBKDF2‑HMAC‑SHA256 master key derivation  
- encrypted JSON container  
- no plaintext storage  
- no cloud sync  
- no telemetry  
- deterministic behavior  

### **Identity Enforcement**
- OWNER → full access (read/write/delete)  
- FAMILY → read‑only  
- STRANGER → denied  
- all access routed through Security Family 4.0  
- NL Router + RuntimeCore enforce identity rules  

### **Threat Protections**
- tamper‑resistant encrypted container  
- no direct filesystem access (FS‑AGENT only)  
- no direct crypto access (vault_crypto only)  
- no remote execution  
- no dynamic imports  
- no unsafe code paths  

---

# 🌐 5.1 SIRIUS ENVOY 4.0 — Internet Isolation & Quarantine Model
(unchanged)

---

# 6. 🧪 Diagnostics & Self‑Repair Hooks (Runtime 4.0)
(unchanged)

---

# 7. 🕒 Response Time
(unchanged)

---

# 8. 🤝 Responsible Disclosure
(unchanged)

---

# 9. 📄 Document Status

**Version:** 4.0.0 (Stable)  
This SECURITY.md describes the official security policy for **SIRIUS LOCAL AI Runtime 4.0**, including the new **Password Vault 4.0** module.
