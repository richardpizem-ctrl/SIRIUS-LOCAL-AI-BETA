# 🔐 SECURITY FAMILY 5.x — Identity Engine 3.1 & Unified Permission Framework  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.x (Updated for 5.9.1 UNIFIED)  
**Component:** Security Family  
**Role:** Identity enforcement, permission gating, terminal decoupling, dual-language graph isolation, COLNÍK Guard shell access control, Token Guard sanitization, HitL Safe Trash governance, and orchestrator-supervised security logic

---

## 🎯 Purpose  
Security Family 5.x is the unified identity, permission, and system protection layer of SIRIUS Local AI (v5.9.1).  
It ensures that every natural language query, workflow transition, compound noun phrase evaluation (`InputParser5`), Knowledge Graph mutation across dual-language stores (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN), native entity merge (`kg merge`), reasoning derivation, and host system operation is validated through identity profiles, deep symbolic explainability, single-process orchestration (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore), interactive `PanelAPI` confirmation loops with confirmation state latching, `Guard` supervision, COLNÍK Guard command blocking (0.0s), Human-in-the-Loop Safe Trash review, Token Guard sanitization, and AUTONOMY‑6.x governance.

Security Family protects the local workstation from unauthorized access, destructive shell executions, unverified file deletions, erratic execution loops, cross-domain contamination, cross-lingual graph corruption, and terminal shell hijacking.

---

## 🧩 Architecture Overview  
**Identity Engine 3.1 → Token Guard → Security Family 5.x → InputParser5 (.rstrip("?")) → sirius_orchestrator.py (Port 8080) → COLNÍK Guard (0.0s Block) → System Agent 5 → AUTONOMY 6.x → COLNIK-6.x → PanelAPI [ÁNO/NIE] / [YES/NO] → HitL Safe Trash / Dual KG Commit (`autosave_kg.json` / `autosave_kg_en.json`)**

### Core Responsibilities  
- enforce identity access tiers (OWNER / FAMILY / STRANGER) in constant time ($O(1)$)  
- sanitize raw inputs via Token Guard, instantly rejecting forbidden characters (`@#$%^&*`)  
- strip trailing punctuation (`.rstrip("?")`) to preserve clean entity lookup identifiers  
- maintain confirmation state latching across conversation turns for pending proposals  
- enforce COLNÍK Guard shell security (0.0s hard blocking of `format`, `diskpart`, `rmdir /s`, etc.)  
- govern the Human-in-the-Loop Safe Trash pipeline (diverting file removals to quarantine, requiring manual approval via `GET /trash`)  
- preserve linguistic isolation between Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) knowledge graphs  
- supervise native lossless entity mergers (`kg merge <src> into <tgt>`)  
- auto-commit verified taxonomical categories (`KG_VERIFY`) with zero proposal recurrence  
- enforce terminal input decoupling (`currentModule = "none"`) upon query clearance  
- supply derivation metadata for `KG_EXPLAIN` and `KG_EXPLAIN_DEEP` proof trees  
- enforce the 100-file sliding-window quarantine ceiling in `COLNIK-6.x/envoy/quarantine/`  
- coordinate real-time hardware telemetry and threat containment with Guard  
- route suspicious payloads safely into `COLNIK-6.x/triage`  

### Key Files  
- `security_family/security_family.py`  
- `security_family/identity_engine_3_1.py`  
- `security_family/identity_modes.json`  
- `security_family/permissions.json`  
- `security_family/family_safety_rules5_x.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/security_events.json`  

---

## 🔍 Identity Modes & Access Profiles  

