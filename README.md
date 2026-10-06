![SIRIUS Futuristic](SIRIUS%20LOCAL%20FUTURISTICKY%20OBR.png)
![SIRIUS Architecture Diagram 6](diagram%20(6).png)

---

# ⚠️ WARNING — SYSTEM UNDER ACTIVE DEVELOPMENT (RUNTIME 5.9.1)
### ⚠️ EXPERIMENTAL & REFINEMENT NOTICE — WORK IN PROGRESS

> **CRITICAL NOTICE:**  
> SIRIUS LOCAL AI is currently under **intensive active development**.  
> The codebase, semantic extraction rules, dual-language graph schemas, security gates, parsing logic, and user interface are undergoing **continuous refinement, polishing, and modification**.  
> The system **MAY PRODUCE ERRORS, INACCURACIES, OR UNEXPECTED BEHAVIOR**.  
> Architectural modules, security policies, and APIs are subject to change in upcoming builds.  
> Test and run this software strictly as an evolving developmental build!

---

## ⚠️ ARCHITECTURAL NOTICE — RUNTIME 5.9.1
### Runtime 5.x + Dual-Language KG + COLNÍK Guard + Safe UI Trash + AUTONOMY 6.x + 4-Panel UI Suite

The operational stack currently integrates:
- **Dual-Language Isolated Knowledge Stores:** Physical and logical partition across Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) with dynamic language context switching.
- **Native Lossless KG Merge Engine:** Full in-memory runtime support for `kg merge <src> into <tgt>` with attribute retention and automatic alias mapping.
- **Ontological & Taxonomical Reasoning:** Hierarchical deduction (`KG_VERIFY`) recognizing biological sub-taxa (marsupials and macropods committed under mammals) with persistent edge auto-commits.
- **Non-Destructive Reverse Location Engine:** Multi-stem location parsing with anti-collision flora shielding protecting tree-dwelling fauna (e.g., *Koala*, *Macropus*).
- **COLNÍK Guard & TerminalAssistant:** Shell command categorization matrix with 0.0s hard blocking of forbidden commands (`format`, `diskpart`, `rmdir /s`) and TimeCore latency profiling (`cycle_delta()`).
- **Human-in-the-Loop Safe UI Trash:** Files flagged for deletion route into quarantine storage requiring explicit manual approval via `GET /trash`, preventing direct unverified disk destruction.
- **Hard Token Guard:** Entry-level sanitization immediately rejecting corrupted and malicious symbol sequences (`@#$%^&*`).
- **Envoy Sliding-Window Quarantine:** Automated rotation limiting log files in `COLNIK-6.x/envoy/quarantine/` to a strict 100-record ceiling.
- **Resilient Trailing Punctuation Stripping:** Greedy punctuation trimming (`.rstrip("?")`) preventing entity key mismatches.
- **Confirmation State Latching:** Deterministic proposal preservation ensuring `[ÁNO/NIE]` / `[YES/NO]` inputs never lose conversational context.
- **COLNIK‑6.x:** Standard Mode and High-Performance IPC validation layer.
- **AUTONOMY‑6.x:** Analyzer + Proposer + Guard + Duplicates/Triage modules.
- **4-Panel UI Suite:** Fully integrated `Duplicates`, `Triage`, `Navigation`, and `Terminal` with deterministic state release (`currentModule = "none"`).
- **Integrated Single-Process IPC Bridge:** Native daemon executing inside `sirius_orchestrator.py` on port `8080`.
- **Semantic Multi-Word Parser:** `InputParser5` preserving full compound noun phrases without modifier truncation.
- **Autonomous Disambiguation Triage:** `EnvoyExecutionLayer5` sub-article resolution, strip-bracket fallback, and anti-prefix guard.
- **Contextual Habitat Filter:** `EnvoyNormalizer5` strict non-biological domain shielding.

### 🔄 EXECUTION STANDARD
- **Unified Entry Point:** Isolated CLI scripts have been permanently replaced by the central orchestrator:  
  `python sirius_orchestrator.py`  
- The orchestrator governs Runtime 5, the embedded HTTP/WebSocket IPC daemon on port 8080, dual Knowledge Graphs, Token Guard, COLNÍK Guard, and real-time browser communication (`index.html`).

---

# SIRIUS LOCAL AI — Version 5.9.1
**Enterprise‑Grade Symbolic Reasoning • Dual-Language KG Architecture • Native Lossless Entity Merge • Ontological Habitat Reasoning • COLNÍK Guard Security Protocol • 4-Panel UI Suite**

## 🧭 Philosophy of SIRIUS
> *“To err is human… and among AI, they say that to err is algorithmic.”*

SIRIUS embraces this principle: mistakes are not failures — they are signals, data points, and structural opportunities for refinement. The system is designed to learn from syntactic anomalies, workflow deviations, and knowledge edge cases, transforming them into resilient execution rules.

