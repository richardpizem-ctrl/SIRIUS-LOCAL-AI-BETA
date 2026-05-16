# 🎨 STYLEGUIDE – SIRIUS LOCAL AI (v3.0.0 → 4.3.0 EXPANDED)

This document defines the unified code style, naming conventions, module structure, and cleanliness rules for the SIRIUS LOCAL AI project.  
Originally written for Runtime 3.0.0, it is now expanded to include the new architectural rules introduced in **Runtime 4.0.0**, **UI Automation Engine 4.2.0**, and **Semantic UI Automation Engine 4.3.0**.

All processing is fully local; no data leaves the user’s PC.

---

# 1. Core Principles

- code must be clean, readable, and modular  
- no monolithic functions or modules  
- no magic constants — everything must be named  
- no hidden side effects  
- every module must follow SRP (Single Responsibility Principle)  
- security always has priority over convenience  
- predictable, transparent behavior  
- consistent structure across all modules  
- minimal cognitive load for future maintainers  
- plugin code must follow Plugin API 3.0  
- **safety‑critical modules (SECURITY FAMILY) must follow strict isolation rules**  
- **no code may weaken time‑limits or Schoolwork Priority Mode**  
- **identity‑restricted logic must be deterministic and constant‑time**  
- **UI Automation Engine (4.2–4.3) must follow deterministic, sandbox‑safe execution rules** ← *NEW*  
- **semantic UI actions must never bypass identity or sandbox rules** ← *NEW*  

---

# 2. Naming Conventions

## Variables
- `lower_snake_case`
- short but descriptive
- no meaningless abbreviations

**Examples:**  
`target_path`, `pending_action`, `user_confirmation_required`

## Functions
- `lower_snake_case`
- name must express an action
- verbs first, nouns second

**Examples:**  
`resolve_target_folder()`, `validate_path()`, `generate_confirmation_dialog()`, `load_context_state()`

## Classes / Modules
- `PascalCase`
- name = responsibility of the module

**Examples:**  
`FilesystemAgent`, `NaturalLanguageRouter`, `ContextMemoryEngine`, `WorkflowEngine`,  
`SecurityFamily`, `TimeLimitsEngine`, `SchoolworkDetector`,  
`HomeAssistant`, `CookingAdvisor`, `DeviceDiagnostics`, `SchoolHelper`, `ImageAnalyzer`

### NEW (4.2–4.3)
UI Automation Engine modules must follow strict naming:

- `UIGraph`  
- `UIParser`  
- `UIActions`  
- `UISandbox`  
- `UIWorkflow`  
- `WinCapabilities`  

These names are **reserved** and must not be repurposed.

## Constants
- `UPPER_SNAKE_CASE`
- must be descriptive

**Examples:**  
`MAX_RETRY_COUNT`, `DEFAULT_TIMEOUT_MS`, `CHILD_TIME_LIMIT_MINUTES`

---

# 3. File & Folder Structure

```
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
/ui_automation        ← NEW (4.2.0)
/ui_automation/os     ← NEW (4.3.0)
```

Each module has its own folder:

- `__init__.py`
- main module file
- helper utilities (if needed)

### Rules:
- no cross‑module imports except through public interfaces  
- Runtime Core is the only module allowed to initialize others  
- no circular imports  
- no global mutable state  
- **SECURITY FAMILY must remain isolated from all other modules except Runtime Core, AITE, and WIN‑CAP**  
- **SchoolworkDetector may not access filesystem or OS directly**  
- **UI Automation Engine must remain isolated from SECURITY FAMILY except for identity checks** ← *NEW*  
- **UIActions may only call OS functions through WinCapabilities** ← *NEW*  

---

# 4. Function Length

- ideal length: **5–25 lines**  
- maximum: **50 lines**  
- if a function grows too large, split it  
- avoid deeply nested logic  
- prefer early returns over complex branching  

### NEW (4.3.0)
- fuzzy matching logic must be split into **strategy functions**  
- fallback logic must be split into **deterministic stages**  
- UI actions must not contain OS‑specific code directly  

