![SIRIUS Futuristic](SIRIUS%20LOCAL%20FUTURISTICKY%20OBR.png)
![SIRIUS Architecture Diagram 6](diagram%20(6).png)

---

# ⚠️ WARNING — SYSTEM UNDER ACTIVE DEVELOPMENT (RUNTIME 5.9.1)
### ⚠️ EXPERIMENTAL RESEARCH BUILD — WORK IN PROGRESS

> **CRITICAL NOTICE:**  
> SIRIUS LOCAL AI is currently under **intensive active research and development**.  
> The codebase, semantic extraction rules, dual-language graph schemas, security gates, parsing logic, and user interface are undergoing **continuous refinement, polishing, and empirical testing**.  
> The system **MAY PRODUCE ERRORS, INACCURACIES, OR UNEXPECTED BEHAVIOR**.  
> Architectural modules, security policies, and APIs are subject to change in upcoming builds.  
> Test and run this software strictly as an evolving developmental build!

---

## 📦 DISTRIBUTION & QUICK START (OFFICIAL RELEASE)

> **IMPORTANT FOR TESTERS & AUDITORS:**  
> The raw Git repository tree reflects the active staging workspace.  
> **A fully packaged, self-contained, and tested standalone distribution** (including all core modules, dual knowledge bases, UI assets, and runtime dependencies) is available directly in the **[Releases (v5.9.1)]** section.

### 🚀 Running SIRIUS in 3 Steps:
1. **Download & Extract:** Download the pre-packaged `SIRIUS-LOCAL-AI-v5.9.1-STANDALONE.zip` from **Releases** and extract it.
2. **Launch Orchestrator:** Open terminal in the directory and run:
   python sirius_orchestrator.py
3. **Open Dashboard:** Navigate to `http://127.0.0.1:8080` (or open `UI_PANEL/ui/index.html`) to access the bilingual interactive panel.

---

## 🏗️ ARCHITECTURAL SPECIFICATION — RUNTIME 5.9.1
### Runtime 5.x + Dual-Language KG + COLNÍK Guard + Safe UI Trash + AUTONOMY 6.x + 4-Panel UI Suite

