# RFC: SIRIUS Satellite Subsystem — Professor

**Status:** Active · Updated for SIRIUS LOCAL AI BETA v6.1.0  
**Author:** SIRIUS Core Architecture Team  
**Original date:** 2026-11-10  
**Revision date:** 2026-11-14  
**Target environment:** Windows desktop workstation running SIRIUS locally  
**Core dependencies:** Python standard library for the v6.1.0 idle synthesis path

---

## 1. Executive Summary

Professor is the SIRIUS subsystem for offline knowledge enrichment and linguistic processing. It operates on separate Slovak and English knowledge graphs, `autosave_kg.json` and `autosave_kg_en.json`.

The v6.0.1 RFC defined a design for linguistic enrichment, validated graph updates, and controlled ingestion. SIRIUS LOCAL AI BETA v6.1.0 implements a specific part of that design: idle-time processing that derives an explanation from explicit relationships in one graph and saves the supporting facts with it.

---

## 2. Architectural Principles

### 2.1 Integrated Orchestration

`sirius_orchestrator.py` coordinates the desktop panel, the local HTTP IPC bridge on port 8080, and background graph processing. Professor processes bounded batches during idle time so the orchestrator can return to user requests between batches.

### 2.2 Controlled Ingestion and Input Validation

The original design limits network ingestion to configured sources and calls for filtering imported text before it can become graph data. Markup stripping, token filtering, and quarantine are design measures for ingestion paths.

The v6.1.0 idle synthesis path reads local graph files. Facts previously added by ENVOY can support an explanation when they exist as explicit relationships that match the rule. Available source references are preserved alongside the supporting facts.

### 2.3 Atomic Graph Writes

Before saving a derived explanation, Professor rechecks the supporting relationships under the graph file lock. The write uses a temporary file followed by `os.replace()` to update the target graph. An identical explanation is skipped. If writing fails, the proposal remains pending for retry during the current session.

The original RFC also proposed version-conflict detection through monotonic `kg_version` counters and recovery after interrupted updates. Those remain separate acceptance targets for the broader architecture.

### 2.4 Bilingual Processing

The Slovak and English graphs have independent paths. If the path for a language is missing, its synthesis pass is skipped. Each explanation uses facts from its own language graph.

The broader linguistic design covers Slovak reflexive verbs such as *sa* and *si*, English phrasal verbs, collocations, and conjunctions. The v6.1.0 synthesis rule uses fixed Slovak and English wording with the required grammatical forms.

The original RFC proposed the fact states `provisional`, `verified_multi_source`, and `conflicted` for ingestion. The idle synthesis rule checks explicit supporting relationships before it saves an explanation.

### 2.5 Recovery and Offline Operation

The original design proposed integration with `SafeRollback` for module-level backup and recovery. It also proposed freezing network ingestion once a graph reached a defined saturation threshold. Both remain design goals. Professor's v6.1.0 idle synthesis runs locally on the available graphs.

---

## 3. Directory and File Manifest

Paths are relative to the v6.1.0 Windows build source.

| Path | Role |
| --- | --- |
| `sirius_orchestrator.py` | Coordinates the desktop panel, local IPC, and idle processing. |
| `runtime5/runtime_core_5.py` | Defines and loads the active Slovak and English graphs. |
| `professor/idle_synthesis.py` | Scans each graph in batches, builds candidate explanations, and checks their supporting relationships. |
| `professor/grammar_engine.py` | Provides existing linguistic processing and triplet extraction. |
| `professor/atomic_committer.py` | Provides the existing triplet commit path. |
| `professor/gatekeeper_net.py` | Contains network gatekeeping logic for ingestion. |
| `professor/staging_quarantine.py` | Contains staging and quarantine logic for proposed facts. |
| `kg_file_io.py` | Provides graph file locking and atomic replacement for the idle synthesis path. |
| `BUILD_EXE/test_idle_professor.py` | Tests idle synthesis on isolated copies of both graphs. |

In the Windows Preview, the writable graph files are `SIRIUS_DATA/autosave_kg.json` and `SIRIUS_DATA/autosave_kg_en.json`.

---

## 4. Implemented in v6.1.0

1. **Idle trigger.** After five seconds without activity, Professor scans the Slovak and English graphs in alternating batches. Panel activity and a pending ENVOY confirmation pause scanning. Processing resumes when SIRIUS is idle again.
2. **First synthesis rule.** Professor builds an explanation about fish when one graph explicitly identifies fish as vertebrates, links them to still waters, and provides examples of those waters. The rule can follow these relationships wherever they occur in the JSON file.
3. **Language-specific wording.** The rule produces Slovak or English text. The Slovak template includes the grammatical form *v stojatých vodách*.
4. **Evidence and persistence.** Professor saves the explanation on the subject as `professor_explanation`, together with the supporting relationships and any available source references. It checks the graph again before writing.
5. **Duplicate prevention and retry.** An identical explanation is skipped. A failed write leaves the proposal pending for retry while SIRIUS is running.

---

## 5. Verification and Acceptance Tests

### Verified on graph copies in v6.1.0

- Pause and resume while scanning both languages.
- Save a supported explanation and retain it after reloading the graph.
- Run the same rule again without creating a duplicate.
- Reject a proposal when a supporting relationship is missing.
- Keep and retry a proposal after a failed write.
- Skip a missing English graph path without using the Slovak graph.

The Windows desktop build was verified to start and load both live graphs. An automatic Professor write to those live graphs has yet to be confirmed.

### Acceptance targets for the broader design

| Scenario | Expected result |
| --- | --- |
| Concurrent Runtime and Professor writes | Preserve user-created facts and verify how overlapping updates are resolved and reported. |
| Interrupted staging or write | Keep the graph readable after restart and verify any recovery procedure separately. |
| Conflicting or malformed ingestion input | Reject or quarantine unsuitable proposals before they reach the active graph. |
| Saturation and ingestion freeze | Define the saturation threshold and verify the transition to frozen ingestion. |
