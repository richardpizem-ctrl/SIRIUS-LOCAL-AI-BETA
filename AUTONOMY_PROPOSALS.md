# 🤖 AUTONOMY PROPOSALS 6.x — Supervised Autonomous Decision Generation  
**Status:** ✔ Production-Enhanced  
**Version:** 6.x (Updated for Runtime 5.9.0 UNIFIED)  
**Component:** AUTONOMY Proposal Engine  
**Role:** Generate safe, explainable, supervised autonomous proposals for system actions, workflows, multi-alias KG mutations, and UI automation under orchestrator and PanelAPI supervision

---

## 🎯 Purpose  
The AUTONOMY Proposal Engine 6.x is responsible for generating **autonomous suggestions** (proposals) based on system context, multi-word semantic parsing, KG reasoning, identity rules, predictive intelligence, and Triage Mode diagnostics.  
These proposals represent *what SIRIUS thinks should happen next* — but every proposal is supervised, validated, and confirmed through COLNIK‑6.x (Standard & High-Performance IPC Mode), System Agent 5, and interactive PanelAPI loops with `[ÁNO/NIE]` confirmations.

AUTONOMY never executes actions directly.  
It **proposes**, **explains**, **justifies**, and **waits for validation**.

---

## 🧩 Architecture Overview  
**System Intelligence Layer / InputParser5 → AUTONOMY Proposal Engine → `sirius_orchestrator.py` (Port 8080) → COLNIK (IPC Mode) → PanelAPI [ÁNO/NIE] → Workflow Engine → Multi-Alias KG Commit (`autosave_kg.json`)**

### Core Responsibilities  
- generate autonomous learning proposals (`kg.learn_proposal`) for missing concepts  
- prevent proposal recurrence: evaluate multi-alias mappings so confirmed entities are not repeatedly proposed  
- evaluate system context via TimeCore heartbeat & Guard resource monitors  
- integrate multi-word compound parsing from `InputParser5`  
- supervise encyclopedic web triage via `EnvoyExecutionLayer5` (disambiguation resolution & anti-prefix protection)  
- enforce contextual domain filtering (`EnvoyNormalizer5`) preventing false geographic habitat extraction  
- provide explainability metadata (proof trees and evidence chains)  
- route proposals through COLNIK‑6.x (Standard & IPC Mode)  
- coordinate supervised autonomy via Control & Triage Mode (`COLNIK-6.x/triage`)  
- interface directly with the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) with automatic module release (`currentModule = "none"`)  