---

# 🔍 System Overview

SIRIUS LOCAL AI 5.9.1 delivers a major architectural advancement focusing on complete bilingual knowledge isolation, native in-memory graph operations, resilient taxonomical inference, and comprehensive security hardening across the SIRIUS / COLNÍK ecosystem. While version 5.9.0 focused on multi-word parsing and basic disambiguation, version **5.9.1** focuses on **dual-language isolation**, **lossless entity merging**, **hierarchical category deduction**, and **multi-tiered local security**.

### Key Milestones in Version 5.9.1:
- **Dual-Language Isolated Knowledge Bases:** Physical and logical partition across Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`). Dynamic context dispatching routes queries, node retrieval, attributes, and relations dynamically based on the active UI language flag (`SK` / `EN`), completely preventing cross-lingual contamination.
- **Native Lossless Entity Merge Engine (`kg merge <src> into <tgt>`):** Direct runtime interceptor inside `RuntimeCore` that relocates all properties, descriptions, and habitat records from source to target without data loss, while converting the source node into a persistent alias pointer (`src -[alias]-> tgt`).
- **Ontological & Taxonomical Reasoning (`KG_VERIFY`):** Deduces higher-order biological categories directly from summary records (recognizing that marsupials and macropods belong to mammals) and auto-commits verified relations directly to disk with zero confirmation recurrence.
- **Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`):** Multi-stem regional matching (*Austrálii*, *Austrália*, *Australia*) combined with the False-Positive Flora Guard to ensure tree-dwelling animals (*„stromový vačkovec“*) are not misclassified as plants, reliably indexing *Koala*, *Macropus*, and *Krokodíl morský* under Australian fauna. Direct attribute inspection standardized via `self.kg.get_attributes()`.
- **Comprehensive Security Protocol (COLNÍK Guard & Safe UI Trash):** 
  - **COLNÍK Guard Shell Filter:** 0.0s hard blocking of forbidden commands (`format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`), prompt checks for risky commands, and safe pass-through for telemetric inspections (`ps`, `mem`, `sys`).
  - **Human-in-the-Loop Safe UI Trash:** Direct unverified disk deletions are blocked; files flagged for removal route into quarantine and require explicit user review via `GET /trash`.
  - **Token Guard:** Entry-level sanitization rejecting corrupted or dangerous symbol sequences (`@#$%^&*`) on raw input before runtime processing.
  - **Sliding-Window Quarantine Rotation:** Enforces a strict 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`, automatically pruning older JSON payloads upon new arrivals.
- **Punctuation Hygiene & Confirmation State Latching:** Greedy trailing punctuation stripping (`.rstrip("?")`) prevents entity lookup failures (e.g., `CO JE MACROPUS?` cleanly resolves to node `macropus`). Confirmation state latching ensures pending proposal entities remain preserved in memory across interactive turns so user confirmations (`ÁNO` / `YES`) execute without detached states.
- **Multi-Word Noun Phrases (`InputParser5`):** Preserves compound noun phrases (`ovcia vlna`, `mobilny telefon`, `pevna linka`) without truncating modifiers down to isolated words, isolating copula verbs (`je`, `sú`, `is`, `are`).
- **Autonomous Disambiguation Triage (`EnvoyExecutionLayer5`):** Automatically detects Wikipedia disambiguation pages (*„môže byť...“*) and resolves the underlying target article, backed by phonetic and anti-prefix guards.
- **Contextual Habitat Filtering (`EnvoyNormalizer5`):** Strict domain guards prevent scientific fields, engineering concepts, and abstract topics from receiving inaccurate geographic habitat metadata.
- **Full 4-Panel UI Suite Integration:** `Duplicates`, `Triage`, `Navigation`, and `Terminal` panels operate with verified state cleanup (`currentModule = "none"`), permanently decoupling user queries from host command capture.

---

# 🌐 Why SIRIUS Operates via Web & Python

- **Python as the Core Logic Engine:**
  - Serves as a transparent, locally auditable runtime under the hood.
  - Executes symbolic logic, inference trees, dual-graph operations, and Token Guard checks without external cloud dependencies.
- **Web Browser as the Command Interface:**
  - Avoids cumbersome proprietary GUI installations; control runs seamlessly in modern browsers via native HTTP/WebSocket calls on port `8080`.
- **Offline-First Privacy Guarantee:**
  - 100% open-source, local execution.
  - When disconnected from the internet, knowledge, reasoning traces, and user interactions remain strictly on your local hardware.

---

# 🧠 Knowledge Graph Architecture & Explainability (XAI)

SIRIUS combines symbolic knowledge representation with auditable explainable AI:
- **Hierarchical Proof Trees** for transparent multi-hop derivations (ASCII + HTML view).
- **Symbolic Rule Attribution** (`MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`, `TranzitivneRelacieRule`, `AutoTypeInferenceRule`, `OrbitTypeInferenceRule`, `TaxonomyRule`).
- **Dual Independent Knowledge Graphs** backed by atomic serialization into `autosave_kg.json` (SK) and `autosave_kg_en.json` (EN).

---

# 🛡️ COLNIK‑6.x & AUTONOMY Tandem Execution

COLNIK operates as an internal **customs control authority and security firewall**, validating each operation before mutations reach graph storage or workflow pipelines:
- **COLNÍK Guard Shell Security:** Intercepts forbidden system routines in 0.0s.
- **Safe Trash Governance:** Enforces Human-in-the-Loop quarantine review before file deletion.
- **Token Guard Enforcement:** Drops injection characters (`@#$%^&*`) at entry.
- **Permission & Policy Audits:** Enforced by `PermissionLayer5` and `PolicyEngine5`.
- **Autonomous Proposal Governance:** Evaluates decisions in tandem with `AUTONOMY-6.x` using confirmation state latching.
- **Live System Telemetry:** Audits system resources and latency timing governed by `Guard` and `TimeCore` (`cycle_delta()`).

