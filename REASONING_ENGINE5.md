# 🧠 REASONING ENGINE 5.x — Deterministic Multi‑Hop Inference Core  
**Status:** ✔ Active (Enhanced)  
**Version:** 5.x  
**SIRIUS Local AI Version:** 5.9.0  
**Component:** ReasoningEngine5  
**Role:** Deterministic symbolic reasoning engine performing multi-hop inference, compound entity rule evaluation, multi-alias resolution, and proof-tree generation under single-process orchestrator supervision

---

## 🎯 Purpose  
ReasoningEngine5 is the core inference module of SIRIUS Local AI (v5.9.0).  
It evaluates symbolic rules, performs multi-hop graph derivations, validates semantic hypotheses, handles compound noun phrases via `InputParser5`, resolves multi-alias pointers, and generates structured explanations based on the unified Knowledge Graph (`autosave_kg.json`).

The engine is completely deterministic, transparent, and designed for enterprise-grade symbolic explainability (XAI), orchestrated through `sirius_orchestrator.py` on local port 8080 and supervised by `TimeCore` and `Guard`.

---

## 🧩 Architecture Overview  
**Runtime 5.9.0 / InputParser5 → sirius_orchestrator.py (Port 8080) → KG ENGINE (`autosave_kg.json`) → ReasoningEngine5 → AUTONOMY 6.x → COLNIK-6.x (IPC Mode) → PanelAPI [ÁNO/NIE] → EXECUTE 6.x**