The operational stack integrates:
- **Dual-Language Isolated Knowledge Stores:** Physical and logical partition across Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) with dynamic language context switching.
- **Native Lossless KG Merge Engine:** Full in-memory runtime support for `kg merge <src> into <tgt>` with attribute retention and automatic alias mapping.
- **Ontological & Taxonomical Reasoning:** Hierarchical deduction (`KG_VERIFY`) recognizing biological sub-taxa (e.g., marsupials and macropods categorized under mammals) with persistent edge auto-commits.
- **Non-Destructive Reverse Location Engine:** Multi-stem regional location matching (*Austrálii*, *Austrália*, *Australia*) combined with the False-Positive Flora Guard protecting tree-dwelling fauna.
- **COLNÍK Guard & TerminalAssistant:** Pre-execution shell command filter rejecting destructive system calls (`format`, `diskpart`, `rmdir /s`) prior to OS process creation, supported by TimeCore latency telemetry (`cycle_delta()`).
- **Human-in-the-Loop Safe UI Trash:** Files flagged for deletion route into quarantine storage requiring explicit manual approval via `GET /trash`, preventing unverified disk removal.
- **Token Guard Sanitization:** Entry-level input hygiene rejecting malformed or dangerous symbol sequences (`@#\$%^&*`) on raw inputs.
- **Sliding-Window Quarantine Rotation:** Automated pruning mechanism enforcing a 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`.
- **Punctuation Trimming:** Trailing punctuation stripping (`.rstrip("?")`) preventing entity key mismatches.
- **Confirmation State Latching:** Deterministic state latching ensuring pending interactive proposals (`[ÁNO/NIE]` / `[YES/NO]`) remain preserved across conversational turns.
- **COLNIK‑6.x Decision Gateway:** Standard Mode and High-Performance IPC validation layer.
- **AUTONOMY‑6.x:** Analyzer + Proposer + Guard + Duplicates/Triage supervisor.
- **4-Panel UI Suite:** Fully integrated `Duplicates`, `Triage`, `Navigation`, and `Terminal` panels with deterministic state release (`currentModule = "none"`).
- **Integrated Single-Process IPC Bridge:** Native HTTP daemon embedded directly inside `sirius_orchestrator.py` on port `8080`.
- **Semantic Multi-Word Parser:** `InputParser5` preserving compound noun phrases without modifier truncation.
- **Autonomous Disambiguation Triage:** `EnvoyExecutionLayer5` sub-article resolution, strip-bracket fallback, and anti-prefix guard.
- **Contextual Domain Filter:** `EnvoyNormalizer5` strict non-biological domain shielding.

### 🔄 EXECUTION STANDARD
- **Unified Entry Point:** Modular CLI scripts are unified under the central orchestrator:  
  python sirius_orchestrator.py  
- The orchestrator manages Runtime 5, the embedded HTTP IPC server on port 8080, dual Knowledge Graphs, Token Guard, COLNÍK Guard, and real-time browser communication (`index.html`).

---

# SIRIUS LOCAL AI — Version 5.9.1
**Deterministic Symbolic Reasoning Engine • Dual-Language KG Architecture • Native Lossless Entity Merge • Ontological Reasoning • COLNÍK Guard Security Protocol • 4-Panel UI Suite**

## 🧭 Philosophy of SIRIUS
> *“To err is human… and among AI, they say that to err is algorithmic.”*

SIRIUS embraces this principle: anomalies and parsing deviations are structural opportunities for refinement. The system is designed to learn from syntactic variations, edge cases, and user confirmations, converting them into deterministic graph assertions.

---

# 🔍 System Overview

SIRIUS LOCAL AI 5.9.1 represents a significant evolution in localized symbolic computing, focusing on strict bilingual knowledge separation, in-memory graph manipulation, structured taxonomical inference, and layered local security. While version 5.9.0 focused on initial parsing enhancements, version **5.9.1** delivers **dual-language isolation**, **lossless entity merging**, **hierarchical deduction**, and **pre-execution security barriers**.

### Key Milestones in Version 5.9.1:
- **Dual-Language Isolated Knowledge Bases:** Physical and logical partition across Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`). Dynamic context dispatching routes queries, node retrieval, attributes, and relations based on the active UI language flag (`SK` / `EN`), preventing cross-lingual contamination.
- **Native Lossless Entity Merge Engine (`kg merge <src> into <tgt>`):** In-memory interceptor inside `RuntimeCore` that relocates properties, descriptions, and habitat records from source to target without data loss, while binding the source node into a persistent alias pointer (`src -[alias]-> tgt`).
- **Ontological & Taxonomical Reasoning (`KG_VERIFY`):** Deduces higher-order taxonomic categories directly from summary records and commits verified relations to disk to permanently eliminate confirmation loops.
- **Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`):** Multi-stem regional matching combined with the False-Positive Flora Guard to ensure tree-dwelling animals (*„stromový vačkovec“*) are not misclassified as flora.
- **Layered Security Protocol (COLNÍK Guard & Safe UI Trash):** 
  - **COLNÍK Guard Shell Filter:** Immediate pre-execution rejection of forbidden commands (`format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`), prompt checks for risky commands, and pass-through for telemetric inspections (`ps`, `mem`, `sys`).
  - **Human-in-the-Loop Safe UI Trash:** Direct file removals are routed to quarantine storage, requiring explicit confirmation via `GET /trash`.
  - **Token Guard:** Raw input inspection dropping invalid injection characters (`@#\$%^&*`) before grammar parsing begins.
  - **Sliding-Window Quarantine Rotation:** Enforces a strict 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`, purging older JSON payloads.
- **Punctuation Hygiene & Confirmation State Latching:** Trailing punctuation stripping (`.rstrip("?")`) prevents query lookup misses. Confirmation state latching ensures pending proposal entities remain preserved in memory across interactive turns so user confirmations (`ÁNO` / `YES`) execute without losing execution context.
- **Multi-Word Noun Phrases (`InputParser5`):** Preserves compound noun phrases (`ovcia vlna`, `mobilny telefon`, `pevna linka`) without truncating modifiers down to isolated words, isolating copula verbs (`je`, `sú`, `is`, `are`).
- **Autonomous Disambiguation Triage (`EnvoyExecutionLayer5`):** Detects Wikipedia disambiguation pages (*„môže byť...“*) and resolves the underlying target article, supported by phonetic and anti-prefix guards.
- **Contextual Habitat Filtering (`EnvoyNormalizer5`):** Domain guards prevent scientific fields, engineering concepts, and abstract topics from receiving inaccurate geographic habitat metadata.
- **Full 4-Panel UI Suite Integration:** `Duplicates`, `Triage`, `Navigation`, and `Terminal` panels operate with verified state cleanup (`currentModule = "none"`), permanently decoupling user queries from host command capture.

---

# 🌐 Architectural Design: Web Interface & Local Python Core

- **Python as the Symbolic Logic Engine:**
  - Serves as a transparent, locally auditable runtime under the hood.
  - Executes deterministic logic, rule engines, dual-graph queries, and Token Guard validation without cloud dependencies.
- **Web Browser as the Native Dashboard:**
  - Avoids heavy proprietary GUI runtimes; communication runs through the local browser via native HTTP/WebSocket endpoints on port `8080`.
- **Strict Privacy Invariant:**
  - 100% local execution.
  - Knowledge graphs, reasoning traces, and user interactions remain strictly on the local hardware.

---

# 🧠 Knowledge Graph Architecture & Explainability (XAI)

SIRIUS combines symbolic knowledge representation with transparent explainability:
- **Hierarchical Proof Trees** for auditable multi-hop derivations (ASCII + HTML view).
- **Symbolic Rule Attribution** (`MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`, `TranzitivneRelacieRule`, `AutoTypeInferenceRule`, `OrbitTypeInferenceRule`, `TaxonomyRule`).
- **Dual Independent Knowledge Stores** with atomic serialization into `autosave_kg.json` (SK) and `autosave_kg_en.json` (EN).

---

# 🛡️ COLNIK‑6.x & AUTONOMY Tandem Execution

COLNIK operates as an application-level inspection authority, validating operations before state transitions reach graph storage or workflow pipelines:
- **COLNÍK Guard Shell Security:** Intercepts forbidden system commands prior to subprocess spawning.
- **Safe Trash Governance:** Enforces Human-in-the-Loop quarantine review before file deletions.
- **Token Guard Enforcement:** Drops unsupported symbol sequences (`@#\$%^&*`) at entry.
- **Permission & Policy Audits:** Governed by `PermissionLayer5` and `PolicyEngine5`.
- **Interactive Proposal State:** Governed in tandem with `AUTONOMY-6.x` using confirmation state latching.
- **Live System Telemetry:** Gathers system resource metrics and loop timings governed by `Guard` and `TimeCore` (`cycle_delta()`).

