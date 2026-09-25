# ⚙️ Automatic Input Triage Engine (AITE) — v5.9.0  
SIRIUS‑LOCAL‑AI Runtime 5.9.0 — Semantic Multi-Word Engine & Orchestrated Architecture

AITE v5.9.0 is the latest generation of the triage and input processing layer engineered for the SIRIUS Runtime.  
It serves as the mission-critical gateway that parses multi-word queries, isolates copula grammatical terms, establishes multi-alias semantic entities, and determines deterministic module routing under the central orchestration of `sirius_orchestrator.py`.

AITE 5.9.0 is fully offline, deterministic, and natively synchronized across Runtime 5.9.0 components and the integrated IPC Daemon on port 8080.

---

# 🚀 MODULE STATUS — v5.9.0 (ENHANCED & INTEGRATED)

AITE 5.9.0 is fully aligned with the unified Runtime 5.9.0 production architecture:

- Multi-Word InputParser5 (Preserving compound noun phrases)  
- Autonomous Envoy Execution Layer 5 (Disambiguation Triage & Anti-Prefix Guard)  
- Envoy Normalizer 5 (Contextual biological filters & non-bio domain shielding)  
- Knowledge Graph 5.9.0 (Multi-Alias persistence via `autosave_kg.json`)  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` state management)  
- Integrated IPC Bridge (Single-process daemon on port 8080)  
- Reasoning Engine 5.9.0 (`MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`, etc.)  
- Workflow Engine 5.9.0  
- KG_EXPLAIN & KG_EXPLAIN_DEEP  
- System Agent 5  
- ENVOY Permission Layer 5 & PolicyEngine5  
- COLNIK‑6.x Validation Layer (Standard & High-Performance IPC)  
- AUTONOMY 6.x (Control, Guard & Triage Mode)  
- PanelAPI (Interactive `[ÁNO/NIE]` confirmation workflows)  

AITE 5.9.0 delivers production-grade classification and zero proposal recurrence on stored semantic concepts.

---

# 🔥 What’s New in v5.9.0

### Multi-Word Semantic Engine (`InputParser5`)
- Native extraction of multi-word noun phrases (`ovcia vlna`, `mobilny telefon`, `pevna linka`) without stripping modifiers down to isolated single tokens.  
- Strict copula verb isolation (`je`, `sú`) preventing grammatical concatenation errors (eliminating corruptions such as `jeovcia vlna`).  
- Pre-sanitized semantic tokens ready for direct Knowledge Graph queries and Envoy enrichment.  

### Autonomous Disambiguation Triage
- Automatic identification of encyclopedic disambiguation structures (*„môže byť...“*).  
- Direct contextual resolution to precise sub-articles (e.g., categorizing `slon` into genus *Elephas*).  
- Strip-bracket fallback resolving parenthetical wiki entities to root articles.  

### Phonetic & Anti-Prefix Protection
- Shielding against prefix over-matching (stopping query deviations like *Káva* -> *Kavala* or *Skript* -> *Skrytá vášeň*).  
- Normalized diacritic mapping preserving native query syntax.  

### Multi-Alias Graph Routing
- Dual-key Knowledge Graph commitment: records entities under both raw user input and normalized target titles.  
- Permanent resolution of interactive loop cycles: once confirmed via `[ÁNO/NIE]`, subsequent requests are immediately satisfied from local storage without duplicate enrichment triggers.  

### Contextual Domain Blocker (`EnvoyNormalizer5`)
- Non-biological domain shielding preventing abstract, technological, and formal disciplines (*ekológia*, *architektúra*, *fyzika*) from receiving inaccurate geographic habitat attributes.  
- Sentence-bound extraction strictly requiring explicit habitat predicate verbs.  

### UI State & Terminal Safety Bridge
- Direct hook into the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`).  
- Automatic reset of `currentModule = "none"` upon input clearing, preventing terminal lockup and accidental OS-level execution.  

### High-Performance Integrated IPC
- Unified communication pipeline operating natively on port 8080 inside `sirius_orchestrator.py`.  
- Elimination of external file locks and race conditions during rapid interactive sessions.  

---

# 1. Module Purpose

AITE 5.9.0 automatically determines:

- what the input is and its exact grammatical structure  
- whether multi-word compounds constitute a single semantic entity  
- which underlying concept is intended when faced with disambiguation  
- which module or engine is responsible for execution  
- which identity rules and access policies apply  
- whether the concept already exists under an alias in the Knowledge Graph  
- whether ENVOY enrichment is strictly necessary  
- whether COLNIK customs validation is required  
- whether an interactive AUTONOMY proposal (`[ÁNO/NIE]`) must be dispatched to PanelAPI  
- whether host terminal commands should be isolated or cleared  

Supported inputs:

- text (single-word, compound noun phrases, complex questions)  
- images / photos / screenshots (via OCR Engine)  
- documents (pdf, docx, txt, pptx)  
- code and structured configurations  
- schoolwork and academic problems  
- multimodal mixed content  

---

# 2. Module Functions

