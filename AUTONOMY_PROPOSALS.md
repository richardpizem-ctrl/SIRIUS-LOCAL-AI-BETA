# 🤖 AUTONOMY PROPOSALS 6.x — Supervised Autonomous Decision Generation  
**Status:** ✔ Production-Enhanced  
**Version:** 6.x (Updated for Runtime 5.9.1 UNIFIED)[cite: 1, 2]  
**Component:** AUTONOMY Proposal Engine  
**Role:** Generate safe, explainable, supervised autonomous proposals for system actions, workflows, dual-language KG mutations, lossless entity merges, and UI automation under orchestrator and PanelAPI supervision[cite: 1, 2, 3]

---

## 🎯 Purpose  
The AUTONOMY Proposal Engine 6.x is responsible for generating **autonomous suggestions** (proposals) based on system context, multi-word semantic parsing, dual-language KG reasoning, identity rules, predictive intelligence, and Triage Mode diagnostics[cite: 1, 2].  
These proposals represent *what SIRIUS thinks should happen next* — but every proposal is supervised, validated, and confirmed through COLNIK‑6.x (Standard & High-Performance IPC Mode), System Agent 5, Token Guard, and interactive PanelAPI loops with `[ÁNO/NIE]` / `[YES/NO]` confirmations[cite: 1, 2, 3].

AUTONOMY never executes actions directly.  
It **proposes**, **explains**, **justifies**, **latches confirmation state**, and **waits for validation**[cite: 1, 2].

---

## 🧩 Architecture Overview  
**System Intelligence Layer / InputParser5 → Token Guard → AUTONOMY Proposal Engine → `sirius_orchestrator.py` (Port 8080) → COLNIK (IPC Mode) → PanelAPI [ÁNO/NIE] → Workflow Engine → Dual-Language KG Commit (`autosave_kg.json` / `autosave_kg_en.json`)[cite: 1, 2, 3]**

### Core Responsibilities  
- generate autonomous learning proposals (`kg.learn_proposal`) for missing concepts with target language binding (`SK` / `EN`)[cite: 1, 2]
- enforce confirmation state latching: track pending proposal entities across interactive turns so user confirmations (`ÁNO` / `YES`) reliably trigger external enrichment[cite: 1, 2]
- prevent proposal recurrence: evaluate multi-alias mappings and taxonomical edges so confirmed entities are not repeatedly proposed[cite: 1, 2]
- supervise native lossless entity mergers (`kg merge <src> into <tgt>`), relocating attributes without external script dependencies[cite: 1, 2]
- support taxonomical category inference (`KG_VERIFY`), automatically establishing and committing sub-taxa relations (e.g., marsupials/macropods -> mammals)[cite: 1, 2]
- supervise non-destructive reverse location queries (`_execute_reverse_location_query`) with anti-flora classification guards protecting tree-dwelling fauna[cite: 1, 2]
- enforce entry-level input sanitization via Token Guard, blocking malformed injection characters (`@#$%^&*`)[cite: 2, 3]
- manage automatic sliding-window rotation limiting quarantine logs in `COLNIK-6.x/envoy/quarantine/` to a 100-file ceiling[cite: 2, 3]
- supervise non-destructive file disposal by routing delete requests into the Human-in-the-Loop Safe Trash pipeline[cite: 2, 3]
- audit console execution safety via COLNÍK Guard with 0.0s hard blocks on forbidden commands (`format`, `diskpart`)[cite: 2, 3]
- interface directly with the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) with automatic module release (`currentModule = "none"`)[cite: 1]

### Key Files  
- `autonomy/autonomy_proposer.py`  
- `autonomy/proposals.json`  
- `autonomy/proposal_metadata.json`  
- `IPC_DATA/autonomy_events.json`  
- `runtime5/runtime_core_5.py`  
- `runtime5/input_parser_5.py`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_normalizer_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  

---

## 🔍 Proposal Pipeline  

### **1 — Context Collection & Input Sanitization**  
AUTONOMY gathers signals from:  
- Token Guard input filter (verifying absence of forbidden injection symbols `@#$%^&*`)[cite: 2, 3]
- InputParser5 with greedy punctuation trimming (`.rstrip("?")`) preventing token key fragmentation[cite: 1, 2]
- Active language selector (`SK` / `EN`) binding the operational context to `autosave_kg.json` or `autosave_kg_en.json`[cite: 1, 2]
- KG ENGINE, Alias Registry, and Taxonomical Traversal Layer[cite: 1, 2]
- ReasoningEngine5 (symbolic derivation rules)[cite: 1]
- System Agent 5, Identity Engine, and TimeCore / Guard Monitors[cite: 1, 3]

