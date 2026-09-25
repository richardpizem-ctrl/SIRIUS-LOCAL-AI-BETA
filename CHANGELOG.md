# 📜 CHANGELOG — SIRIUS LOCAL AI

## v5.9.0 — Semantic Multi-Word Parsing + Autonomous Envoy Disambiguation Triage + 4-Panel UI Suite + Multi-Alias KG Persistence (2026‑09‑25)

### 🔥 Major Update
Version 5.9.0 delivers a decisive leap in natural language comprehension, encyclopedic web triage, and UI stability.  
This release resolves compound phrase truncation through a multi-word semantic parser (`InputParser5`), deploys autonomous disambiguation triage and phonetic prefix protection in `EnvoyExecutionLayer5`, introduces strict non-biological domain shielding in `EnvoyNormalizer5`, implements multi-alias persistence in `RuntimeCore` (permanently eliminating interactive loop recurrences), and fully integrates the 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) with deterministic state release.

All operations execute 100% offline, orchestrated inside a single-process IPC daemon running natively on port 8080 via `sirius_orchestrator.py`.

---

### 🔤 Multi-Word Semantic Engine (`InputParser5`)
- Native preservation of compound noun phrases (e.g., `ovcia vlna`, `mobilny telefon`, `pevna linka`) without truncating modifiers down to isolated single tokens.
- Complete isolation of copula verbs (`je`, `sú`) from subject entities, preventing linguistic corruptions like `jeovcia vlna`.
- Diacritic-aware normalization retaining precise compound concepts for Knowledge Graph querying.

---

### 🌐 Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)
- Autonomous Disambiguation Triage: automatically detects encyclopedic disambiguation structures (*„môže byť...“*) and resolves the underlying biological, material, or technical target article (e.g., categorizing `slon` directly into the genus *Elephas*).
- Phonetic & Anti-Prefix Guard: eliminated prefix over-matching anomalies (stops query drift such as *Káva* jumping to *Kavala* or *Skript* to soap operas).
- Strip-Bracket Fallback: gracefully recovers from non-existent parenthetical wiki entries by falling back to root lemmas.

---

### 🌿 Contextual Domain & Habitat Filtering (`EnvoyNormalizer5`)
- Strict Non-Bio Domain Shield: prevents abstract, scientific, and technical concepts (e.g., *ekológia*, *architektúra*, *fyzika*) from receiving inaccurate geographic habitat metadata.
- Sentence-Bound Extractor: restricts habitat attribute assignment exclusively to sentences containing explicit biological occurrence verbs (*žije*, *obýva*, *prirodzený výskyt*).

---

### 🧠 Multi-Alias Graph Persistence (`RuntimeCore`)
- Dual-key Knowledge Graph commitment: records entities under both raw user queries and normalized encyclopedic titles.
- Zero Proposal Recurrence: once an entity is confirmed via `[ÁNO/NIE]`, subsequent requests are served directly from graph memory without triggering duplicate interactive learning prompts.
- Atomic serialization directly to `autosave_kg.json`.

---

### 🖥 4-Panel UI Suite & Terminal Decoupling
- Duplicates Panel: monitors system resource metrics and categorizes file duplicates into safe vs. critical buckets.
- Triage Panel: live monitoring of quarantine queues and unclassified files (`COLNIK-6.x/triage`).
- Navigation Panel: deterministic routing across Runtime 5, Knowledge Graph, Envoy, and Autonomy layers.
- Terminal Panel: permanent fix for host lockup by automatically resetting `currentModule = "none"` when clearing input, preventing conversational queries from executing as host OS commands.

---

### 🚀 Integrated Single-Process Orchestrator
- Central execution loop running directly via `sirius_orchestrator.py`.
- Integrated HTTP/WebSocket IPC daemon operating on port 8080, eliminating disk file locks and race conditions during rapid interactive sessions.

---

### ⚙ Execution Command
SIRIUS Runtime 5.9.0 is launched via the central orchestrator:

python sirius_orchestrator.py

---

### 📦 Included in ZIP (SIRIUS-LOCAL-AI-5.9.0.zip)
- Full clean Runtime 5.9.0 codebase (all `__pycache__` and compiled `.pyc` artifacts removed)
- `sirius_orchestrator.py` with native port 8080 IPC bridge
- Enhanced `InputParser5`, `EnvoyExecutionLayer5`, and `EnvoyNormalizer5`
- 4-Panel UI suite assets and browser dashboard (`index.html`)
- COLNIK‑6.x validation subsystem (Standard & IPC Mode)
- AUTONOMY 6.x (Control, Guard & Triage Mode)
- Unified Knowledge Graph schema with multi-alias support (`autosave_kg.json`)
- Full symbolic reasoning engine and XAI proof-tree pipeline

---

## v5.8 — Unified Orchestrator + PanelAPI Loops + TimeCore & Guard Supervision + COLNIK/AUTONOMY IPC (2026‑09‑10)  
(Previous version)

## v5.7.0 — Unified Logic Layer + Stabilized KG Platform + COLNIK‑AUTONOMY Integration  
(Previous version)

## v5.6.2 — Stabilized Logic Layer + Unified KG Platform  
(Previous version)

## v5.5.0 — Unified Reasoning & Explainability Architecture  
(Previous version)

## v5.0.0 — Unified Offline Reasoning Runtime  
(Previous version)

## v4.5.0 PRO — System Intelligence Expansion  
(Previous version)
