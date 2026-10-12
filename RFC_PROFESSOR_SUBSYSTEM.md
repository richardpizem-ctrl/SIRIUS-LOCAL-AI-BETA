# RFC: SIRIUS Satellite Subsystem — "Professor" (Offline Knowledge & Linguistic Enrichment)
**Status:** PROPOSED / DRAFT  
**Author:** SIRIUS Core Architecture Team  
**Date:** 2026-10-12  
**Target Environment:** Windows 11 PC / Local Host Workstation  
**Core Dependencies:** Standard Python Library (Zero-Dependency Ingestion)

---

## 1. Executive Summary
This RFC specifies the architecture of the satellite subsystem **Professor** (`sirius_professor_daemon`). Its purpose is the asynchronous, deterministic enrichment of the core Knowledge Graph (`autosave_kg.json`) with a verified linguistic skeleton (grammar rules, case declensions, collocations) and cross-validated ontological triplets. The subsystem operates strictly as an isolated, out-of-core background process without intrusive runtime hooks into `runtime_core_5.py`, ensuring a guaranteed permanent Air-Gap freeze once target graph saturation is achieved.

---

## 2. Architectural Principles

1. **Process & Memory Isolation:**
   - The Professor module executes as an independent operating system process.
   - Any crash, network latency, or socket timeout inside the Professor process has zero runtime blast radius on the local HTTP IPC bridge (`:8080`) or `sirius_orchestrator.py`.

2. **Zero-Trust Network Ingestion:**
   - No open-ended web crawling or indiscriminate scrapers. Network operations are strictly confined via `gatekeeper_net.py` to an explicit whitelist of authoritative endpoints (e.g., national linguistic corpora, structured repositories).
   - All ingested streams are aggressively stripped of executable scripts, HTML/XML tags, styles, and binary artifacts down to sanitized UTF-8 text.
   - Deterministic Token Guards filter out prompt injection patterns, imperative command tokens, and illegal control sequences.

3. **Optimistic Concurrency & Atomic File Commits:**
   - The persistent state file `autosave_kg.json` contains a monotonically increasing version counter (`kg_version`).
   - Mutations are staged entirely inside a secondary working file (`autosave_kg.tmp`) guarded by an OS-level file lock (`kg_lock.lock`).
   - Production promotion executes via an atomic system call (`os.replace()`). Any concurrent version drift caused by interactive user commits in the SIRIUS terminal immediately triggers an automatic rollback.

4. **Epistemic Fact Classification:**
   - Every triple `[Subject -> Predicate -> Object]` must carry explicit epistemic metadata:
     - `provisional`: In staging quarantine awaiting cross-validation.
     - `verified_multi_source`: Confirmed across multiple independent whitelist domains.
     - `conflicted`: Logical or semantic contradiction detected; strictly excluded from the production graph.
   - Sentences carrying negation, modal uncertainty (*might*, *allegedly*, *perhaps*), or ambiguous syntax are deterministically pruned.

5. **Cooperative Idle Scheduling & Immediate Preemption:**
   - Ingestion cycles trigger only when the primary orchestrator confirms an idle state (`STATUS_IDLE_LEARNING_ALLOWED`).
   - Any keyboard interrupt or interactive terminal prompt yields top scheduling priority, executing instant preemption of active background ingestion routines.

---

## 3. Directory & File Manifest

```text
sirius_project/
├── core/
│   ├── runtime_core_5.py             # Deterministic local inference runtime
│   ├── sirius_orchestrator.py        # Embedded HTTP IPC Server (:8080) & TimeCore
│   └── autosave_kg.json              # Versioned Master Knowledge Graph
│
└── professor/
    ├── sirius_professor_daemon.py    # Idle scheduler & enrichment coordinator
    ├── gatekeeper_net.py             # Domain-whitelisted proxy & prompt sanitizer
    ├── grammar_engine.py             # Morphological parser & negation filter
    ├── staging_quarantine.py         # Sliding-window quarantine buffer
    ├── atomic_committer.py           # Concurrency-safe file lock & atomic replace
    └── kg_lock.lock                  # OS filesystem lock handle

    4. Acceptance Test Scenarios (Definition of Done)
Scenario A (Race Condition Defense): Simulate simultaneous write execution between SIRIUS Core and Professor. The committer must abort the satellite transaction, preserve user-created nodes, and log a version conflict.

Scenario B (Crash Resilience): Force-terminate the Professor daemon (SIGKILL / taskkill /F) during staging operations. The master autosave_kg.json must remain uncorrupted and parseable on subsequent boot.

Scenario C (Poisoning & Injection Immunity): Submit conflicting, adversarial, or malicious imperative prompts. The staging quarantine must tag them as conflicted or rejected, completely preventing insertion into the golden graph.
---



```
# PROFESSOR SUBSYSTEM GOVERNANCE & EXECUTION PROTOCOL (V1.0)
**Security Classification:** STRICT AIR-LOCK INTERFACE  
**Operational Objective:** Deterministic Knowledge Graph saturation prior to permanent Air-Gap