---

# 5. Comments

- comments explain **why**, not **what**  
- document non‑obvious decisions  
- document all SECURITY FAMILY logic clearly  
- document SCHOOLWORK PRIORITY MODE triggers  
- document UI Sandbox rules (4.2.0) ← *NEW*  
- document fallback logic (4.3.0) ← *NEW*  
- document fuzzy matching thresholds (4.3.0) ← *NEW*  

---

# 6. Error Messages

- clear, concise, informative  
- must include a reason + recommendation  
- avoid unnecessary technical jargon  

**Example:**  
`"Invalid path: target directory does not exist. Please choose a valid location."`

### NEW (4.3.0)
UI Automation Engine errors must follow:

- `"UI target not found – confidence too low."`  
- `"UI action blocked by sandbox policy."`  
- `"OS‑level action requires OWNER identity."`  

---

# 7. Security Rules in Code

- no operation may bypass user confirmation  
- all file operations must be validated  
- no direct deletion without double confirmation  
- no network operations in any module  
- no hidden background tasks  
- no automatic actions without explicit approval  
- no implicit state sharing  
- all privileged operations must go through WIN‑CAP 3.0  
- plugins must follow capability boundaries  
- **SECURITY FAMILY rules must never be bypassed**  
- **time‑limits must be enforced deterministically**  
- **Schoolwork Priority Mode must always override restrictions**  
- **STRANGER‑mode must block privileged actions**  

### NEW (4.2–4.3)
- UI actions must always pass through `UISandbox`  
- OS‑level UI actions must always pass through `WinCapabilities`  
- fuzzy matching must never auto‑execute without confidence threshold  
- fallback logic must be deterministic and bounded  
- UI workflows must never loop indefinitely  
- no direct Win32/UIA calls allowed  

---

# 8. Testing Requirements

Every module must include:

- basic tests  
- error‑state tests  
- security‑constraint tests  
- input‑validation tests  
- predictable behavior tests  
- no reliance on external network or cloud  
- **SECURITY FAMILY tests (identity, time‑limits, schoolwork detection)**  
- **Schoolwork Priority Mode tests**  
- **STRANGER‑mode restriction tests**  

### NEW (4.2–4.3)
UI Automation Engine must include:

- fuzzy matching tests  
- confidence threshold tests  
- fallback logic tests  
- sandbox enforcement tests  
- OS‑routing tests  
- deterministic workflow tests  

---

# 9. Logging Rules

- concise and technical  
- no sensitive data  
- format: `[MODULE] action – status`

**Example:**  
`[FS-AGENT] move_file – confirmed`

### SECURITY FAMILY logging rules:
- never log identity profiles  
- never log behavior patterns  
- never log child usage data  
- only log high‑level events  

### NEW (4.3.0)
UI Automation logging rules:
- never log raw UI element text  
- never log OS‑level handles  
- log only semantic actions  
- log confidence scores only when safe  

---

# 10. Formatting Rules

- indentation: **4 spaces**  
- max line width: **100 characters**  
- blank line between logical blocks  
- no trailing spaces  
- consistent import ordering  

---

# 11. Module Boundaries

- modules may not access each other's internals  
- communication must go through public interfaces  
- Runtime Core is the only module allowed to orchestrate all others  
- no circular imports  
- no global mutable state  
- plugins must remain isolated and follow Plugin API 3.0  
- **SECURITY FAMILY may only communicate with Runtime Core, AITE, and WIN‑CAP**  
- **SchoolworkDetector may not access filesystem or OS directly**  
- **household modules (v3) must remain sandboxed**  
- **UI Automation Engine must remain isolated from OS except via WinCapabilities** ← *NEW*  
- **UIParser may not access UIActions directly** ← *NEW*  

---

# Document Status

Current version: **3.0.0 (Expanded to include 4.2.0 and 4.3.0 rules)**  
This styleguide evolves with new modules and capabilities.
