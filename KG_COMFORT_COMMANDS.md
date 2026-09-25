# 🧩 KG COMFORT COMMANDS — Developer‑Friendly Knowledge Graph Operations  
**Status:** ✔ Active (Enhanced)  
**Version:** 6.x (Updated for Runtime 5.9.0 UNIFIED)  
**Component:** KG Comfort Commands  
**Role:** Fast, safe, deterministic developer commands for manipulating the Knowledge Graph with multi-alias indexing, compound phrase handling, and orchestrator/PanelAPI supervision

---

## 🎯 Purpose  
KG Comfort Commands provide a **developer‑friendly command interface** for interacting directly with the Knowledge Graph.  
They simplify entity creation, multi-alias mapping, relation management, searching, renaming, exporting, importing, and debugging — all while maintaining:

- deterministic single-process execution via `sirius_orchestrator.py` on local port 8080  
- dual-key multi-alias persistence committed atomically to `autosave_kg.json`  
- compound noun phrase preservation via `InputParser5`  
- zero proposal recurrence on stored concepts  
- customs-grade validation through COLNIK‑6.x (Standard & High-Performance IPC Mode)  
- AUTONOMY 6.x gating, Guard resource supervision, and Triage Mode (`COLNIK-6.x/triage`)  
- interactive `PanelAPI` confirmation gates (`[ÁNO/NIE]`)  
- complete symbolic explainability (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP` proof trees)  

These commands are built for **rapid testing**, **schema debugging**, and **manual Knowledge Graph maintenance** inside SIRIUS Local AI.

---

## 🧩 Architecture Overview  
**Developer Mode / InputParser5 → KG Comfort Commands → sirius_orchestrator.py (Port 8080) → KG ENGINE / RuntimeCore → ReasoningEngine5 → AUTONOMY 6.x → COLNIK-6.x → PanelAPI [ÁNO/NIE] → autosave_kg.json**

### Core Responsibilities  
- simplify graph inspection and entity manipulation  
- register and link multi-word compound noun phrases without token truncation  
- support multi-alias mapping (linking colloquial queries to formal encyclopedic titles)  
- enforce zero proposal recurrence for established concepts and aliases  
- maintain atomic serialization consistency with `autosave_kg.json`  
- generate explainability metadata and proof trees  
- validate mutations through COLNIK-6.x prior to storage commit  
- support terminal debugging with automatic module release (`currentModule = "none"`)  

### Key Files  
- `KG/kg_engine.py`  
- `runtime5/runtime_core.py`  
- `runtime5/input_parser_5.py`  
- `KG/autosave_kg.json`  
- `KG/kg_export.json`  
- `KG/kg_import.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  

---

## 🔍 Command Categories  

### **1 — Entity & Alias Commands**  
#### `kg add entity <NAME>`  
Creates a new entity (supporting compound phrases like `ovcia vlna`) with deterministic metadata via the orchestrator.

#### `kg add alias <PRIMARY_ENTITY> <ALIAS>`  
Registers a secondary lookup alias for an entity, ensuring queries under either term resolve to the same node without triggering redundant learning proposals.

#### `kg rename entity <OLD> <NEW>`  
Renames an entity while preserving all incoming and outgoing relations and alias pointers.

#### `kg delete entity <NAME>`  
Deletes an entity and its bound edges (requires AUTONOMY proposal, COLNIK validation, and explicit PanelAPI `[ÁNO/NIE]` approval).

#### `kg list entities`  
Lists all indexed primary entities and registered aliases in the Knowledge Graph.

---

### **2 — Relation & Explainability Commands**  
#### `kg add relation <A> <B> <TYPE>`  
Creates a typed relation between two nodes (e.g., `ovcia vlna` -> `vlna` -> `is_type_of`).

#### `kg unset relation <A> <B>`  
Removes a specific relation safely without corrupting adjacent branches.

#### `kg list relations [ENTITY]`  
Displays all active relations (optionally filtered by a specific node) with confidence and provenance tags.

#### `kg explain <A> <B>`  
Executes `KG_EXPLAIN`, displaying the direct derivation path and active inference rule attribution.

#### `kg explain deep <A> <B>`  
Executes `KG_EXPLAIN_DEEP`, rendering the full multi-hop hierarchical proof tree (ASCII + HTML view).

---

### **3 — Search & Pathfinding Commands**  
#### `kg search <TERM>`  
Fuzzy and multi-word semantic search across entities, aliases, and attribute fields.

#### `kg find related <ENTITY>`  
Lists all first-degree inbound and outbound neighbors for the specified node.

#### `kg find path <A> <B>`  
Executes cycle-safe deterministic pathfinding between two nodes, displaying orbital transitions.

---

### **4 — Import, Export & Persistence Commands**  
#### `kg export [FILE]`  
Exports the complete Knowledge Graph snapshot to `kg_export.json` (or a designated path).

#### `kg import <FILE>`  
Imports an external graph package (enforces schema validation, cycle checks, and mandatory user approval).

#### `kg commit`  
Forces an immediate atomic write of active memory graphs to `autosave_kg.json`.

#### `kg autosave on/off`  
Toggles automatic serialization tracking managed by TimeCore.

---

### **5 — Diagnostics & Guard Commands**  
#### `kg debug entity <NAME>`  
Outputs raw JSON representation of an entity, including aliases, bound rules, and timestamp metadata.

#### `kg debug relation <A> <B>`  
Inspects property inheritance, confidence weights, and rule provenance between two nodes.

#### `kg debug stats`  
Displays total node counts, alias density, relation counts, depth metrics, and memory consumption verified by Guard.

#### `kg release`  
Forces the terminal context to reset `currentModule = "none"`, unlocking the host command line interface.

---

## 🔐 Safety & Validation  

### **Identity & Domain Protection**  
All developer commands strictly respect:  
- OWNER / FAMILY / STRANGER access modes  
- SCHOOLWORK priority rules  
- Non-Bio Domain Shield (preventing arbitrary binding of biological habitat properties to technical concepts)  

### **Explainability Enforcement**  
Every KG modification automatically updates:  
- `KG_EXPLAIN` reasoning traces  
- rule attribution metadata (`MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`, etc.)  
- proof tree derivation nodes  

### **COLNIK-6.x Customs Clearance**  
All mutations pass through COLNIK‑6.x (Standard & High-Performance IPC Mode):  
- enterprise-grade graph cycle and anomaly detection  
- reversible mutation verification  
- schema integrity enforcement  

### **AUTONOMY Supervision & PanelAPI Confirmation**  
AUTONOMY 6.x and `PanelAPI` supervise high-impact operations:  
- mass entity or relation deletions  
- foreign package imports  
- unverified entity creations without provenance  

---

## 📊 Module Status (v5.9.0)  
- ✔ Fully updated & optimized for Runtime 5.9.0  
- ✔ Compound noun phrase support active  
- ✔ Multi-alias indexing and lookup validated  
- ✔ Zero proposal recurrence verified  
- ✔ Single-process orchestrator integration on port 8080 operational  
- ✔ Atomic serialization to `autosave_kg.json` verified  
- ✔ 4-Panel UI Suite integration and terminal state release active  
- ✔ COLNIK‑6.x High-Performance IPC verification functional  
- ✔ Explainability proof trees (`KG_EXPLAIN_DEEP`) verified  

---

## 🏁 Summary  
KG Comfort Commands provide a **safe, deterministic, developer‑friendly interface** for managing the Knowledge Graph in SIRIUS Local AI (v5.9.0).  
They streamline entity creation, multi-alias mapping, relation management, search queries, debugging, and data export/import — while upholding strict explainability, central orchestrator execution, zero proposal recurrence, and customs-grade COLNIK validation.
