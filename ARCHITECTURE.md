# 🏗 Architecture – SIRIUS LOCAL AI (v3.0.0 RELEASE)

<p align="center">
  <img src="https://img.shields.io/badge/version-3.0.0-blue">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/architecture-modular-lightgrey">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

SIRIUS LOCAL AI is a fully modular, **offline‑only AI runtime** designed to safely interpret user commands and interact with Windows 11 through isolated capability modules.

Version **3.0.0** introduces a major architectural expansion, new intelligent subsystems, SCHOOLWORK PRIORITY MODE, SECURITY FAMILY integration, and the first generation of household‑oriented modules.

The architecture emphasizes:

- **safety**
- **predictability**
- **strict modularity**
- **identity‑based access**
- **full local control**

---

# 🛡 Stability Notice (v3.0.0)

SIRIUS LOCAL AI now operates on the **stable Runtime 3.0 architecture**, which guarantees:

- isolated, deterministic modules  
- zero cloud communication  
- no hidden background automation  
- fully local processing  
- stable plugin interfaces  
- validated core modules (runtime, context, filesystem, commands, security)  
- SCHOOLWORK PRIORITY MODE fully integrated  
- SECURITY FAMILY as an active core module  

This version is **production‑ready** and forms the foundation for v4.0.0.

---

# 🧩 Architectural Principles (v3.0.0)

- strict modular separation  
- deterministic behavior  
- identity‑based access control  
- FAMILY‑safe operation  
- SCHOOLWORK always allowed  
- no hidden automation  
- no network communication  
- predictable, reversible actions  
- capability‑based access to Windows functions  
- explicit user intent required  
- plugin‑driven extensibility  

---

# 🖼 Architecture Diagram (Placeholder)

A high‑level architecture diagram will be added in a future update.

<p align="center">
  <img src="docs/architecture_diagram_placeholder.png" width="600">
</p>

---

# 🧱 Core Layers (v3.0.0)

## 1. Runtime Core 3.0
The central orchestrator responsible for:

- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing security boundaries  
- capability registration  
- event routing  
- global system stability  
- SECURITY FAMILY integration  

Runtime Core 3.0 is the **heart of the system**.

---

## 2. Natural Language Router (NL Router 3.0)
Processes natural‑language commands.

Responsibilities:

- command classification  
- plugin NL command detection  
- routing to modules  
- fallback interpretation  
- preventing ambiguous or unsafe actions  
- FAMILY identity rule integration  

Ensures **clear intent and safe execution**.

---

## 3. Filesystem Agent (FS‑AGENT 3.0)
Safe filesystem operations.

Responsibilities:

- move, copy, delete  
- path validation  
- safety checks  
- conflict detection  
- rollback‑safe operations  
- SCHOOLWORK priority routing  

Performs only **safe, validated actions**.

---

## 4. Context Memory Engine (CME‑MEM 3.0)
Maintains short‑term workflow context.

Responsibilities:

- storing recent paths  
- tracking last actions  
- contextual hints  
- multi‑step workflow support  
- SCHOOLWORK metadata tagging  

Stores **only workflow‑related context**, never personal data.

---

## 5. Workflow Engine 3.0
Controls multi‑step logic.

Responsibilities:

- workflow state machine  
- plugin workflow execution  
- transition validation  
- predictable behavior  
- preventing invalid sequences  
- SCHOOLWORK workflow prioritization  

Ensures **transparent, deterministic workflows**.

---

## 6. GUI Layer 3.0
Plugin‑driven user interface.

Responsibilities:

- rendering plugin buttons  
- executing GUI actions  
- RuntimeManager integration  
- future tray/voice expansion  
- SCHOOLWORK visual indicators  

Fully modular and extensible.

---

## 7. Automatic Input Triage Engine (AITE 3.0)
Classifies incoming user inputs.

Recognized types:

- text  
- images/photos  
- installers/applications  
- documents  
- **schoolwork (NEW)** — academic content with priority bypass  

Responsibilities:

- type detection  
- routing  
- metadata generation  
- FS‑AGENT + CME‑MEM integration  
- **bypassing FAMILY time limits for schoolwork**  
- SCHOOLWORK PRIORITY MODE  

Ensures the system always knows **what kind of input it is handling**.

---

## 8. Windows System Capabilities Layer (WIN‑CAP 3.0)
Abstracted access to Windows 11 system functions.

Submodules:

- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  

Provides **safe, high‑level system actions**.

---

## 9. Plugin System 3.0
A fully modular plugin ecosystem.

Features:

