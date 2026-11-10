# 🔐 SECURITY FAMILY 6.0.1 — Identity Engine 3.1 & Unified Permission Framework  
**Status:** ✔ Active (Enhanced)  
**Version:** 6.0.1 (Updated for 6.0.1 UNIFIED)  
**Component:** Security Family  
**Role:** Identity enforcement, permission gating, terminal decoupling, dual-language graph isolation, COLNÍK Guard shell access control, Token Guard sanitization, HitL Safe Trash governance, SafeRollback crash protection, Professor Middleware verification, and orchestrator-supervised security logic

---

## 🎯 Purpose  
Security Family 6.0.1 is the unified identity, permission, and system protection layer of SIRIUS Local AI (v6.0.1).  
It ensures that every natural language query, workflow transition, compound noun phrase evaluation (`InputParser5`), Knowledge Graph mutation across dual-language stores (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN), native entity merge (`kg merge`), reasoning derivation, and host system operation is validated through identity profiles, deep symbolic explainability, single-process orchestration (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore), interactive `PanelAPI` confirmation loops with confirmation state latching, `Guard` supervision, COLNÍK Guard command blocking (0.0s), Human-in-the-Loop Safe Trash review (tested in `dist_V6_CHECK`), SafeRollback backup protection (`safe_rollback.py`), Professor Middleware cognitive verification (`PASS / WARN / REJECT`), Token Guard sanitization, and AUTONOMY‑6.x governance.

Security Family protects the local workstation from unauthorized access, destructive shell executions, unverified file deletions, erratic execution loops, cross-domain contamination, cross-lingual graph corruption, and terminal shell hijacking.

---

## 🧩 Architecture Overview  
**Identity Engine 3.1 → Token Guard → Security Family 6.0.1 → InputParser5 (.rstrip("?")) → sirius_orchestrator.py (Port 8080) → COLNÍK Guard (0.0s Block) → System Agent 5 → Professor Validator (PASS/WARN/REJECT) → AUTONOMY 6.x → COLNIK-6.x → PanelAPI [ÁNO/NIE] / [YES/NO] → HitL Safe Trash (dist_V6_CHECK) / Dual KG Commit (`autosave_kg.json` / `autosave_kg_en.json`)**

### Core Responsibilities  
- enforce identity access tiers (OWNER / FAMILY / STRANGER) in constant time ($O(1)$)[cite: 1]  
- sanitize raw inputs via Token Guard, instantly rejecting forbidden characters (`@#$%^&*`)[cite: 1]  
- strip trailing punctuation (`.rstrip("?")`) to preserve clean entity lookup identifiers[cite: 1]  
- maintain confirmation state latching across conversation turns for pending proposals[cite: 1]  
- enforce COLNÍK Guard shell security (0.0s hard blocking of `format`, `diskpart`, `rmdir /s`, etc.)[cite: 1]  
- govern the Human-in-the-Loop Safe Trash pipeline (diverting file removals to quarantine, requiring manual approval via `GET /trash`, tested in `dist_V6_CHECK`)[cite: 1]  
- protect module states using SafeRollback (`safe_rollback.py`)[cite: 1]  
- enforce cognitive validation via Professor Middleware (`professor_validator.py`)[cite: 1]  
- preserve linguistic isolation between Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) knowledge graphs[cite: 1]  
- supervise native lossless entity mergers (`kg merge <src> into <tgt>`)[cite: 1]  
- auto-commit verified taxonomical categories (`KG_VERIFY`) with zero proposal recurrence[cite: 1]  
- enforce terminal input decoupling (`currentModule = "none"`) upon query clearance[cite: 1]  
- supply derivation metadata for `KG_EXPLAIN` and `KG_EXPLAIN_DEEP` proof trees[cite: 1]  
- enforce the 100-file sliding-window quarantine ceiling in `COLNIK-6.x/envoy/quarantine/`[cite: 1]  
- coordinate real-time hardware telemetry and threat containment with Guard[cite: 1]  
- route suspicious payloads safely into `COLNIK-6.x/triage`[cite: 1]  

