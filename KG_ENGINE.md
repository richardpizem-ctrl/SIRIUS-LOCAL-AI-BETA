# 🧠 KG ENGINE 6.x — Knowledge Graph Core  
**Status:** ✔ Active (Enhanced)  
**Version:** 6.x  
**SIRIUS Local AI Version:** 5.9.1  
**Component:** KG ENGINE  
**Role:** Unified symbolic knowledge graph engine powering isolated dual-language partitions, native lossless entity merging, taxonomical deduction, non-destructive reverse location reasoning, Token Guard sanitization, and multi-hop reasoning under orchestrator and PanelAPI supervision

---

## 🎯 Purpose  
The KG ENGINE 6.x module is the central symbolic knowledge system of SIRIUS Local AI (v5.9.1).  
It manages isolated language stores (`autosave_kg.json` for Slovak and `autosave_kg_en.json` for English), native lossless entity mergers (`kg merge`), ontological taxonomical deduction (`KG_VERIFY`), reverse habitat querying, compound semantic concepts, multi-alias mappings, and graph-based reasoning operations.  
All explainability, relation discovery, and multi-hop inference rely directly on this engine.

KG ENGINE provides deterministic, transparent, and fully inspectable knowledge operations driven by `sirius_orchestrator.py` on local port 8080 with embedded TerminalAssistant + TimeCore, protected by Token Guard, and governed by COLNÍK Guard and AUTONOMY 6.x.

---

## 🧩 Architecture Overview  
**Runtime 5.9.1 / InputParser5 → Token Guard → sirius_orchestrator.py (Port 8080) → Language Context Router → KG ENGINE / RuntimeCore → ReasoningEngine5 → AUTONOMY 6.x → COLNIK (IPC Mode) → PanelAPI [ÁNO/NIE] / [YES/NO] → Dual-Graph Commit (`autosave_kg.json` / `autosave_kg_en.json`)**

### Core Responsibilities  
- Manage entities, relations, and compound noun phrases (`ovcia vlna`, `mobilny telefon`, `pevna linka`)  
- Enforce strict physical and logical isolation between Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) knowledge graphs  
- Support dynamic language context switching bound to caller UI language headers (`SK` / `EN`)  
- Execute native lossless entity mergers (`kg merge <src> into <tgt>`), migrating all attributes and establishing alias edges without external scripts  
- Perform context-aware taxonomical inference (`KG_VERIFY`), automatically deducing higher-order biological categories (e.g., marsupials/macropods -> mammals) with persistent edge auto-commits  
- Execute non-destructive reverse location queries (`_execute_reverse_location_query`) with multi-stem matching and anti-flora classification guards  
- Support uniform attribute retrieval via `self.kg.get_attributes()` across all traversals  
- Enforce greedy trailing punctuation stripping (`.rstrip("?")`) and confirmation state latching across interactive turns  
- Enforce zero proposal recurrence: suppress redundant learning proposals once an entity, alias, or taxonomical edge is committed  
- Provide semantic explainability (KG_EXPLAIN, KG_EXPLAIN_DEEP with proof trees)  
- Perform relation discovery (KG_RELATE)  
- Handle graph import/export with schema and cycle validation  
- Maintain atomic serialization integrity across both language backends  
- Provide developer comfort commands with automatic UI state clearance (`currentModule = "none"`)  

### Key Files  
- `KG/kg_engine.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/input_parser_5.py`  
- `runtime5/envoy_quarantine_5.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  
- `KG/kg_store/`  
- `KG/kg_export.json`  
- `KG/kg_import.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  

---

## 🧱 Knowledge Structure  

### **Dual-Language Isolated Stores**  
Physical separation prevents cross-lingual contamination, mixed summaries, and bilingual hallucinations:  
- `autosave_kg.json` — dedicated Slovak knowledge domain  
- `autosave_kg_en.json` — dedicated English knowledge domain  
- `RuntimeCore` binds active graph operations dynamically to the matching store during request execution.

### **Entities & Multi-Alias Nodes**  
Fundamental nodes representing concepts, objects, categories, or compound phrases (`ovcia vlna`, `macropus`).  
Each node supports an internal alias registry:  
- Primary canonical identifier  
- Alternate query aliases (e.g., `ovcia vlna` ⇄ `Vlna (textil)`)  
- Transferred alias links from native entity mergers (`src -[alias]-> tgt`)  
- Provenance, language tag, and origin metadata  

