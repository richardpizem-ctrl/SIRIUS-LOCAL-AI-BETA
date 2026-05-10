# 🔐 SECURITY POLICY – SIRIUS LOCAL AI (v3.0.0)

This document defines the **security rules, guarantees, and responsibilities** for users and contributors of **SIRIUS LOCAL AI**.  
Version **3.0.0** introduces identity‑based protection, Schoolwork Priority Mode, and the SECURITY FAMILY module.

All processing is fully local; no data leaves the user’s PC.

---

# 1. 🛡 Core Security Principles (v3.0.0)

- **No operation may execute without explicit user confirmation.**  
- **No module may bypass safety checks.**  
- **No network communication is allowed anywhere in the system.**  
- **All filesystem operations must be validated and reversible when possible.**  
- **No hidden automation or background tasks.**  
- **No global mutable state.**  
- **All privileged actions must go through WIN‑CAP 3.0.**  
- **Plugins must follow strict capability boundaries.**  
- **SECURITY FAMILY decisions must never be bypassed or overridden.**  
- **Schoolwork must always be allowed (Schoolwork Priority Mode).**  
- **Identity‑restricted actions must be enforced deterministically.**

These principles ensure predictable, transparent, and safe behavior.

---

# 2. 🔒 Filesystem Safety Rules (FS‑AGENT 3.0)

FS‑AGENT is the **only module** allowed to perform filesystem operations.

Rules:

- destructive actions (delete, overwrite) require double confirmation  
- protected directories must be blocked  
- invalid paths must be rejected  
- no recursive operations without explicit approval  
- no automatic cleanup or background deletion  
- rollback‑safe operations must be used whenever possible  
- SCHOOLWORK files must bypass restrictions safely  
- identity‑restricted deletes must be enforced (OWNER‑only)

---

# 3. 🪟 Windows System Interaction Rules (WIN‑CAP 3.0)

All system‑level actions must:

- go through WIN‑CAP  
- validate permissions  
- respect identity level (OWNER / FAMILY / STRANGER)  
- avoid modifying system state without confirmation  
- avoid interacting with system‑critical processes  
- fail safely if access is denied  

WIN‑CAP must never:

- inject input  
- simulate keystrokes  
- modify registry keys  
- alter system configuration  
- perform privileged actions without explicit user approval  
- allow OWNER‑level actions in FAMILY or STRANGER mode  

---

# 4. 🔍 Input Validation (AITE 3.0)

All user inputs must be:

- validated  
- sanitized  
- classified by AITE  
- rejected if ambiguous or unsafe  

AITE 3.0 responsibilities:

- detect schoolwork  
- trigger Schoolwork Priority Mode  
- enforce identity‑based routing  
- block unsafe or unsupported inputs  

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

### Security Guarantees:
- identity classification must be deterministic  
- no biometric data, no external services  
- no background training loops  
- time‑limit enforcement must be constant‑time  
- schoolwork bypass must be instant and safe  
- no module may override SECURITY FAMILY decisions  

---

# 6. 🎓 Schoolwork Priority Mode (v3.0.0)

Schoolwork is **never blocked**.

This mode:

- bypasses time‑limits  
- bypasses FAMILY restrictions  
- bypasses STRANGER restrictions  
- overrides identity rules  
- ensures academic tasks always run  
- cannot be disabled by plugins or workflows  

Triggered by:

- AITE 3.0  
- SCHOOL_HELPER  
- IMAGE_ANALYZER (homework detection)  
- CONTEXT_ROUTER v3  

---

# 7. 🧪 Security Testing Requirements

Every release must include:

- filesystem safety tests  
- workflow validation tests  
- permission‑level tests  
- WIN‑CAP capability tests  
- plugin sandboxing tests  
- error‑state and fallback tests  
- **SECURITY FAMILY identity and time‑limit tests**  
- **Schoolwork Priority Mode tests**  
- **STRANGER‑mode restrictions**  
- **OWNER‑only action validation**  

Security tests must be reproducible and manual.

---

# 8. 🛠️ Self‑Repair & Health‑Check Layer (Future Module)

A future security‑critical module designed to maintain long‑term system stability.

### Responsibilities:
- integrity checks for core modules  
- detection of corrupted states, missing files, invalid configs  
- safe automatic repairs (cache reset, index rebuild, default config restore)  
- patch suggestions for code‑level fixes (manual approval required)  
- strict protection against uncontrolled source‑code modifications  
- system‑wide health reporting to Runtime Core  

### Security Guarantees:
- no automatic modification of source code  
- no self‑rewriting behavior  
- all repairs must be reversible  
- all repairs must be logged  
- all high‑risk repairs require explicit user approval  

---

# 9. 📄 Supported Versions

Only the **latest stable release** receives security updates.

| Version | Status |
|--------|--------|
| **v3.0.0** | Supported |
| v2.x.x | Critical fixes only |
| v1.x.x | Unsupported |

---

# 10. 📌 Document Status

Current version: **3.0.0 (Stable)**  
This policy evolves with new modules and capabilities.