### Key Files  
- `security_family/security_family.py`  
- `security_family/identity_engine_3_1.py`  
- `security_family/identity_modes.json`  
- `security_family/permissions.json`  
- `security_family/family_safety_rules5_x.py`  
- `core/safe_rollback.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/professor_validator.py`  
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
- final review and purge authorization for quarantined files via Human-in-the-Loop Safe Trash (`GET /trash`, tested in `dist_V6_CHECK`)  

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

## 🔍 Permission & Gating Pipeline (v6.0.1)  

### **1 — Identity Verification, Token Guard & Input Sanitization**  
Before query processing begins:  
- evaluates caller profile in constant time ($O(1)$)[cite: 1]  
- checks input against **Token Guard**: immediately drops payloads containing forbidden symbols (`@`, `#`, `$`, `%`, `^`, `&`, `*`)[cite: 1]  
- applies **trailing punctuation stripping** (`.rstrip("?")`) to preserve canonical entity identifiers (e.g., `CO JE MACROPUS?` resolves to `macropus`)[cite: 1]  
- invokes `InputParser5` to isolate copula verbs (`je`, `sú`, `is`, `are`) and preserve compound noun phrases without token truncation[cite: 1]  
- applies STRANGER lockdown if caller identity fails verification[cite: 1]  

---

### **2 — Host Command Security: COLNÍK Guard (TerminalAssistant)**  
When terminal or shell commands are invoked:  
- **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs[cite: 1]  
- **RISKY (Explicit Prompt):** `rm`, `kill`, `taskkill`, `del`[cite: 1]  
- **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`[cite: 1]  
- Profiles execution latency via TimeCore `cycle_delta()` and applies multi-stage character decoding fallback (UTF-8 -> CP1250 -> CP852)[cite: 1]  

---

### **3 — Human-in-the-Loop Safe UI Trash Governance**  
Protects the local filesystem from unintended data destruction:  
- operations proposing file deletion (duplicates, empty folders, cleanup) are intercepted[cite: 1]  
- direct disk deletion is blocked; files are moved to quarantine storage[cite: 1]  
- files remain held until explicit manual review and approval via `GET /trash` (tested in `dist_V6_CHECK`)[cite: 1]  

---

### **4 — SafeRollback Crash Protection & Professor Verification**  
Before executing state mutations:  
- `safe_rollback.py` creates granular module backups via `shutil.copytree`[cite: 1]  
- Professor Middleware evaluates cognitive fact quality (`PASS / WARN / REJECT`), blocking unreliable or contradictory data before graph commit[cite: 1]  

---

### **5 — Symbolic Explainability & Proof-Tree Enforcement**  
Every identity-relevant decision compiles an auditable provenance trace:  
- `KG_EXPLAIN` direct relation justification[cite: 1]  
- `KG_EXPLAIN_DEEP` hierarchical multi-hop proof trees (ASCII + HTML)[cite: 1]  
- applied security rules (`IdentityAccessRule`, `FamilySafetyRules5_x`, `ColnikGuardRule`)[cite: 1]  
- confidence metrics and permission rationale[cite: 1]  

Explainability is mandatory for all access decisions.

---

### **6 — Terminal State Decoupling Guard**  
To prevent conversational queries or failed commands from capturing host console input:  
- clearing an input field or canceling a prompt immediately triggers `currentModule = "none"`[cite: 1]  
- completely isolates the web-based Terminal Panel on port 8080 from executing raw host shell binaries[cite: 1]  
- prevents command injection and UI state lockups[cite: 1]  

---

### **7 — COLNIK‑6.x Customs Clearance (Standard & IPC Mode)**  
All operations pass through the Kýklos customs gate:  
- enterprise-grade structural and cycle-safety checks[cite: 1]  
- validation against Non-Bio Domain Shield (no habitat metadata on technical concepts)[cite: 1]  
- verification of Anti-Prefix and Anti-Drift guards[cite: 1]  
- sliding-window quarantine rotation enforcement (100-file ceiling in `COLNIK-6.x/envoy/quarantine/`)[cite: 1]  
- threat classification and payload inspection across high-performance IPC[cite: 1]  
- unverified, malformed, or suspicious mutations are routed to `COLNIK-6.x/triage`[cite: 1]  

---

### **8 — AUTONOMY 6.x Governance, Confirmation Latching & Zero Recurrence**  
Supervised learning and state transitions:  
- unindexed concepts trigger structured proposals (`kg.learn_proposal`) bound to active language stores (`SK` / `EN`)[cite: 1]  
- confirmation states remain latched in memory across turns so affirmative responses (`ÁNO` / `YES`) execute reliably[cite: 1]  
- **Zero Proposal Recurrence:** once approved, the entity is committed to `autosave_kg.json` or `autosave_kg_en.json`; subsequent lookups and deduced taxonomies (`KG_VERIFY`) resolve instantly from memory without duplicate confirmation loops[cite: 1]  

---

### **9 — Dual-Language KG Mutation & Native Merge Protection**  
Security Family audits all Knowledge Graph write requests:  
- preserves linguistic separation: Slovak entities persist to `autosave_kg.json`; English entities persist to `autosave_kg_en.json`[cite: 1]  
- validates native lossless entity merges (`kg merge`), ensuring zero property loss and verifying directional alias links (`src -[alias]-> tgt`)[cite: 1]  
- verifies that compound phrases retain contextual integrity[cite: 1]  
- enforces atomic dual serialization[cite: 1]  

---

## 🧱 Protection Layers  

### **Identity & Behavioral Layer**  
- OWNER / FAMILY / STRANGER / SCHOOLWORK modes[cite: 1]  
- constant-time classification without background biometric monitoring[cite: 1]  
- outbound ENVOY permission enforcement[cite: 1]  

### **Input Hygiene & Command Security Layer**  
- Token Guard input sanitization blocking `@#$%^&*`[cite: 1]  
- greedy trailing punctuation stripping (`.rstrip("?")`)[cite: 1]  
- COLNÍK Guard 0.0s hard blocking of destructive shell commands[cite: 1]  
- Human-in-the-Loop Safe UI Trash quarantine pipeline (tested in `dist_V6_CHECK`)[cite: 1]  

