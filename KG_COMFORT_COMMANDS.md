# 🧩 KG COMFORT COMMANDS — Developer‑Friendly Knowledge Graph Operations  
**Status:** ✔ Active (Enhanced)  
**Version:** 6.x (Updated for Runtime 5.9.1 UNIFIED)  
**Component:** KG Comfort Commands  
**Role:** Fast, safe, deterministic developer commands for manipulating the Knowledge Graph with dual-language partition support, native entity merging, taxonomical reasoning, Token Guard sanitization, and orchestrator/PanelAPI supervision

---

## 🎯 Purpose  
KG Comfort Commands provide a **developer‑friendly command interface** for interacting directly with the Knowledge Graph.  
They simplify entity creation, multi-alias mapping, native entity merging (`kg merge`), relation management, reverse location searching, renaming, exporting, importing, and debugging — all while maintaining:

- deterministic single-process execution via `sirius_orchestrator.py` on local port 8080 with embedded TerminalAssistant + TimeCore  
- dynamic language context switching across isolated graph stores (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN)  
- native lossless entity merging (`kg merge <src> into <tgt>`) without external dependencies  
- taxonomical & marsupial inference (`KG_VERIFY`) with persistent edge auto-commits  
- non-destructive reverse location queries (`_execute_reverse_location_query`) with anti-flora classification guards  
- entry-level Token Guard sanitization rejecting corrupted or malicious injection strings (`@#$%^&*`)  
- greedy trailing punctuation stripping (`.rstrip("?")`) preventing token lookup mismatch  
- confirmation state latching across conversation turns  
- zero proposal recurrence on stored concepts and inferred taxonomies  
- customs-grade validation through COLNIK‑6.x (Standard & High-Performance IPC Mode) with COLNÍK Guard 0.0s command blocking  
- AUTONOMY 6.x gating, Guard resource supervision, and HitL Safe Trash quarantine pipeline  
- interactive `PanelAPI` confirmation gates (`[ÁNO/NIE]` / `[YES/NO]`)  
- complete symbolic explainability (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP` proof trees)  

These commands are built for **rapid testing**, **schema debugging**, and **manual Knowledge Graph maintenance** inside SIRIUS Local AI.

---

## 🧩 Architecture Overview  
**Developer Mode / InputParser5 → Token Guard → KG Comfort Commands → sirius_orchestrator.py (Port 8080) → Language Context Router → KG ENGINE / RuntimeCore → ReasoningEngine5 → AUTONOMY 6.x → COLNIK-6.x → PanelAPI [ÁNO/NIE] / [YES/NO] → Dual KG Commit (`autosave_kg.json` / `autosave_kg_en.json`)**

### Core Responsibilities  
- simplify graph inspection and entity manipulation across Slovak and English partitions  
- execute native lossless entity mergers (`kg merge <src> into <tgt>`), transferring all attributes and generating alias edges  
- deduce and auto-commit taxonomical categories (`kangaroo -[is_a]-> mammal`, `macropus -[je]-> cicavec`) without confirmation loops  
- execute robust reverse location lookups with anti-flora protection for tree-dwelling fauna  
- register and link multi-word compound noun phrases without token truncation  
- enforce zero proposal recurrence for established concepts, aliases, and deduced relations  
- maintain atomic serialization consistency with `autosave_kg.json` and `autosave_kg_en.json`  
- generate explainability metadata and proof trees  
- validate mutations through COLNIK-6.x and Token Guard prior to storage commit  
- support terminal debugging with automatic module release (`currentModule = "none"`)  

### Key Files  
- `KG/kg_engine.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/input_parser_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  
- `KG/kg_export.json`  
- `KG/kg_import.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  

---

## 🔍 Command Categories  

### **1 — Entity, Alias & Merge Commands**  
#### `kg add entity <NAME>`  
Creates a new entity (supporting compound phrases like `ovcia vlna` or `mobilny telefon`) in the active language graph store (`autosave_kg.json` or `autosave_kg_en.json`).

#### `kg merge <SOURCE> into <TARGET>`  
Natively merges `<SOURCE>` into `<TARGET>` directly inside RuntimeCore: relocates all attributes (descriptions, habitats, properties) without data loss and transitions `<SOURCE>` into an alias node with a directional edge (`SOURCE -[alias]-> TARGET`).

#### `kg add alias <PRIMARY_ENTITY> <ALIAS>`  
Registers a secondary lookup alias for an entity, ensuring queries under either term resolve to the canonical node without triggering redundant learning proposals.

#### `kg rename entity <OLD> <NEW>`  
Renames an entity while preserving all incoming and outgoing relations and alias pointers.

#### `kg delete entity <NAME>`  
Deletes an entity and its bound edges (routes through HitL Safe Trash quarantine, requires AUTONOMY proposal, COLNIK validation, and explicit PanelAPI confirmation).

#### `kg list entities`  
Lists all indexed primary entities and registered aliases in the active Knowledge Graph partition.

---

### **2 — Relation, Taxonomy & Explainability Commands**  
#### `kg add relation <A> <B> <TYPE>`  
Creates a typed relation between two nodes (e.g., `macropus` -> `cicavec` -> `je` or `kangaroo` -> `mammal` -> `is_a`).

#### `kg verify <ENTITY> <CATEGORY>`  
Executes `KG_VERIFY` taxonomical inference: checks relational paths and stored text summaries to deduce hierarchical category membership (e.g., verifying macropods as mammals) and auto-commits the edge directly to the graph.

#### `kg unset relation <A> <B>`  
Removes a specific relation safely without corrupting adjacent branches.

#### `kg list relations [ENTITY]`  
Displays all active relations (optionally filtered by a specific node) with confidence and provenance tags.

#### `kg explain <A> <B>`  
Executes `KG_EXPLAIN`, displaying the direct derivation path and active inference rule attribution.

#### `kg explain deep <A> <B>`  
Executes `KG_EXPLAIN_DEEP`, rendering the full multi-hop hierarchical proof tree (ASCII + HTML view).

---

### **3 — Search, Habitat & Pathfinding Commands**  
#### `kg search <TERM>`  
Fuzzy and multi-word semantic search across entities, aliases, and attribute fields with greedy trailing punctuation stripping (`.rstrip("?")`).

#### `kg where <ENTITY>`  
Queries the geographic occurrence or habitat of an entity with automatic alias resolution.

#### `kg reverse location <LOCATION>`  
Executes `_execute_reverse_location_query`: uses multi-stem matching (*Austrálii*, *Austrália*, *Australia*) and anti-flora shielding to list all animals living in the specified habitat without misclassifying tree-dwelling fauna as plants.

#### `kg find related <ENTITY>`  
Lists all first-degree inbound and outbound neighbors for the specified node.

#### `kg find path <A> <B>`  
Executes cycle-safe deterministic pathfinding between two nodes, displaying orbital transitions.

---

### **4 — Import, Export & Dual-Language Persistence Commands**  
#### `kg export [FILE]`  
Exports the complete Knowledge Graph snapshot to `kg_export.json` (or a designated path).

#### `kg import <FILE>`  
Imports an external graph package (enforces schema validation, cycle checks, and mandatory user approval).

#### `kg switch language <SK|EN>`  
Dynamically toggles active runtime graph binding between `autosave_kg.json` (SK) and `autosave_kg_en.json` (EN).

#### `kg commit`  
Forces an immediate atomic write of active memory graphs to `autosave_kg.json` and `autosave_kg_en.json`.

#### `kg autosave on/off`  
Toggles automatic serialization tracking managed by TimeCore.

---

### **5 — Diagnostics, Security & Guard Commands**  
#### `kg debug entity <NAME>`  
Outputs raw JSON representation of an entity, including aliases, bound rules, uniform attributes (`get_attributes()`), and timestamp metadata.

#### `kg debug relation <A> <B>`  
Inspects property inheritance, confidence weights, and rule provenance between two nodes.

#### `kg debug stats`  
Displays total node counts, alias density, relation counts, language partition distribution, depth metrics, and memory consumption verified by Guard.

#### `kg release`  
Forces the terminal context to reset `currentModule = "none"`, unlocking the host command line interface.

---

## 🔐 Safety & Validation  

### **Dual-Language Isolation & Token Guard**  
All developer commands strictly respect:  
- Token Guard validation: instantly rejects inputs with forbidden symbols (`@#$%^&*`)  
- Linguistic separation: SK and EN mutations strictly affect their respective JSON stores  
- OWNER / FAMILY / STRANGER access modes  
- SCHOOLWORK priority rules  
- Non-Bio Domain Shield (preventing arbitrary binding of biological habitat properties to technical concepts)  

### **Explainability Enforcement**  
Every KG modification automatically updates:  
- `KG_EXPLAIN` reasoning traces  
- rule attribution metadata (`MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`, `TaxonomyRule`, etc.)  
- proof tree derivation nodes  

### **COLNIK-6.x Customs Clearance & COLNÍK Guard**  
All mutations pass through COLNIK‑6.x (Standard & High-Performance IPC Mode):  
- enterprise-grade graph cycle and anomaly detection  
- 0.0s hard blocking of forbidden system routines (`format`, `diskpart`, `rmdir /s`)  
- reversible mutation verification  
- schema integrity enforcement  

### **AUTONOMY Supervision & PanelAPI Confirmation**  
AUTONOMY 6.x and `PanelAPI` supervise high-impact operations:  
- mass entity or relation deletions (routed to Human-in-the-Loop Safe Trash)  
- native entity merges (`kg merge`)  
- foreign package imports  
- unverified entity creations without provenance  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully updated & optimized for Runtime 5.9.1 architecture  
- ✔ Dual-Language Graph Isolation (`autosave_kg.json` & `autosave_kg_en.json`) active  
- ✔ Native Lossless Entity Merge (`kg merge`) operational  
- ✔ Taxonomical inference auto-commit (`KG_VERIFY`) verified  
- ✔ Reverse habitat engine with anti-flora guard operational  
- ✔ Token Guard entry-level sanitization verified  
- ✔ Trailing punctuation trimming and confirmation state latching active  
- ✔ Compound noun phrase support active  
- ✔ Multi-alias indexing and lookup validated  
- ✔ Zero proposal recurrence verified  
- ✔ Single-process orchestrator integration on port 8080 operational  
- ✔ Atomic serialization to dual graphs verified  
- ✔ 4-Panel UI Suite integration and terminal state release active  
- ✔ COLNIK‑6.x High-Performance IPC and COLNÍK Guard verification functional  
- ✔ Explainability proof trees (`KG_EXPLAIN_DEEP`) verified  

---

## 🏁 Summary  
KG Comfort Commands provide a **safe, deterministic, developer‑friendly interface** for managing the Knowledge Graph in SIRIUS Local AI (v5.9.1).  
They streamline entity creation, dual-language routing, native lossless merging, taxonomical deduction, reverse location queries, multi-alias mapping, relation management, search queries, debugging, and data export/import — while upholding strict explainability, central orchestrator execution, zero proposal recurrence, and customs-grade COLNIK validation.
