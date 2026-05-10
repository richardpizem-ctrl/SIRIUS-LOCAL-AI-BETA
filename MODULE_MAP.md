# 🗺️ Module Map – SIRIUS LOCAL AI (v3.0.0)

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map for the stable Runtime 3.0 architecture.

All processing is fully local; no data leaves the user's PC.

---

# 1. Runtime Core 3.0
**Purpose:** Central system layer.  
**Responsibilities:**
- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing security boundaries  
- capability registration  
- event routing  
- maintaining global system stability  
- integration with SECURITY FAMILY  

---

# 2. Filesystem Agent (FS‑AGENT 3.0)
**Purpose:** Safe file operations.  
**Responsibilities:**
- moving, copying, deleting  
- path validation  
- safety checks  
- action confirmations  
- conflict detection  
- rollback‑safe operations  
- SCHOOLWORK priority routing  

---

# 3. Natural Language Router (NL Router 3.0)
**Purpose:** Translation and routing of user commands.  
**Responsibilities:**
- recognizing command type  
- extracting parameters  
- routing to modules or plugins  
- detecting plugin NL commands  
- fallback interpretation  
- preventing ambiguous or unsafe actions  
- applying FAMILY identity rules  

---

# 4. Context Memory Engine (CME‑MEM 3.0)
**Purpose:** Maintaining context and recent actions.  
**Responsibilities:**
- tracking recent user actions  
- storing paths and states  
- providing contextual suggestions  
- supporting multi‑step workflows  
- metadata for plugins and workflows  
- SCHOOLWORK metadata tagging  

---

# 5. Workflow Engine 3.0
**Purpose:** Logic of step sequences and plugin workflows.  
**Responsibilities:**
- workflow state machine  
- executing plugin workflows  
- validating transitions  
- generating next‑step predictions  
- preventing invalid sequences  
- SCHOOLWORK workflow prioritization  

---

# 6. GUI Layer 3.0
**Purpose:** Modular user interface.  
**Responsibilities:**
- rendering plugin buttons  
- executing GUI actions  
- integrating with Runtime Core  
- providing visual feedback  
- tray/voice integration (planned)  
- SCHOOLWORK visual indicators  

---

# 7. Email Composer
**Purpose:** Generating email text (without sending).  
**Responsibilities:**
- email drafts  
- structured responses  
- professional text generation  

---

# 8. Automatic Input Triage Engine (AITE 3.0)
**Purpose:** Automatic detection and classification of input type.  
**Responsibilities:**
- detecting input type (text, image, application, document)  
- routing to the correct module  
- metadata generation  
- integration with FS‑AGENT and CME‑MEM  
- rejecting unsupported or unsafe inputs  
- detecting schoolwork  
- triggering **Schoolwork Priority Mode**  
- bypassing FAMILY time‑limits for academic content  

---

# 9. Windows System Capabilities Layer (WIN‑CAP 3.0)
**Purpose:** Provide safe, abstracted access to Windows 11 system functions.  
This module transforms SIRIUS into a true local OS‑level AI agent.

**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions and allowed scopes  
- providing safe wrappers around OS operations  
- enabling multi‑step system actions through AI reasoning  
- integrating with SECURITY FAMILY identity restrictions  

**Submodules:**
- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  

---

# 10. UI Components
**Purpose:** Modular UI building blocks.  
**Responsibilities:**
- reusable UI elements  
- layout components  
- visual helpers  
- animation hooks  

**Subfolder: `animations/`**
- `animation_engine.py`  
- `animation_objects.py`  
- `animation_scenes.py`  
- `animation_manager.py`  

---

# 11. Workflow Module
**Purpose:** High‑level workflow logic.  
**Responsibilities:**
- orchestrating multi‑step operations  
- validating transitions  
- predictable behavior  
- integrating CME, FS‑AGENT, and GUI  
- SCHOOLWORK workflow routing  

---

# 12. Plugin System 3.0
**Purpose:** Extensible plugin ecosystem.  
**Responsibilities:**
- loading plugin manifests  
- registering NL commands  
- registering AI tasks  
- registering workflows  
- registering AI loop rules  
- registering GUI elements  
- safe plugin isolation  
- SCHOOLWORK‑aware plugin behavior  

Official plugins include:
- automation  
- clipboard  
- example  
- file_manager  
- notes  
- system_tools  
- translator  

---

# 13. AI Loop 3.0
**Purpose:** Autonomous interval‑based logic.  
**Responsibilities:**
- executing plugin heartbeat rules  
- safe periodic tasks  
- deterministic scheduling  
- error protection  
- SCHOOLWORK‑aware timing  

---