### **Relations & Taxonomical Edges**  
Directed semantic links between entities, such as:  
- `A is_a B` / `A je B` (taxonomic classification, e.g., `macropus` -> `cicavec` / `kangaroo` -> `mammal`)  
- `A part_of B` (meronymy)  
- `A related_to B` (general association)  
- `A causes B` (causal linkage)  
- `A is_alias_of B` / `A alias B` (synonym / merge redirection pointer)  
- `A vyskyt B` / `A lives_in B` (geographic habitat binding)  

### **Metadata**  
Each node and relation stores:  
- confidence score  
- novelty score  
- origin module (e.g., `InputParser5`, `EnvoyExecutionLayer5`, `MergeEngine`)  
- verification and commit timestamps  
- multi-hop depth and orbital level  

---

## 🔍 Core Operations  

### **Dual-Language Dynamic Context Switching**  
Switches the active graph pointer between `self.kg_sk` and `self.kg_en` based on the query language parameter, ensuring retrieval, reasoning, and persistence remain isolated.

### **Native Lossless Entity Merge (`kg merge`)**  
Consolidates two entities in-memory directly within `RuntimeCore`:  
1. Copies all attributes, descriptions, and habitat notes from `<source>` to `<target>`.  
2. Converts `<source>` into an alias node pointing directly to `<target>` with an `alias` edge.  
3. Atomically commits changes to the active language JSON store.

### **Taxonomical Category Deduction (`KG_VERIFY`)**  
Evaluates relation chains and stored textual descriptions to deduce hierarchical biological categories (e.g., recognizing that a marsupial/macropod is a mammal).  
Verified categories auto-commit directly to the graph with zero proposal recurrence on future queries.

### **Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`)**  
Traverses graph entities using uniform getters (`self.kg.get_attributes()`):  
- matches inflected regional stems across both languages (*Austrálii*, *Austrália*, *Australia*)  
- applies the False-Positive Flora Guard to ensure tree-dwelling animals (*„stromový vačkovec“*) are not misclassified as plants, reliably indexing *Koala*, *Macropus*, and *Krokodíl morský* under Australian fauna.

### **KG_EXPLAIN**  
Provides a human-readable explanation of why two entities are connected.  
Shows direct relations, attribute links, and supporting rule provenance.

### **KG_EXPLAIN_DEEP**  
Generates full multi-hop hierarchical proof trees across several layers of the graph.  
Renders ASCII and HTML structured trees for deep symbolic transparency.

### **KG_RELATE**  
Discovers semantic relations between two entities using direct edges, alias bridges, multi-hop paths, transitive inference, and novelty scoring.

### **Punctuation Stripping & Confirmation Latching**  
Sanitizes raw query inputs by trimming trailing question marks (`.rstrip("?")`), guaranteeing that `CO JE MACROPUS?` resolves to `macropus`.  
Latches pending proposal targets in memory so positive confirmations (`ÁNO` / `YES`) execute reliably without losing context.

### **KG_EXPORT**  
Exports the entire knowledge graph snapshot into a portable JSON structure (`kg_export.json`).

### **KG_IMPORT**  
Loads external or archived knowledge graphs under strict schema validation, cycle checks, and `PanelAPI` confirmation.

### **Comfort Commands**  
Developer-friendly CLI shortcuts:  
- `kg add entity <NAME>`  
- `kg merge <SOURCE> into <TARGET>`  
- `kg verify <ENTITY> <CATEGORY>`  
- `kg where <ENTITY>`  
- `kg reverse location <LOCATION>`  
- `kg add alias <PRIMARY> <ALIAS>`  
- `kg add relation <A> <B> <TYPE>`  
- `kg switch language <SK|EN>`  
- `kg list entities`  
- `kg list relations`  
- `kg search <TERM>`  
- `kg rename entity`  
- `kg unset relation`  
- `kg release` (resets UI context to `none`)  

---

## 🔄 Operational Cycle  

