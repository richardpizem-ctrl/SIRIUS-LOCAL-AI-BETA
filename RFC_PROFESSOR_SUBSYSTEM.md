# RFC: SIRIUS Satellite Subsystem — "Professor" (Offline Knowledge & Linguistic Enrichment)
**Status:** ACTIVE / REVISED (V2.0)  
**Author:** SIRIUS Core Architecture Team  
**Date:** 2026-10-22  
**Target Environment:** Windows 11 PC / Local Host Workstation  
**Core Dependencies:** Standard Python Library (Zero-Dependency Ingestion)

---

## 1. Executive Summary
This RFC specifies the refined architecture of the satellite subsystem **Professor** integrated within SIRIUS 6.x. Its purpose is the deterministic enrichment of core Knowledge Graphs (`autosave_kg.json` for Slovak and `autosave_kg_en.json` for English) with a verified linguistic skeleton (grammar rules, reflexive/active verbs, collocations) and cross-validated ontological triplets. The subsystem operates with embedded orchestration, ensuring seamless local IPC execution on port 8080 and a guaranteed permanent Air-Gap freeze once target graph saturation is achieved.

---

## 2. Architectural Principles

1. **Integrated Orchestration & Process Safety:**
   - The Professor validation and logic routines operate seamlessly within the unified `sirius_orchestrator.py` architecture and runtime modules.
   - Any anomaly or validation rejection inside the subsystem has zero blast radius on the local HTTP IPC bridge (`:8080`) or core inference loops.

2. **Zero-Trust Network Ingestion & Sanitization:**
   - No open-ended web crawling. Network operations are strictly confined via whitelisted configuration sources to authoritative endpoints.
   - All ingested streams pass through HTML/XML tag strippers and Token Guard filters.
   - Deterministic filters block prompt injection patterns, imperative command tokens, and illegal control sequences.

3. **Optimistic Concurrency & Atomic File Commits:**
   - Persistent state files (`autosave_kg.json` and `autosave_kg_en.json`) maintain monotonically increasing version counters (`kg_version`).
   - Mutations are staged entirely inside secondary working files (`.tmp`) guarded by OS-level file locks (`kg_lock.lock`).
   - Production promotion executes via atomic system calls (`os.replace()`). Concurrency collisions trigger automatic rollback and rescheduling.

4. **Bilingual Epistemic Fact Classification:**
   - Graph storage and relational ingestion are strictly separated into parallel localized repositories (`autosave_kg.json` and `autosave_kg_en.json`) to prevent cross-language contamination.
   - Triplet extraction supports advanced linguistic structures (e.g., Slovak reflexive verbs with *sa/si*, English phrasal verbs, preserved conjunctions).
   - Epistemic states (`provisional`, `verified_multi_source`, `conflicted`) govern promotion eligibility.

5. **SafeRollback Integration:**
   - In case of collision, syntax failure, or structural corruption, the built-in `SafeRollback` module (`safe_rollback.py`) bypasses Git dependencies, executing granular module-level backups (`shutil.copytree`) and instant restorations (`shutil.rmtree`) to restore the last known healthy state.

---

## 3. Directory & File Manifest

sirius_project/
├── core/
│   ├── runtime_core_5.py              # Deterministic local inference runtime
│   ├── sirius_orchestrator.py        # Embedded HTTP IPC Server (:8080) & TimeCore
│   ├── safe_rollback.py              # Module-level granular backup & restore
│   ├── autosave_kg.json              # Versioned Master Knowledge Graph (SK)
│   └── autosave_kg_en.json           # Versioned Master Knowledge Graph (EN)
│
└── professor/
    ├── professor_validator.py        # PASS / WARN / REJECT verification matrix
    ├── gatekeeper_net.py             # Domain-whitelisted proxy & prompt sanitizer
    ├── grammar_engine.py             # Bilingual morphological parser & filter
    ├── staging_quarantine.py         # Sliding-window quarantine buffer & rotation
    └── kg_lock.lock                  # OS filesystem lock handle

---

## 4. Acceptance Test Scenarios (Definition of Done)

- **Scenario A (Race Condition Defense):** Simulate simultaneous write execution between SIRIUS Core and Professor. The committer must abort the transaction, preserve user-created nodes, and log a version conflict.
- **Scenario B (Crash Resilience):** Force-terminate background operations during staging. Master graph files must remain uncorrupted and parseable on subsequent boot, leveraging `SafeRollback` if recovery is required.
- **Scenario C (Poisoning & Injection Immunity):** Submit conflicting, adversarial, or malicious imperative prompts. The staging quarantine must tag them as `conflicted` or `rejected`, completely preventing insertion into the golden graph.
