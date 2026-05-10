# 🗺️ Module Map – SIRIUS LOCAL AI (v4.0.0)

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map for the **Intelligent Runtime 4.0** architecture.

All processing is fully local; no data leaves the user's PC.

---

# 1. Runtime Core 4.0
**Purpose:** Central orchestrator of the entire system.  
**Responsibilities:**
- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing capability boundaries  
- event routing  
- global system stability  
- integration with Security Family 4.0  
- integration with Self‑Repair Layer  
- deterministic execution  

---

# 2. Filesystem Agent (FS‑AGENT 4.0)
**Purpose:** Safe, deterministic file operations.  
**Responsibilities:**
- moving, copying, deleting  
- path validation  
- safety checks  
- rollback‑safe operations  
- semantic routing (documents, code, schoolwork)  
- integration with Schoolwork Engine 4.0  

---

# 3. Natural Language Router (NL Router 4.0)
**Purpose:** Semantic interpretation and routing of user commands.  
**Responsibilities:**
- command classification  
- semantic extraction  
- routing to modules or plugins  
- plugin NL command detection  
- fallback interpretation  
- preventing ambiguous or unsafe actions  
- identity‑aware filtering (OWNER / FAMILY / STRANGER)  

---

# 4. Context Memory Engine (CME‑MEM 4.0)
**Purpose:** Semantic workflow context.  
**Responsibilities:**
- tracking recent actions  
- storing semantic tags  
- supporting multi‑step workflows  
- providing contextual hints  
- subject/difficulty metadata  
- integration with Schoolwork Engine 4.0  

---

# 5. Workflow Engine 4.0
**Purpose:** Deterministic multi‑step logic.  
**Responsibilities:**
- workflow state machine  
- plugin workflow execution  
- semantic transitions  
- preventing invalid sequences  
- SCHOOLWORK workflow prioritization  
- integration with Reasoning Engine 4.0  

---

# 6. GUI Layer 4.0
**Purpose:** Modular user interface.  
**Responsibilities:**
- rendering plugin UI  
- executing GUI actions  
- identity indicators  
- SCHOOLWORK indicators  
- future tray/voice integration  

---

# 7. Email Composer
**Purpose:** Generating email text (without sending).  
**Responsibilities:**
- email drafts  
- structured responses  
- professional text generation  

---

# 8. Automatic Input Triage Engine (AITE 4.0)
**Purpose:** Semantic detection and classification of all inputs.  
**Responsibilities:**
- detecting input type (text, image, code, document, installer)  
- OCR extraction  
- semantic analysis  
- subject detection  
- difficulty scoring  
- routing to correct modules  
- metadata generation  
- integration with FS‑AGENT, CME‑MEM  
- integration with Schoolwork Engine 4.0  
- integration with Reasoning Engine 4.0  
- ENVOY 4.0 support  

---

# 9. Windows System Capabilities Layer (WIN‑CAP 4.0)
**Purpose:** Safe, abstracted access to Windows 11 system functions.  
**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions and allowed scopes  
- safe wrappers around OS operations  
- multi‑step system actions  
- identity‑aware restrictions  

**Submodules:**
- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  
- `automation_ops`  

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
- integrating CME, FS‑AGENT, GUI  
- SCHOOLWORK workflow routing  

---

# 12. Plugin System 4.0
**Purpose:** Extensible plugin ecosystem.  
**Responsibilities:**
- loading plugin manifests  
- registering NL commands  
- registering AI tasks  
- registering workflows  
- registering reasoning hooks  
- registering GUI elements  
- safe plugin isolation  
- SCHOOLWORK‑aware plugin behavior  

Official plugins include:
- automation  
- clipboard  
- file_manager  
- notes  
- system_tools  
- translator  
- developer_tools  

---

# 13. AI Loop 4.0
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
- generating patch suggestions  
- preventing uncontrolled modifications  
- reporting system health to Runtime Core  

**Submodules:**  
- `health_check_engine.py`  
- `self_repair_safe.py`  
- `repair_suggestions.py`  

---