---

# 📊 Module Status Matrix (v5.9.1)

| Module / Component | Status | Operational Notes |
| :--- | :---: | :--- |
| **`sirius_orchestrator.py`** | 🟩 Stable | Unified single-process runtime, native IPC bridge (port 8080), embedded TerminalAssistant + TimeCore |
| **`TokenGuard`** | 🟩 Operational | Entry-level input sanitization, immediate rejection of `@#$%^&*` |
| **`InputParser5`** | 🟩 Enhanced | Multi-word phrase preservation, `.rstrip("?")` trailing punctuation stripping |
| **Dual KG Storage** | 🟩 Operational | Full partition: `autosave_kg.json` (SK) & `autosave_kg_en.json` (EN) |
| **Native Merge Engine** | 🟩 Operational | In-memory `kg merge <src> into <tgt>` with attribute retention & alias edge binding |
| **Taxonomical Reasoner** | 🟩 Operational | Contextual deduction (`KG_VERIFY`) with persistent edge auto-commit |
| **Reverse Habitat Engine** | 🟩 Operational | Multi-stem regional search with False-Positive Flora Guard |
| **`EnvoyQuarantine5`** | 🟩 Operational | Automated sliding-window rotation enforcing 100-file ceiling |
| **`EnvoyExecutionLayer5`** | 🟩 Enhanced | Autonomous Disambiguation Triage, Anti-Prefix Guard, language-specific endpoints |
| **`EnvoyNormalizer5`** | 🟩 Enhanced | Contextual semantic parser, non-bio domain blocker |
| **UI Suite (4 Panels)** | 🟩 Stable | `Duplicates`, `Triage`, `Navigation`, `Terminal` (clean state reset `currentModule = "none"`) |
| **COLNÍK Guard & HitL Trash** | 🟩 Operational | 0.0s hard block on `format`/`diskpart`, quarantine routing for file deletions (`GET /trash`) |
| **Reasoning Engine 5.9.1** | 🟩 Stable | Multi-hop inference rules, XAI proof-tree generation, taxonomical inference |
| **AUTONOMY 6.x** | 🟩 Stable | Proposal generation, confirmation latching, Guard supervision, Safe Trash governance |

---

# 🗺️ Strategic Roadmap (Upcoming Iterations)

1. **Standalone Binary Packaging (`.exe`):** Compiling an isolated, distributable executable eliminating external Python dependencies.
2. **Hybrid Isolation Layer (HIL v7.x):** Unifying technical process sandboxing with logical semantic quarantine.
3. **Autonomous Household AI:** Task planning, offline inventory workflows, and device troubleshooting.
4. **Offline Voice & Interaction:** Local speech-to-text processing and verbal explainability summaries.

---

# 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

# 🏁 Summary

SIRIUS LOCAL AI 5.9.1 unites deterministic symbolic graph logic with dual-language isolation, native lossless entity merging, automated taxonomical deduction, and comprehensive system protection under COLNÍK Guard and Human-in-the-Loop Safe Trash. The runtime is fast, secure, explainable, and prepared for continuous expansion.

---
**Metadata & SEO:**  
Keywords: SIRIUS LOCAL AI, Symbolic AI, Knowledge Graph, Offline AI, Dual-Language KG, KG Merge, COLNIK Guard, Token Guard, Safe UI Trash, Envoy Triage, Python Orchestrator, Autonomous AI, Localhost AI  
Version: 5.9.1  
License: MIT License  
Author: richardpizem-ctrl  
Environment: Localhost / Windows 11 / Port 8080  
Build Status: Active Development (WIP)