# 14. Self‑Repair & Health‑Check Layer (v4.0.0)
**Purpose:** Diagnostics and safe automatic recovery.  
**Responsibilities:**  
- checking integrity of core modules  
- detecting corrupted states, missing files, invalid configs  
- performing safe automatic repairs  
- generating patch suggestions (manual approval required)  
- preventing uncontrolled modifications of source code  
- reporting system health to Runtime Core  

**Submodules:**  
- `health_check_engine.py`  
- `self_repair_safe.py`  
- `repair_suggestions.py`  

---

# 15. SECURITY FAMILY (v3.0.0)
**Purpose:** Behavior‑based identity and family safety layer.  
This module introduces **OWNER / FAMILY / STRANGER** identity levels.

**Responsibilities:**
- behavior‑based identity recognition  
- offline learning of owner and family profiles  
- safe‑mode for unknown users  
- restricted mode for children  
- protection of sensitive operations  
- integration with NL Router and WIN‑CAP  
- **time‑based limits for children**  
- **Schoolwork Priority Mode (schoolwork always allowed)**  
- STRANGER‑mode restrictions  

**Submodules:**
- `identity_engine.py`  
- `behavior_audit.py`  
- `access_control.py`  
- `family_mode.py`  
- `stranger_mode.py`  
- `time_limits.py`  
- `schoolwork_detector.py`  
- `profile_store.json`  

This is a **core security module** in version **3.0.0**.

---

# 16. v3.0.0 Intelligent Runtime Modules

These modules extend SIRIUS from a system automation runtime into a **full offline household assistant**, while staying safe, modular, and local‑only.

---

## 16.1 HOME_ASSISTANT (v3.0.0)
**Purpose:** General household advice and daily assistance.  
**Responsibilities:**
- safe household recommendations  
- cleaning tips  
- organization workflows  
- safety‑first guidance  
- integration with IMAGE_ANALYZER  

---

## 16.2 COOKING_ADVISOR (v3.0.0)
**Purpose:** Offline cooking and recipe assistant.  
**Responsibilities:**
- recipe generation  
- suggestions based on available ingredients  
- step‑by‑step cooking workflows  
- dietary filters  
- integration with Knowledge Packs  

---

## 16.3 DEVICE_DIAGNOSTICS (v3.0.0)
**Purpose:** Safe troubleshooting for household devices.  
**Responsibilities:**
- identifying common device issues  
- providing safe repair suggestions  
- detecting dangerous situations  
- routing to OWNER‑only actions  
- integration with SECURITY FAMILY  

---

## 16.4 SCHOOL_HELPER (v3.0.0)
**Purpose:** Offline schoolwork assistant.  
**Responsibilities:**
- math, language, science explanations  
- step‑by‑step reasoning  
- safe educational help  
- SCHOOLWORK PRIORITY MODE integration  
- image‑based homework recognition  

---

## 16.5 IMAGE_ANALYZER (v3.0.0)
**Purpose:** Local image understanding.  
**Responsibilities:**
- reading homework from photos  
- identifying household objects  
- detecting device issues visually  
- routing results to correct modules  

---

## 16.6 CONTEXT_ROUTER v3 (v3.0.0)
**Purpose:** Smarter routing of user intent.  
**Responsibilities:**
- detecting household tasks  
- detecting cooking tasks  
- detecting device issues  
- detecting schoolwork  
- routing to new v3 modules  

---

## 16.7 KNOWLEDGE_PACKS (v3.0.0+)
**Purpose:** Modular offline knowledge expansions.  
**Responsibilities:**
- domain‑specific knowledge (kitchen, repairs, school subjects)  
- safe curated datasets  
- plug‑and‑play expansions  
- no internet required  

---

# 17. Module Interconnections

- **NL Router → FS‑AGENT:** determines file operations  
- **NL Router → Plugins:** routes NL commands  
- **CME‑MEM → Workflow Engine:** provides context  
- **AITE → FS‑AGENT:** routes inputs based on type  
- **AITE → CME‑MEM:** stores metadata  
- **AITE → SECURITY FAMILY:** schoolwork detection → bypass time limits  
- **SECURITY FAMILY → Runtime Core:** identity‑based access control  
- **WIN‑CAP → Runtime Core:** privileged capability layer  
- **Runtime Core → all modules:** initialization and security  
- **Plugins → Runtime Core:** register capabilities  
- **IMAGE_ANALYZER → SCHOOL_HELPER / DEVICE_DIAGNOSTICS / HOME_ASSISTANT**  
- **CONTEXT_ROUTER v3 → all v3 modules**  

All communication is explicit and controlled.

---

# Document Status
Current version: **3.0.0 (Stable)**  
Future modules for **v4.0.0** are defined as part of the long‑term vision.