---

### ARTICLE I: INITIATION & SCHEDULING CONSTRAINTS
1. The execution daemon `sirius_professor_daemon.py` MUST NOT spin up unless all of the following preconditions evaluate to `TRUE`:
   - The file lock `kg_lock.lock` is released and writable.
   - The primary orchestrator reports a continuous idle duration exceeding 900 seconds (`idle_time >= 900s`).
   - The total validated node/edge metric in `autosave_kg.json` is below the configured saturation threshold.

---

### ARTICLE II: NETWORK GATEKEEPER & INGESTION RULES
1. **Domain Whitelist Enforcement:** Network connections are restricted strictly to fully qualified domain names listed in `whitelist_sources.json`. HTTP 3xx redirects pointing to unlisted hosts must be severed immediately.
2. **Payload Sanitization Pipeline:**
   - Ingested payloads must pass through an HTML/XML tag stripper prior to memory ingestion.
   - Any continuous string exceeding 500 characters without valid grammatical punctuation marks must be dropped.
   - Strings containing command injection signatures (`IGNORE PREVIOUS`, `SYSTEM:`, `DELETE_NODE`, `<SCRIPT>`) must trigger immediate rejection and endpoint demotion.

---

### ARTICLE III: LINGUISTIC & EPISTEMIC VALIDATION PIPELINE
1. **Strict Dependency Extraction:** A candidate triplet is admitted to staging quarantine if and only if the syntactic tree resolves unambiguously to: `[Subject (Nominative)] -> [Predicate (Active Transitive Verb)] -> [Object (Direct Case)]`.
2. **Deterministic Negation & Modality Bar:**
   - Any statement containing negative prefixes (*ne-*), negation adverbs (*nie*), or modal operators (*môže*, *pravdepodobne*, *údajne*) must be discarded.
3. **Sliding-Window Quarantine:** New triplets must endure a minimum retention window of three sliding cycles or obtain affirmative multi-domain corroboration before eligibility for promotion.

---

### ARTICLE IV: ATOMIC COMMIT & DATA INTEGRITY PROTOCOL
1. **Pre-Commit Sequence:**
   - Acquire exclusive system file handle lock on `kg_lock.lock`.
   - Read and store baseline version `base_version` from `autosave_kg.json`.
   - Write merged graph into transient disk location `autosave_kg.tmp`.
   - Run complete JSON schema validation and AST syntax integrity checks against `autosave_kg.tmp`.
2. **Execution & Promotion:**
   - Read current version from `autosave_kg.json`.
   - If `current_version == base_version`:
     - Perform atomic filesystem operation `os.replace("autosave_kg.tmp", "autosave_kg.json")`.
     - Increment persistent version counter to `current_version + 1`.
     - Release `kg_lock.lock`.
   - If `current_version != base_version`:
     - Erase `autosave_kg.tmp`.
     - Emit concurrency collision event and re-schedule merge cycle against the updated baseline.

---

### ARTICLE V: PERMANENT AIR-GAP PROTOCOL (SYSTEM FREEZE)
1. Upon formal verification that knowledge density, vocabulary coverage, and grammatical stability have met target thresholds:
   - Terminate the background daemon `sirius_professor_daemon.py`.
   - Invalidate or delete `gatekeeper_net.py` and network configuration records.
   - Set `"immutable": true` inside `autosave_kg.json` root metadata.