### Core Responsibilities  
- evaluate deterministic symbolic inference rules  
- perform multi-hop graph traversals and orbital jumps across compound concepts (`ovcia vlna`, `mobilny telefon`)  
- resolve multi-alias entities to canonical nodes, ensuring zero proposal recurrence  
- auto-detect hypotheses from natural language queries and copula verb structures (`je`, `sú`)  
- validate semantic relations against the Non-Bio Domain Shield (`EnvoyNormalizer5`)  
- generate structured WHY reasoning and proof trees (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP`) in ASCII and HTML  
- integrate with AUTONOMY 6.x decision layers, the 4-Panel UI Suite, and the single-process IPC daemon  

### Key Files  
- `runtime5/ReasoningEngine5.py`  
- `runtime5/input_parser_5.py`  
- `KG/kg_engine.py`  
- `KG/autosave_kg.json`  
- `ORCHESTRATOR/sirius_orchestrator.py`  
- `PANEL_API/panel_api.py`  
- `IPC_DATA/proposals.json`  
- `IPC_DATA/responses.json`  

---

## 🔍 Reasoning Pipeline (v5.9.0)  

### **1 — Semantic Query Ingestion & Hypothesis Detection**  
Input parsed by `InputParser5` preserves complete multi-word compound noun phrases.  
If no explicit hypothesis is provided by the caller, the engine inspects canonical nodes and multi-alias mappings in `autosave_kg.json` to auto-detect the most relevant relation.

### **2 — Deterministic Rule Evaluation**  
The engine loads and evaluates pre-indexed symbolic inference rules in constant time:  
- `OrbitTypeInferenceRule`  
- `AutoTypeInferenceRule`  
- `MultiHopOrbitInferenceRule`  
- `DedicsnostVlastnostiRule`  
- `TranzitivneRelacieRule`  

Each rule execution is strictly deterministic and appends nodes to the evidence trace.

### **3 — Bounded Multi-Hop Reasoning**  
The engine traverses multi-hop edges across the Knowledge Graph:  
- direct edges and alias bridges (`is_alias_of`)  
- transitive relation chains (`A is B` ∧ `B is C` ⇒ `A is C`)  
- inherited attribute propagation across taxonomic hierarchies  
- orbital semantic category leaps  
- multi-layer proof-tree compilation  

Traversal depth is strictly capped to prevent runaway cyclic recursion, tracked within `TimeCore` cycle budgets.

### **4 — WHY Reasoning & Deep Explainability (XAI)**  
Produces a structured, auditable explanation payload:  
- target hypothesis and evaluated query  
- verified rule provenance and evidence nodes  
- confidence score calculation  
- multi-hop transition chain  
- hierarchical ASCII / HTML proof tree  

WHY reasoning feeds directly into AUTONOMY 6.x decision governance and interactive `PanelAPI` confirmation prompts (`[ÁNO/NIE]`). Once confirmed and recorded in `autosave_kg.json`, subsequent reasoning cycles resolve instantly without triggering redundant learning proposals.

### **5 — Workflow & UI Suite Integration**  
Reasoning outputs are dispatched to:  
- **AUTONOMY 6.x:** Autonomous governance, Guard metric monitoring, and Triage containment (`COLNIK-6.x/triage`)  
- **COLNIK-6.x:** Customs inspection across Standard and High-Performance IPC modes  
- **EXECUTE 6.x:** Deterministic mutation execution and multi-alias commits  
- **4-Panel UI Suite:** Renders directly in browser panels on port 8080, triggering automatic module release (`currentModule = "none"`) upon query clearance  

---

## 🧱 Core Inference Rules  

### **OrbitTypeInferenceRule**  
Determines contextual and semantic orbital associations between high-level categories and specific concepts.

### **AutoTypeInferenceRule**  
Infers entity types and class memberships automatically based on Knowledge Graph ontology schemas and attributes.

### **MultiHopOrbitInferenceRule**  
Executes multi-step orbital jumps, discovering non-obvious indirect relations between distant graph clusters while enforcing cycle safety.

### **DedicsnostVlastnostiRule**  
Propagates inherited characteristics down taxonomic hierarchies (e.g., if mammal has attribute X, specific animal inherits attribute X), while barring cross-domain biological attribute leakage onto technical/abstract entities.

### **TranzitivneRelacieRule**  
Evaluates transitive logic across chains of directed edges, verifying structural deduction across intermediate nodes.

---

## 🔐 Safety Rules  
- ❌ No destructive graph mutations or deletions without explicit user confirmation (`PanelAPI` [ÁNO/NIE])  
- 🔒 Deterministic, reproducible rule chaining without probabilistic hallucinations  
- 🛑 Multi-hop traversal depth is bounded by strict orbital thresholds enforced by Guard  
- 🚫 Strict non-biological domain shields prevent attributing habitat or biological properties to abstract or technical concepts  
- 🔁 Zero Proposal Recurrence: Entities confirmed under secondary aliases resolve from graph memory without repeated confirmation prompts  
- 🛡 UI input clearance enforces immediate state release (`currentModule = "none"`), protecting host shells from command execution  
- 🧠 Transparent derivation proof trees required for all outputs  

---

## 📊 Module Status (v5.9.0)  
- ✔ Fully implemented & synchronized with Runtime 5.9.0  
- ✔ Compound noun phrase inference verified (`InputParser5`)  
- ✔ Multi-alias graph resolution operational (`autosave_kg.json`)  
- ✔ Zero proposal recurrence confirmed  
- ✔ Multi-hop inference and orbital rules verified  
- ✔ Hierarchical proof-tree generation active (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP`)  
- ✔ Single-process orchestrator integration on port 8080 operational  
- ✔ COLNIK-6.x Customs validation handshake verified  
- ✔ AUTONOMY 6.x proposal/confirmation & Triage Mode integrated  
- ✔ 4-Panel UI Suite synchronization and terminal decoupling verified  

---

## 🏁 Summary  
ReasoningEngine5 is the deterministic inference core of SIRIUS Local AI (v5.9.0).  
It performs multi-hop reasoning, evaluates symbolic rules, resolves multi-word compound concepts, and generates transparent WHY explanations and proof trees throughout the autonomy cycle under central orchestrator supervision.  
The engine is production-stable and fully integrated with KG ENGINE, `sirius_orchestrator.py`, AUTONOMY 6.x, COLNIK-6.x, PanelAPI, EXECUTE, and the 4-Panel UI Suite.