### Key Files  
- `autonomy/autonomy_proposer.py`  
- `autonomy/proposals.json`  
- `autonomy/proposal_metadata.json`  
- `IPC_DATA/autonomy_events.json`  
- `runtime5/input_parser_5.py`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_normalizer_5.py`  

---

## 🔍 Proposal Pipeline  

### **1 — Context Collection**  
AUTONOMY gathers signals from:  
- System Intelligence Layer & InputParser5 (compound noun extraction)  
- KG ENGINE & Multi-Alias Registry  
- ReasoningEngine5 (symbolic derivation rules)  
- Workflow Engine 5.9.0  
- System Agent 5  
- Identity Engine  
- TimeCore & Guard Temporal/Security Monitors  

Context determines whether a proposal is safe, relevant, or strictly necessary.

---

### **2 — Proposal Generation**  
AUTONOMY generates proposals across specialized operational categories:

#### **Knowledge Graph & Learning Proposals**
- `kg.learn_proposal` — propose fetching missing entities via Envoy  
- multi-alias registration — map queried synonyms to official target article titles  
- add / remove semantic relation  
- validate graph consistency and persist changes to `autosave_kg.json`  
- enforce zero recurrence: suppress proposals for concepts already stored under an alias  

#### **System Proposals**
- optimize CPU/RAM load detected by Guard  
- classify duplicate files into safe vs. critical buckets  
- close heavy or unresponsive background tasks  
- stabilize OS runtime state  
- trigger self-repair routines  

#### **Workflow Proposals**
- advance multi-step workflow  
- pause or reroute execution pipeline  
- fallback to base lemma when facing parenthetical article names (Strip-Bracket Fallback)  
- engage safe-mode execution on network anomalies  

#### **UI Automation & Navigation Proposals**
- route queries cleanly across the 4 UI panels (`Duplicates`, `Triage`, `Navigation`, `Terminal`)  
- release terminal input focus upon clearing to prevent host CLI lockups  
- display interactive confirmation dialogs via PanelAPI  
- block destructive sequences in web views  

#### **Identity Proposals**
- restrict action based on identity profile  
- enforce STRANGER / FAMILY permission boundaries  
- mandate explicit confirmation (`PanelAPI` [ÁNO/NIE]) for system mutations  

---

### **3 — Explainability Generation**  
Every proposal includes:

- KG_EXPLAIN / KG_EXPLAIN_DEEP traces  
- multi-hop symbolic reasoning derivation  
- rule attribution metadata  
- confidence metrics  
- justification summary in human-readable natural language  

Explainability is mandatory for all autonomous proposals.

---

### **4 — COLNIK‑Validated Routing**  
Before a proposal is staged for user confirmation, COLNIK‑6.x performs:

- enterprise-grade security and mutation validation  
- deterministic allow/deny filtering  
- check against reversible action constraints  
- threat classification and payload inspection  
- identity policy enforcement  

Unsafe, unverified, or malformed proposals are rejected immediately.

---

### **5 — System Agent Enforcement**  
System Agent 5 checks:

- active identity permissions  
- operating system stability metrics  
- process safety limits  
- terminal execution boundaries  
- self-repair triggers  

If safety constraints are violated, the proposal is neutralized.

---

### **6 — Proposal Confirmation & Execution**  
AUTONOMY never mutates the environment blindly.  
It completes the supervised loop:

- COLNIK authorization check  
- System Agent stability approval  
- Explicit user confirmation via PanelAPI `[ÁNO/NIE]` (interactive Web UI / Terminal prompt)  
- Multi-alias indexing and atomic commit to `autosave_kg.json`  

Only after full validation is the proposal converted into an executable workflow.

---

## 🧱 Proposal Types  

### **1 — ALLOW Proposal**  
Safe, verified, explainable, and adheres to identity rules.  
Action proceeds automatically.

### **2 — DENY Proposal**  
Violates security constraints, identity rules, or system limits.  
Action is blocked and logged.

### **3 — REQUIRE_CONFIRMATION Proposal**  
Covers new knowledge enrichment (`kg.learn_proposal`) or high-impact system modifications.  
Requires interactive approval via PanelAPI `[ÁNO/NIE]`.

### **4 — FALLBACK Proposal**  
Activates alternate safe execution paths (e.g., stripping brackets on disambiguation failure).  
Used during knowledge gaps or system triage states.

### **5 — REPAIR Proposal**  
Engages Self‑Repair Layer 5.4 / 5.8 routines.  
Triggered when file duplicities, schema corruption, or loop anomalies are detected.

---

## 🔐 Safety Rules  
- ❌ **Zero Blind Execution:** AUTONOMY never executes mutations without pipeline approval.  
- 🔒 **Customs Clearance Required:** All mutations pass through COLNIK‑6.x inspection.  
- ⚠️ **Mandatory Explainability:** Every proposal must carry structural derivation evidence.  
- 🛑 **Zero Proposal Recurrence:** Confirmed concepts must never re-trigger learning prompts.  
- 🚫 **Anti-Prefix & Hallucination Guard:** Disallows prefix-drift during web lookups.  
- 🛡️ **UI Isolation:** Clearing user input releases panel locks, preventing host shell capture.  

---

## 📊 Module Status (v5.9.0)  
- ✔ Fully updated & verified for Runtime 5.9.0  
- ✔ Multi-word parsing and noun phrase support active  
- ✔ Autonomous Disambiguation Triage integration operational  
- ✔ Multi-alias graph indexing validated (`autosave_kg.json`)  
- ✔ Recurrence elimination confirmed  
- ✔ 4-Panel UI Suite integration stabilized  
- ✔ COLNIK‑6.x High-Performance IPC handshake verified  
- ✔ PanelAPI interactive confirmation loops functional  
- ✔ Single-process orchestrator integration (Port 8080) complete  

---

## 🏁 Summary  
AUTONOMY Proposal Engine 6.x is the supervised autonomous decision generator of SIRIUS Local AI (v5.9.0).  
It generates safe, explainable, identity-aware, and system-aware proposals for knowledge enrichment, workflows, UI automation, and system diagnostics — fully orchestrated via `sirius_orchestrator.py`, audited by COLNIK‑6.x, supervised by Guard, and confirmed via interactive PanelAPI loops.

It powers a **predictive, deterministic, supervised autonomous system** that acts responsibly, respects user confirmation, and explains its reasoning end-to-end.
