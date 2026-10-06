# ⚡ AUTONOMY 6.x — Autonomous Decision Engine  
**Status:** ✔ Production-Enhanced  
**Version:** 6.x  
**SIRIUS Local AI Version:** 5.9.1  
**Component:** AUTONOMY  
**Role:** Core autonomous reasoning, proposal generation, Dual-Language KG dispatch, Lossless Entity Merge governance, Human-in-the-Loop Safe Trash supervision, and 4-Panel UI integration[cite: 1, 2, 3]

---

## 🎯 1. Purpose  
The AUTONOMY 6.x module is the central decision-making, governance, and arbitration engine of the SIRIUS Local AI ecosystem (v5.9.1)[cite: 1, 2].  
Its mission is to evaluate semantic reasoning signals, supervise safe learning proposals, bind execution context dynamically to isolated dual-language graphs (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN), coordinate native entity mergers (`kg merge`), supervise non-destructive quarantine workflows (Human-in-the-Loop Safe Trash), and orchestrate the full autonomy cycle via `sirius_orchestrator.py` on embedded port 8080 and PanelAPI[cite: 1, 2, 3].

AUTONOMY 6.x guarantees that autonomous knowledge acquisition, category deduction, and file operations remain 100% deterministic, audit-traceable, and strictly bound to user confirmation loops without proposal recurrence[cite: 1, 2].

---

## 🧠 2. Architecture Overview  
**ReasoningEngine5 / InputParser5 → Token Guard → AUTONOMY (Control & Triage Mode) → proposals.json → COLNIK (IPC Mode) → EXECUTE → responses.json → Dual-Language Graph Commit (`autosave_kg.json` / `autosave_kg_en.json`)[cite: 1, 2, 3]**

### 🔍 Core Responsibilities  
- Interpret semantic multi-word inputs, questions with stripped trailing punctuation, and language headers (`SK` / `EN`)[cite: 1, 2]
- Bind operational targets dynamically to the active language graph partition (`autosave_kg.json` or `autosave_kg_en.json`)[cite: 1, 2]
- Supervise interactive learning proposals (`kg.learn_proposal`) with latched `[ÁNO/NIE]` / `[YES/NO]` state confirmation[cite: 1, 2]
- Authorize and validate in-memory lossless entity mergers (`kg merge <src> into <tgt>`) with zero property loss and bi-directional alias tracking[cite: 1, 2]
- Enforce taxonomical inference auto-commits (e.g., marsupials/macropods recognized as mammals) directly to the target graph with zero prompt recurrence[cite: 1, 2]
- Govern non-destructive file disposal by routing deletions into isolated quarantine storage awaiting explicit HitL approval via `GET /trash`[cite: 2, 3]
- Monitor terminal execution safety via COLNÍK Guard with 0.0s hard blocks on forbidden commands (`format`, `diskpart`, `rmdir /s`)[cite: 2, 3]
- Enforce the 100-file sliding window ceiling inside `COLNIK-6.x/envoy/quarantine/` via automated rotation[cite: 2, 3]
- Direct integration with the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) with automatic module resets (`currentModule = "none"`)[cite: 1]
- Record latency telemetries via TimeCore heartbeat `cycle_delta()`[cite: 2, 3]

### 📁 Key Files  
- `AUTONOMY/autonomy.py`  
- `AUTONOMY/state_manager.py`  
- `AUTONOMY/triage_mode.py`  
- `AUTONOMY/guard.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  
- `runtime5/runtime_core_5.py`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_normalizer_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  

---

## 🔄 3. Operational Cycle  

### **Step 1 — Ingest System, Language & Semantic State**  
AUTONOMY collects signals from `InputParser5`, `ReasoningEngine5`, active language selectors (`SK` / `EN`), TimeCore monitors, Guard resource scanners, and internal state registers[cite: 1, 2, 3].

### **Step 2 — Semantic Analysis, Token Guard & Ambiguity Check**  
- Pass raw input through Token Guard; immediately drop forbidden symbolic injections (`@#$%^&*`)[cite: 2, 3]
- Strip trailing punctuation (`.rstrip("?")`) to preserve raw entity keys (e.g., `CO JE MACROPUS?` cleanly resolves to `macropus`)[cite: 1, 2]
- Route query context to the active language Knowledge Graph (`self.kg_sk` or `self.kg_en`)[cite: 1, 2]
- Check for existing entity nodes, alias mappings, or taxonomical inheritance rules[cite: 1, 2]

### **Step 3 — Generate Structured Proposals & Confirmation Latching**  
If factual knowledge or category confirmation is missing, AUTONOMY latches the pending entity state in memory and generates a structured proposal written to:  
`IPC_DATA/proposals.json`

Each proposal defines:  
- Action type (e.g., `kg.learn_proposal`, `kg_merge`, `file_quarantine`, `system_cleanup`)[cite: 1, 2]
- Target semantic entity, attribute, or system path[cite: 1, 2]
- Target language partition (`autosave_kg.json` vs. `autosave_kg_en.json`)[cite: 1, 2]
- Safety tier (Safe vs. Critical)[cite: 2, 3]
- Mandatory confirmation prompt dispatched to PanelAPI (`[ÁNO/NIE]` / `[YES/NO]`)[cite: 1, 2]
- Execution metadata and alias mapping instructions[cite: 1]

