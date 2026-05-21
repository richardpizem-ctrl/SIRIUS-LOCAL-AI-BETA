# 🗺️ Module Map – SIRIUS LOCAL AI (v4.4.0 PRO EXPANDED)

This document defines all modules of the project, their purpose, responsibilities, and interconnections.  
It serves as an architectural orientation map for the **Intelligent Runtime 4.x** architecture.

Version **4.4.0 PRO** expands the module map with:
- **AITE 4.4 (Multimodal Semantic Triage)**  
- **Reasoning Engine 4.4**  
- **Workflow Engine 4.4**  
- **Knowledge Packs 4.4**  
- **UI Automation Engine 4.4**  
- **System Agent 4.2 (Safe Action Execution Layer)**  
- hardened SECURITY FAMILY 4.4  
- upgraded System Intelligence Layer 4.4  

All processing is fully local; no data leaves the user's PC.

---

# 1. Runtime Core 4.x
**Purpose:** Central orchestrator of the entire system.  
**Responsibilities:**
- module initialization  
- lifecycle management  
- plugin loading  
- task and workflow dispatch  
- enforcing capability boundaries  
- event routing  
- global system stability  
- integration with Security Family 4.4  
- integration with Self‑Repair Layer  
- deterministic execution  
- System Agent 4.2 routing  
- UI Automation Engine 4.4 integration  

---

# 2. Filesystem Agent (FS‑AGENT 4.x)
**Purpose:** Safe, deterministic file operations.  
**Responsibilities:**
- moving, copying, deleting  
- path validation  
- rollback‑safe operations  
- semantic routing (documents, code, schoolwork)  
- integration with Schoolwork Engine 4.4  
- integration with UI Automation Engine 4.4 (file‑based workflows)  

---

# 3. Natural Language Router (NL Router 4.x)
**Purpose:** Semantic interpretation and routing of user commands.  
**Responsibilities:**
- command classification  
- semantic extraction  
- routing to modules or plugins  
- plugin NL command detection  
- fallback interpretation  
- preventing ambiguous or unsafe actions  
- identity‑aware filtering (OWNER / FAMILY / STRANGER)  
- UI automation command routing (v4.4.0)  
- System Agent 4.2 validation for system‑level intents  

---

# 4. Context Memory Engine (CME‑MEM 4.x)
**Purpose:** Semantic workflow context.  
**Responsibilities:**
- tracking recent actions  
- storing semantic tags  
- supporting multi‑step workflows  
- providing contextual hints  
- subject/difficulty metadata  
- integration with Schoolwork Engine 4.4  
- integration with UI Automation Engine 4.4 (contextual UI hints)  

---

# 5. Workflow Engine 4.4
**Purpose:** Deterministic multi‑step logic.  
**Responsibilities:**
- workflow state machine  
- plugin workflow execution  
- semantic transitions  
- preventing invalid sequences  
- SCHOOLWORK workflow prioritization  
- integration with Reasoning Engine 4.4  
- integration with UIWorkflow 4.4  
- deterministic fallback behavior  

---

# 6. GUI Layer 4.x
**Purpose:** Modular user interface.  
**Responsibilities:**
- rendering plugin UI  
- executing GUI actions  
- identity indicators  
- SCHOOLWORK indicators  
- future tray/voice integration  
- UI automation visual feedback (v4.4.0)  

---

# 7. Email Composer
**Purpose:** Generating email text (without sending).  
**Responsibilities:**
- email drafts  
- structured responses  
- professional text generation  

---

# 8. Automatic Input Triage Engine (AITE 4.4)
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
- integration with Schoolwork Engine 4.4  
- integration with Reasoning Engine 4.4  
- ENVOY 4.0 support  
- UI automation intent detection (v4.4.0)  
- identity‑aware triage 3.1  

---

# 9. Windows System Capabilities Layer (WIN‑CAP 4.x)
**Purpose:** Safe, abstracted access to Windows 11 system functions.  
**Responsibilities:**
- exposing high‑level system capabilities  
- enforcing permissions and allowed scopes  
- safe wrappers around OS operations  
- multi‑step system actions  
- identity‑aware restrictions  
- UI automation OS‑level routing (v4.4.0)  
- System Agent 4.2 enforcement  

