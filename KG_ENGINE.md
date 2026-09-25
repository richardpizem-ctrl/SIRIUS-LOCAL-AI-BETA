# 🧠 KG ENGINE 6.x — Knowledge Graph Core  
**Status:** ✔ Active (Enhanced)  
**Version:** 6.x  
**SIRIUS Local AI Version:** 5.9.0  
**Component:** KG ENGINE  
**Role:** Unified symbolic knowledge graph engine powering multi-alias indexing, compound phrase persistence, explainability, exports, imports, and multi-hop reasoning under orchestrator and PanelAPI supervision

---

## 🎯 Purpose  
The KG ENGINE 6.x module is the central symbolic knowledge system of SIRIUS Local AI (v5.9.0).  
It manages entities, relations, compound semantic concepts, multi-alias mappings, and graph-based reasoning operations.  
All explainability, relation discovery, and multi-hop inference rely directly on this engine.

KG ENGINE provides deterministic, transparent, and fully inspectable knowledge operations driven by `sirius_orchestrator.py` on local port 8080 and guarded by `TimeCore` and `Guard`.

---

## 🧩 Architecture Overview  
**Runtime 5.9.0 / InputParser5 → `sirius_orchestrator.py` (Port 8080) → KG ENGINE / RuntimeCore → ReasoningEngine5 → AUTONOMY 6.x → COLNIK (IPC Mode) → PanelAPI [ÁNO/NIE] → Multi-Alias Commit (`autosave_kg.json`)**

### Core Responsibilities  
- Manage entities, relations, and compound noun phrases (`ovcia vlna`, `mobilny telefon`)  
- Support dual-key multi-alias persistence (mapping colloquial queries to formal encyclopedic titles)  
- Enforce zero proposal recurrence: suppress redundant learning proposals once an alias is committed  
- Provide semantic explainability (KG_EXPLAIN, KG_EXPLAIN_DEEP with proof trees)  
- Perform relation discovery (KG_RELATE)  
- Handle graph import/export with schema and cycle validation  
- Support multi-hop reasoning and orbital transitions  
- Maintain atomic serialization integrity via `autosave_kg.json`  
- Provide developer comfort commands with automatic UI state clearance (`currentModule = "none"`)  

