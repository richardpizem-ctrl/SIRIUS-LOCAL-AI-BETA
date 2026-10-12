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
   - SIRIUS transitions permanently into an autonomous, 100% offline deterministic runtime.