**Submodules:**
- `file_ops`  
- `app_ops`  
- `window_ops`  
- `audio_ops`  
- `system_context`  
- `automation_ops`  
- `ui_capabilities_4_4` (UPDATED)  

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
- UI automation workflow integration (v4.4.0)  

---

# 12. Plugin System 4.x
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
- UI automation plugin hooks (v4.4.0)  

Official plugins include:
- automation  
- clipboard  
- file_manager  
- notes  
- system_tools  
- translator  
- developer_tools  

---

# 13. AI Loop 4.x
**Purpose:** Autonomous interval‑based logic.  
**Responsibilities:**
- executing plugin heartbeat rules  
- safe periodic tasks  
- deterministic scheduling  
- error protection  
- SCHOOLWORK‑aware timing  

---

# 14. Self‑Repair & Health‑Check Layer (v4.x)
**Purpose:** Diagnostics and safe automatic recovery.  
**Responsibilities:**  
- checking integrity of core modules  
- detecting corrupted states, missing files, invalid configs  
- performing safe automatic repairs  
- generating patch suggestions  
- preventing uncontrolled modifications  
- reporting system health to Runtime Core  
- validating UI automation modules (v4.4.0)  
- integration with System Agent 4.2  

**Submodules:**  
- `health_check_engine.py`  
- `self_repair_safe.py`  
- `repair_suggestions.py`  

---

# 15. Security Family 4.4 (Identity Engine 2.0)
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
- UI automation identity gating (v4.4.0)  
- System Agent 4.2 enforcement  

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

# 16. Intelligent Runtime Modules (v4.x)

## 16.1 HOME_ASSISTANT 4.0  
## 16.2 COOKING_ADVISOR 4.0  
## 16.3 DEVICE_DIAGNOSTICS 2.0  
## 16.4 SCHOOL_HELPER 4.0  
## 16.5 IMAGE_ANALYZER 4.0  
## 16.6 CONTEXT_ROUTER 4.0  
## 16.7 KNOWLEDGE_PACKS 4.4 (UPDATED)  

---

# 17. PASSWORD_VAULT 4.0
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

# 18. UI Automation Engine 4.4 (UPDATED)
**Purpose:** Semantic, deterministic UI automation.  
**Responsibilities:**
- improved fuzzy UI parsing  
- semantic alias mapping  
- multi‑stage resolution pipeline  
- deterministic fallback logic  
- OS‑level routing  
- safe sandboxed execution  
- WIN‑CAP 4.4 integration  
- System Agent 4.2 validation  

**Submodules:**
- `ui_parser_4_4.py`  
- `ui_workflow_4_4.py`  
- `ui_actions_4_4.py`  
- `win_capabilities_4_4.py`  

---

# 19. System Agent 4.2 (NEW)
**Purpose:** Final gatekeeper for all system‑level actions.  
**Responsibilities:**
- validating every system action  
- enforcing identity rules  
- blocking unsafe operations  
- deterministic safety enforcement  
- logging system actions  
- protecting OS‑level automation  

**Submodules:**
- `agent_core_4_2.py`  
- `agent_rules_4_2.py`  
- `agent_validation_4_2.py`  

---

# 20. SIRIUS ENVOY 4.0 (Safe Retrieval Layer)
**Purpose:** Safe, outbound‑only online retrieval.  
**Responsibilities:**  
- scraper layer  
- quarantine sandbox  
- validator & policy filter  
- safe payload delivery  
- Knowledge Pack updates  

---

# 21. Module Interconnections
All modules communicate through:

- Runtime Core 4.x  
- NL Router 4.x  
- Workflow Engine 4.4  
- CME‑MEM 4.x  
- Security Family 4.4  
- WIN‑CAP 4.x  
- UI Automation Engine 4.4  
- System Agent 4.2  

---

# Document Status
**Version:** 4.4.0 PRO (Expanded)  
Updated to reflect the **4.3 → 4.4 transition**, new **System Agent 4.2**, and the upgraded **UI Automation Engine 4.4**.
