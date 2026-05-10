# 🏗 Architecture – SIRIUS LOCAL AI (v4.0.0 RELEASE)

<p align="center">
  <img src="https://img.shields.io/badge/version-4.0.0-purple">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/runtime-Intelligent%204.0-orange">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

SIRIUS LOCAL AI v4.0.0 is a **next‑generation offline AI runtime**, built on a fully modular, deterministic, and capability‑isolated architecture.

Version **4.0.0** introduces:

- **Runtime Core 4.0**
- **Self‑Repair & Health‑Check Layer**
- **Reasoning Engine 4.0**
- **Knowledge Packs 4.0**
- **AITE 4.0 (Semantic Triage)**
- **SECURITY FAMILY 4.0 (Identity Engine 2.0)**
- **PC Automation Runtime 4.0**
- **SIRIUS ENVOY 4.0 (Safe Online Retrieval)**

The system remains **100% offline**; only ENVOY is allowed controlled network access.

---

# 🛡 Stability Notice (v4.0.0)

SIRIUS LOCAL AI now operates on the **Intelligent Runtime 4.0 architecture**, which guarantees:

- deterministic, reproducible behavior  
- strict module isolation  
- self‑repair and integrity checks  
- no hidden background automation  
- fully local processing (runtime, reasoning, triage)  
- stable plugin and capability interfaces  
- SCHOOLWORK ENGINE 4.0 fully integrated  
- SECURITY FAMILY 4.0 as a core identity layer  

This version is **production‑ready** and designed for long‑term stability and extensibility.

---

# 🧩 Architectural Principles (v4.0.0)

- strict modular separation  
- deterministic execution  
- identity‑aware access control  
- FAMILY‑safe operation  
- SCHOOLWORK always allowed  
- no hidden automation  
- no direct network communication from runtime  
- reversible, predictable actions  
- capability‑based access to Windows functions  
- semantic understanding of inputs and tasks  
- self‑repair and health monitoring  
- plugin‑driven extensibility  

---

# 🖼 Architecture Diagram (Placeholder)

A high‑level architecture diagram for Runtime 4.0 will be added in a future update.

<p align="center">
  <img src="docs/architecture_diagram_v4_placeholder.png" width="600">
</p>

---

# 🧱 Core Layers (v4.0.0)

## 1. Runtime Core 4.0

Central orchestrator responsible for:

- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing capability and security boundaries  
- event routing  
- maintaining global system stability  
- integration with SECURITY FAMILY 4.0  
- integration with Self‑Repair & Health‑Check Layer  

Runtime Core 4.0 is the **central nervous system** of SIRIUS.

---

## 2. Natural Language Router (NL Router 4.0)

Processes natural‑language commands with semantic awareness.

Responsibilities:

- command classification  
- plugin NL command detection  
- semantic routing to modules  
- fallback interpretation  
- preventing ambiguous or unsafe actions  
- integration with identity rules (OWNER / FAMILY / STRANGER)  

NL Router 4.0 ensures **clear intent and safe execution**.

---

## 3. Filesystem Agent (FS‑AGENT 4.0)

Safe, deterministic filesystem operations.

Responsibilities:

- move, copy, delete  
- path validation  
- safety checks and conflict detection  
- rollback‑safe operations  
- semantic routing (documents, code, schoolwork)  
- SCHOOLWORK ENGINE 4.0 integration  

FS‑AGENT 4.0 performs only **safe, validated actions**.

---

## 4. Context Memory Engine (CME‑MEM 4.0)

Semantic short‑term workflow context.

Responsibilities:

- storing recent paths and actions  
- tracking workflow state  
- providing contextual hints  
- supporting multi‑step workflows  
- semantic tags (subject, difficulty, intent)  
- SCHOOLWORK metadata tagging  

CME‑MEM 4.0 stores **only workflow‑related context**, never personal identity data.

---

## 5. Workflow Engine 4.0

Controls multi‑step logic with semantic transitions.

Responsibilities:

- workflow state machine  
- executing plugin and system workflows  
- validating transitions  
- ensuring predictable behavior  
- preventing invalid sequences  
- SCHOOLWORK workflow prioritization  
- integration with Reasoning Engine 4.0  

Workflow Engine 4.0 ensures **transparent, deterministic workflows**.

---

## 6. GUI Layer 4.0

Plugin‑driven user interface.

Responsibilities:

- rendering plugin buttons and panels  
- executing GUI actions  
- integration with Runtime Core 4.0  
- SCHOOLWORK visual indicators  
- identity and mode indicators (OWNER/FAMILY/STRANGER)  
- future expansion to tray/voice layers  

GUI 4.0 is fully modular and extensible.

---

## 7. Automatic Input Triage Engine (AITE 4.0)

Semantic triage engine for all user inputs.

Recognized types:

- text (plain, formatted, code)  
- images/photos/screenshots  
- documents (pdf, docx, txt, pptx)  
- installers/applications (exe, msi, zip, apk, dmg)  
- schoolwork (deep detection: math, essays, assignments, STEM)  
- mixed content (image + text + code)  
- OCR‑extracted content  

Responsibilities:

- type detection + semantic analysis  
- routing to correct modules  
- metadata and semantic tag generation  
- integration with FS‑AGENT 4.0 and CME‑MEM 4.0  
- **bypassing FAMILY time limits for schoolwork**  
- SCHOOLWORK ENGINE 4.0 integration  
- integration with Reasoning Engine 4.0, Knowledge Packs 4.0, ENVOY 4.0  

AITE 4.0 ensures the system always knows **what kind of input it is handling and what it means**.

---

## 8. Windows System Capabilities Layer (WIN‑CAP 4.0)

Abstracted access to Windows 11 system functions.

Submodules:

- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  
- `automation_ops` (PC automation hooks)  

WIN‑CAP 4.0 provides **safe, high‑level system actions** with strict capability boundaries.

---

## 9. Plugin System 4.0

A fully modular, semantic plugin ecosystem.

Features:

- manifest‑based plugin definitions  
- NL commands and triggers  
- AI tasks and workflows  
- AI loop rules  
- GUI elements  
- SCHOOLWORK‑aware plugins  
- hooks into Reasoning Engine 4.0 and Knowledge Packs 4.0  

All official plugins are **v4‑ready**.

---

# 🔐 SECURITY FAMILY 4.0 (Identity Engine 2.0)

A core module providing identity‑based safety and family‑oriented restrictions.

## Purpose

- behavior‑based recognition of **OWNER**, **FAMILY**, **STRANGER**  
- offline identity learning (no biometrics, no cloud)  
- safe‑mode for unknown users  
- restricted mode for children  
- protection of sensitive operations  
- **time‑based limits for children (v2)**  
- **schoolwork bypass mode (deep integration with SCHOOLWORK ENGINE 4.0)**  

## Submodules

- `identity_engine_v2.py`  
- `behavior_audit_v2.py`  
- `access_control_v2.py`  
- `family_mode_v2.py`  
- `stranger_mode_v2.py`  
- `time_limits_v2.py`  
- `profile_store_v2.json`  

SECURITY FAMILY 4.0 is a **core security and identity layer** in Runtime 4.0.

---

# 🌟 Intelligent Modules (v4.0.0)

These modules expand SIRIUS into a **full offline household and developer assistant**, powered by semantic reasoning.

## 🏠 HOME_ASSISTANT 4.0

- safe household recommendations  
- cleaning and organization workflows  
- safety‑first guidance  
- integration with IMAGE_ANALYZER 4.0  
- Knowledge Packs (home, safety, organization)  

---

## 🍳 COOKING_ADVISOR 4.0

- recipe generation  
- ingredient‑based suggestions  
- step‑by‑step cooking workflows  
- dietary filters  
- integration with Knowledge Packs (kitchen, nutrition)  

---

## 🔧 DEVICE_DIAGNOSTICS 4.0

- device issue detection  
- safe troubleshooting flows  
- dangerous‑situation detection  
- OWNER‑only repair actions  
- SECURITY FAMILY 4.0 integration  

---

## 🎓 SCHOOL_HELPER 4.0

- math, language, science explanations  
- step‑by‑step reasoning via Reasoning Engine 4.0  
- safe educational help  
- image‑based homework recognition via IMAGE_ANALYZER 4.0  
- deep integration with SCHOOLWORK ENGINE 4.0  

---

## 🖼 IMAGE_ANALYZER 4.0

- reading homework from photos and screenshots  
- identifying household objects  
- detecting device issues visually  
- routing results to SCHOOL_HELPER, DEVICE_DIAGNOSTICS, HOME_ASSISTANT, or PC Automation  

---

## 🧭 CONTEXT_ROUTER 4.0

- detects household tasks  
- cooking tasks  
- device issues  
- schoolwork and academic tasks  
- developer/automation tasks  
- routes to appropriate v4 modules  