---

# 📊 Module Status Matrix (v5.9.1)

| Module / Component | Status | Operational Notes |
| :--- | :---: | :--- |
| **`sirius_orchestrator.py`** | 🟩 Stable | Unified single-process runtime, native IPC bridge (port 8080), embedded TerminalAssistant + TimeCore |
| **`TokenGuard`** | 🟩 Operational | Pre-parsing input sanitization, immediate filtering of `@#\$%^&*` |
| **`InputParser5`** | 🟩 Enhanced | Multi-word phrase retention, trailing punctuation trimming (`.rstrip("?")`) |
| **Dual KG Storage** | 🟩 Operational | Partitioned storage: `autosave_kg.json` (SK) & `autosave_kg_en.json` (EN) |
| **Native Merge Engine** | 🟩 Operational | In-memory `kg merge <src> into <tgt>` with attribute retention & alias mapping |
| **Taxonomical Reasoner** | 🟩 Operational | Deductive inference (`KG_VERIFY`) with persistent edge auto-commit |
| **Reverse Habitat Engine** | 🟩 Operational | Multi-stem regional search with False-Positive Flora Guard |
| **`EnvoyQuarantine5`** | 🟩 Operational | Automated sliding-window rotation enforcing 100-file ceiling |
| **`EnvoyExecutionLayer5`** | 🟩 Enhanced | Autonomous Disambiguation Triage, Anti-Prefix Guard, language-specific endpoints |
| **`EnvoyNormalizer5`** | 🟩 Enhanced | Contextual semantic parser, non-bio domain blocker |
| **UI Suite (4 Panels)** | 🟩 Stable | `Duplicates`, `Triage`, `Navigation`, `Terminal` (clean state reset `currentModule = "none"`) |
| **COLNÍK Guard & HitL Trash** | 🟩 Operational | Pre-spawn blocking of destructive shell calls, quarantine routing for deletions (`GET /trash`) |
| **Reasoning Engine 5.9.1** | 🟩 Stable | Multi-hop inference rules, XAI proof-tree generation, taxonomical inference |
| **AUTONOMY 6.x** | 🟩 Stable | Proposal generation, confirmation latching, Guard supervision, Safe Trash governance |

