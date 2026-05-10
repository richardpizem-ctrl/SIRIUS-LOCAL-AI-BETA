# 🏗 Architecture – SIRIUS LOCAL AI (v4.0.0 RELEASE)

<p align="center">
  <img src="https://img.shields.io/badge/version-4.0.0-purple">
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/platform-Windows%2011-blue">
  <img src="https://img.shields.io/badge/runtime-Intelligent%204.0-orange">
  <img src="https://img.shields.io/badge/local%20AI-100%25-blueviolet">
</p>

SIRIUS LOCAL AI v4.0.0 is a fully modular, **offline‑only intelligent runtime** designed to safely interpret user commands, automate workflows, and interact with Windows 11 through isolated capability modules.

Version **4.0.0** introduces a new generation of intelligent subsystems, including:

- **Runtime Core 4.0**
- **Reasoning Engine 4.0**
- **AITE 4.0 (Semantic Triage)**
- **Security Family 4.0 (Identity Engine 2.0)**
- **Self‑Repair & Health‑Check Layer**
- **Knowledge Packs 4.0**
- **PC Automation Runtime 4.0**
- **SIRIUS ENVOY 4.0 (Safe Online Retrieval)**

The architecture emphasizes **safety**, **predictability**, **semantic intelligence**, **identity‑based access**, and **full local control**.

---

# 🛡 Stability Notice (v4.0.0)

SIRIUS LOCAL AI now operates on the **Intelligent Runtime 4.0 architecture**, which guarantees:

- deterministic, isolated modules  
- zero cloud communication  
- no hidden background automation  
- semantic reasoning and triage  
- stable plugin interfaces  
- SCHOOLWORK ENGINE 4.0 fully integrated  
- SECURITY FAMILY 4.0 as a core identity layer  
- self‑repair and integrity monitoring  

This version is production‑ready and forms the foundation for v4.x and v5.

---

# 🧩 Architectural Principles (v4.0.0)

- strict modular separation  
- deterministic behavior  
- semantic understanding of inputs  
- identity‑aware access control  
- FAMILY‑safe operation  
- SCHOOLWORK always allowed  
- no hidden automation  
- no direct network communication  
- reversible, predictable actions  
- capability‑based access to Windows functions  
- plugin‑driven extensibility  
- self‑repair and health monitoring  

---

# 🖼 Architecture Diagram (Placeholder)

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
- enforcing capability boundaries  
- event routing  
- global system stability  
- integration with SECURITY FAMILY 4.0  
- integration with Self‑Repair Layer  

Runtime Core 4.0 is the **heart of the system**.

---

## 2. Natural Language Router (NL Router 4.0)
Processes natural‑language commands with semantic understanding.

Responsibilities:

- command classification  
- plugin NL command detection  
- semantic routing  
- fallback interpretation  
- preventing ambiguous or unsafe actions  
- identity‑aware filtering  

Ensures **clear intent and safe execution**.

---

## 3. Filesystem Agent (FS‑AGENT 4.0)
Safe, deterministic filesystem operations.

Responsibilities:

- move, copy, delete  
- path validation  
- rollback‑safe operations  
- semantic routing (documents, code, schoolwork)  
- SCHOOLWORK ENGINE integration  

---

## 4. Context Memory Engine (CME‑MEM 4.0)
Semantic workflow context.

Responsibilities:

- storing recent paths  
- tracking last actions  
- semantic tags (subject, difficulty, intent)  
- multi‑step workflow support  
- SCHOOLWORK metadata tagging  

Stores **only workflow‑related context**, never personal data.

---

## 5. Workflow Engine 4.0
Controls multi‑step logic with semantic transitions.

Responsibilities:

- workflow state machine  
- plugin workflow execution  
- academic workflows  
- code workflows  
- automation workflows  
- transition validation  
- deterministic behavior  

---

## 6. GUI Layer 4.0
Modular user interface.

Responsibilities:

- rendering plugin UI  
- executing GUI actions  
- identity indicators  
- SCHOOLWORK indicators  
- future tray/voice expansion  

---

## 7. Automatic Input Triage Engine (AITE 4.0)
Semantic triage engine.

Recognized types:

