# 🔐 Security – SIRIUS LOCAL AI  
### v4.0.0 → 4.3.0 → **4.4.0 PRO (Expanded)**

Thank you for taking the time to help improve the security of **SIRIUS LOCAL AI**.  
This document defines the **official security policy**, **threat model**, and **reporting process** for the **Runtime 4.x architecture**.

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

# 5. 🔐 Security Architecture Summary (v4.0.0 → 4.3.0 → **4.4.0 PRO**)

SIRIUS LOCAL AI Runtime 4.x includes the full security stack, expanded in later versions (4.2.0, 4.3.0, and 4.4.0 PRO) with:

- UI‑level sandboxing  
- deterministic OS‑aware action routing  
- identity‑aware system‑level automation  
- System Agent 4.2 (NEW)  
- hardened Security Family 4.4  

---

## ✔ SECURITY FAMILY (Identity Layer)
- OWNER / FAMILY / STRANGER identity  
- offline behavior‑based recognition  
- restricted mode for children  
- safe‑mode for unknown users  
- time‑limits engine  
- Schoolwork Priority Mode  
- **Password Vault 4.0 access control**  
  - OWNER: full read/write  
  - FAMILY: read‑only  
  - STRANGER: blocked  
- identity‑aware routing enforced by Security Family  
- **Security Family 4.4 (NEW)**  
  - stronger identity gating for OS‑level actions  
  - deterministic permission evaluation  
  - SCHOOLWORK bypass logic 2.0  
  - hardened STRANGER‑mode protections  
  - integration with System Agent 4.2  

Security Family remains the **root of all identity enforcement** across Runtime 4.0 → 4.4.0 PRO.

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

# 🔐 5.2 Password Vault 4.0 — Secure Credential Storage
*(unchanged)*

Password Vault 4.0 is a **fully offline, encrypted, identity‑aware credential storage module** integrated into the Security Family.

---

# 🛡 5.3 UI Automation Security (4.2.0 → 4.3.0)
*(unchanged)*

The UI Automation Engine introduced in **4.2.0** and expanded in **4.3.0** adds a new security surface.  
All UI‑level actions are strictly sandboxed and identity‑aware.

---

# 🛡 **5.4 System Agent 4.2 – OS‑Level Security Layer (NEW in 4.4.0 PRO)**

System Agent 4.2 is the **final security gatekeeper** for all OS‑level actions introduced in Runtime 4.4.0 PRO.

### **Purpose**
To ensure that **every system‑level action** is:
- safe  
- reversible  
- identity‑validated  
- logged  
- deterministic  

### **Security Guarantees**
- no direct OS access from any module  
- no privileged operations  
- no kernel‑level calls  
- no raw Win32/UIA/WinRT access  
- all system actions must pass through System Agent  
- OWNER / FAMILY / STRANGER enforcement  
- SCHOOLWORK bypass logic preserved  
- deterministic allow/deny evaluation  

### **Threat Protections**
- blocks unsafe system operations  
- blocks destructive commands  
- blocks unverified automation  
- blocks unauthorized UI actions  
- blocks privilege escalation  
- blocks background system manipulation  
- blocks persistent hooks or injections  

### **Integration**
System Agent 4.2 mediates:
- UI Automation Engine 4.4  
- WIN‑CAP 4.4  
- Workflow Engine 4.4  
- AITE 4.4  
- Security Family 4.4  

System Agent is the **core of OS‑level safety** in Runtime 4.4.0 PRO.

---

# 🛡 **5.5 UI Automation Security (Expanded in 4.4.0 PRO)**

UI Automation Engine 4.4 introduces **real OS‑level UI control**, protected by:

### **OS‑Level Safety**
- all actions validated by System Agent  
- deterministic fallback logic  
- identity‑aware UI actions  
- sandbox‑protected execution  
- no uncontrolled input injection  
- no persistent hooks  
- no global event listeners  
- no background UI scanning  

### **WinCapabilities 4.4**
- safe adapter for Win32/UIA/WinRT  
- no direct access to raw APIs  
- deterministic routing  
- unified audit logging  

### **Workflow Safety**
- bounded retries  
- deterministic fallback  
- semantic target resolution  
- mis‑click prevention  
- identity‑aware gating  

UI Automation Engine 4.4 is **safe by design**, with no ability to perform unsafe or privileged UI actions.

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

**Version:** **4.4.0 PRO (Expanded)**  
This SECURITY.md describes the official security policy for **SIRIUS LOCAL AI Runtime 4.x**, including:

- Password Vault 4.0  
- UI Sandbox 4.2.0  
- Semantic UI Automation Security 4.3.0  
- **System Agent 4.2 (NEW)**  
- **UI Automation Engine 4.4 (NEW)**  
- **Security Family 4.4 (NEW)**  