Context determines whether a proposal is safe, relevant, or strictly necessary[cite: 1].

---

### **2 — Proposal Generation & Confirmation Latching**  
AUTONOMY generates proposals across specialized operational categories:

#### **Knowledge Graph & Learning Proposals**
- `kg.learn_proposal` — propose fetching missing entities via Envoy for the active language store[cite: 1, 2]
- confirmation state latching — store target entity name in memory so positive responses (`ÁNO`, `ANO`, `YES`, `Y`) directly execute the pending proposal[cite: 1, 2]
- `kg_merge` proposal — lossless relocation of attributes from source to target with bidirectional alias preservation[cite: 1, 2]
- multi-alias registration — map queried synonyms to official target article titles[cite: 1]
- add / remove semantic relation and taxonomical edge commitment (`is_a mammal`, `je cicavec`)[cite: 1, 2]
- validate graph consistency and atomic persistence to `autosave_kg.json` or `autosave_kg_en.json`[cite: 1, 2]
- enforce zero recurrence: suppress proposals for concepts already stored or inferred[cite: 1, 2]

#### **System & File Security Proposals (HitL Safe Trash)**
- route proposed file deletions (duplicates, empty folders) into quarantine storage rather than executing direct disk removal[cite: 2, 3]
- require explicit user confirmation via `GET /trash` before permanent removal[cite: 2, 3]
- enforce automatic sliding-window rotation on `COLNIK-6.x/envoy/quarantine/` at the 100-file threshold[cite: 2, 3]
- optimize CPU/RAM load detected by Guard[cite: 1]
- stabilize OS runtime state and trigger self-repair routines[cite: 1]

#### **Workflow Proposals**
- advance multi-step workflow[cite: 1]
- pause or reroute execution pipeline[cite: 1]
- fallback to base lemma when facing parenthetical article names (Strip-Bracket Fallback)[cite: 1]
- engage safe-mode execution on network anomalies[cite: 1]

#### **UI Automation & Navigation Proposals**
- route queries cleanly across the 4 UI panels (`Duplicates`, `Triage`, `Navigation`, `Terminal`)[cite: 1]
- release terminal input focus upon clearing (`currentModule = "none"`) to prevent host CLI lockups[cite: 1]
- display interactive confirmation dialogs via PanelAPI (`[ÁNO/NIE]` / `[YES/NO]`)[cite: 1, 2]
- block destructive sequences in web views[cite: 1]

#### **Identity & Command Security Proposals**
- enforce COLNÍK Guard shell security (0.0s hard block on `format`, `diskpart`, `rmdir /s`)[cite: 2, 3]
- restrict action based on identity profile[cite: 1]
- enforce STRANGER / FAMILY permission boundaries[cite: 1]

---

### **3 — Explainability Generation**  
Every proposal includes:

- KG_EXPLAIN / KG_EXPLAIN_DEEP traces[cite: 1]
- multi-hop symbolic reasoning derivation[cite: 1]
- rule attribution metadata[cite: 1]
- confidence metrics[cite: 1]
- justification summary in human-readable natural language[cite: 1]

Explainability is mandatory for all autonomous proposals[cite: 1].

---

### **4 — COLNIK‑Validated Routing**  
Before a proposal is staged for user confirmation, COLNIK‑6.x performs:

- enterprise-grade security and mutation validation[cite: 1]
- verification against the command categorization matrix (FORBIDDEN, RISKY, ALLOWED)[cite: 2, 3]
- check against reversible action constraints and quarantine trash routing[cite: 1, 2, 3]
- threat classification and payload inspection[cite: 1]
- identity policy enforcement[cite: 1]

Unsafe, unverified, or malformed proposals are rejected immediately[cite: 1].

---

### **5 — System Agent Enforcement**  
System Agent 5 checks:

- active identity permissions[cite: 1]
- operating system stability metrics[cite: 1]
- process safety limits[cite: 1]
- terminal execution boundaries and TimeCore telemetry[cite: 1, 2, 3]
- self-repair triggers[cite: 1]

If safety constraints are violated, the proposal is neutralized[cite: 1].

---

### **6 — Proposal Confirmation & Execution**  
AUTONOMY completes the supervised loop:

- COLNIK authorization check[cite: 1]
- System Agent stability approval[cite: 1]
- Explicit user confirmation via PanelAPI (`[ÁNO/NIE]` / `[YES/NO]`)[cite: 1, 2]
- Execution of active latch: external context scrape, domain normalization, and alias indexing[cite: 1, 2]
- Atomic serialization into the designated language store (`autosave_kg.json` or `autosave_kg_en.json`)[cite: 1, 2]