### **OWNER Mode**  
Full administrative and root access tier:  
- unrestricted execution of safe workflows, local system tasks, and developer comfort commands  
- authorized to perform atomic Knowledge Graph modifications, native entity merges (`kg merge`), and exports  
- sensitive or destructive actions gate through interactive `PanelAPI` confirmation (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching  
- final review and purge authorization for quarantined files via Human-in-the-Loop Safe Trash (`GET /trash`)  

### **FAMILY Mode**  
Trusted household access tier:  
- full access to conversational reasoning, academic tasks, household guides, and safe file browsing  
- read-only access to Password Vault shared credentials  
- blocked from administrative OS mutations, raw shell executions, and destructive file deletions  
- protected from dangerous shell commands via automatic COLNÍK Guard interception  

### **STRANGER Mode**  
Zero-trust restricted sandbox:  
- immediately isolates user session upon unrecognized behavioral markers or access requests  
- completely blocks Knowledge Graph mutations, file modifications, and OS-level execution  
- forces terminal detachment and locks module state (`currentModule = "none"`)  

### **SCHOOLWORK Mode (Guaranteed Academic Bypass)**  
Deterministic educational bypass governed by Schoolwork Engine 5.8:  
- academic inquiries, homework assistance, and educational lookups bypass household time limits and restrictions with zero latency  
- fully permitted for Knowledge Graph navigation, multi-hop reasoning, and educational ENVOY retrieval  
- strictly blocks OS automation and administrative system mutations  

---

## 🔍 Permission & Gating Pipeline (v5.9.1)  

### **1 — Identity Verification, Token Guard & Input Sanitization**  
Before query processing begins:  
- evaluates caller profile in constant time ($O(1)$)  
- checks input against **Token Guard**: immediately drops payloads containing forbidden symbols (`@`, `#`, `$`, `%`, `^`, `&`, `*`)  
- applies **trailing punctuation stripping** (`.rstrip("?")`) to preserve canonical entity identifiers (e.g., `CO JE MACROPUS?` resolves to `macropus`)  
- invokes `InputParser5` to isolate copula verbs (`je`, `sú`, `is`, `are`) and preserve compound noun phrases without token truncation  
- applies STRANGER lockdown if caller identity fails verification  

---

### **2 — Host Command Security: COLNÍK Guard (TerminalAssistant)**  
When terminal or shell commands are invoked:  
- **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs  
- **RISKY (Explicit Prompt):** `rm`, `kill`, `taskkill`, `del`  
- **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`  
- Profiles execution latency via TimeCore `cycle_delta()` and applies multi-stage character decoding fallback (UTF-8 -> CP1250 -> CP852)  

---

### **3 — Human-in-the-Loop Safe UI Trash Governance**  
Protects the local filesystem from unintended data destruction:  
- operations proposing file deletion (duplicates, empty folders, cleanup) are intercepted  
- direct disk deletion is blocked; files are moved to quarantine storage  
- files remain held until explicit manual review and approval via `GET /trash`  

---

### **4 — Symbolic Explainability & Proof-Tree Enforcement**  
Every identity-relevant decision compiles an auditable provenance trace:  
- `KG_EXPLAIN` direct relation justification  
- `KG_EXPLAIN_DEEP` hierarchical multi-hop proof trees (ASCII + HTML)  
- applied security rules (`IdentityAccessRule`, `FamilySafetyRules5_x`, `ColnikGuardRule`)  
- confidence metrics and permission rationale  

Explainability is mandatory for all access decisions.

---

### **5 — Terminal State Decoupling Guard**  
To prevent conversational queries or failed commands from capturing host console input:  
- clearing an input field or canceling a prompt immediately triggers `currentModule = "none"`  
- completely isolates the web-based Terminal Panel on port 8080 from executing raw host shell binaries  
- prevents command injection and UI state lockups  

---

### **6 — COLNIK‑6.x Customs Clearance (Standard & IPC Mode)**  
All operations pass through the Kýklos customs gate:  
- enterprise-grade structural and cycle-safety checks  
- validation against Non-Bio Domain Shield (no habitat metadata on technical concepts)  
- verification of Anti-Prefix and Anti-Drift guards  
- sliding-window quarantine rotation enforcement (100-file ceiling in `COLNIK-6.x/envoy/quarantine/`)  
- threat classification and payload inspection across high-performance IPC  
- unverified, malformed, or suspicious mutations are routed to `COLNIK-6.x/triage`  

---

### **7 — AUTONOMY 6.x Governance, Confirmation Latching & Zero Recurrence**  
Supervised learning and state transitions:  
- unindexed concepts trigger structured proposals (`kg.learn_proposal`) bound to active language stores (`SK` / `EN`)  
- confirmation states remain latched in memory across turns so affirmative responses (`ÁNO` / `YES`) execute reliably  
- **Zero Proposal Recurrence:** once approved, the entity is committed to `autosave_kg.json` or `autosave_kg_en.json`; subsequent lookups and deduced taxonomies (`KG_VERIFY`) resolve instantly from memory without duplicate confirmation loops  

---

### **8 — Dual-Language KG Mutation & Native Merge Protection**  
Security Family audits all Knowledge Graph write requests:  
- preserves linguistic separation: Slovak entities persist to `autosave_kg.json`; English entities persist to `autosave_kg_en.json`  
- validates native lossless entity merges (`kg merge`), ensuring zero property loss and verifying directional alias links (`src -[alias]-> tgt`)  
- verifies that compound phrases retain contextual integrity  
- enforces atomic dual serialization  

---

## 🧱 Protection Layers  

### **Identity & Behavioral Layer**  
- OWNER / FAMILY / STRANGER / SCHOOLWORK modes  
- constant-time classification without background biometric monitoring  
- outbound ENVOY permission enforcement  

### **Input Hygiene & Command Security Layer**  
- Token Guard input sanitization blocking `@#$%^&*`  
- greedy trailing punctuation stripping (`.rstrip("?")`)  
- COLNÍK Guard 0.0s hard blocking of destructive shell commands  
- Human-in-the-Loop Safe UI Trash quarantine pipeline  

### **Semantic & Domain Integrity Layer**  
- compound phrase preservation via `InputParser5`  
- Non-Bio Domain Shield and Sentence-Bound habitat filtering via `EnvoyNormalizer5`  
- Anti-Prefix Guard blocking semantic drift (*Káva* -> *Kavala*)  
- Reverse habitat querying with False-Positive Flora Guard  

### **Execution & Terminal Decoupling Layer**  
- single-process orchestration via `sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore  
- automatic state reset (`currentModule = "none"`) on input clear  
- System Agent 5 OS-action validation and reversibility checks  

### **Knowledge & Persistence Layer**  
- isolated dual-language graph stores (`autosave_kg.json` & `autosave_kg_en.json`)  
- native lossless entity merge engine (`kg merge`)  
- automated taxonomical category deduction (`KG_VERIFY`) with edge auto-commits  
- 100-file sliding-window quarantine rotation  
- multi-hop proof-tree generation in `KG_EXPLAIN_DEEP`  

---

## 🔐 Safety Rules  
- ❌ No execution of forbidden host OS commands (0.0s block via COLNÍK Guard)  
- ⛔ Immediate Token Guard rejection on inputs containing malformed symbols (`@#$%^&*`)  
- 🗄️️ Strict dual-language isolation: SK and EN graphs must never cross-contaminate  
- 🗑️ No direct unverified disk deletions: file removals must route through HitL Safe Trash (`GET /trash`)  
- 🔒 Mandatory customs clearance via COLNIK‑6.x (Standard & High-Performance IPC Mode)  
- 🛡 Supervised decision gating via AUTONOMY 6.x (Control, Guard, Safe Trash & Triage Mode)  
- 💬 Interactive human-in-the-loop validation via `PanelAPI` `[ÁNO/NIE]` / `[YES/NO]` with confirmation state latching  
- 🛑 Terminal state decoupling must trigger `currentModule = "none"` upon input reset  
- 🚫 Strict non-biological domain shields active across all external data ingestion  
- 📦 Automatic quarantine sliding-window rotation enforcing 100-file ceiling  
- 🔁 Zero proposal recurrence on established entities, aliases, and deduced taxonomies  
- ⚠ Deterministic proof-tree explainability required for all decisions  
- 📉 Real-time hardware telemetry (CPU, RAM, Disk) monitored via Guard  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully implemented & synchronized with Runtime 5.9.1 architecture  
- ✔ Identity access tiers verified (OWNER / FAMILY / STRANGER)  
- ✔ Token Guard input sanitization active  
- ✔ Trailing punctuation trimming (`.rstrip("?")`) and confirmation state latching verified  
- ✔ COLNÍK Guard shell access control (0.0s block on `format`/`diskpart`) operational  
- ✔ Human-in-the-Loop Safe UI Trash pipeline verified  
- ✔ Sliding-window quarantine rotation operational (100-file ceiling)  
- ✔ Dual-language graph isolation (`autosave_kg.json` & `autosave_kg_en.json`) operational  
- ✔ Native lossless entity merge (`kg merge`) validated  
- ✔ Taxonomical category inference auto-commit (`KG_VERIFY`) verified  
- ✔ Reverse habitat engine with anti-flora guard operational  
- ✔ Terminal decoupling and module state reset confirmed  
- ✔ Single-process orchestrator integration on port 8080 operational with embedded TerminalAssistant + TimeCore  
- ✔ PanelAPI interactive confirmation loops verified  
- ✔ TimeCore temporal tracking (`cycle_delta()`) and Guard resource telemetry active  
- ✔ COLNIK‑6.x customs validation functional (Standard & IPC Mode)  
- ✔ AUTONOMY 6.x governance and triage containment verified  
- ✔ Complete 4-Panel UI Suite synchronization operational  

---

## 🏁 Summary  
Security Family 5.x is the unified identity and permission enforcement framework of SIRIUS Local AI (v5.9.1).  
It validates every query, workflow, dual-language Knowledge Graph mutation, native entity merge, reasoning step, shell command, and system operation through identity tiers, entry-level Token Guard sanitization, COLNÍK Guard 0.0s shell protection, Human-in-the-Loop Safe Trash, deep symbolic explainability, central orchestrator execution, confirmation state latching, COLNIK‑6.x customs validation, and AUTONOMY‑6.x governance.

It ensures that SIRIUS operates on local workstations **safely, deterministically, identity‑aware, linguistically segregated, shielded from destructive actions, and with verifiable explainability**.
