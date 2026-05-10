# 🏗 Architecture – SIRIUS LOCAL AI (v3.0.0 RELEASE)

<p align="center">
  <img src="https://img.shields.io/badge/version-3.0.0-blue">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/architecture-modular-lightgrey">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

SIRIUS LOCAL AI is a fully modular, local‑only AI runtime designed to safely interpret user commands and interact with the Windows 11 environment through isolated capability modules.

Version **3.0.0** introduces a major architectural expansion, new intelligent subsystems, SCHOOLWORK PRIORITY MODE, SECURITY FAMILY integration, and the first generation of household‑oriented modules.

The architecture emphasizes **safety**, **predictability**, **modularity**, **identity‑based access**, and **full local control**.

---

# 🛡 Stability Notice (v3.0.0)

SIRIUS LOCAL AI now operates on the **stable Runtime 3.0 architecture**.

- All modules are isolated and deterministic  
- No cloud communication  
- No background automation unless explicitly defined  
- All processing is fully local  
- All plugin interfaces are stable  
- All core modules (runtime, context, filesystem, commands, security) are validated for v3.0.0  
- SCHOOLWORK PRIORITY MODE is fully integrated  
- SECURITY FAMILY is now an active core module  

This version is production‑ready and forms the foundation for v4.0.0.

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
- explicit user intent for all operations  
- plugin‑driven extensibility  

---

# 🖼 Architecture Diagram (Placeholder)

> A high‑level architecture diagram will be added in a future update.

<p align="center">
  <img src="docs/architecture_diagram_placeholder.png" width="600">
</p>

---

# 🧱 Core Layers (v3.0.0)

## 1. Runtime Core 3.0
Central orchestrator responsible for:

- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing security boundaries  
- capability registration  
- event routing  
- maintaining global system stability  
- integration with SECURITY FAMILY  

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
- integration with FAMILY identity rules  

NL Router 3.0 ensures **clear intent and safe execution**.

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

FS‑AGENT 3.0 performs only **safe, validated actions**.

---

## 4. Context Memory Engine (CME‑MEM 3.0)
Maintains short‑term workflow context.

Responsibilities:

- storing recent paths  
- tracking last actions  
- providing contextual hints  
- supporting multi‑step workflows  
- SCHOOLWORK metadata tagging  

CME‑MEM stores **only workflow‑related context**, never personal data.

---

## 5. Workflow Engine 3.0
Controls multi‑step logic.

Responsibilities:

- workflow state machine  
- executing plugin workflows  
- validating transitions  
- predictable behavior  
- preventing invalid sequences  
- SCHOOLWORK workflow prioritization  

Workflow Engine 3.0 ensures **transparent, deterministic workflows**.

---

## 6. GUI Layer 3.0
Plugin‑driven user interface.

Responsibilities:

- rendering plugin buttons  
- executing GUI actions  
- integrating with RuntimeManager  
- future expansion to tray/voice layers  
- SCHOOLWORK visual indicators  

GUI 3.0 is fully modular and extensible.

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
- integration with FS‑AGENT and CME‑MEM  
- **bypassing FAMILY time limits for schoolwork**  
- SCHOOLWORK PRIORITY MODE  

AITE ensures the system always knows **what kind of input it is handling**.

---

## 8. Windows System Capabilities Layer (WIN‑CAP 3.0)
Abstracted access to Windows 11 system functions.

Submodules:

- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  

WIN‑CAP provides **safe, high‑level system actions**.

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

A new core module providing identity‑based safety and family‑oriented restrictions.

## SECURITY FAMILY – Behavior‑Based Identity & Family Safety Layer

Purpose:
- behavior‑based recognition of **OWNER**, **FAMILY**, and **STRANGER**  
- offline identity learning (no biometrics, no cloud)  
- safe‑mode for unknown users  
- restricted mode for children  
- protection of sensitive operations  
- **time‑based limits for children**  
- **schoolwork bypass mode**  

Submodules:

- `identity_engine.py`  
- `behavior_audit.py`  
- `access_control.py`  
- `family_mode.py`  
- `stranger_mode.py`  
- `time_limits.py`  
- `profile_store.json`  

SECURITY FAMILY is now a **core security layer** in version **3.0.0**.

---

# 🌟 New v3.0.0 Modules

These modules expand SIRIUS from a system automation runtime into a **full offline household assistant**, while staying safe, predictable, and local‑only.

---

## 🏠 HOME_ASSISTANT (v3.0.0)
General household assistant.

Responsibilities:
- safe household recommendations  
- cleaning tips  
- organization workflows  
- safety‑first guidance  
- integration with IMAGE_ANALYZER  

---

## 🍳 COOKING_ADVISOR (v3.0.0)
Offline cooking and recipe assistant.

