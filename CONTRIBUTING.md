# 🤝 Contributing Guidelines – SIRIUS LOCAL AI (v5.0.0 UNIFIED)

Thank you for your interest in contributing to **SIRIUS LOCAL AI**.  
This document defines the rules, processes, and expectations for all contributors.  
The goal is to maintain a **clean, safe, modular, deterministic, and intelligent** local AI system built on the **Unified Runtime 5.0 architecture**.

All processing is fully local.  
No data leaves your device.

Version **5.0.0** expands these guidelines to include:

- the new **Unified Runtime Architecture (PC + Mobile)**  
- **UI Automation Engine 5.0**  
- **Identity Engine 3.0**  
- **SECURITY FAMILY 5.0**  
- **Schoolwork Engine 5.0**  
- **System Agent 5.0**  
- **ENVOY 5.0**  
- hardened deterministic routing  
- cross‑platform safety rules  

---

# 1. 🔐 Core Principles

- **Security has absolute priority**  
- **No action may bypass user confirmations**  
- **Modular architecture must remain clean and separated**  
- **All contributions must respect existing module APIs**  
- **No network operations or external data transmission**  
- **No hidden automation or background actions**  
- **Every change must preserve system transparency and predictability**  
- **No global mutable state**  
- **No circular imports**  
- **Deterministic, reversible behavior whenever possible**  
- **Plugin System 5.x rules must be followed**  
- **Safety‑critical modules must never be weakened or bypassed**, including:  
  - SECURITY FAMILY 5.0  
  - Identity Engine 3.0  
  - Schoolwork Engine 5.0  
  - Time‑Limits Engine v3  
  - Self‑Repair Layer 5.x  
  - **UI Automation Engine 5.0**  
  - **System Agent 5.0**  
- **Reasoning Engine 5.x must not be misused or extended unsafely**  
- **ENVOY 5.0 sanitization must never be bypassed**  

---

# 2. 🚀 How to Start

1. **Fork** the repository  
2. **Create a new branch** for your change  
3. **Implement** the change according to the Runtime 5.0 architecture  
4. **Test** it in your local environment (PC or Mobile)  
5. **Submit a Pull Request** with a clear description  

Recommended branch naming:
- feature/<name>  
- fix/<name>  
- refactor/<name>  
- docs/<name>  

---

# 3. 🧼 Code Style

All contributions must follow the project’s **STYLEGUIDE.md**.

Key rules:

- clean, readable, consistent  
- no magic constants  
- clear naming of functions and modules  
- comments explain **why**, not **what**  
- avoid unnecessary complexity  
- follow the architecture and module map  
- functions ideally 5–25 lines  
- no monolithic modules  
- no deep nesting — prefer early returns  
- imports grouped: standard → third‑party → internal  
- plugin code must follow Plugin API 5.x  
- SECURITY FAMILY 5.0 code must follow safety‑first design  
- SCHOOLWORK ENGINE 5.0 must remain intact and non‑bypassable  
- Reasoning Engine 5.x integrations must be deterministic and safe  
- Self‑Repair Layer 5.x must not be disabled or bypassed  
- **UI Automation Engine 5.0 integrations must follow deterministic fallback rules**  
- **System Agent 5.0 must validate all system‑level actions**  
- **ENVOY 5.0 must sanitize all system requests**  

---

# 4. 🧪 Testing Requirements

Every change must include:

- basic functional tests  
- verification of security constraints  
- input validation  
- error‑state testing  
- predictable behavior under invalid inputs  
- no silent failures  
- no destructive operations without confirmation  
- no reliance on network access  

If your change affects:

- **FS‑AGENT 5.x** → test path validation, safety prompts  
- **NL Router 5.x** → test semantic routing and ambiguity handling  
- **Workflow Engine 5.x** → test semantic transitions  
- **Reasoning Engine 5.x** → test deterministic reasoning behavior  
- **WIN‑CAP 5.x** → test safe fallback behavior  
- **Plugin System 5.x** → test manifest, NL commands, tasks, workflows, GUI elements  
- **UI Automation Engine 5.0** →  
  - fuzzy matching behavior  
  - fallback logic  
  - deterministic retries  
  - safe OS‑level routing  
- **SECURITY FAMILY 5.0** →  
  - identity classification (OWNER / FAMILY / STRANGER)  
  - time‑limit enforcement v3  
  - schoolwork bypass logic  
  - safe‑mode restrictions  
  - STRANGER‑mode protections  
- **Schoolwork Engine 5.0** →  
  - subject detection  
  - difficulty scoring  
  - bypass logic  
