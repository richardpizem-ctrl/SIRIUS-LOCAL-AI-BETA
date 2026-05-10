# 🧪 TESTING GUIDE – SIRIUS LOCAL AI (v3.0.0)

This document defines the testing strategy, procedures, and safety validation rules for the SIRIUS LOCAL AI project.  
All tests are fully local and must be executed manually by the user.

The system interacts with Windows 11 APIs, filesystem operations, window management, application control, identity‑based safety, and schoolwork‑aware routing.  
All behavior must remain deterministic, safe, and reversible.

---

# 1. Testing Philosophy

- all tests must be reproducible  
- no automated tests that modify the system without confirmation  
- every test must validate safety, predictability, and reversibility  
- tests must not rely on network access  
- tests must not require external dependencies  
- plugin tests must follow Plugin System 3.0 rules  
- WIN‑CAP tests must validate permission boundaries  
- workflows must behave deterministically  
- identity‑restricted actions must be enforced  
- **SECURITY FAMILY tests must validate identity, time‑limits, and schoolwork bypass logic**  
- **Schoolwork Priority Mode must always override restrictions**  

---

# 2. Test Categories

## A) Filesystem Tests (FS‑AGENT 3.0)
Validate:
- move, copy, delete  
- path validation  
- safety prompts  
- rollback behavior  
- protected directory blocking  
- identity‑restricted deletes  
- SCHOOLWORK file bypass behavior  

Checklist:
- invalid paths must be rejected  
- protected locations must be blocked  
- delete must require double confirmation  
- rollback must succeed on failure  
- no destructive action may run without explicit approval  
- FAMILY and STRANGER modes must block privileged operations  
- SCHOOLWORK files must always be allowed  

---

## B) Natural Language Router Tests (NL Router 3.0)
Validate:
- command recognition  
- parameter extraction  
- plugin NL command routing  
- ambiguity detection  
- confirmation prompts  
- identity‑aware routing  
- schoolwork‑aware routing  

Checklist:
- unclear commands must trigger clarification  
- missing parameters must trigger questions  
- no command executes automatically  
- plugin commands must route correctly  
- invalid commands must be rejected  
- OWNER‑only commands must be blocked in FAMILY/STRANGER modes  
- schoolwork commands must bypass restrictions  

---

## C) Workflow Engine Tests (Workflow Engine 3.0)
Validate:
- multi‑step sequences  
- state transitions  
- context memory behavior  
- plugin workflow execution  
- SCHOOLWORK workflow prioritization  
- identity‑restricted transitions  

Checklist:
- workflows must not skip steps  
- invalid transitions must be blocked  
- context must reset after completion  
- plugin workflows must follow deterministic rules  
- SCHOOLWORK workflows must always run  
- restricted workflows must be blocked in FAMILY/STRANGER modes  

---

## D) GUI Tests (GUI Layer 3.0)
Validate:
- confirmation dialogs  
- folder selection  
- safety warnings  
- plugin UI elements  
- identity‑aware UI states  
- SCHOOLWORK indicators  

Checklist:
- UI must never auto‑confirm  
- UI must show correct target paths  
- UI must block unsafe operations  
- plugin buttons must execute correct actions  
- FAMILY/STRANGER mode warnings must appear instantly  
- SCHOOLWORK mode must be visually indicated  

---

## E) WIN‑CAP Tests (WIN‑CAP 3.0)
Validate:
- window snapping  
- app launching  
- audio device switching  
- system context detection  
- capability boundaries  
- identity‑restricted system actions  

Checklist:
- actions must require confirmation  
- invalid operations must be rejected  
- system state must remain stable  
- no privileged action may bypass WIN‑CAP  
- OWNER‑only actions must be blocked in FAMILY/STRANGER modes  
- SCHOOLWORK actions must bypass restrictions  

---

## F) Plugin System Tests (Plugin System 3.0)
Validate:
- plugin loading  
- manifest parsing  
- NL command registration  
- workflow registration  
- AI loop rule execution  
- GUI element rendering  
- identity‑aware plugin behavior  

Checklist:
- plugins must load without errors  
- invalid plugins must be rejected  
- plugin isolation must be preserved  
- no plugin may access restricted capabilities  
- plugin workflows must follow Workflow Engine 3.0 rules  
- SCHOOLWORK‑aware plugins must behave deterministically  

---

## G) AI Loop Tests (AI Loop 3.0)
Validate:
- interval execution  
- plugin heartbeat rules  
- deterministic scheduling  
- safe error handling  
- identity‑aware timing  
- SCHOOLWORK‑aware timing  

Checklist:
- no blocking operations  
- no long‑running tasks  
- no infinite loops  
- plugin rules must not break runtime stability  
- time‑limit checks must be constant‑time  
- SCHOOLWORK tasks must never be delayed  

---

## H) SECURITY FAMILY Tests (v3.0.0)
Validate:
- identity classification (OWNER / FAMILY / STRANGER)  
- behavior‑based recognition  
- restricted mode for children  
- safe‑mode for unknown users  
- time‑limit enforcement  
- Schoolwork Priority Mode (schoolwork always allowed)  
- integration with NL Router, AITE, FS‑AGENT, WIN‑CAP  

Checklist:
- identity must be deterministic  
- time‑limits must trigger correctly  
- schoolwork must bypass restrictions instantly  
- stranger mode must block sensitive operations  
- no module may override SECURITY FAMILY decisions  
- OWNER‑only actions must be enforced correctly  

---

## I) Household Modules Tests (v3.0.0)
Modules:
- HOME_ASSISTANT  
- COOKING_ADVISOR  
- DEVICE_DIAGNOSTICS  
- SCHOOL_HELPER  
- IMAGE_ANALYZER  
- CONTEXT_ROUTER v3  

Validate:
- safe recommendations  
- deterministic routing  
- SCHOOLWORK detection  
- identity‑restricted actions  
- safe fallback behavior  

Checklist:
- SCHOOL_HELPER must always run  
- IMAGE_ANALYZER must detect homework reliably  
- DEVICE_DIAGNOSTICS must block OWNER‑only actions in FAMILY/STRANGER modes  
- HOME_ASSISTANT must avoid unsafe suggestions  
- CONTEXT_ROUTER must route tasks correctly  

---

# 3. Test Execution Rules

- run tests in a clean environment  
- close unnecessary applications  
- avoid testing on system‑critical directories  
- verify each step manually  
- log results in plain text  
- repeat tests after major module changes  
- plugin tests must be isolated  
- SECURITY FAMILY tests must be performed with multiple user profiles  
- SCHOOLWORK tests must include real academic tasks  

---

# 4. Logging Format

Format:
`[MODULE] action – status – notes`

Examples:
- `[FS-AGENT] delete_file – blocked – protected directory`  
- `[WIN-CAP] snap_window – confirmed – window positioned left`  
- `[PLUGIN:notes] create_note – success – workflow completed`  
- `[SECURITY_FAMILY] time_limit_check – enforced – child profile exceeded limit`  
- `[SECURITY_FAMILY] schoolwork_detected – bypass – restrictions lifted`  
- `[AITE] classify_input – schoolwork – priority mode enabled`  

---

# 5. Document Status

Current version: **3.0.0 (Stable)**  
This guide evolves with new modules and capabilities.