### **Semantic & Domain Integrity Layer**  
- compound phrase preservation via `InputParser5`[cite: 1]  
- Non-Bio Domain Shield and Sentence-Bound habitat filtering via `EnvoyNormalizer5`[cite: 1]  
- Anti-Prefix Guard blocking semantic drift (*Káva* -> *Kavala*)[cite: 1]  
- Reverse habitat querying with False-Positive Flora Guard[cite: 1]  

### **Execution & Terminal Decoupling Layer**  
- single-process orchestration via `sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore[cite: 1]  
- automatic state reset (`currentModule = "none"`) on input clear[cite: 1]  
- System Agent 5 OS-action validation and reversibility checks[cite: 1]  

### **Knowledge & Persistence Layer**  
- isolated dual-language graph stores (`autosave_kg.json` & `autosave_kg_en.json`)[cite: 1]  
- native lossless entity merge engine (`kg merge`)[cite: 1]  
- automated taxonomical category deduction (`KG_VERIFY`) with edge auto-commits[cite: 1]  
- SafeRollback crash protection (`safe_rollback.py`)[cite: 1]  
- Professor Middleware cognitive gating (`PASS / WARN / REJECT`)[cite: 1]  
- 100-file sliding-window quarantine rotation[cite: 1]  
- multi-hop proof-tree generation in `KG_EXPLAIN_DEEP`[cite: 1]  

---

## 🔐 Safety Rules  
- ❌ No execution of forbidden host OS commands (0.0s block via COLNÍK Guard)[cite: 1]  
- ⛔ Immediate Token Guard rejection on inputs containing malformed symbols (`@#$%^&*`)[cite: 1]  
- 🗄 Strict dual-language isolation: SK and EN graphs must never cross-contaminate[cite: 1]  
- 🗑️ No direct unverified disk deletions: file removals must route through HitL Safe Trash (`GET /trash`, tested in `dist_V6_CHECK`)[cite: 1]  
- 🔄 Mandatory module backups via SafeRollback (`safe_rollback.py`) before risky mutations[cite: 1]  
- 🎓 Mandatory cognitive validation via Professor Middleware (`PASS / WARN / REJECT`)[cite: 1]  
- 🔒 Mandatory customs clearance via COLNIK‑6.x (Standard & High-Performance IPC Mode)[cite: 1]  
- 🛡 Supervised decision gating via AUTONOMY 6.x (Control, Guard, Safe Trash & Triage Mode)[cite: 1]  
- 💬 Interactive human-in-the-loop validation via `PanelAPI` `[ÁNO/NIE]` / `[YES/NO]` with confirmation state latching[cite: 1]  
- 🛑 Terminal state decoupling must trigger `currentModule = "none"` upon input reset[cite: 1]  
- 🚫 Strict non-biological domain shields active across all external data ingestion[cite: 1]  
- 📦 Automatic quarantine sliding-window rotation enforcing 100-file ceiling[cite: 1]  
- 🔁 Zero proposal recurrence on established entities, aliases, and deduced taxonomies[cite: 1]  
- ⚠ Deterministic proof-tree explainability required for all decisions[cite: 1]  
- 📉 Real-time hardware telemetry (CPU, RAM, Disk) monitored via Guard[cite: 1]  

