# SIRIUS‑LOCAL‑AI  
**A fully modular, offline‑only AI runtime with unified orchestration (`sirius_orchestrator.py` on Port 8080), multi-word semantic parsing (`InputParser5`), autonomous disambiguation triage & anti-prefix protection (`EnvoyExecutionLayer5`), contextual domain shielding (`EnvoyNormalizer5`), multi-alias KG persistence (`autosave_kg.json`), 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`), interactive PanelAPI [ÁNO/NIE] loops, TimeCore & Guard supervision, unified reasoning, deep explainability, self‑repair, COLNIK‑6.x (Standard & High-Performance IPC Mode), AUTONOMY 6.x (Control, Guard & Triage Mode), and a next‑generation capability architecture.**

SIRIUS‑LOCAL‑AI is a next‑generation local AI framework designed for **speed, linguistic accuracy, architectural stability, modularity, symbolic intelligence, deep explainability, interactive human-in-the-loop control, and full offline autonomy**.

Version **5.9.0** delivers the most refined and semantically precise generation of the **Unified Runtime Architecture 5.x**, establishing an integrated single-process execution daemon, eliminating repetitive learning loops through multi-alias graph mapping, and completely decoupling UI terminal interaction from host command execution.

This release enhances the runtime architecture with:

- unified single-process orchestration via `sirius_orchestrator.py` executing natively on port 8080  
- multi-word compound semantic parsing (`InputParser5` preserving compound noun phrases)  
- autonomous disambiguation triage & strip-bracket fallback (`EnvoyExecutionLayer5`)  
- phonetic & anti-prefix guard preventing fuzzy query drifts  
- contextual domain shield & sentence-bound bio extractor (`EnvoyNormalizer5`)  
- multi-alias Knowledge Graph persistence with dual-key mapping (`autosave_kg.json`)  
- permanent elimination of interactive proposal recurrence on confirmed knowledge  
- complete 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)  
- integrated high-performance IPC bridge eliminating file-locking contention and race conditions  
- interactive PanelAPI loops with `[ÁNO/NIE]` confirmation prompts  
- TimeCore temporal tracking & Guard security supervision (CPU, RAM, Disk metrics)  
- unified symbolic reasoning pipeline (`ReasoningEngine5.9.0`)  
- KG_EXPLAIN & KG_EXPLAIN_DEEP generating hierarchical proof trees (XAI)  
- deterministic symbolic rules (multi‑hop, inheritance, transitivity, orbital inference)  
- identity‑aware system control (Identity Engine 3.1 & SECURITY FAMILY 5.x)  
- hardened security boundaries with customs validation  
- ENVOY Execution Layer 5 & ENVOY Permission Layer 5  
- **COLNIK‑6.x enterprise validation layer (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x autonomous proposal/confirmation, Guard monitoring & Triage Mode**  

The entire system runs **100% locally**, without external dependencies or cloud services.

---

## 📌 Table of Contents
- [Architecture](ARCHITECTURE.md)
- [Module Map](MODULE_MAP.md)
- [Styleguide](STYLEGUIDE.md)
- [Testing Guide](TESTING_GUIDE.md)
- [Performance Guide](PERFORMANCE_GUIDE.md)
- [Release Notes](RELEASE_NOTES.md)
- [Roadmap](ROADMAP.md)
- [Security Family](SECURITY_FAMILY.md)
- [AITE 5.9.0](AITE.md)
- [ENVOY 5](ENVOY_TUTORIAL.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Future Vision](FUTURE_VISION.md)
- [Password Vault 5.0](PASSWORD_VAULT.md)

---

## 🚀 Key Features (v5.9.0 UNIFIED)

### **Unified Runtime 5.9.0 & Single-Process Orchestration**
A fully upgraded runtime driven by `sirius_orchestrator.py` on local port 8080 with:

- centralized deterministic execution pipeline eliminating external file locks  
- compound phrase semantic routing preserving multi-word tokens (`ovcia vlna`, `mobilny telefon`)  
- interactive PanelAPI [ÁNO/NIE] confirmation prompts  
- TimeCore temporal tracking & Guard system metric supervision  
- explainability routing with hierarchical proof trees (KG_EXPLAIN & KG_EXPLAIN_DEEP)  
- identity‑aware logic and family-safe boundaries  
- self‑repair integration (Layer 5.8)  
- capability isolation and deterministic fallback states  
- hardened System Agent 5 validation  
- ENVOY Execution + Permission Layers 5  
- **COLNIK‑6.x validation (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x proposal/confirmation, Guard supervision & Triage Mode**  
- complete 4-Panel UI Suite with automatic module state reset on input clearance  

---

### **Modular Architecture (v5.9.0)**
Each module is isolated and follows strict boundaries:

- `commands/` – NL routing and command logic  
- `context/` – semantic context engine  
- `filesystem/` – safe file operations  
- `runtime/` – Runtime Core 5.9.0 & InputParser5  
- `orchestrator/` – Unified Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)  
- `panel_api/` – PanelAPI interactive loops (`[ÁNO/NIE]`)  
- `supervision/` – TimeCore & Guard security/temporal/resource monitoring  
- `triage/` – AITE 5.9.0 (semantic compound + disambiguation triage)  
- `ui/` – 4-Panel UI dashboard (`index.html`)  
- `workflow/` – Workflow Engine 5.9.0  
- `plugins/` – Plugin System 5.x  
- `security_family/` – Identity Engine 3.1, time‑limits v3, schoolwork engine  
- `self_repair/` – Self‑Repair Layer 5.8  
- `knowledge_packs/` – Unified Knowledge Graph Packs with Multi-Alias Indexing  
- `envoy/` – ENVOY Execution + Normalizer + Permission Layers 5  
- `colnik/` – COLNIK-6.x Customs Validation & Triage Queue (`COLNIK-6.x/triage`)  
- `autonomy/` – AUTONOMY 6.x Decision Engine & Guard Supervision  
- `system_agent/` – System Agent 5  
- `sirius.py` – Entry point  

The system is designed to be extended **without modifying the core**.

---

### **Plugin System 5.x**
Plugins can define:

- NL commands  
- AI tasks  
- workflows  
- reasoning hooks  
- GUI elements  
- pack‑aware logic  

All official plugins are fully prepared for v5.x.

---

### **Automatic Input Triage Engine (AITE 5.9.0)**
AITE analyzes inputs, classifies them, and routes them to the correct modules.

It ensures:

- compound multi-word semantic parsing without token mutilation  
- copula verb separation (`je`, `sú`) preventing grammatical corruptions  
- OCR extraction  
- subject detection  
- difficulty scoring  
- identity‑aware routing  
- deterministic behavior  
- explainability detection (“why … ?”)  
- **Schoolwork Engine 5.8 — academic tasks always bypass FAMILY restrictions**  
- **integration with SECURITY FAMILY 5.x**  
- **integration with Reasoning Engine 5.9.0**  
- **integration with Workflow Engine 5.9.0 & Orchestrator**  

---

### **Reasoning Engine 5.9.0**
A structured symbolic reasoning layer:

- multi‑hop inference  
- property inheritance reasoning (`DedicsnostVlastnostiRule`)  
- transitive relations reasoning (`TranzitivneRelacieRule`)  
- orbital inference (`MultiHopOrbitInferenceRule`)  
- deterministic rule chaining  
- proof tree foundations (ASCII and HTML generation)  
- evidence tree generation  
- confidence scoring  
- KG_EXPLAIN & KG_EXPLAIN_DEEP integration  
- pack‑aware reasoning  

---

### **Self‑Repair Layer 5.8**
Ensures long‑term stability:

- integrity checks  
- corruption detection  
- safe automatic repairs  
- fallback states  
- dependency validation  
- system‑wide health reporting  

---

### **Unified Knowledge Graph 5.9.0 & Multi-Alias Core**
Offline knowledge expansions:

- multi-alias persistence linking raw queries to formal encyclopedic entries  
- atomic serialization to `autosave_kg.json`  
- zero proposal recurrence on stored concepts  
- household  
- cooking  
- school subjects  
- device diagnostics  
- safety & troubleshooting  
- definitions & facts  

All nodes are semantic, reasoning‑ready, and explainability‑ready.

---

### **SIRIUS ENVOY 5 – Safe External Retrieval & Disambiguation Triage**
Optional isolated agent for safe external lookups:

- outbound‑only architecture  
- autonomous encyclopedic disambiguation triage (*„môže byť...“*)  
- anti-prefix guard preventing query drift (*Káva* -> *Kavala*)  
- strip-bracket fallback to root lemmas  
- strict non-biological domain shield (blocking false habitat properties)  
- quarantine sandbox stripping HTML, scripts, and trackers  
- sentence-bound fact extraction  
- **COLNIK‑validated payload delivery**  
- **AUTONOMY‑aware validation traces**  

ENVOY never sends local data outward.

---

### **Workflow Engine 5.9.0**
Manages:

- multi‑step processes  
- semantic transitions  
- plugin workflows  
- safe command execution  
- deterministic state changes  
- explainability routing  
- SCHOOLWORK workflow prioritization  
- **COLNIK‑validated workflow steps**  
- **AUTONOMY‑aware transitions**  

---

### **Unified Automation Runtime 5.9.0**
Developer‑level offline automation:

- filesystem automation  
- editor integration  
- code workflows  
- structured command parsing  
- command routing  
- safe system task validation  

---

### **4-Panel UI Suite & Terminal State Decoupling**
A dedicated browser dashboard running on port 8080:

- **Duplicates Panel:** monitors system resource metrics and categorizes duplicates into safe vs. critical  
- **Triage Panel:** live supervision of quarantine queues and unclassified files (`COLNIK-6.x/triage`)  
- **Navigation Panel:** deterministic module switching across Runtime, KG, Envoy, and Autonomy  
- **Terminal Panel:** decoupled command line interface that automatically resets `currentModule = "none"` when clearing input, preventing shell lockup and accidental OS-level execution  

---

## 📁 Project Structure (v5.9.0)
```text
src/  
├── commands/  
├── context/  
├── envoy/  
│   ├── envoy_execution_layer_5.py  
│   └── envoy_normalizer_5.py  
├── filesystem/  
├── knowledge_packs/  
├── runtime/  
│   ├── input_parser_5.py  
│   └── runtime_core.py  
├── orchestrator/  
│   └── sirius_orchestrator.py  
├── panel_api/  
├── supervision/  
│   ├── time_core.py  
│   └── guard.py  
├── colnik/  
│   └── triage/  
├── autonomy/  
│   ├── autonomy.py  
│   └── triage_mode.py  
├── security_family/  
├── self_repair/  
├── triage/  
├── ui/  
Each directory has a clear responsibility and is described in MODULE_MAP.md.