Only after full validation is the proposal converted into an executable workflow[cite: 1].

---

## 🧱 Proposal Types  

### **1 — ALLOW Proposal**  
Safe, verified, explainable, and adheres to identity rules[cite: 1].  
Action proceeds automatically[cite: 1].

### **2 — DENY Proposal**  
Violates security constraints, token guard policies, or command restrictions[cite: 1, 2, 3].  
Action is blocked immediately (0.0s for forbidden commands) and logged[cite: 2, 3].

### **3 — REQUIRE_CONFIRMATION Proposal**  
Covers new knowledge enrichment (`kg.learn_proposal`), node merges, or quarantine deletions[cite: 1, 2, 3].  
Latches target state and requires interactive approval via PanelAPI `[ÁNO/NIE]` / `[YES/NO]`[cite: 1, 2].

### **4 — FALLBACK Proposal**  
Activates alternate safe execution paths (e.g., stripping brackets on disambiguation failure)[cite: 1].  
Used during knowledge gaps or system triage states[cite: 1].

### **5 — REPAIR Proposal**  
Engages Self‑Repair Layer routines[cite: 1].  
Triggered when file duplicities, schema corruption, or sliding window overflows occur[cite: 1, 2, 3].

---

## 🔐 Safety Rules  
- ❌ **Zero Blind Execution:** AUTONOMY never executes mutations without pipeline approval[cite: 1].  
- 🔒 **Customs Clearance Required:** All mutations pass through COLNIK‑6.x inspection[cite: 1].  
- 🗑️ **Human-in-the-Loop Safe Trash:** Deletions are quarantined; direct unverified file deletion is strictly prohibited[cite: 2, 3].  
- 🛡️ **COLNÍK Guard Shell Access Control:** Immediate 0.0s blocking of destructive shell commands (`format`, `diskpart`, `rmdir /s`)[cite: 2, 3].  
- ⛔ **Token Guard Input Sanitization:** Commands containing dangerous symbols (`@#$%^&*`) are rejected at entry[cite: 2, 3].  
- 🗄️ **Dual-Language Isolation:** Proposals strictly target their originating language store (`autosave_kg.json` or `autosave_kg_en.json`), preventing cross-lingual corruption[cite: 1, 2].  
- ⚠️ **Mandatory Explainability:** Every proposal must carry structural derivation evidence[cite: 1].  
- 🛑 **Zero Proposal Recurrence:** Confirmed concepts and inferred categories auto-commit to disk, suppressing repetitive prompts[cite: 1, 2].  
- 📦 **Quarantine Ceiling Rotation:** Automatically maintains a 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`[cite: 2, 3].  
- 🛡️ **UI Isolation:** Clearing user input releases panel locks (`currentModule = "none"`), preventing host shell capture[cite: 1].  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully updated & verified for Runtime 5.9.1 architecture[cite: 1, 2]  
- ✔ Dual-Language Graph Isolation (`autosave_kg.json` & `autosave_kg_en.json`) active[cite: 1, 2]  
- ✔ Confirmation state latching and punctuation trimming operational[cite: 1, 2]  
- ✔ Native Lossless Entity Merge (`kg merge`) proposal handling verified[cite: 1, 2]  
- ✔ Taxonomical inference auto-commit (`KG_VERIFY`) operational[cite: 1, 2]  
- ✔ Multi-word parsing and noun phrase support active[cite: 1]  
- ✔ Token Guard input sanitization active[cite: 2, 3]  
- ✔ Envoy quarantine sliding-window rotation (100-file ceiling) active[cite: 2, 3]  
- ✔ COLNIK‑6.x High-Performance IPC handshake verified[cite: 1]  
- ✔ Safe UI Trash & HitL confirmation pipeline active[cite: 2, 3]  
- ✔ PanelAPI interactive confirmation loops functional[cite: 1]  
- ✔ Single-process orchestrator integration (Port 8080) complete[cite: 1, 3]  

---

## 🏁 Summary  
AUTONOMY Proposal Engine 6.x is the supervised autonomous decision generator of SIRIUS Local AI (v5.9.1)[cite: 1, 2].  
It generates safe, explainable, identity-aware, and system-aware proposals for dual-language knowledge enrichment, entity mergers, workflows, UI automation, and system diagnostics — fully orchestrated via `sirius_orchestrator.py`, audited by COLNIK‑6.x, safeguarded by Token Guard and HitL Safe Trash, and confirmed via interactive PanelAPI loops[cite: 1, 2, 3].

It powers a **predictive, deterministic, supervised autonomous system** that acts responsibly, respects user confirmation, and explains its reasoning end-to-end[cite: 1].
