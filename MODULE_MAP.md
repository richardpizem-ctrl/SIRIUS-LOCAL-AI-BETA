# 🗺️ Module Map – SIRIUS LOCAL AI (v5.0.0 UNIFIED)

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map for the **Unified Runtime 5.0** architecture.

Version **5.0.0 UNIFIED** expands the module map with:

- **AITE 5.0 (Multimodal Semantic Triage)**  
- **Reasoning Engine 5.0**  
- **Workflow Engine 5.0**  
- **Knowledge Packs 5.0**  
- **UI Automation Engine 5.0**  
- **System Agent 5.0 (Safe Action Execution Layer)**  
- **Security Family 5.0 (Identity Engine 3.0)**  
- **ENVOY 5.0 (Safe External Retrieval)**  
- **Self‑Repair Layer 5.x**  
- **Mobile Runtime 5.0**  
- **Unified PC/Mobile deterministic routing**  

All processing is fully local; no data leaves the user's device.

---

# 1. Runtime Core 5.0 (Unified)
**Purpose:** Central orchestrator of the entire system.  
**Responsibilities:**
- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing capability boundaries  
- event routing  
- global system stability  
- integration with Security Family 5.0  
- integration with Self‑Repair Layer 5.x  
- deterministic execution  
- System Agent 5.0 routing  
- UI Automation Engine 5.0 integration  
- unified PC/Mobile behavior  

---

# 2. Filesystem Agent (FS‑AGENT 5.0)
**Purpose:** Safe, deterministic file operations.  
**Responsibilities:**
- moving, copying, deleting  
- path validation  
- rollback‑safe operations  
- semantic routing (documents, code, schoolwork)  
- integration with Schoolwork Engine 5.0  
- integration with UI Automation Engine 5.0  
- unified PC/Mobile filesystem logic  

---

# 3. Natural Language Router (NL Router 5.0)
**Purpose:** Semantic interpretation and routing of user commands.  
**Responsibilities:**
- command classification  
- semantic extraction  
- routing to modules or plugins  
- plugin NL command detection  
- fallback interpretation  
- preventing ambiguous or unsafe actions  
- identity‑aware filtering (OWNER / FAMILY / STRANGER)  
- UI automation command routing  
- System Agent 5.0 validation for system‑level intents  

---

# 4. Context Memory Engine (CME‑MEM 5.0)
**Purpose:** Semantic workflow context.  
**Responsibilities:**
- tracking recent actions  
- storing semantic tags  
- supporting multi‑step workflows  
- providing contextual hints  
- subject/difficulty metadata  
- integration with Schoolwork Engine 5.0  
- integration with UI Automation Engine 5.0  
- unified PC/Mobile context memory  

---

# 5. Workflow Engine 5.0
**Purpose:** Deterministic multi‑step logic.  
**Responsibilities:**
- workflow state machine  
- plugin workflow execution  
- semantic transitions  
- preventing invalid sequences  
- SCHOOLWORK workflow prioritization  
- integration with Reasoning Engine 5.0  
- integration with UIWorkflow 5.0  
- deterministic fallback behavior  
- unified PC/Mobile workflows  

---

# 6. GUI Layer 5.0
**Purpose:** Modular user interface.  
**Responsibilities:**
- rendering plugin UI  
- executing GUI actions  
- identity indicators  
- SCHOOLWORK indicators  
- tray/voice integration  
- UI automation visual feedback  
- unified PC/Mobile UI  

---

# 7. Email Composer
**Purpose:** Generating email text (without sending).  
**Responsibilities:**
- email drafts  
- structured responses  
- professional text generation  

---

# 8. Automatic Input Triage Engine (AITE 5.0)
**Purpose:** Multimodal semantic detection and classification of all inputs.  
**Responsibilities:**
- detecting input type (text, image, code, document, installer)  
- OCR extraction  
- semantic analysis  
- subject detection  
- difficulty scoring  
- routing to correct modules  
- metadata generation  
- integration with FS‑AGENT, CME‑MEM  
- integration with Schoolwork Engine 5.0  
- integration with Reasoning Engine 5.0  
- ENVOY 5.0 support  
- UI automation intent detection  
- identity‑aware triage 4.0  
- unified PC/Mobile triage  

---

# 9. Windows System Capabilities Layer (WIN‑CAP 5.0)
**Purpose:** Safe, abstracted access to Windows system functions.  
**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions and allowed scopes  
- safe wrappers around OS operations  
- multi‑step system actions  
- identity‑aware restrictions  
- UI automation OS‑level routing  
- System Agent 5.0 enforcement  

**Submodules:**
- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  
- `automation_ops`  
- `ui_capabilities_5_0`  

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
- UI automation workflow integration  
- unified PC/Mobile workflow logic  

---

# 12. Plugin System 5.x
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
- UI automation plugin hooks  
- unified PC/Mobile plugin behavior  

Official plugins include:
- automation  
- clipboard  
- file_manager  
- notes  
- system_tools  
- translator  
- developer_tools  

---

# 13. AI Loop 5.0
**Purpose:** Autonomous interval‑based logic.  
**Responsibilities:**
- executing plugin heartbeat rules  
- safe periodic tasks  
- deterministic scheduling  
- error protection  
- SCHOOLWORK‑aware timing  
- unified PC/Mobile loop behavior  