🧪 Testing
The project includes a complete testing plan:

multi-word compound noun phrase extraction tests

disambiguation resolution and strip-bracket fallback tests

non-bio domain shielding and habitat filtering tests

multi-alias graph persistence and zero-recurrence verification tests

4-Panel UI state reset and terminal decoupling tests

functional tests

semantic routing tests

real‑time tests

workflow sequence tests

plugin integration tests

SECURITY FAMILY identity tests

SCHOOLWORK ENGINE tests

self‑repair integrity tests

System Agent 5 validation tests

ENVOY 5 sanitization tests

KG_EXPLAIN & KG_EXPLAIN_DEEP explainability tests

Reasoning Engine 5.9.0 rule tests

Orchestrator, PanelAPI & TimeCore/Guard integration tests

Details are in TESTING_GUIDE.md.

⚙️ Performance
The system is optimized for:

zero external API latency (100% offline-first)

single-process HTTP/IPC daemon running natively on port 8080 without file contention

instant memory resolution for multi-alias graph queries

lightweight, non-blocking asynchronous UI loops

long‑term stability

predictable processing

minimal thread blocking

efficient event routing

deterministic reasoning

More in PERFORMANCE_GUIDE.md.

🗓️ Release Plan
v5.9.0 – Semantic Multi-Word Parsing, Disambiguation Triage & 4-Panel UI Suite (Current)
Single-Process Orchestrator (sirius_orchestrator.py on Port 8080)

Multi-Word Compound Parser (InputParser5)

Autonomous Disambiguation Triage & Anti-Prefix Guard (EnvoyExecutionLayer5)

Contextual Domain Shield & Habitat Filtering (EnvoyNormalizer5)

Multi-Alias Graph Persistence (autosave_kg.json)

4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal) with automatic state release

PanelAPI interactive confirmation loops ([ÁNO/NIE])

TimeCore & Guard system resource supervision

AITE 5.9.0

Reasoning Engine 5.9.0

Workflow Engine 5.9.0

Unified Knowledge Graph 5.9.0

KG_EXPLAIN & KG_EXPLAIN_DEEP with proof trees

System Agent 5

ENVOY Execution + Permission Layers 5

COLNIK‑6.x validation (Standard & High-Performance IPC Mode)

AUTONOMY 6.x (Control, Guard & Triage Mode)

🧩 License
The project is open‑source and available to the community under the MIT License.

✨ Author
Richard Pizem

Lead architect & solo maintainer

SIRIUS‑LOCAL‑AI
│   └── index.html  
├── workflow/  
└── sirius.py
