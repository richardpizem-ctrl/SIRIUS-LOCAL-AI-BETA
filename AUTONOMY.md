# ⚡ AUTONOMY 6.x — Autonomous Decision Engine  
**Status:** ✔ Production-Enhanced  
**Version:** 6.x  
**SIRIUS Local AI Version:** 5.9.0  
**Component:** AUTONOMY  
**Role:** Core autonomous reasoning, proposal-generation, Control & Triage Mode, Multi-Alias validation, and 4-Panel UI integration

---

## 🎯 1. Purpose  
The AUTONOMY 6.x module is the central decision-making and governance engine of the SIRIUS Local AI system (v5.9.0).  
Its mission is to analyze system state, evaluate multi-word semantic reasoning outputs, generate safe learning proposals, coordinate through Control & Triage Mode, and orchestrate the full autonomy cycle via the central orchestrator (`sirius_orchestrator.py`), native IPC Daemon on port 8080, and PanelAPI.

AUTONOMY 6.x guarantees that autonomous entity learning, encyclopedic enrichment, and system mutations remain deterministic, audit-traceable, and strictly bound to user confirmation loops without proposal recurrence.

---

## 🧠 2. Architecture Overview  
**ReasoningEngine5 / InputParser5 → AUTONOMY (Control & Triage Mode) → proposals.json → COLNIK (IPC Mode) → EXECUTE → responses.json → Multi-Alias Graph Commit (`autosave_kg.json`)**

### 🔍 Core Responsibilities  
- Interpret semantic multi-word inputs and reasoning structures  
- Supervise interactive learning proposals (`kg.learn_proposal`) with `[ÁNO/NIE]` confirmation  
- Coordinate autonomous encyclopedic enrichment alongside EnvoyExecutionLayer5 disambiguation  
- Enforce zero-proposal recurrence: ensure confirmed entities are indexed across aliases to eliminate repetitive prompts  
- Direct integration with the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`)  
- Ensure clean terminal decoupling by resetting module state (`currentModule = "none"`) on input clearing  
- Maintain autonomy cycle timing via TimeCore heartbeat and Guard security supervision  
- Validate and route background file triage in `COLNIK-6.x/triage`  
- Update internal state deterministically for the next operational cycle  

### 📁 Key Files  
- `AUTONOMY/autonomy.py`  
- `AUTONOMY/state_manager.py`  
- `AUTONOMY/triage_mode.py`  
- `AUTONOMY/guard.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_normalizer_5.py`  

---

## 🔄 3. Operational Cycle  

### **Step 1 — Ingest System & Semantic State**  
AUTONOMY collects signals from `InputParser5`, `ReasoningEngine5`, TimeCore temporal monitors, Guard resource scanners, and internal state managers.

### **Step 2 — Semantic Analysis & Ambiguity Check**  
- Evaluate user input for compound concepts (`ovcia vlna`, `mobilny telefon`, `pevna linka`)  
- Check Knowledge Graph for existing entities or established aliases  
- Detect disambiguation requirements or trigger Triage Mode if structural anomalies occur  
- Enforce deterministic decision paths via `sirius_orchestrator.py`  

### **Step 3 — Generate Structured Proposals**  
If knowledge is missing, AUTONOMY generates structured proposals and writes them to:  
`IPC_DATA/proposals.json`

Each proposal defines:  
- Action type (e.g., `kg.learn_proposal`, `file_quarantine`, `system_cleanup`)  
- Target semantic entity or system path  
- Safety tier (Safe vs. Critical)  
- Mandatory confirmation prompts via `PanelAPI` (`[ÁNO/NIE]`)  
- Execution metadata and alias mapping instructions  

### **Step 4 — Wait for Customs Clearance & Confirmation**  
AUTONOMY coordinates with COLNÍK-6.x (Customs Validation) and awaits direct user confirmation via the Web UI (`index.html`) on port 8080 or terminal interface.

### **Step 5 — Autonomous Execution & Multi-Alias Commit**  
Upon approval:  
- Triggers `EnvoyExecutionLayer5` with disambiguation triage and anti-prefix guards  
- Normalizes attributes via `EnvoyNormalizer5` blocking non-biological habitat leakage  
- Commits knowledge under both the queried phrase and encyclopedia title to `autosave_kg.json`  
- Reads execution outcomes from `IPC_DATA/responses.json`  

### **Step 6 — State Synchronization & UI Release**  
AUTONOMY updates internal state registers, clears temporary IPC buffers, releases UI panel locks (`currentModule = "none"`), and readies the loop for the next cycle.

---

## 🔐 4. Safety Rules  

### **Critical Safety Guarantees**  
- 🔒 **Zero Direct File Mutations:** AUTONOMY never performs unsanctioned disk operations; all modifications route through COLNIK-validated executors.  
- ⚠️ **Mandatory User Confirmation:** High-impact and learning actions strictly require explicit confirmation via PanelAPI `[ÁNO/NIE]` prompts.  
- 🛑 **Anti-Prefix & Hallucination Guard:** Disallows prefix drift during web triage (e.g., stops queries like *Káva* from jumping to *Kavala*).  
- 🚫 **Strict Non-Bio Domain Shield:** Abstract and technical entities (physics, architecture) are barred from receiving biological habitat tags.  
- 🔁 **Zero Proposal Recurrence:** Previously confirmed entities cannot trigger repetitive confirmation loops.  
- 🛡️ **Terminal Isolation:** Input clearing triggers immediate reset to `none`, preventing conversational prompts from leaking into system shell execution.  

---

## 📊 5. Module Status (v5.9.0)  
- ✔ Fully implemented & synchronized with Runtime 5.9.0  
- ✔ Production-enhanced and operational under Windows 11  
- ✔ Semantic multi-word integration validated  
- ✔ Control & Triage Mode fully integrated with 4-Panel UI Suite  
- ✔ Multi-alias persistence support active  
- ✔ Single-process IPC daemon integration (Port 8080) verified  
- ✔ COLNÍK-6.x IPC handshake verified  
- ✔ PanelAPI interactive confirmation loops verified  
- ✔ Terminal lockup prevention confirmed  
- ✔ Deterministic cycle behavior and Guard supervision active  

---

## 📂 6. Related Files  
- `AUTONOMY/autonomy.py`  
- `AUTONOMY/state_manager.py`  
- `AUTONOMY/guard.py`  
- `REASONING/engine5.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `runtime5/input_parser_5.py`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_normalizer_5.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  

---

## 🏁 7. Summary  
AUTONOMY 6.x is the central decision engine of SIRIUS Local AI (v5.9.0).  
It generates safe, validated proposals, directs autonomous cycles (Control & Triage Mode), eliminates repetitive learning prompts via multi-alias tracking, and integrates seamlessly with COLNÍK-6.x, PanelAPI, and the 4-Panel UI Suite.  
Its deterministic logic guarantees robust, audit-ready, and predictable autonomous execution across the entire SIRIUS 5.9.0 architecture.