---

# 14. Self‑Repair & Health‑Check Layer (5.x)
**Purpose:** Diagnostics and safe automatic recovery.  
**Responsibilities:**  
- checking integrity of core modules  
- detecting corrupted states, missing files, invalid configs  
- performing safe automatic repairs  
- generating patch suggestions  
- preventing uncontrolled modifications  
- reporting system health to Runtime Core  
- validating UI automation modules  
- integration with System Agent 5.0  
- unified PC/Mobile diagnostics  

**Submodules:**  
- `health_check_engine.py`  
- `self_repair_safe.py`  
- `repair_suggestions.py`  

---

# 15. Security Family 5.0 (Identity Engine 3.0)
**Purpose:** Behavior‑based identity and family safety layer.  
**Responsibilities:**
- OWNER / FAMILY / STRANGER identity  
- behavior‑based recognition  
- safe‑mode for unknown users  
- restricted mode for children  
- time‑limits v3  
- Schoolwork Engine integration  
- identity‑aware routing  
- STRANGER‑mode restrictions  
- UI automation identity gating  
- System Agent 5.0 enforcement  

**Submodules:**
- `identity_engine_3_0.py`  
- `behavior_audit_3_0.py`  
- `access_control_3_0.py`  
- `family_mode_v3.py`  
- `stranger_mode_v3.py`  
- `time_limits_v3.py`  
- `schoolwork_engine_5_0.py`  
- `profile_store_v3.json`  

---

# 16. Intelligent Runtime Modules (v5.0)

## 16.1 HOME_ASSISTANT 5.0  
## 16.2 COOKING_ADVISOR 5.0  
## 16.3 DEVICE_DIAGNOSTICS 3.0  
## 16.4 SCHOOL_HELPER 5.0  
## 16.5 IMAGE_ANALYZER 5.0  
## 16.6 CONTEXT_ROUTER 5.0  
## 16.7 KNOWLEDGE_PACKS 5.0  

---

# 17. PASSWORD_VAULT 5.0
**Purpose:** Secure offline credential storage.  
**Responsibilities:**
- AES‑256‑GCM encrypted vault  
- PBKDF2‑HMAC‑SHA256 master key derivation  
- OWNER‑only write access  
- FAMILY read‑only access  
- STRANGER blocked  
- deterministic API for workflows  
- NL Router integration  
- Runtime Core integration  

---

# 18. UI Automation Engine 5.0
**Purpose:** Semantic, deterministic UI automation.  
**Responsibilities:**
- improved fuzzy UI parsing  
- semantic alias mapping  
- multi‑stage resolution pipeline  
- deterministic fallback logic  
- OS‑level routing  
- safe sandboxed execution  
- WIN‑CAP 5.0 integration  
- System Agent 5.0 validation  
- unified PC/Mobile automation  

**Submodules:**
- `ui_parser_5_0.py`  
- `ui_workflow_5_0.py`  
- `ui_actions_5_0.py`  
- `win_capabilities_5_0.py`  

---

# 19. System Agent 5.0
**Purpose:** Final gatekeeper for all system‑level actions.  
**Responsibilities:**
- validating every system action  
- enforcing identity rules  
- blocking unsafe operations  
- deterministic safety enforcement  
- logging system actions  
- protecting OS‑level automation  
- unified PC/Mobile execution  

**Submodules:**
- `agent_core_5_0.py`  
- `agent_rules_5_0.py`  
- `agent_validation_5_0.py`  

---

# 20. SIRIUS ENVOY 5.0 (Safe External Retrieval)
**Purpose:** Safe, outbound‑only external retrieval.  
**Responsibilities:**  
- scraper layer  
- quarantine sandbox  
- validator & policy filter  
- safe payload delivery  
- Knowledge Pack updates  
- identity‑aware sanitization  
- unified PC/Mobile behavior  

---

# 21. System Intelligence Layer 5.0
**Purpose:** Cross‑platform diagnostics and safe optimization.  
**Responsibilities:**
- hardware analysis  
- driver checks  
- service health  
- process analysis  
- optimization suggestions  
- deterministic system workflows  
- System Agent 5.0 enforcement  
- unified PC/Mobile diagnostics  

---

# 22. Mobile Runtime 5.0
**Purpose:** Unified mobile execution layer.  
**Responsibilities:**
- mobile‑optimized workflows  
- mobile filesystem logic  
- mobile UI automation  
- mobile AITE integration  
- mobile reasoning integration  

---

# 23. Module Interconnections
All modules communicate through:

- Runtime Core 5.0  
- NL Router 5.0  
- Workflow Engine 5.0  
- CME‑MEM 5.0  
- Security Family 5.0  
- WIN‑CAP 5.0  
- UI Automation Engine 5.0  
- System Agent 5.0  
- ENVOY 5.0  
- Self‑Repair Layer 5.x  
- Mobile Runtime 5.0  

---

# Document Status
**Version:** 5.0.0 UNIFIED  
Updated to reflect the **4.x → 5.0 transition**, new **System Agent 5.0**, and the **Unified Runtime Architecture**.