### Key Files  
- `KG/kg_engine.py`  
- `runtime5/runtime_core.py`  
- `runtime5/input_parser_5.py`  
- `KG/kg_store/`  
- `KG/autosave_kg.json`  
- `KG/kg_export.json`  
- `KG/kg_import.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  

---

## 🧱 Knowledge Structure  

### **Entities & Multi-Alias Nodes**  
Fundamental nodes representing concepts, objects, categories, or compound phrases (`ovcia vlna`).  
Each node supports an internal alias registry:  
- Primary canonical identifier  
- Alternate query aliases (e.g., `ovcia vlna` ⇄ `Vlna (textil)`)  
- Provenance and origin metadata  

### **Relations**  
Directed semantic links between entities, such as:  
- `A is B` (taxonomic classification)  
- `A part_of B` (meronymy)  
- `A related_to B` (general association)  
- `A causes B` (causal linkage)  
- `A is_alias_of B` (synonym / disambiguation pointer)  

### **Metadata**  
Each node and relation stores:  
- confidence score  
- novelty score  
- origin module (e.g., `InputParser5`, `EnvoyExecutionLayer5`)  
- verification and commit timestamps  
- multi-hop depth and orbital level  

---

## 🔍 Core Operations  

### **KG_EXPLAIN**  
Provides a human-readable explanation of why two entities are connected.  
Shows direct relations, attribute links, and supporting rule provenance.

### **KG_EXPLAIN_DEEP**  
Generates full multi-hop hierarchical proof trees across several layers of the graph.  
Renders ASCII and HTML structured trees for deep symbolic transparency.

### **KG_RELATE**  
Discovers semantic relations between two entities using:  
- direct edges and alias bridges  
- multi-hop paths  
- transitive inference  
- novelty scoring  

### **Multi-Alias Resolution & Loop Suppression**  
Resolves user input against both primary labels and registered aliases.  
If any matching alias exists, KG ENGINE immediately fulfills the query from memory, blocking redundant AUTONOMY proposals.

### **KG_EXPORT**  
Exports the entire knowledge graph into a portable JSON structure (`kg_export.json`).

### **KG_IMPORT**  
Loads external or archived knowledge graphs under strict schema validation, cycle checks, and `PanelAPI` confirmation.

### **Comfort Commands**  
Developer-friendly CLI shortcuts:  
- `kg add entity <NAME>`  
- `kg add alias <PRIMARY> <ALIAS>`  
- `kg add relation <A> <B> <TYPE>`  
- `kg list entities`  
- `kg list relations`  
- `kg search <TERM>`  
- `kg rename entity`  
- `kg unset relation`  
- `kg release` (resets UI context to `none`)  

---

## 🔄 Operational Cycle  

### **1 — Load KG & Aliases**  
KG ENGINE loads the current graph and alias registry from:  
`autosave_kg.json`  
or fallback snapshots in `KG/kg_store/`.

### **2 — Ingest & Parse Query**  
Input arrives from `sirius_orchestrator.py` (via native IPC on port 8080).  
`InputParser5` extracts complete compound noun phrases and isolates copula verbs (`je`, `sú`).

### **3 — Graph Lookup & Alias Evaluation**  
- Check for exact entity or registered alias match.  
- If present → generate reasoning output and render directly.  
- If missing → trigger AUTONOMY proposal loop (`[ÁNO/NIE]`).  

### **4 — Process Mutation & Customs Validation**  
Upon confirmed learning or manual developer command:  
- Validate payload against Non-Bio Domain Shield (no habitat on technical concepts).  
- Authorize structural changes via COLNIK‑6.x (Customs Inspection).  
- Atomically commit the node and all linked aliases to `autosave_kg.json`.  

### **5 — Provide Output & Telemetry**  
Results are dispatched to:  
- ReasoningEngine5  
- AUTONOMY 6.x (Control, Guard & Triage Mode)  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) on port 8080  

---

## 🔐 Safety Rules  
- ❌ No destructive graph operations without explicit confirmation (`PanelAPI` [ÁNO/NIE])  
- 🔒 Atomic serialization to `autosave_kg.json` guarantees graph persistence  
- 🛑 Confirmed entities must never trigger repetitive learning proposals (Zero Recurrence)  
- 🚫 Strict non-biological domain shields prevent false habitat attributes on technical concepts  
- ⚠ Multi-hop traversal depth is strictly bounded to prevent infinite cyclic loops  
- 🛡 UI input clearance triggers automatic context release (`currentModule = "none"`), isolating host shells  

---

## 📊 Module Status (v5.9.0)  
- ✔ Fully implemented & synchronized with Runtime 5.9.0  
- ✔ Compound noun phrase support active (`InputParser5`)  
- ✔ Multi-alias indexing and persistence verified  
- ✔ Zero proposal recurrence confirmed  
- ✔ Single-process orchestrator integration (Port 8080) operational  
- ✔ Multi-hop reasoning and proof trees verified  
- ✔ COLNIK‑6.x High-Performance IPC validation functional  
- ✔ Autosave/autoload stability verified on Windows 11  
- ✔ 4-Panel UI Suite integration complete  

---

## 🏁 Summary  
KG ENGINE 6.x is the symbolic core of SIRIUS Local AI (v5.9.0).  
It manages entities, aliases, relations, explainability, and multi-hop reasoning with deterministic precision.  
The engine is fully integrated with Runtime 5.9.0, `sirius_orchestrator.py`, ReasoningEngine5, AUTONOMY 6.x, COLNIK-6.x, and PanelAPI, forming the foundation of SIRIUS’s transparent, offline-first knowledge architecture.