- text  
- images/photos/screenshots  
- documents  
- code  
- installers  
- **schoolwork (deep detection)**  
- mixed content  
- OCR‑extracted content  

Responsibilities:

- type detection + semantic analysis  
- routing  
- metadata generation  
- integration with FS‑AGENT, CME‑MEM  
- **schoolwork bypass**  
- integration with Reasoning Engine 4.0  
- integration with Knowledge Packs 4.0  
- integration with ENVOY 4.0  

---

## 8. Windows System Capabilities Layer (WIN‑CAP 4.0)
Abstracted access to Windows 11 system functions.

Submodules:

- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  
- `automation_ops`  

Provides **safe, high‑level system actions**.

---

## 9. Plugin System 4.0
A fully modular plugin ecosystem.

Features:

- semantic plugin manifests  
- NL commands  
- AI tasks  
- workflows  
- GUI elements  
- SCHOOLWORK‑aware plugins  
- Reasoning Engine hooks  

All official plugins are **v4‑ready**.

---

# 🔐 SECURITY FAMILY 4.0 (Identity Engine 2.0)

Purpose:
- behavior‑based recognition of **OWNER**, **FAMILY**, **STRANGER**  
- offline identity learning  
- safe‑mode for unknown users  
- restricted mode for children  
- protection of sensitive operations  
- **time‑limits 2.0**  
- **schoolwork bypass**  

Submodules:

- `identity_engine_v2.py`  
- `behavior_audit_v2.py`  
- `access_control_v2.py`  
- `family_mode_v2.py`  
- `stranger_mode_v2.py`  
- `time_limits_v2.py`  
- `profile_store_v2.json`  

---

# 🌟 Intelligent Modules (v4.0.0)

## 🏠 HOME_ASSISTANT 4.0
## 🍳 COOKING_ADVISOR 4.0
## 🔧 DEVICE_DIAGNOSTICS 4.0
## 🎓 SCHOOL_HELPER 4.0
## 🖼 IMAGE_ANALYZER 4.0
## 🧭 CONTEXT_ROUTER 4.0
## 📚 KNOWLEDGE_PACKS 4.0

All upgraded for semantic routing and Reasoning Engine 4.0.

---

# 🧠 Reasoning Engine 4.0
Structured reasoning layer.

Capabilities:

- step‑by‑step reasoning  
- academic explanations  
- code analysis  
- semantic breakdown  
- integration with AITE 4.0  
- integration with Knowledge Packs 4.0  

---

# 🛠 Self‑Repair & Health‑Check Layer (NEW)
Ensures long‑term stability.

Functions:

- module integrity checks  
- automatic repair routines  
- fallback states  
- corruption detection  
- dependency validation  

---

# 🆕 PC Automation Runtime (v4.0.0)

Developer‑level offline automation.

Modules:

- FS Module 4.0  
- Editor Module 4.0  
- Workflow Module 4.0  
- Command Parser 4.0  
- Command Router 4.0  

---

# 🌐 SIRIUS ENVOY 4.0 — SAFE ONLINE RETRIEVAL

Optional isolated agent.

Pipeline:

1. Envoy Client  
2. Scraper Layer  
3. Quarantine Sandbox  
4. Validator & Filter  
5. Safe Payload Delivery  

Never sends local data outward.

---

# 🔌 Module Interconnections (v4.0.0)

User Input  
↓  
AITE 4.0 → FS‑AGENT 4.0 → CME‑MEM 4.0  
↓  
Workflow Engine 4.0  
↓  
Runtime Core 4.0 → WIN‑CAP 4.0  

Key relationships:

- AITE → Reasoning Engine  
- AITE → Knowledge Packs  
- AITE → Security Family  
- IMAGE_ANALYZER → SCHOOL_HELPER / DEVICE_DIAGNOSTICS / HOME_ASSISTANT  
- CONTEXT_ROUTER → all v4 modules  
- PC Automation → Runtime Core  
- ENVOY → Knowledge Packs / Reasoning  

All communication is **explicit and controlled**.

---

# 📌 Document Status

Current version: **4.0.0 (Stable)**  
Architecture is fully defined and ready for v4.x expansions.
