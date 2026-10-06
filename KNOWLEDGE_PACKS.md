# SIRIUS‑LOCAL‑AI  
**A fully modular, offline‑only AI runtime with unified orchestration (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore), dual-language isolated KG architecture (`autosave_kg.json` for SK & `autosave_kg_en.json` for EN), native lossless entity merge (`kg merge`), taxonomical & marsupial inference (`KG_VERIFY`), non-destructive reverse location reasoning, entry-level Token Guard, 100-file sliding-window quarantine rotation, COLNÍK Guard shell access control (0.0s hard blocks), Human-in-the-Loop Safe Trash, multi-word semantic parsing (`InputParser5`), autonomous disambiguation triage & anti-prefix protection (`EnvoyExecutionLayer5`), contextual domain shielding (`EnvoyNormalizer5`), 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`), interactive PanelAPI [ÁNO/NIE] / [YES/NO] loops, TimeCore & Guard supervision, unified reasoning, deep explainability, self‑repair, COLNIK‑6.x (Standard & High-Performance IPC Mode), and AUTONOMY 6.x (Control, Guard & Triage Mode).**

SIRIUS‑LOCAL‑AI is a next‑generation local AI framework designed for **speed, linguistic accuracy, architectural stability, modularity, symbolic intelligence, deep explainability, interactive human-in-the-loop control, and full offline autonomy**.

Version **5.9.1** delivers the most refined and secure generation of the **Unified Runtime Architecture 5.x**, establishing isolated dual-language knowledge storage backends, native in-memory entity consolidation, taxonomical category deduction, resilient reverse location querying, input token sanitization, and enterprise-grade command and filesystem protection under COLNÍK Guard.

This release enhances the runtime architecture with:

- unified single-process orchestration via `sirius_orchestrator.py` executing natively on port 8080 with embedded TerminalAssistant + TimeCore
- dual-language isolated knowledge stores (`autosave_kg.json` for SK and `autosave_kg_en.json` for EN) with dynamic language context switching
- native lossless entity merge engine (`kg merge <src> into <tgt>`) integrated directly in RuntimeCore
- ontological & taxonomical category deduction (`KG_VERIFY`) with zero proposal recurrence on inferred categories
- non-destructive reverse location engine (`_execute_reverse_location_query`) with anti-flora classification guard
- greedy trailing punctuation stripping (`.rstrip("?")`) and confirmation state latching across conversation turns
- hard Token Guard entry-level sanitization blocking malicious or corrupted injection strings (`@#$%^&*`)
- automatic sliding-window quarantine rotation enforcing a 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`
- COLNÍK Guard shell access control with 0.0s hard blocking of forbidden commands (`format`, `diskpart`, `rmdir /s`)
- Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction
- multi-word compound semantic parsing (`InputParser5` preserving compound noun phrases)
- autonomous disambiguation triage & strip-bracket fallback (`EnvoyExecutionLayer5`)
- phonetic & anti-prefix guard preventing fuzzy query drifts
- contextual domain shield & sentence-bound bio extractor (`EnvoyNormalizer5`)
- permanent elimination of interactive proposal recurrence on confirmed knowledge
- complete 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)
- integrated high-performance IPC bridge eliminating file-locking contention and race conditions
- interactive PanelAPI loops with `[ÁNO/NIE]` / `[YES/NO]` confirmation prompts
- TimeCore temporal tracking (`cycle_delta()`) & Guard security supervision (CPU, RAM, Disk metrics)
- unified symbolic reasoning pipeline (`ReasoningEngine5.9.1`)
- KG_EXPLAIN & KG_EXPLAIN_DEEP generating hierarchical proof trees (XAI)
- deterministic symbolic rules (multi‑hop, inheritance, transitivity, orbital & taxonomical inference)
- identity‑aware system control (Identity Engine 3.1 & SECURITY FAMILY 5.x)
- hardened security boundaries with customs validation
- ENVOY Execution Layer 5, ENVOY Permission Layer 5 & EnvoyQuarantine5
- COLNIK‑6.x enterprise validation layer (Standard, High-Performance IPC Mode & COLNÍK Guard)
- AUTONOMY 6.x autonomous proposal/confirmation, Guard monitoring, HitL Trash Governance & Triage Mode

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
- [AITE 5.9.1](AITE.md)
- [ENVOY 5](ENVOY_TUTORIAL.md)
- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Future Vision](FUTURE_VISION.md)
- [Password Vault 5.0](PASSWORD_VAULT.md)

---

## 🚀 Key Features (v5.9.1 UNIFIED)

### Unified Runtime 5.9.1 & Single-Process Orchestration
A fully upgraded runtime driven by `sirius_orchestrator.py` on local port 8080 with:

- centralized deterministic execution pipeline eliminating external file locks
- dynamic dual-language routing across `autosave_kg.json` (SK) and `autosave_kg_en.json` (EN)
- native lossless entity merging (`kg merge`) with zero attribute loss and alias preservation
- context-aware taxonomical category deduction (`KG_VERIFY`) with edge auto-commits
- reverse location reasoning with anti-flora protection for tree-dwelling fauna
- Token Guard input filter rejecting corrupted symbols (`@#$%^&*`) at runtime threshold
- Human-in-the-Loop Safe UI Trash routing deletions into quarantine for manual user review
- interactive PanelAPI [ÁNO/NIE] / [YES/NO] confirmation prompts with active confirmation latching
- TimeCore temporal tracking (`cycle_delta()`) & Guard system metric supervision
- explainability routing with hierarchical proof trees (KG_EXPLAIN & KG_EXPLAIN_DEEP)
- identity‑aware logic and family-safe boundaries
- self‑repair integration (Layer 5.8)
- capability isolation and deterministic fallback states
- hardened System Agent 5 validation
- ENVOY Execution + Permission Layers 5 with 100-file sliding-window quarantine rotation
- COLNIK‑6.x validation (Standard, High-Performance IPC Mode & COLNÍK Guard)
- AUTONOMY 6.x proposal/confirmation, Guard supervision & Triage Mode
- complete 4-Panel UI Suite with automatic module state reset on input clearance

