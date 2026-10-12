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

---

## 4. Acceptance Test Scenarios (Definition of Done)

- **Scenario A (Race Condition Defense):** Simulate simultaneous write execution between SIRIUS Core and Professor. The committer must abort the satellite transaction, preserve user-created nodes, and log a version conflict.
- **Scenario B (Crash Resilience):** Force-terminate the Professor daemon (`SIGKILL` / `taskkill /F`) during staging operations. The master `autosave_kg.json` must remain uncorrupted and parseable on subsequent boot.
- **Scenario C (Poisoning & Injection Immunity):** Submit conflicting, adversarial, or malicious imperative prompts. The staging quarantine must tag them as `conflicted` or `rejected`, completely preventing insertion into the golden graph.
