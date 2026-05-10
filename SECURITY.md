# 🔐 Security – SIRIUS LOCAL AI (v3.0.0)

Thank you for taking the time to help improve the security of **SIRIUS LOCAL AI**.  
This document explains **how to report vulnerabilities**, what is considered a security issue, and how the project handles security‑related disclosures.

All processing in SIRIUS LOCAL AI is fully local.  
No data leaves the user’s PC.

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
| **v3.0.0** | Supported |
| v2.x.x | Security fixes only for critical issues |
| v1.x.x | No longer supported |

---

# 3. 🔍 What Counts as a Security Issue?

You should report:

- bypassing **SECURITY FAMILY** identity rules  
- bypassing **time‑limits**  
- bypassing **Schoolwork Priority Mode**  
- unauthorized access to OWNER‑level actions  
- unsafe filesystem operations  
- privilege escalation inside WIN‑CAP  
- workflow execution that ignores safety boundaries  
- plugin sandbox escape  
- unintended destructive actions  
- any behavior that violates deterministic execution guarantees  

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

# 5. 🔐 Security Architecture Summary (v3.0.0)

SIRIUS LOCAL AI includes:

### ✔ SECURITY FAMILY  
- OWNER / FAMILY / STRANGER identity  
- offline behavior‑based recognition  
- restricted mode for children  
- safe‑mode for unknown users  
- time‑limits engine  
- Schoolwork Priority Mode  

### ✔ Runtime Safety  
- deterministic execution  
- no network communication  
- no telemetry  
- no hidden background tasks  
- capability‑based access to Windows APIs  

### ✔ Filesystem Safety  
- rollback‑safe operations  
- path validation  
- identity‑restricted deletes  

### ✔ Workflow Safety  
- validated transitions  
- blocked unsafe sequences  

---

# 🌐 5.1 SIRIUS ENVOY 4.0 — Internet Isolation & Quarantine Model  
*(Introduced for SIRIUS 4.0 architecture)*

Although SIRIUS LOCAL AI is fully offline, future versions introduce an **optional, isolated online retrieval agent** called **SIRIUS ENVOY 4.0**.

ENVOY allows safe, controlled retrieval of external information **without exposing the local AI runtime to the internet**.

### **Core Security Guarantees**
- Local AI remains **100% offline**  
- ENVOY is a **separate process** with no access to local memory  
- All retrieved data passes through a **quarantine sandbox**  
- Only sanitized, validated, text‑only data is delivered to SIRIUS  
- No scripts, HTML, binaries, or active content are ever allowed  

### **ENVOY Security Pipeline**
1. **Outbound‑Only Envoy Client**  
   - performs external requests  
   - cannot receive commands from outside  
   - cannot access local AI internals  

2. **Scraper Layer**  
   - extracts text  
   - removes scripts, trackers, active content  

3. **Quarantine Sandbox**  
   - isolates all incoming data  
   - checks for unsafe patterns  
   - strips unknown formats  

4. **Validator & Policy Filter**  
   - enforces domain rules  
   - marks uncertainty  
   - blocks unsafe or unverifiable content  

5. **Safe Payload Delivery**  
   - only clean, structured, offline‑safe text is passed to SIRIUS  

### **Security Purpose**
ENVOY exists to support:

- health information lookups  
- educational content  
- definitions and factual data  
- dynamic updates for Knowledge Packs  

ENVOY **never** sends local data outward and **never** interacts directly with the runtime core.

---

# 6. 🕒 Response Time

You can expect:

- **Acknowledgment:** within 72 hours  
- **Initial assessment:** within 7 days  
- **Fix or mitigation:** depending on severity  

Critical issues are handled with priority.

---

# 7. 🤝 Responsible Disclosure

Please:

- report issues privately  
- allow time for a fix before public disclosure  
- avoid exploiting vulnerabilities  
- avoid sharing proof‑of‑concepts publicly  

---

# 8. 📄 Document Status

**Version:** 3.0.0 (Stable)  
This SECURITY.md describes the official security reporting process for SIRIUS LOCAL AI.
