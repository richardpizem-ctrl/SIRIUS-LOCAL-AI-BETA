# 🎨 STYLEGUIDE – SIRIUS LOCAL AI  
### v3.0.0 → 4.3.0 → **4.4.0 PRO (Expanded)**

This document defines the unified code style, naming conventions, module structure, and cleanliness rules for the SIRIUS LOCAL AI project.  
Originally written for Runtime 3.0.0, it is now expanded to include the new architectural rules introduced in:

- **Runtime 4.0.0**  
- **UI Automation Engine 4.2.0**  
- **Semantic UI Automation Engine 4.3.0**  
- **Deterministic OS Automation 4.4.0 PRO (NEW)**  

All processing is fully local; no data leaves the user’s PC.

---

# 1. Core Principles

*(unchanged, plus new 4.4.0 rules)*

- code must be clean, readable, modular  
- no monolithic functions  
- no magic constants  
- no hidden side effects  
- SRP everywhere  
- security > convenience  
- predictable behavior  
- consistent structure  
- minimal cognitive load  
- Plugin API 3.0 compliance  
- **SECURITY FAMILY isolation rules**  
- **identity‑restricted logic must be deterministic and constant‑time**  
- **UI Automation Engine (4.2–4.3) must follow deterministic, sandbox‑safe execution**  
- **semantic UI actions must never bypass identity or sandbox rules**  
- **System Agent 4.2 must validate all OS‑level actions** ← *NEW (4.4.0)*  
- **OS‑level automation must be reversible and identity‑aware** ← *NEW (4.4.0)*  
- **no module may call OS APIs directly — only through WinCapabilities 4.4** ← *NEW (4.4.0)*  

---

# 2. Naming Conventions

*(unchanged + new 4.4.0 modules)*

## Variables
- `lower_snake_case`

## Functions
- `lower_snake_case`

## Classes / Modules
- `PascalCase`

### Reserved Names (4.2–4.3)
- `UIGraph`, `UIParser`, `UIActions`, `UISandbox`, `UIWorkflow`, `WinCapabilities`

### NEW Reserved Names (4.4.0 PRO)
- `SystemAgent`  
- `OSActionValidator`  
- `OSRoutingContext`  
- `DeterministicFallbackEngine`  
- `IdentityGatekeeper`  

These names are **reserved** and must not be repurposed.

## Constants
- `UPPER_SNAKE_CASE`

---

# 3. File & Folder Structure

*(unchanged + new 4.4.0 folders)*
/runtime
/filesystem
/commands
/context
/workflow
/ui
/email
/ui_components
/ui_components/animations
/plugins
/security_family
/home_assistant
/cooking_advisor
/device_diagnostics
/school_helper
/image_analyzer
/context_router
/ui_automation
/ui_automation/os
/system_agent              ← NEW (4.4.0)
/os_routing                ← NEW (4.4.0)
/os_validation             ← NEW (4.4.0)

### NEW Rules (4.4.0 PRO)
- **System Agent must be isolated from all modules except Runtime Core, Security Family, and WinCapabilities**  
- **UI Automation Engine may not call OS APIs directly — only through WinCapabilities 4.4**  
- **OS‑level modules must never bypass identity checks**  
- **Workflow Engine 4.4 must route system workflows through System Agent**  

---

# 4. Function Length

*(unchanged + new 4.4.0 rules)*

### NEW (4.4.0 PRO)
- OS‑level validation must be split into:
  - `precheck_identity()`
  - `precheck_safety()`
  - `execute_action()`
  - `postcheck_reversibility()`

- no OS‑level function may exceed **40 lines**  
- fallback logic must be deterministic and staged  

---

# 5. Comments

*(unchanged + new 4.4.0 rules)*

### NEW (4.4.0 PRO)
Comments must document:

- System Agent validation steps  
- OS‑level safety rules  
- identity gating logic  
- reversibility guarantees  
- deterministic fallback stages  

---

# 6. Error Messages

*(unchanged + new 4.4.0 rules)*

### NEW (4.4.0 PRO)
OS‑level errors must follow:

- `"OS action blocked by System Agent – insufficient identity level."`  
- `"OS operation rejected – reversibility not guaranteed."`  
- `"Unsafe system action – requires OWNER identity."`  
- `"OS routing failed – capability boundary exceeded."`  

---

# 7. Security Rules in Code

*(unchanged + new 4.4.0 rules)*

### NEW (4.4.0 PRO)
- all OS‑level actions must pass through `SystemAgent`  
- no direct Win32/UIA/WinRT calls  
- no privileged operations  
- no kernel‑level access  
- no bypass of identity gating  
- no bypass of reversibility checks  
- no implicit OS state modification  
- no persistent hooks or listeners  
- no background OS manipulation  

---

# 8. Testing Requirements

*(unchanged + new 4.4.0 rules)*

### NEW (4.4.0 PRO)
System Agent tests must include:

- identity gating tests  
- reversibility tests  
- OS safety boundary tests  
- capability boundary tests  
- deterministic fallback tests  
- workflow → system routing tests  

UI Automation 4.4 tests must include:

- OS routing tests  
- WinCapabilities integration tests  
- mis‑click prevention tests  
- identity‑aware UI action tests  

---

# 9. Logging Rules

*(unchanged + new 4.4.0 rules)*

### NEW (4.4.0 PRO)
System Agent logging:

- never log OS handles  
- never log sensitive system paths  
- log only semantic actions  
- log identity level only as category (OWNER/FAMILY/STRANGER)  
- log reversibility status  

---

# 10. Formatting Rules
(unchanged)

---

# 11. Module Boundaries

*(unchanged + new 4.4.0 rules)*

### NEW (4.4.0 PRO)
- **System Agent is the ONLY module allowed to validate OS‑level actions**  
- **WinCapabilities 4.4 is the ONLY module allowed to touch OS APIs**  
- **UI Automation Engine 4.4 must route all OS actions through System Agent**  
- **Workflow Engine 4.4 must not execute OS actions directly**  
- **Security Family 4.4 must be consulted before any OS‑level action**  

---

# Document Status

**Version:** 3.0.0 (Expanded to include 4.2.0, 4.3.0, and **4.4.0 PRO**)  
This styleguide evolves with new modules and capabilities.