- manifest‑based plugin definitions  
- NL commands  
- AI tasks  
- workflows  
- AI loop rules  
- GUI elements  
- SCHOOLWORK‑aware plugins  

All official plugins are **v3‑ready**.

---

# 🔐 SECURITY FAMILY (NEW in v3.0.0)

A core module providing identity‑based safety and family‑oriented restrictions.

### Purpose:
- behavior‑based recognition of **OWNER**, **FAMILY**, **STRANGER**  
- offline identity learning (no biometrics, no cloud)  
- safe‑mode for unknown users  
- restricted mode for children  
- protection of sensitive operations  
- **time‑based limits for children**  
- **schoolwork bypass mode**  

### Submodules:
- `identity_engine.py`  
- `behavior_audit.py`  
- `access_control.py`  
- `family_mode.py`  
- `stranger_mode.py`  
- `time_limits.py`  
- `profile_store.json`  

SECURITY FAMILY is a **core security layer** in v3.0.0.

---

# 🌟 New v3.0.0 Intelligent Modules

These modules expand SIRIUS into a **full offline household assistant**, while staying safe and predictable.

---

## 🏠 HOME_ASSISTANT
- household recommendations  
- cleaning tips  
- organization workflows  
- safety‑first guidance  
- IMAGE_ANALYZER integration  

---

## 🍳 COOKING_ADVISOR
- recipe generation  
- ingredient‑based suggestions  
- step‑by‑step workflows  
- dietary filters  
- Knowledge Pack integration  

---

## 🔧 DEVICE_DIAGNOSTICS
- device issue detection  
- safe troubleshooting  
- dangerous‑situation detection  
- OWNER‑only repair actions  
- SECURITY FAMILY integration  

---

## 🎓 SCHOOL_HELPER
- math, language, science explanations  
- step‑by‑step reasoning  
- safe educational help  
- SCHOOLWORK PRIORITY MODE integration  
- homework recognition  

---

## 🖼 IMAGE_ANALYZER
- homework reading  
- object recognition  
- device issue detection  
- routing to correct modules  

---

## 🧭 CONTEXT_ROUTER v3
- detects household tasks  
- cooking tasks  
- device issues  
- schoolwork  
- routes to v3 modules  

---

## 📚 KNOWLEDGE_PACKS
- offline knowledge expansions  
- curated datasets  
- plug‑and‑play modules  
- no internet required  

---

# 🆕 PC Automation Runtime (v3.5.0)

Transforms SIRIUS into a **developer‑level offline automation assistant**.

### 🗂 FS MODULE  
- mkdir, move, copy, delete  
- safe‑mode protections  

### 📝 EDITOR MODULE  
- open file/folder  
- jump to line  
- highlight  

### 🔧 WORKFLOW MODULE (PC)  
- scaffolding  
- refactoring  
- version prep  
- module generation  

### 🧠 COMMAND PARSER  
Parses structured commands like:  
`fs.move("src/a.py", "modules/a.py")`

### 🛰 COMMAND ROUTER  
Routes commands to FS / Editor / Workflow.

### 🔌 Runtime Integration  
Registered into **Runtime Core 4.0**.

---

# 🌐 SIRIUS ENVOY 4.0 — SAFE ONLINE RETRIEVAL LAYER

Optional isolated agent for safe external lookups.

### Principles:
- Local AI stays **100% offline**  
- ENVOY is the only process allowed online  
- All data passes through quarantine  
- Only sanitized text enters SIRIUS  

### Pipeline:
1. Envoy Client  
2. Scraper Layer  
3. Quarantine Sandbox  
4. Validator & Filter  
5. Safe Payload Delivery  

### Use Cases:
- health information  
- educational content  
- definitions, facts  
- Knowledge Pack updates  

ENVOY never sends local data outward.

---

# 🔌 Module Interconnections

User Input  
↓  
NL Router → AITE → FS‑AGENT  
↓  
CME‑MEM → Workflow Engine  
↓  
Runtime Core → WIN‑CAP → Windows APIs  

### Key relationships:
- NL Router → Plugins  
- Plugins → Runtime Core  
- AITE → FS‑AGENT / CME‑MEM / SECURITY FAMILY  
- IMAGE_ANALYZER → SCHOOL_HELPER / DEVICE_DIAGNOSTICS / HOME_ASSISTANT  
- CONTEXT_ROUTER v3 → all v3 modules  
- PC Automation Layer → Runtime Core 4.0  
- ENVOY 4.0 → Knowledge Packs / Reasoning Engine  

All communication is **explicit and controlled**.

---

# 📌 Document Status

Current version: **3.0.0 (Stable)**  
Architecture is fully defined and ready for v4.0.0 expansions.
