# 🤝 Contributing Guidelines – SIRIUS LOCAL AI (v4.5.0 EXPANDED)

Thank you for your interest in contributing to **SIRIUS LOCAL AI**.  
This document defines the rules, processes, and expectations for all contributors.  
The goal is to maintain a **clean, safe, modular, deterministic, and intelligent** local AI system built on the **Runtime 4.x architecture**.

All processing is fully local.  
No data leaves your PC.

Version **4.5.0** expands these guidelines to include the new **UI Automation Engine 4.5**, the transition from **4.4 → 4.5 PRO**, upgraded safety‑critical modules, and hardened deterministic routing.

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
- **Plugin System 4.x rules must be followed**  
- **Safety‑critical modules must never be weakened or bypassed**, including:  
  - SECURITY FAMILY 4.5  
  - Identity Engine 2.1  
  - Schoolwork Engine 4.5  
  - Time‑Limits Engine v2  
  - Self‑Repair & Health‑Check Layer  
  - **UI Automation Engine 4.5 (UPDATED)**  
- **Reasoning Engine 4.x must not be misused or extended unsafely**  
- **System Agent 4.5 must remain the final gatekeeper for all system actions**  

---

# 2. 🚀 How to Start

1. **Fork** the repository  
2. **Create a new branch** for your change  
3. **Implement** the change according to the Runtime 4.x architecture  
4. **Test** it in your local environment  
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
- plugin code must follow Plugin API 4.x  
- SECURITY FAMILY 4.5 code must follow safety‑first design  
- SCHOOLWORK ENGINE 4.5 must remain intact and non‑bypassable  
- Reasoning Engine 4.x integrations must be deterministic and safe  
- Self‑Repair Layer must not be disabled or bypassed  
- **UI Automation Engine 4.5 integrations must follow deterministic fallback rules**  
- **System Agent 4.5 must validate all system‑level actions**  

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

- **FS‑AGENT 4.x** → test path validation, safety prompts  
- **NL Router 4.x** → test semantic routing and ambiguity handling  
- **Workflow Engine 4.x** → test semantic transitions  
- **Reasoning Engine 4.x** → test deterministic reasoning behavior  
- **WIN‑CAP 4.x** → test safe fallback behavior  
- **Plugin System 4.x** → test manifest, NL commands, tasks, workflows, GUI elements  
- **UI Automation Engine 4.5** →  
  - fuzzy matching behavior  
  - fallback logic  
  - deterministic retries  
  - safe OS‑level routing  
- **SECURITY FAMILY 4.5** →  
  - identity classification (OWNER / FAMILY / STRANGER)  
  - time‑limit enforcement v2  
  - schoolwork bypass logic  
  - safe‑mode restrictions  
  - STRANGER‑mode protections  
- **Schoolwork Engine 4.5** →  
  - subject detection  
  - difficulty scoring  
  - bypass logic  
- **Self‑Repair Layer** →  
  - integrity checks  
  - fallback behavior  
- **System Agent 4.5** →  
  - validation of all system actions  
  - deterministic safety enforcement  

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
- PRs must not weaken SECURITY FAMILY 4.5 protections  
- PRs must not interfere with SCHOOLWORK ENGINE 4.5  
- PRs must not disable or bypass the Self‑Repair Layer  
- PRs must not misuse Reasoning Engine 4.x  
- **PRs must not compromise UI Automation Engine 4.5 safety rules**  
- **PRs must not bypass System Agent 4.5 validation**  

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
- plugins that violate Plugin API 4.x  
- attempts to disable FAMILY mode, time limits, or schoolwork engine  
- attempts to weaken STRANGER‑mode protections  
- attempts to bypass Identity Engine 2.1  
- attempts to disable Self‑Repair Layer  
- unsafe Reasoning Engine extensions  
- **unsafe or non‑deterministic UI automation behavior**  
- **attempts to bypass System Agent 4.5**  

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

- **ARCHITECTURE.md (v4.5.0)**  
- **MODULE_MAP.md**  
- **STYLEGUIDE.md**  
- **SECURITY.md**  
- **Plugin API 4.x**  
- **SECURITY FAMILY 4.5 design rules**  
- **Schoolwork Engine 4.5 rules**  
- **Self‑Repair Layer requirements**  
- **UI Automation Engine 4.5 specifications**  
- **System Agent 4.5 safety model**  

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

# 10. 🧒 Family Safety Requirements (v4.5.0)

Contributors must respect the integrity of the **SECURITY FAMILY 4.5** module:

- behavior‑based identity must remain deterministic  
- FAMILY mode must remain safe and restricted  
- time‑limits v2 must not be bypassable  
- **schoolwork must always be allowed**  
- stranger‑mode must remain locked down  
- OWNER‑level actions must remain protected  
- Identity Engine 2.1 must not be weakened  
- Schoolwork Engine 4.5 must remain intact  
- UI Automation Engine 4.5 must not perform unsafe actions  
- System Agent 4.5 must validate all system‑level actions  
- no PR may weaken or circumvent these protections  

Any PR affecting SECURITY FAMILY, SCHOOLWORK ENGINE, UI Automation Engine, or System Agent must include **explicit safety tests**.

---

# 11. 📄 License

All contributions are accepted only in accordance with the project’s **MIT License**.

---

# 📌 Document Status

Current version: **4.5.0 (Expanded)**  
Updated to reflect the **4.4 → 4.5 transition** and the new **UI Automation Engine 4.5**.
