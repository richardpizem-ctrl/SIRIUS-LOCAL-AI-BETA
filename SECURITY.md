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

If you discover a security vulnerability, please report it **privately**.

### 📬 Contact (Private Disclosure Only)
**Email:** richardpizem@gmail.com  
**Subject:** `[SECURITY] Vulnerability Report`

Please include:

- clear description of the issue  
- steps to reproduce  
- affected modules (if known)  
- potential impact  
- suggested fix (optional)  

**Do NOT open a public GitHub Issue** for security vulnerabilities.

---

# 2. 🛡 Supported Versions

Only the latest stable version receives security updates.

| Version | Status |
|--------|--------|
| **v4.0.0** | Supported |
| v3.x.x | Security fixes only for critical issues |
| v2.x.x | No longer supported |

---

# 3. 🔍 What Counts as a Security Issue?

You should report:

### **Identity & Access Control**
- bypassing **SECURITY FAMILY** identity rules  
- bypassing **time‑limits**  
- bypassing **Schoolwork Priority Mode**  
- unauthorized access to OWNER‑level actions  

### **Runtime 4.0 Core**
- unsafe scheduler execution  
- priority escalation  
- bypassing safe‑mode restrictions  
- dependency graph corruption  
- module loader accepting invalid or malicious modules  

### **Sandbox 4.0**
- sandbox escape  
- unauthorized capability access  
- execution of unsafe or unvalidated tasks  
- context poisoning  

### **ENVOY 4.0**
- quarantine bypass  
- unsafe payload accepted as valid  
- malformed or active content passing through validator  

### **Filesystem & Automation**
- unsafe filesystem operations  
- identity‑restricted deletes bypass  
- unintended destructive actions  

### **Determinism & Isolation**
- any behavior that violates deterministic execution guarantees  
- hidden background tasks  
- unauthorized network communication  

---

# 4. ❌ What Is *Not* a Security Issue?

- missing features  
- UI bugs  
- plugin errors  
- workflow misconfigurations  
- performance issues  
- documentation mistakes  
- STRANGER‑mode restrictions working as intended  
- SCHOOLWORK bypassing restrictions (this is expected behavior)  

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

---

## ✔ RuntimeCore 4.0 (Deterministic Engine)
- deterministic execution  
- no network communication  
- no telemetry  
- no hidden background tasks  
- capability‑based access to Windows APIs  
- strict type validation  
- defense‑in‑depth checks  

---

## ✔ Scheduler 4.0 (Task Safety)
- priority validation  
- queue overflow protection  
- safe‑mode enforcement  
- schoolwork priority bypass rules  
- context validation  
- no dynamic execution  

---

## ✔ Sandbox 4.0 (Execution Isolation)
- isolated execution envelopes  
- capability‑restricted tasks  
- context validation  
- no dynamic imports  
- no eval/exec  
- no remote code  

---

## ✔ DependencyGraph 4.0
- cycle detection  
- module integrity validation  
- safe topological ordering  
- strict naming rules  

---

## ✔ ModuleLoader 4.0
- safe registration  
- safe initialization  
- module count limits  
- strict type validation  

---

## ✔ Filesystem Safety
- rollback‑safe operations  
- path validation  
- identity‑restricted deletes  

---

# 🌐 5.1 SIRIUS ENVOY 4.0 — Internet Isolation & Quarantine Model

Although SIRIUS LOCAL AI is fully offline, ENVOY 4.0 provides an **optional**, **isolated**, **one‑way retrieval agent** for external information.

### **Core Security Guarantees**
- Local AI remains **100% offline**  
- ENVOY is a **separate process**  
- No access to local memory  
- All data passes through **quarantine**  
- Only sanitized, validated, text‑only data is delivered  
- No scripts, HTML, binaries, or active content  

### **ENVOY Security Pipeline**
1. **Outbound‑Only Envoy Client**  
2. **Scraper Layer**  
3. **Quarantine Sandbox**  
4. **Validator & Policy Filter**  
5. **Safe Payload Delivery**  

### **Purpose**
- educational content  
- definitions  
- factual data  
- dynamic updates for Knowledge Packs  

ENVOY **never** sends local data outward.

---

# 6. 🧪 Diagnostics & Self‑Repair Hooks (Runtime 4.0)

Runtime 4.0 includes internal diagnostic points:

- graph integrity checks  
- module initialization verification  
- sandbox context validation  
- scheduler queue health checks  
- state consistency checks  

These hooks do not send data anywhere — all diagnostics are local.

---

# 7. 🕒 Response Time

You can expect:

- **Acknowledgment:** within 72 hours  
- **Initial assessment:** within 7 days  
- **Fix or mitigation:** depending on severity  

Critical issues are handled with priority.

---

# 8. 🤝 Responsible Disclosure

Please:

- report issues privately  
- allow time for a fix before public disclosure  
- avoid exploiting vulnerabilities  
- avoid sharing proof‑of‑concepts publicly  

---

# 9. 📄 Document Status

**Version:** 4.0.0 (Stable)  
This SECURITY.md describes the official security policy for **SIRIUS LOCAL AI Runtime 4.0**.