Responsibilities:
- recipe generation  
- suggestions based on available ingredients  
- step‑by‑step cooking workflows  
- dietary filters  
- integration with Knowledge Packs  

---

## 🔧 DEVICE_DIAGNOSTICS (v3.0.0)
Safe troubleshooting for household devices.

Responsibilities:
- identifying common device issues  
- providing safe repair suggestions  
- detecting dangerous situations  
- routing to OWNER‑only actions  
- integration with SECURITY FAMILY  

---

## 🎓 SCHOOL_HELPER (v3.0.0)
Offline schoolwork assistant.

Responsibilities:
- math, language, science explanations  
- step‑by‑step reasoning  
- safe educational help  
- image‑based homework recognition  
- integration with SCHOOLWORK PRIORITY MODE  

---

## 🖼 IMAGE_ANALYZER (v3.0.0)
Local image understanding engine.

Responsibilities:
- reading homework from photos  
- identifying household objects  
- detecting device issues visually  
- routing results to correct modules  

---

## 🧭 CONTEXT_ROUTER v3 (v3.0.0)
Smarter intent routing.

Responsibilities:
- detecting household tasks  
- detecting cooking tasks  
- detecting device issues  
- detecting schoolwork  
- routing to new v3 modules  

---

## 📚 KNOWLEDGE_PACKS (v3.0.0+)
Modular offline knowledge expansions.

Responsibilities:
- domain‑specific knowledge (kitchen, repairs, school subjects)  
- safe curated datasets  
- plug‑and‑play expansions  
- no internet required  

---

# 🆕 NEW: PC Automation Runtime (v3.5.0)

Version 3.5.0 introduces a new automation layer that transforms SIRIUS into a **developer‑level PC automation assistant**, capable of manipulating files, code, and project structure — fully offline and under user control.

## 🗂 FS MODULE  
Local filesystem automation  
- mkdir  
- move  
- copy  
- delete  
- read/write  
- safe‑mode protections  

## 📝 EDITOR MODULE  
VS Code integration  
- open file  
- open folder  
- jump to line  
- highlight  

## 🔧 WORKFLOW MODULE (PC)  
Developer workflows  
- project scaffolding  
- refactoring tasks  
- version preparation  
- module generation  

## 🧠 COMMAND PARSER  
Parses structured commands like:  
`fs.move("src/a.py", "modules/a.py")`

## 🛰 COMMAND ROUTER  
Routes parsed commands to correct modules  
- fs  
- editor  
- workflow  

## 🔌 Runtime Integration  
All modules registered into **Runtime Core 4.0** with dependency‑aware startup.

**Purpose:**  
Enable SIRIUS to operate directly on the user’s PC as a safe, deterministic, offline automation engine.

---

# 🌐 SIRIUS ENVOY 4.0 — SAFE ONLINE RETRIEVAL LAYER  
*(Introduced for SIRIUS 4.0 architecture)*

SIRIUS ENVOY 4.0 is an **optional, isolated online retrieval agent** designed to safely fetch information from the internet **without exposing the local AI runtime to any network communication**.

### **Key Principles**
- Local AI remains **100% offline**  
- Only the ENVOY process is allowed to access the internet  
- All retrieved data passes through a **quarantine sandbox**  
- Only validated, sanitized, text‑only information is delivered to SIRIUS  

### **ENVOY Pipeline**
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

### **Use Cases**
- health information  
- educational content  
- definitions, facts, summaries  
- dynamic updates for Knowledge Packs  
- safe external lookups  

ENVOY never sends local data outward and never interacts directly with the runtime core.

---

# 🔌 Module Interconnections

User Input  
↓  
NL Router → AITE → FS‑AGENT  
↓  
CME‑MEM → Workflow Engine  
↓  
Runtime Core → WIN‑CAP → Windows 11 APIs  

### Key relationships:

- NL Router → Plugins  
- Plugins → Runtime Core  
- AITE → FS‑AGENT  
- AITE → CME‑MEM  
- Workflow Engine → Runtime Core  
- WIN‑CAP → Runtime Core  
- **AITE → SECURITY FAMILY (schoolwork bypass)**  
- **IMAGE_ANALYZER → SCHOOL_HELPER / DEVICE_DIAGNOSTICS / HOME_ASSISTANT**  
- **CONTEXT_ROUTER v3 → all v3 modules**  
- **PC AUTOMATION LAYER → Runtime Core 4.0**  
- **ENVOY 4.0 → Knowledge Packs / Reasoning Engine (v4.0.0)**  

All communication is **explicit and controlled**.

---

# 📌 Document Status

Current version: **3.0.0 (Stable)**  
Architecture is fully defined and ready for future expansions in v4.0.0.
