# 🧠 REASONING ENGINE 5.x — Deterministic Multi‑Hop Inference Core  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.x  
**SIRIUS Local AI Version:** 5.9.1  
**Component:** ReasoningEngine5  
**Role:** Deterministic symbolic reasoning engine performing multi-hop inference, dual-language graph reasoning, taxonomical deduction, non-destructive reverse location evaluation, native merge traversal, and proof-tree generation under single-process orchestrator supervision

---

## 🎯 Purpose  
ReasoningEngine5 is the core inference module of SIRIUS Local AI (v5.9.1).  
It evaluates symbolic rules, performs multi-hop graph derivations, validates semantic hypotheses, handles compound noun phrases via `InputParser5` with trailing punctuation hygiene (`.rstrip("?")`), executes taxonomical category deduction (`KG_VERIFY`), evaluates reverse geographic habitats with anti-flora shielding, resolves multi-alias pointers, and generates structured explanations across isolated dual-language Knowledge Graphs (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN).

The engine is completely deterministic, transparent, and designed for enterprise-grade symbolic explainability (XAI), orchestrated through `sirius_orchestrator.py` on local port 8080 with embedded `TerminalAssistant` and `TimeCore` (`cycle_delta()`), protected by `Token Guard`, and supervised by `Guard` and `COLNÍK Guard`.

---

## 🧩 Architecture Overview  
**Runtime 5.9.1 / InputParser5 → Token Guard → sirius_orchestrator.py (Port 8080) → Language Context Router → KG ENGINE (`autosave_kg.json` / `autosave_kg_en.json`) → ReasoningEngine5 → AUTONOMY 6.x → COLNIK-6.x (IPC Mode) → PanelAPI [ÁNO/NIE] / [YES/NO] → EXECUTE 6.x**