---

## 📊 Module Status (v6.0.1)  
- ✔ Fully implemented & synchronized with Runtime 6.0.1 architecture[cite: 1]  
- ✔ Identity access tiers verified (OWNER / FAMILY / STRANGER)[cite: 1]  
- ✔ Token Guard input sanitization active[cite: 1]  
- ✔ Trailing punctuation trimming (`.rstrip("?")`) and confirmation state latching verified[cite: 1]  
- ✔ COLNÍK Guard shell access control (0.0s block on `format`/`diskpart`) operational[cite: 1]  
- ✔ Human-in-the-Loop Safe UI Trash pipeline verified (tested in `dist_V6_CHECK`)[cite: 1]  
- ✔ SafeRollback crash resilience (`safe_rollback.py`) integrated[cite: 1]  
- ✔ Professor Middleware Layer (`PASS / WARN / REJECT`) active[cite: 1]  
- ✔ Sliding-window quarantine rotation operational (100-file ceiling)[cite: 1]  
- ✔ Dual-language graph isolation (`autosave_kg.json` & `autosave_kg_en.json`) operational[cite: 1]  
- ✔ Native lossless entity merge (`kg merge`) validated[cite: 1]  
- ✔ Taxonomical category inference auto-commit (`KG_VERIFY`) verified[cite: 1]  
- ✔ Reverse habitat engine with anti-flora guard operational[cite: 1]  
- ✔ Terminal decoupling and module state reset confirmed[cite: 1]  
- ✔ Single-process orchestrator integration on port 8080 operational with embedded TerminalAssistant + TimeCore[cite: 1]  
- ✔ PanelAPI interactive confirmation loops verified[cite: 1]  
- ✔ TimeCore temporal tracking (`cycle_delta()`) and Guard resource telemetry active[cite: 1]  
- ✔ COLNIK‑6.x customs validation functional (Standard & IPC Mode)[cite: 1]  
- ✔ AUTONOMY 6.x governance and triage containment verified[cite: 1]  
- ✔ Complete 4-Panel UI Suite synchronization operational[cite: 1]  

---

## 🏁 Summary  
Security Family 6.0.1 is the unified identity and permission enforcement framework of SIRIUS Local AI (v6.0.1).  
It validates every query, workflow, dual-language Knowledge Graph mutation, native entity merge, reasoning step, shell command, and system operation through identity tiers, entry-level Token Guard sanitization, COLNÍK Guard 0.0s shell protection, Human-in-the-Loop Safe Trash (tested in `dist_V6_CHECK`), SafeRollback crash protection, Professor Middleware cognitive gating, deep symbolic explainability, central orchestrator execution, confirmation state latching, COLNIK‑6.x customs validation, and AUTONOMY‑6.x governance.

It ensures that SIRIUS operates on local workstations **safely, deterministically, identity‑aware, linguistically segregated, shielded from destructive actions, and with verifiable explainability**.