---

# ⚡ Target Performance SLA & Algorithmic Bounds

The following metrics define the architectural performance targets for Runtime 5.9.1 under standard hardware conditions:

| Component / Operation | Theoretical Complexity | Target Latency (SLA) | Resource Profile |
| :--- | :---: | :---: | :--- |
| **Token Guard Input Sanitization** | $O(N)$ | $< 0.1\text{ ms}$ | Negligible CPU overhead |
| **Punctuation Trimming (`.rstrip("?")`)** | $O(k)$ | $< 0.05\text{ ms}$ | Linear to punctuation count $k$ |
| **`InputParser5` Token Parsing** | $O(N)$ | $< 0.5\text{ ms}$ | Linear token grouping |
| **Dual-Language Graph Lookup (SK/EN)** | Average $O(1)$ | $< 1.0\text{ ms}$ | In-memory hash-indexed RAM retrieval |
| **Native Entity Merge (`kg merge`)** | $O(A + E)$ | $< 3.0\text{ ms}$ | In-memory property and edge migration |
| **Taxonomical Deduction (`KG_VERIFY`)** | Bounded $O(1)$ | $< 2.0\text{ ms}$ | Single-hop indexed taxonomical check |
| **COLNÍK Guard Shell Interception** | $O(1)$ | Sub-millisecond | Pre-execution string match (zero subprocess spawn) |
| **Quarantine Sliding-Window Prune** | $O(N \log N)$ | $< 5.0\text{ ms}$ | Bounded by fixed cap $N = 100$ JSON files |
| **IPC Event Dispatch & Latch** | $O(1)$ | $< 1.0\text{ ms}$ | Non-blocking asynchronous event handling |

*Note: Guaranteed execution times and resource consumption are empirical and subject to underlying hardware configurations (CPU, RAM speed, and storage subsystem).*

---

# 🗺️ Strategic Roadmap (Upcoming Iterations)

1. **Standalone Binary Packaging (`.exe`):** Compiling an isolated, single-file distributable executable eliminating external Python dependencies.
2. **Hybrid Isolation Layer (HIL v7.x):** Unifying OS process isolation with logical semantic quarantine.
3. **Autonomous Household AI:** Task planning, offline inventory workflows, and device troubleshooting.
4. **Offline Voice & Interaction:** Local speech-to-text processing and verbal explainability summaries.

---

# 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

# 🏁 Summary

SIRIUS LOCAL AI 5.9.1 unites deterministic symbolic graph logic with dual-language isolation, native lossless entity merging, automated taxonomical deduction, and layered protection under COLNÍK Guard and Human-in-the-Loop Safe Trash. The runtime is fast, secure, explainable, and prepared for continuous expansion.

---
**Metadata & SEO:**  
Keywords: SIRIUS LOCAL AI, Symbolic AI, Knowledge Graph, Offline AI, Dual-Language KG, KG Merge, COLNIK Guard, Token Guard, Safe UI Trash, Envoy Triage, Python Orchestrator, Autonomous AI, Localhost AI  
Version: 5.9.1 UNIFIED  
License: MIT License  
Author: richardpizem-ctrl  
Environment: Localhost / Windows 11 / Port 8080  
Build Status: Active Research & Development (WIP)