## 2.1 Input Recognition (Engine 5.9.0)
AITE 5.9.0 recognizes:

- multi-word compound phrases and terms  
- plain and formatted natural language queries  
- code structures and shell commands  
- graphical documents and OCR extractions  
- disambiguation flags and parenthetical descriptors  
- autonomy proposal approvals (`ÁNO`, `NIE`, `YES`, `NO`)  

## 2.2 Semantic Routing Logic
AITE 5.9.0 determines:

- Knowledge Graph lookup with alias resolution  
- automatic fallback to EnvoyExecutionLayer5 on missing entities  
- semantic tagging avoiding false geographic habitats  
- UI panel module assignment (`Duplicates`, `Triage`, `Navigation`, `Terminal`, or `none`)  
- workflow activation inside WorkflowEngine5  
- inference rule engagement in Reasoning Engine 5.9.0  
- safety checks via PolicyEngine5 and COLNIK-6.x  

## 2.3 Integration with Other Modules

### InputParser5
- preserves compound noun structures  
- eliminates copula verb collisions  

### EnvoyExecutionLayer5 & EnvoyNormalizer5
- triggers autonomous triage on encyclopedic pages  
- enforces domain filtering for scientific and technical terms  

### RuntimeCore & KnowledgeGraph
- executes dual-key multi-alias persistence  
- commits updates directly to `autosave_kg.json`  

### UI 4-Panel Suite (PanelAPI)
- synchronizes real-time feedback with web dashboard on port 8080  
- manages state transitions between system utilities and reasoning input  

### COLNIK‑6.x & AUTONOMY 6.x
- validates graph modifications prior to persistence  
- controls proposal generation and confirmation loops  

---

# 3. Module Architecture

## 3.1 Components (v5.9.0)

- **InputClassifier 5.9.0** — type, format, and compound noun identification  
- **OCRExtractor 5.9.0** — visual text parsing  
- **SemanticAnalyzer 5.9.0** — multi-word parsing, intent, and grammatical isolation  
- **DisambiguationTriager 5.9.0** — sub-article pathfinding and parenthetical stripping  
- **PrefixGuard 5.9.0** — protects against invalid prefix shifts  
- **DomainFilter 5.9.0** — blocks false habitat extraction on abstract/tech terms  
- **AliasMapper 5.9.0** — coordinates dual-key graph persistence  
- **PanelBridge 5.9.0** — manages 4-panel UI state transitions and confirmation hooks  
- **AITEController 5.9.0** — central execution governed by `sirius_orchestrator.py`  
- **IdentityGate 4.4** — identity and access policy enforcement  
- **ReasoningBridge 5.9.0** — integrates symbolic rules and XAI explanation pathways  
- **COLNIKBridge 5.9.0** — handles customs validation and quarantine logging  

## 3.2 Processing Flow (v5.9.0)
User inserts input via Web UI / Terminal  
↓  
`sirius_orchestrator.py` loop (Port 8080 IPC Bridge)  
↓  
InputParser5 (Compound phrase preservation & copula verb separation)  
↓  
AITE InputClassifier & SemanticAnalyzer 5.9.0  
↓  
IdentityGate & PolicyEngine5 verification  
↓  
Knowledge Graph Alias & Existence Check  
├─ [Entity Exists] ──────────────────────────┐  
│                                            ▼  
│                                   WorkflowEngine5  
│                                            ↓  
│                                   ReasoningEngine5.9.0  
│                                            ↓  
│                                   PanelAPI Output Generation  
│  
└─ [Entity Missing]  
        ↓  
   PanelAPI Dispatches Proposal (`[ÁNO/NIE]`)  
        ↓  
   User Confirmation (`ÁNO`)  
        ↓  
   EnvoyExecutionLayer5 (Disambiguation Triage & Anti-Prefix Check)  
        ↓  
   EnvoyNormalizer5 (Domain filtering: bio vs. non-bio)  
        ↓  
   COLNIK-6.x Validation & Quarantine Backup  
        ↓  
   RuntimeCore Multi-Alias Commitment (Dual-key save to `autosave_kg.json`)  
        ↓  
   KG Query Pipeline & PanelAPI Display  

---

# 4. Module Status — v5.9.0

AITE 5.9.0 is fully operational, deterministic, and integrated with:

- Runtime Core 5.9.0 (orchestrated via `sirius_orchestrator.py`)  
- Knowledge Graph Unified Schema & `autosave_kg.json`  
- InputParser5 with Multi-Word Preservation  
- EnvoyExecutionLayer5 & EnvoyNormalizer5  
- Integrated IPC Bridge (HTTP/WebSocket on port 8080)  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`)  
- COLNIK‑6.x (Standard & IPC Mode)  
- AUTONOMY 6.x Engine & Guard Supervision  
- Reasoning Engine 5.9.0 (XAI Proof Trees & Symbolic Rules)  

AITE 5.9.0 guarantees that complex multi-word expressions, encyclopedic references, and autonomous learning confirmations are parsed accurately and resolved safely without redundant interactive loops.