- **Self‑Repair Layer 5.x** →  
  - integrity checks  
  - fallback behavior  
- **System Agent 5.0** →  
  - validation of all system actions  
  - deterministic safety enforcement  
- **ENVOY 5.0** →  
  - sanitization  
  - identity filtering  
  - safe routing  

---

# 5. 📥 Pull Request Rules

A valid PR must include:

- clear description of the change  
- explanation of why the change is needed  
- reference to related Issues (if applicable)  
- test results or manual test notes  

Restrictions:

- no large PRs — prefer smaller, well‑structured steps  
- PRs must **not** modify the architecture without prior discussion  
- PRs must follow module boundaries  
- PRs must not introduce new dependencies without approval  
- PRs must not break determinism or safety guarantees  
- plugin PRs must include updated manifest if needed  
- PRs must not weaken SECURITY FAMILY 5.0 protections  
- PRs must not interfere with SCHOOLWORK ENGINE 5.0  
- PRs must not disable or bypass the Self‑Repair Layer  
- PRs must not misuse Reasoning Engine 5.x  
- **PRs must not compromise UI Automation Engine 5.0 safety rules**  
- **PRs must not bypass System Agent 5.0 validation**  
- **PRs must not bypass ENVOY 5.0 sanitization**  

---

# 6. ❌ What We Do Not Accept

- network‑based features  
- automatic actions without confirmation  
- bypassing security rules  
- monolithic modules  
- undocumented API changes  
- hidden background tasks  
- features that break modularity  
- unsafe filesystem or system operations  
- code that relies on OS‑specific hacks  
- contributions that reduce clarity or predictability  
- plugins that violate Plugin API 5.x  
- attempts to disable FAMILY mode, time limits, or schoolwork engine  
- attempts to weaken STRANGER‑mode protections  
- attempts to bypass Identity Engine 3.0  
- attempts to disable Self‑Repair Layer  
- unsafe Reasoning Engine extensions  
- **unsafe or non‑deterministic UI automation behavior**  
- **attempts to bypass System Agent 5.0**  
- **attempts to bypass ENVOY 5.0**  

---

# 7. 💬 Communication

All discussions take place through:

- **Issues**  
- **Pull Request comments**  

Guidelines:

- be respectful and constructive  
- provide technical reasoning  
- avoid vague or incomplete reports  
- include reproduction steps when reporting issues  

---

# 8. 🧭 Architecture Compliance

All contributions must respect:

- **ARCHITECTURE.md (v5.0.0)**  
- **MODULE_MAP.md**  
- **STYLEGUIDE.md**  
- **SECURITY.md**  
- **Plugin API 5.x**  
- **SECURITY FAMILY 5.0 design rules**  
- **Schoolwork Engine 5.0 rules**  
- **Self‑Repair Layer 5.x requirements**  
- **UI Automation Engine 5.0 specifications**  
- **System Agent 5.0 safety model**  
- **ENVOY 5.0 sanitization rules**  

Breaking architectural boundaries requires prior approval.

---

# 9. 📝 Commit Message Style

Use clear, structured commit messages:

- feat: added new workflow validation  
- fix: corrected path resolution in FS‑AGENT  
- refactor: simplified NL routing logic  
- docs: updated INSTALLATION.md  

Avoid vague messages like “update”, “fix stuff”, “changes”.

---

# 10. 🧒 Family Safety Requirements (v5.0.0)

Contributors must respect the integrity of the **SECURITY FAMILY 5.0** module:

- behavior‑based identity must remain deterministic  
- FAMILY mode must remain safe and restricted  
- time‑limits v3 must not be bypassable  
- **schoolwork must always be allowed**  
- stranger‑mode must remain locked down  
- OWNER‑level actions must remain protected  
- Identity Engine 3.0 must not be weakened  
- Schoolwork Engine 5.0 must remain intact  
- UI Automation Engine 5.0 must not perform unsafe actions  
- System Agent 5.0 must validate all system‑level actions  
- ENVOY 5.0 must sanitize all system requests  
- no PR may weaken or circumvent these protections  

Any PR affecting SECURITY FAMILY, SCHOOLWORK ENGINE, UI Automation Engine, ENVOY, or System Agent must include **explicit safety tests**.

---

# 11. 📄 License

All contributions are accepted only in accordance with the project’s **MIT License**.

---

# 📌 Document Status

Current version: **5.0.0 (Unified)**  
Updated to reflect the **4.x → 5.0 transition** and the new **Unified Runtime Architecture**.