---

### Modular Architecture (v5.9.1)
Each module is isolated and follows strict boundaries:

- `commands/` – NL routing and command logic
- `context/` – semantic context engine
- `filesystem/` – safe file operations and HitL Safe Trash pipeline
- `runtime/` – Runtime Core 5.9.1 & InputParser5
- `orchestrator/` – Unified Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)
- `panel_api/` – PanelAPI interactive loops (`[ÁNO/NIE]` / `[YES/NO]`)
- `supervision/` – TimeCore & Guard security/temporal/resource monitoring
- `triage/` – AITE 5.9.1 (semantic compound, disambiguation triage & punctuation hygiene)
- `ui/` – 4-Panel UI dashboard (`index.html`)
- `workflow/` – Workflow Engine 5.9.1
- `plugins/` – Plugin System 5.x
- `security_family/` – Identity Engine 3.1, time‑limits v3, schoolwork engine
- `self_repair/` – Self‑Repair Layer 5.8
- `knowledge_packs/` – Dual-Language Knowledge Graph Stores (`autosave_kg.json` & `autosave_kg_en.json`)
- `envoy/` – ENVOY Execution + Normalizer + Permission Layers 5 & EnvoyQuarantine5
- `colnik/` – COLNIK-6.x Customs Validation, COLNÍK Guard & Triage Queue (`COLNIK-6.x/triage`)
- `autonomy/` – AUTONOMY 6.x Decision Engine & Guard Supervision
- `system_agent/` – System Agent 5
- `autosave_kg.json` – Isolated Slovak Knowledge Base
- `autosave_kg_en.json` – Isolated English Knowledge Base
- `sirius.py` – Entry point

The system is designed to be extended without modifying the core.

---

### Plugin System 5.x
Plugins can define:

- NL commands
- AI tasks
- workflows
- reasoning hooks
- GUI elements
- pack‑aware logic

All official plugins are fully prepared for v5.x.

---

### Automatic Input Triage Engine (AITE 5.9.1)
AITE analyzes inputs, sanitizes them, and routes them to the correct modules.

It ensures:

- Token Guard validation rejecting malformed character sequences (`@#$%^&*`)
- greedy trailing punctuation stripping (`.rstrip("?")`) preventing token fragmentation
- compound multi-word semantic parsing without token mutilation
- copula verb separation (`je`, `sú`, `is`, `are`) preventing grammatical corruptions
- dynamic language context switching bound to caller UI language headers (`SK` / `EN`)
- OCR extraction
- subject detection
- difficulty scoring
- identity‑aware routing
- deterministic behavior
- explainability detection (“why … ?”)
- Schoolwork Engine 5.8 — academic tasks always bypass FAMILY restrictions
- integration with SECURITY FAMILY 5.x
- integration with Reasoning Engine 5.9.1
- integration with Workflow Engine 5.9.1 & Orchestrator

---

### Reasoning Engine 5.9.1
A structured symbolic reasoning layer:

- multi‑hop inference
- property inheritance reasoning (`DedicsnostVlastnostiRule`)
- transitive relations reasoning (`TranzitivneRelacieRule`)
- orbital inference (`MultiHopOrbitInferenceRule`)
- ontological & taxonomical category deduction (`KG_VERIFY`)
- non-destructive reverse location reasoning with anti-flora classification guard
- deterministic rule chaining
- proof tree foundations (ASCII and HTML generation)
- evidence tree generation
- confidence scoring
- KG_EXPLAIN & KG_EXPLAIN_DEEP integration
- pack‑aware reasoning

---

### Self‑Repair Layer 5.8
Ensures long‑term stability:

- integrity checks
- corruption detection
- safe automatic repairs
- fallback states
- dependency validation
- system‑wide health reporting

---

### Unified Knowledge Graph 5.9.1 & Dual-Language Architecture
Offline knowledge expansions:

- isolated graph stores for Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`)
- native lossless entity merge engine (`kg merge`) with alias preservation
- multi-alias persistence linking raw queries to formal encyclopedic entries
- zero proposal recurrence on stored concepts and deduced taxonomies
- household
- cooking
- school subjects
- device diagnostics
- safety & troubleshooting
- definitions & facts

All nodes are semantic, reasoning‑ready, and explainability‑ready.

---

### SIRIUS ENVOY 5 – Safe External Retrieval & Disambiguation Triage
Optional isolated agent for safe external lookups:

- outbound‑only architecture
- dynamic language context binding (sk.wikipedia.org for SK, en.wikipedia.org for EN)
- autonomous encyclopedic disambiguation triage (*„môže byť...“*)
- anti-prefix guard preventing query drift (*Káva* -> *Kavala*)
- strip-bracket fallback to root lemmas
- strict non-biological domain shield (blocking false habitat properties)
- quarantine sandbox stripping HTML, scripts, and trackers
- automatic 100-file sliding-window quarantine rotation (`EnvoyQuarantine5`)
- sentence-bound fact extraction
- COLNIK‑validated payload delivery
- AUTONOMY‑aware validation traces

ENVOY never sends local data outward.

---

### Workflow Engine 5.9.1
Manages:

- multi‑step processes
- semantic transitions
- plugin workflows
- safe command execution
- deterministic state changes
- explainability routing
- SCHOOLWORK workflow prioritization
- COLNIK‑validated workflow steps
- AUTONOMY‑aware transitions

---

### Unified Automation Runtime 5.9.1
Developer‑level offline automation:

- filesystem automation with Human-in-the-Loop Safe Trash protection
- terminal command security under COLNÍK Guard (0.0s block on `format`, `diskpart`, `rmdir /s`)
- editor integration
- code workflows
- structured command parsing
- command routing
- safe system task validation

---

### 4-Panel UI Suite & Terminal State Decoupling
A dedicated browser dashboard running on port 8080:

- Duplicates Panel: monitors system resource metrics and categorizes duplicates into safe vs. critical
- Triage Panel: live supervision of quarantine queues and unclassified files (`COLNIK-6.x/triage`)
- Navigation Panel: deterministic module switching across Runtime, KG, Envoy, and Autonomy
- Terminal Panel: decoupled command line interface that automatically resets `currentModule = "none"` when clearing input, preventing shell lockup and accidental OS-level execution

---

## 📁 Project Structure (v5.9.1)

src/
├── commands/
├── context/
├── envoy/
│   ├── envoy_execution_layer_5.py
│   ├── envoy_normalizer_5.py
│   └── envoy_quarantine_5.py
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
│   ├── triage/
│   └── colnik_guard.py
├── autonomy/
│   ├── autonomy.py
│   └── triage_mode.py
├── security_family/
├── self_repair/
├── triage/
├── ui/
│   └── index.html
├── workflow/
├── autosave_kg.json
├── autosave_kg_en.json
└── sirius.py

Each directory has a clear responsibility and is described in MODULE_MAP.md.

---

## 🧪 Testing
The project includes a complete testing plan:

- dual-language graph isolation and dynamic context switching tests
- native `kg merge` attribute retention and alias link tests
- taxonomical inference (`KG_VERIFY`) and edge auto-commit tests
- reverse habitat query and anti-flora classification guard tests
- Token Guard input sanitization and trailing punctuation stripping tests
- sliding-window quarantine rotation (100-record ceiling) tests
- COLNÍK Guard 0.0s command blocking and telemetry tests
- Human-in-the-Loop Safe Trash quarantine tests
- multi-word compound noun phrase extraction tests
- disambiguation resolution and strip-bracket fallback tests
- non-bio domain shielding and habitat filtering tests
- 4-Panel UI state reset and terminal decoupling tests
- functional tests
- semantic routing tests
- real‑time tests
- workflow sequence tests
- plugin integration tests
- SECURITY FAMILY identity tests
- SCHOOLWORK ENGINE tests
- self‑repair integrity tests
- System Agent 5 validation tests
- ENVOY 5 sanitization tests
- KG_EXPLAIN & KG_EXPLAIN_DEEP explainability tests
- Reasoning Engine 5.9.1 rule tests
- Orchestrator, PanelAPI & TimeCore/Guard integration tests

Details are in TESTING_GUIDE.md.

---

## ⚙️️ Performance
The system is optimized for:

- zero external API latency (100% offline-first)
- single-process HTTP/IPC daemon running natively on port 8080 without file contention
- instant memory resolution for dual-language graph queries
- lightweight, non-blocking asynchronous UI loops
- long‑term stability
- predictable processing
- minimal thread blocking
- efficient event routing
- deterministic reasoning

More in PERFORMANCE_GUIDE.md.

---

## 🗓️ Release Plan

### v5.9.1 – Dual-Language KG Architecture, Lossless Entity Merge & Comprehensive System Security Protocol (Current)
- Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)
- Dual-Language Isolated Knowledge Stores (`autosave_kg.json` & `autosave_kg_en.json`)
- Native Lossless KG Merge Engine (`kg merge <src> into <tgt>`)
- Ontological & Taxonomical Category Deduction (`KG_VERIFY`)
- Non-Destructive Reverse Location Engine with Anti-Flora Guard
- Entry-Level Token Guard & 100-File Sliding-Window Quarantine Rotation
- COLNÍK Guard Shell Access Control (0.0s hard block on forbidden commands)
- Human-in-the-Loop Safe UI Trash Pipeline
- Multi-Word Compound Parser (`InputParser5`)
- Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)
- Contextual Domain Shield & Habitat Filtering (`EnvoyNormalizer5`)
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) with automatic state release
- PanelAPI interactive confirmation loops (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching
- TimeCore temporal tracking (`cycle_delta()`) & Guard system resource supervision
- AITE 5.9.1
- Reasoning Engine 5.9.1
- Workflow Engine 5.9.1
- KG_EXPLAIN & KG_EXPLAIN_DEEP with proof trees
- System Agent 5
- ENVOY Execution + Permission Layers 5 & EnvoyQuarantine5
- COLNIK‑6.x validation (Standard & High-Performance IPC Mode)
- AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Trash Governance)

---

## 🧩 License
The project is licensed under the **SIRIUS Unified License (SUL-3.2.0)**.

---

## ✨ Author
**Richard Pizem**  
Lead architect & solo maintainer  
SIRIUS‑LOCAL‑AI