### **1 — Load Dual Language Graphs**  
KG ENGINE loads the current graphs and alias registries from:  
- `autosave_kg.json` (Slovak partition)  
- `autosave_kg_en.json` (English partition)  
or fallback snapshots in `KG/kg_store/`.

### **2 — Ingest, Sanitize & Context Dispatch**  
- Raw input passes Token Guard; forbidden injection characters (`@#$%^&*`) are dropped immediately.  
- `InputParser5` strips trailing punctuation (`.rstrip("?")`), preserves compound noun phrases, and isolates copula verbs.  
- Caller language header (`SK` / `EN`) binds active runtime operations to `autosave_kg.json` or `autosave_kg_en.json`.

### **3 — Graph Lookup & Alias Evaluation**  
- Check active language graph for exact entity or registered alias match.  
- If present → generate reasoning output and render directly.  
- If missing → latch pending proposal target and trigger AUTONOMY confirmation prompt (`[ÁNO/NIE]` / `[YES/NO]`).  

### **4 — Process Mutation & Customs Validation**  
Upon confirmed learning, native merge, or developer command:  
- Validate payload against Non-Bio Domain Shield (no habitat on technical concepts).  
- Authorize structural changes via COLNIK‑6.x (Customs Inspection).  
- Atomically commit the node, attributes, verified taxonomical relations, and linked aliases to the target store (`autosave_kg.json` or `autosave_kg_en.json`).  

### **5 — Provide Output & Telemetry**  
Results are dispatched to:  
- ReasoningEngine5  
- AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Safe Trash)  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) on port 8080  

---

## 🔐 Safety Rules  
- ❌ No destructive graph operations without explicit confirmation (`PanelAPI` [ÁNO/NIE] / [YES/NO])  
- 🗄️ Strict dual-language isolation: Slovak and English entities must never be merged into a single mixed graph  
- ⛔ Token Guard input protection: malformed injection payloads (`@#$%^&*`) are blocked at runtime entry  
- 🔒 Atomic serialization to `autosave_kg.json` and `autosave_kg_en.json` guarantees persistence  
- 🛑 Confirmed entities and inferred taxonomies must never trigger repetitive learning proposals (Zero Recurrence)  
- 🚫 Strict non-biological domain shields prevent false habitat attributes on technical concepts  
- ⚠ Multi-hop traversal depth is strictly bounded to prevent infinite cyclic loops  
- 📦 Automatic quarantine sliding-window rotation enforces a 100-file ceiling in `COLNIK-6.x/envoy/quarantine/`  
- 🛡 UI input clearance triggers automatic context release (`currentModule = "none"`), isolating host shells  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully implemented & synchronized with Runtime 5.9.1 architecture  
- ✔ Dual-Language Graph Isolation (`autosave_kg.json` & `autosave_kg_en.json`) operational  
- ✔ Native Lossless Entity Merge (`kg merge`) validated  
- ✔ Taxonomical category inference auto-commit (`KG_VERIFY`) operational  
- ✔ Non-destructive reverse habitat engine with anti-flora guard verified  
- ✔ Token Guard raw input sanitization verified  
- ✔ Trailing punctuation trimming and confirmation state latching active  
- ✔ Compound noun phrase support active (`InputParser5`)  
- ✔ Multi-alias indexing and persistence verified  
- ✔ Zero proposal recurrence confirmed  
- ✔ Single-process orchestrator integration (Port 8080) operational  
- ✔ Multi-hop reasoning and proof trees verified  
- ✔ COLNIK‑6.x High-Performance IPC and COLNÍK Guard validation functional  
- ✔ Autosave/autoload stability verified under Windows 11  
- ✔ 4-Panel UI Suite integration complete  

---

## 🏁 Summary  
KG ENGINE 6.x is the symbolic core of SIRIUS Local AI (v5.9.1).  
It manages isolated dual-language knowledge bases, native lossless entity merges, taxonomical deductions, reverse habitat queries, aliases, relations, explainability, and multi-hop reasoning with deterministic precision.  
The engine is fully integrated with Runtime 5.9.1, `sirius_orchestrator.py` on port 8080, ReasoningEngine5, AUTONOMY 6.x, COLNIK-6.x, Token Guard, and PanelAPI, forming the foundation of SIRIUS’s transparent, offline-first knowledge architecture.