---

## 📚 KNOWLEDGE_PACKS 4.0

Modular offline knowledge expansions.

Responsibilities:

- domain‑specific knowledge (kitchen, repairs, school subjects, coding)  
- safe curated datasets  
- semantic linking with Reasoning Engine 4.0  
- plug‑and‑play expansions  
- no internet required  

---

# 🧠 Reasoning Engine 4.0

Structured reasoning layer for explanations and analysis.

Capabilities:

- step‑by‑step reasoning  
- academic explanations (math, science, languages)  
- code analysis and refactoring suggestions  
- semantic breakdown of complex inputs  
- integration with AITE 4.0 and Knowledge Packs 4.0  

---

# 🛠 Self‑Repair & Health‑Check Layer (NEW in v4.0.0)

Ensures long‑term stability and resilience.

Responsibilities:

- module integrity checks  
- configuration validation  
- automatic repair routines  
- safe fallback states  
- detection of corrupted or missing components  

---

# 🆕 PC Automation Runtime (v4.0.0)

Transforms SIRIUS into a **developer‑level offline automation assistant**.

## 🗂 FS MODULE 4.0

- mkdir, move, copy, delete  
- safe‑mode protections  
- semantic project routing  

## 📝 EDITOR MODULE 4.0

- open file/folder  
- jump to line  
- highlight ranges  
- integration with code workflows  

## 🔧 WORKFLOW MODULE (PC) 4.0

- project scaffolding  
- refactoring tasks  
- version preparation  
- module generation  

## 🧠 COMMAND PARSER 4.0

Parses structured commands like:

`fs.move("src/a.py", "modules/a.py")`

## 🛰 COMMAND ROUTER 4.0

Routes parsed commands to:

- FS module  
- Editor module  
- Workflow module  

All modules are registered into **Runtime Core 4.0** with dependency‑aware startup.

---

# 🌐 SIRIUS ENVOY 4.0 — SAFE ONLINE RETRIEVAL LAYER

SIRIUS ENVOY 4.0 is an **optional, isolated online retrieval agent** designed to safely fetch information from the internet **without exposing the local AI runtime to any network communication**.

## Key Principles

- Local AI remains **100% offline**  
- Only the ENVOY process can access the internet  
- All retrieved data passes through a **quarantine sandbox**  
- Only validated, sanitized, text‑only information is delivered to SIRIUS  

## ENVOY Pipeline

1. **Envoy Client**  
   - isolated process  
   - performs outbound requests  
   - no access to local AI memory or capabilities  

2. **Scraper Layer**  
   - extracts text  
   - removes scripts, HTML, trackers, active content  

3. **Quarantine Sandbox**  
   - validates structure  
   - checks for unsafe patterns  
   - strips unknown formats  

4. **Validator & Filter**  
   - ensures data safety  
   - marks uncertainty  
   - enforces domain rules  

5. **Safe Payload Delivery**  
   - only clean, structured, offline‑safe text is passed to SIRIUS  

## Use Cases

- health information  
- educational content  
- definitions, facts, summaries  
- dynamic updates for Knowledge Packs  
- safe external lookups  

ENVOY never sends local data outward and never interacts directly with the runtime core.

---

# 🔌 Module Interconnections (v4.0.0)

User Input  
↓  
AITE 4.0 → FS‑AGENT 4.0 → CME‑MEM 4.0  
↓  
Workflow Engine 4.0  
↓  
Runtime Core 4.0 → WIN‑CAP 4.0 → Windows 11 APIs  

### Key relationships:

- NL Router 4.0 → Plugins 4.0  
- Plugins 4.0 → Runtime Core 4.0  
- AITE 4.0 → FS‑AGENT 4.0 / CME‑MEM 4.0 / SECURITY FAMILY 4.0  
- IMAGE_ANALYZER 4.0 → SCHOOL_HELPER 4.0 / DEVICE_DIAGNOSTICS 4.0 / HOME_ASSISTANT 4.0  
- CONTEXT_ROUTER 4.0 → all v4 modules  
- PC Automation Runtime 4.0 → Runtime Core 4.0  
- ENVOY 4.0 → Knowledge Packs 4.0 / Reasoning Engine 4.0  

All communication is **explicit, controlled, and deterministic**.

---

# 📌 Document Status

Current version: **4.0.0 (Stable)**  
Architecture is fully defined and ready for future v4.x expansions.