### Core Responsibilities  
- evaluate deterministic symbolic inference rules across isolated Slovak and English graph stores  
- perform context-aware taxonomical category deduction (`KG_VERIFY`), recognizing higher-order sub-taxa (e.g., marsupials/macropods -> mammals) and auto-committing edges with zero proposal recurrence  
- execute non-destructive reverse location reasoning (`_execute_reverse_location_query`) with multi-stem matching (*Austrálii*, *Austrália*, *Australia*) and anti-flora shielding for tree-dwelling fauna  
- support traversal across native entity merges (`kg merge`), seamlessly following directional alias edges (`src -[alias]-> tgt`)  
- evaluate uniform node attributes via `self.kg.get_attributes()` across all rule evaluations  
- perform multi-hop graph traversals and orbital jumps across compound concepts (`ovcia vlna`, `mobilny telefon`, `pevna linka`)  
- resolve multi-alias entities to canonical nodes, ensuring zero proposal recurrence on established concepts  
- auto-detect hypotheses from natural language queries and copula verb structures (`je`, `sú`, `is`, `are`) with greedy punctuation stripping (`.rstrip("?")`)  
- maintain confirmation state latching across interactive conversation turns  
- validate semantic relations against the Non-Bio Domain Shield (`EnvoyNormalizer5`)  
- generate structured WHY reasoning and proof trees (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP`) in ASCII and HTML  
- integrate with AUTONOMY 6.x decision layers, the 4-Panel UI Suite, and the single-process IPC daemon on port 8080  

### Key Files  
- `runtime5/ReasoningEngine5.py`  
- `runtime5/runtime_core_5.py`  
- `runtime5/input_parser_5.py`  
- `KG/kg_engine.py`  
- `autosave_kg.json`  
- `autosave_kg_en.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  

---

## 🔍 Reasoning Pipeline (v5.9.1)  

### **1 — Semantic Query Ingestion, Token Guard & Context Binding**  
- Inputs pass through **Token Guard**; malicious symbolic character sequences (`@#$%^&*`) are dropped at entry.  
- `InputParser5` strips trailing question marks (`.rstrip("?")`) and extracts complete compound noun phrases and isolated copula verbs (`je`, `sú`, `is`, `are`).  
- Caller language parameters dynamically bind the engine to the dedicated partition: `autosave_kg.json` (SK) or `autosave_kg_en.json` (EN).  
- If no explicit hypothesis is supplied, the engine inspects canonical nodes, merge-alias edges, and alias registries to auto-detect target relations.

### **2 — Deterministic Rule Evaluation**  
The engine loads and evaluates pre-indexed symbolic inference rules in constant time:  
- `TaxonomyRule` & `TaxonomicalCategoryDeductionRule`  
- `OrbitTypeInferenceRule`  
- `AutoTypeInferenceRule`  
- `MultiHopOrbitInferenceRule`  
- `DedicsnostVlastnostiRule`  
- `TranzitivneRelacieRule`  

Each rule execution is strictly deterministic and appends nodes to the evidence trace.

### **3 — Taxonomical & Marsupial Inference (`KG_VERIFY`)**  
- Evaluates biological sub-taxa classifications directly from textual records and relation chains (e.g., establishing that *Macropus* or kangaroos belong to the class *Mammalia*).  
- Inferred edges (`is_a mammal`, `je cicavec`) are committed directly to disk with zero future confirmation recurrence.

### **4 — Non-Destructive Reverse Location Engine**  
- Executes `_execute_reverse_location_query` using uniform attribute traversal (`self.kg.get_attributes()`).  
- Supports multi-stem location queries (*Austrálii*, *Austrália*, *Australia*).  
- Applies the **False-Positive Flora Guard**: prevents tree-dwelling fauna (*„stromový vačkovec“*) from being misclassified as plants, reliably confirming *Koala*, *Macropus*, and *Krokodíl morský* as Australian fauna.

### **5 — Bounded Multi-Hop Reasoning & Merge Bridges**  
The engine traverses multi-hop edges across the active Knowledge Graph:  
- direct edges, alias bridges, and merge-redirection edges (`src -[alias]-> tgt`)  
- transitive relation chains (`A is B` ∧ `B is C` ⇒ `A is C`)  
- inherited attribute propagation across taxonomic hierarchies  
- orbital semantic category leaps  
- multi-layer proof-tree compilation  

Traversal depth is strictly capped to prevent runaway cyclic recursion, tracked within `TimeCore` cycle budgets (`cycle_delta()`).

### **6 — WHY Reasoning & Deep Explainability (XAI)**  
Produces a structured, auditable explanation payload:  
- target hypothesis, language partition tag, and evaluated query  
- verified rule provenance and evidence nodes  
- confidence score calculation  
- multi-hop transition chain  
- hierarchical ASCII / HTML proof tree  

WHY reasoning feeds directly into AUTONOMY 6.x decision governance and interactive `PanelAPI` confirmation prompts (`[ÁNO/NIE]` / `[YES/NO]`) with active state latching. Once confirmed and recorded in `autosave_kg.json` or `autosave_kg_en.json`, subsequent reasoning cycles resolve instantly without triggering redundant learning proposals.

### **7 — Workflow & UI Suite Integration**  
Reasoning outputs are dispatched to:  
- **AUTONOMY 6.x:** Autonomous governance, Guard metric monitoring, Safe Trash governance, and Triage containment (`COLNIK-6.x/triage`)  
- **COLNIK-6.x & COLNÍK Guard:** Customs inspection and 0.0s command execution auditing  
- **EXECUTE 6.x:** Deterministic mutation execution, native merge commits, and dual-graph persistence  
- **4-Panel UI Suite:** Renders directly in browser panels on port 8080, triggering automatic module release (`currentModule = "none"`) upon query clearance  

---

## 🧱 Core Inference Rules  

### **TaxonomicalCategoryDeductionRule (`KG_VERIFY`)**  
Analyzes entity summaries and ontological links to deduce higher-order taxonomical groupings (e.g., deducing that macropods are mammals), auto-committing verified relationships directly to the active knowledge store.

### **OrbitTypeInferenceRule**  
Determines contextual and semantic orbital associations between high-level categories and specific concepts.

### **AutoTypeInferenceRule**  
Infers entity types and class memberships automatically based on Knowledge Graph ontology schemas and attributes.

### **MultiHopOrbitInferenceRule**  
Executes multi-step orbital jumps, discovering non-obvious indirect relations between distant graph clusters while enforcing cycle safety.

### **DedicsnostVlastnostiRule**  
Propagates inherited characteristics down taxonomic hierarchies (e.g., if mammal has attribute X, specific animal inherits attribute X), while barring cross-domain biological attribute leakage onto technical/abstract entities.

### **TranzitivneRelacieRule**  
Evaluates transitive logic across chains of directed edges, verifying structural deduction across intermediate nodes and alias links resulting from `kg merge`.

---

## 🔐 Safety Rules  
- ❌ No destructive graph mutations or file deletions without explicit user confirmation (`PanelAPI` [ÁNO/NIE] / [YES/NO] & HitL Safe Trash)  
- ⛔ Immediate Token Guard rejection on inputs containing malformed symbolic sequences (`@#$%^&*`)  
- 🗄️ Strict dual-language isolation: Slovak and English reasoning cycles execute exclusively within their corresponding graph partitions  
- 🔒 Deterministic, reproducible rule chaining without probabilistic hallucinations  
- 🛑 Multi-hop traversal depth is bounded by strict orbital thresholds enforced by Guard  
- 🚫 Strict non-biological domain shields prevent attributing habitat or biological properties to abstract or technical concepts  
- 🔁 Zero Proposal Recurrence: Entities confirmed under secondary aliases or deduced taxonomies resolve from graph memory without repeated confirmation prompts  
- 🛡 UI input clearance enforces immediate state release (`currentModule = "none"`), protecting host shells from command execution  
- 🧠 Transparent derivation proof trees required for all outputs  

---

## 📊 Module Status (v5.9.1)  
- ✔ Fully implemented & synchronized with Runtime 5.9.1 architecture  
- ✔ Dual-Language Graph Reasoning (`autosave_kg.json` & `autosave_kg_en.json`) operational  
- ✔ Taxonomical category inference auto-commit (`KG_VERIFY`) operational  
- ✔ Non-destructive reverse habitat engine with False-Positive Flora Guard verified  
- ✔ Native `kg merge` alias traversal operational  
- ✔ Token Guard input sanitization active  
- ✔ Trailing punctuation trimming (`.rstrip("?")`) and confirmation state latching active  
- ✔ Compound noun phrase inference verified (`InputParser5`)  
- ✔ Multi-alias graph resolution operational with zero proposal recurrence  
- ✔ Multi-hop inference and orbital rules verified  
- ✔ Hierarchical proof-tree generation active (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP`)  
- ✔ Single-process orchestrator integration on port 8080 operational with embedded TerminalAssistant + TimeCore  
- ✔ COLNIK-6.x Customs validation and COLNÍK Guard handshake verified  
- ✔ AUTONOMY 6.x proposal/confirmation, HitL Safe Trash & Triage Mode integrated  
- ✔ 4-Panel UI Suite synchronization and terminal decoupling verified  

---

## 🏁 Summary  
ReasoningEngine5 is the deterministic inference core of SIRIUS Local AI (v5.9.1).  
It performs multi-hop reasoning, evaluates symbolic rules, executes taxonomical deductions, navigates reverse habitat inquiries, traverses merged entity aliases, and generates transparent WHY explanations and proof trees throughout the autonomy cycle under central orchestrator supervision.  
The engine is production-stable and fully integrated with KG ENGINE, `sirius_orchestrator.py`, AUTONOMY 6.x, COLNIK-6.x, Token Guard, COLNÍK Guard, PanelAPI, EXECUTE, and the 4-Panel UI Suite.