### **Step 4 — Wait for Customs Clearance & Human Confirmation**  
AUTONOMY synchronizes with COLNÍK-6.x (Customs Validation) and awaits user confirmation via the Web UI (`index.html`) on port 8080 or the terminal interface[cite: 1, 2, 3]. Confirmation state latching guarantees affirmative replies (`ÁNO` / `YES`) strictly trigger the latched proposal without encountering detached states[cite: 1, 2].

### **Step 5 — Autonomous Execution & Atomic Dual Commit**  
Upon approval:  
- Triggers `EnvoyExecutionLayer5` for encyclopedic context resolution[cite: 1, 2]
- Normalizes attributes via `EnvoyNormalizer5` blocking non-biological habitat leakage[cite: 1, 2]
- Commits knowledge, verified relations (`is_a mammal`, `je cicavec`), and aliases directly into the target language graph (`autosave_kg.json` or `autosave_kg_en.json`)[cite: 1, 2]
- Automatically rotates the quarantine directory if cached JSON records exceed 100 files[cite: 2, 3]
- Reads execution outcomes from `IPC_DATA/responses.json`  

### **Step 6 — State Synchronization & UI Release**  
AUTONOMY updates internal state registers, clears temporary IPC buffers, releases UI panel locks (`currentModule = "none"`), synchronizes dual autosaves to disk, and readies the loop for the next cycle[cite: 1, 2].

---

## 🔐 4. Safety Rules  

### **Critical Safety Guarantees**  
- 🔒 **Zero Direct File Deletions (HitL Safe Trash):** Files flagged for removal are never deleted directly; they are routed into quarantine and require manual user confirmation via `GET /trash`[cite: 2, 3].  
- 🛡️ **Terminal Command Access Control (COLNÍK Guard):** Immediate 0.0s hard blocking of forbidden commands (`format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`)[cite: 2, 3].  
- ⛔ **Token Guard Input Sanitization:** Commands containing dangerous character sequences (`@#$%^&*`) are blocked at runtime entry[cite: 2, 3].  
- 🗄️ **Dual-Language Isolation:** Total segregation between Slovak and English knowledge graphs, eliminating bilingual corruption and linguistic hallucinations[cite: 1, 2].  
- ⚠️ **Mandatory User Confirmation:** External learning and system-level actions require explicit user confirmation via PanelAPI `[ÁNO/NIE]` / `[YES/NO]` prompts[cite: 1, 2].  
- 🛑 **Anti-Prefix & Hallucination Guard:** Disallows prefix drift during web triage (e.g., prevents queries like *Káva* from jumping to *Kavala*)[cite: 1].  
- 🚫 **Strict Non-Bio Domain Shield:** Abstract and technical entities (physics, architecture) are barred from receiving biological habitat tags[cite: 1, 2].  
- 🔁 **Zero Proposal Recurrence:** Previously confirmed entities and inferred relations are committed directly to disk, permanently preventing repetitive prompt loops[cite: 1, 2].  
- 📦 **Quarantine Ceiling Rotation:** Automatically maintains a maximum ceiling of 100 JSON files inside `COLNIK-6.x/envoy/quarantine/` via sliding window pruning[cite: 2, 3].  

---

## 📊 5. Module Status (v5.9.1)  
- ✔ Fully implemented & synchronized with Runtime 5.9.1 architecture[cite: 1, 2]  
- ✔ Production-enhanced and operational under Windows 11 on port 8080[cite: 1, 2, 3]  
- ✔ Dual-Language Graph Isolation (`autosave_kg.json` & `autosave_kg_en.json`) active[cite: 1, 2]  
- ✔ Native Lossless Entity Merge (`kg merge`) validated[cite: 1, 2]  
- ✔ Ontological category deduction (`KG_VERIFY`) and edge auto-commit verified[cite: 1, 2]  
- ✔ Non-destructive reverse habitat query engine with anti-flora guard verified[cite: 1, 2]  
- ✔ Trailing punctuation hygiene and confirmation latching active[cite: 1, 2]  
- ✔ Hard Token Guard entry-level sanitization operational[cite: 2, 3]  
- ✔ Envoy quarantine sliding-window rotation (100-file ceiling) active[cite: 2, 3]  
- ✔ COLNÍK Guard shell access control (0.0s block on `format`) operational[cite: 2, 3]  
- ✔ Safe UI Trash & Human-in-the-Loop quarantine pipeline active[cite: 2, 3]  
- ✔ 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) synchronized[cite: 1]  

---

## 📂 6. Related Files  
- `AUTONOMY/autonomy.py`  
- `AUTONOMY/state_manager.py`  
- `AUTONOMY/guard.py`  
- `REASONING/engine5.py`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/input_parser_5.py`  
- `runtime5/envoy_execution_layer_5.py`  
- `runtime5/envoy_normalizer_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  

---

## 🏁 7. Summary  
AUTONOMY 6.x is the central decision, arbitration, and governance engine of SIRIUS Local AI (v5.9.1)[cite: 1, 2].  
It directs autonomous cycles (Control & Triage Mode), routes transactions across isolated dual-language knowledge graphs, governs lossless entity merges, deduces ontological taxonomies, eliminates repetitive interactive loops via auto-committing memory, and strictly protects system integrity through Token Guard, COLNÍK Guard, and the Human-in-the-Loop Safe Trash architecture[cite: 1, 2, 3].  
Its deterministic logic guarantees robust, audit-ready, and predictable autonomous execution across the entire SIRIUS 5.9.1 runtime[cite: 1, 2].