# 15. Security Family 4.0 (Identity Engine 2.0)
**Purpose:** Behavior‑based identity and family safety layer.  
**Responsibilities:**
- OWNER / FAMILY / STRANGER identity  
- behavior‑based recognition  
- safe‑mode for unknown users  
- restricted mode for children  
- time‑limits v2  
- Schoolwork Engine integration  
- identity‑aware routing  
- STRANGER‑mode restrictions  

**Submodules:**
- `identity_engine_v2.py`  
- `behavior_audit_v2.py`  
- `access_control_v2.py`  
- `family_mode_v2.py`  
- `stranger_mode_v2.py`  
- `time_limits_v2.py`  
- `schoolwork_engine.py`  
- `profile_store_v2.json`  

---

# 16. Intelligent Runtime Modules (v4.0.0)

These modules extend SIRIUS into a **full offline household, schoolwork, and developer assistant**.

---

## 16.1 HOME_ASSISTANT 4.0
**Purpose:** Household assistance.  
**Responsibilities:**
- cleaning, safety, organization  
- workflows  
- pack‑aware reasoning  
- IMAGE_ANALYZER integration  

---

## 16.2 COOKING_ADVISOR 4.0
**Purpose:** Offline cooking assistant.  
**Responsibilities:**
- recipe generation  
- ingredient reasoning  
- step‑by‑step workflows  
- Knowledge Packs integration  

---

## 16.3 DEVICE_DIAGNOSTICS 2.0
**Purpose:** Safe troubleshooting.  
**Responsibilities:**
- symptom detection  
- cause mapping  
- safety warnings  
- OWNER‑only actions  
- pack‑aware reasoning  

---

## 16.4 SCHOOL_HELPER 4.0
**Purpose:** Offline schoolwork assistant.  
**Responsibilities:**
- math, science, language reasoning  
- step‑by‑step explanations  
- Schoolwork Engine integration  
- image‑based homework recognition  

---

## 16.5 IMAGE_ANALYZER 4.0
**Purpose:** Local image understanding.  
**Responsibilities:**
- OCR  
- object detection  
- homework reading  
- routing to correct modules  

---

## 16.6 CONTEXT_ROUTER 4.0
**Purpose:** Semantic routing of user intent.  
**Responsibilities:**
- detecting household tasks  
- detecting cooking tasks  
- detecting device issues  
- detecting schoolwork  
- detecting developer tasks  
- routing to all v4 modules  

---

## 16.7 KNOWLEDGE_PACKS 4.0
**Purpose:** Offline knowledge expansions.  
**Responsibilities:**
- domain‑specific knowledge  
- curated datasets  
- semantic linking  
- pack‑aware reasoning  

---

# 17. SIRIUS ENVOY 4.0 (Safe Retrieval Layer)
**Purpose:** Optional isolated online retrieval.  
**Responsibilities:**
- outbound‑only requests  
- scraper layer  
- quarantine sandbox  
- validator & policy filter  
- safe payload delivery  
- updating Knowledge Packs  

ENVOY never sends local data outward.

---

# 18. Module Interconnections

- **NL Router → FS‑AGENT:** semantic file operations  
- **NL Router → Plugins:** NL command routing  
- **CME‑MEM → Workflow Engine:** semantic context  
- **AITE → FS‑AGENT:** input routing  
- **AITE → CME‑MEM:** metadata  
- **AITE → Schoolwork Engine:** subject/difficulty detection  
- **Security Family → Runtime Core:** identity‑based access control  
- **WIN‑CAP → Runtime Core:** privileged capability layer  
- **Runtime Core → all modules:** initialization & security  
- **Plugins → Runtime Core:** capability registration  
- **IMAGE_ANALYZER → SCHOOL_HELPER / DEVICE_DIAGNOSTICS / HOME_ASSISTANT**  
- **CONTEXT_ROUTER → all v4 modules**  
- **ENVOY → Knowledge Packs / Reasoning Engine**  

All communication is explicit, deterministic, and controlled.

---

# Document Status
Current version: **4.0.0 (Stable)**  
This document defines the complete module map for SIRIUS LOCAL AI v4.0.0.
