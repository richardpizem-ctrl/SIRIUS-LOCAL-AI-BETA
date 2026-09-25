# ⚡ PERFORMANCE GUIDE – SIRIUS LOCAL AI (v5.9.0 UNIFIED)

This document defines the performance model, optimization rules, and runtime guarantees of the  
**Semantic Multi-Word Parsing, Autonomous Disambiguation Triage, 4-Panel UI Suite & Multi-Alias KG Persistence Architecture 5.9.0**.

Version **5.9.0 UNIFIED** expands and optimizes the runtime profile with:

- **Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080) (zero IPC socket overhead, no file contention)**  
- **Multi-Word Semantic Engine (`InputParser5`) (constant-time token grouping and copula isolation)**  
- **Multi-Alias KG Persistence (`autosave_kg.json`) (O(1) memory lookup suppressing redundant learning proposals)**  
- **Autonomous Disambiguation Triage (`EnvoyExecutionLayer5`) (bounded network timeouts and prefix checks)**  
- **Contextual Domain & Bio Filtering (`EnvoyNormalizer5`) (sentence-bound declarative parsing)**  
- **4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) (asynchronous state decoupling, non-blocking)**  
- **Terminal State Decoupling (`currentModule = "none"`) (zero input lockups or CLI stalling)**  
- **PanelAPI & Interactive [ÁNO/NIE] Confirmation Loops (non-blocking async polling)**  
- **TimeCore Temporal Tracking & Guard Resource Telemetry (lightweight CPU/RAM/Disk metrics)**  
- **Workflow Engine 5.9.0 (constant-time transitions, COLNIK-validated and AUTONOMY-aware routing)**  
- **Reasoning Engine 5.9.0 (bounded multi-hop derivation, property inheritance, orbital rules)**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (deterministic proof-tree generation under bounded memory constraints)**  
- **COLNIK-6.x Customs Decision Gate (constant-time allow/deny evaluation — Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x (supervised proposal cycle, Guard metric integration, and bounded Triage Mode)**  

All processing is fully local; no data leaves the user's device.

---

# 1. Performance Philosophy

- predictable, deterministic execution > unconstrained throughput  
- single-process orchestration: eliminate disk-based IPC locks and inter-process polling latency  
- zero proposal recurrence: once an alias is indexed in `autosave_kg.json`, subsequent queries resolve in O(1)  
- no uncontrolled conversational loops or terminal command captures  
- compound noun preservation must not degrade parsing time (`O(N)` token scan)  
- strict boundaries for autonomous web triage: fast timeouts, anti-prefix guards, and non-bio domain checks  
- minimal overhead across all modules: complete cycle response under 10ms for local graph queries  
- SCHOOLWORK workflows must remain instant and non-bypassable  
- **Security Family 5.x checks must remain strictly O(1)**  
- **System Agent 5 validation must remain O(1)**  
- **COLNIK-6.x Customs inspection (Standard & IPC Mode) must remain constant-time**  
- **Guard system resource monitoring must operate asynchronously with < 1% CPU utilization**  
- **Orchestrator and PanelAPI loop latency must remain < 1ms per event**  

---

# 2. Runtime Guarantees (Runtime 5.9.0)

- **Zero Socket Contention:** Single-process architecture hosting HTTP/WebSocket on port 8080 eliminates socket conflicts  
- **Zero Proposal Recurrence:** Confirmed knowledge is served from primary or secondary alias indexes with zero interactive prompt latency  
- **Terminal Isolation:** Clearing input immediately resets active execution context to `currentModule = "none"` in O(1) time  
- **Cycle-Safe Reasoning:** Multi-hop graph traversal and orbital rules are bounded to fixed recursion depths, preventing runaway inference  
- **Atomic Persistence:** Graph mutations are written atomically to `autosave_kg.json` without corrupting active memory snapshots  
- **Deterministic Tokenization:** `InputParser5` separates copula verbs (`je`, `sú`) and retains compound entities without backtracking  
- **No Blocking Operations:** PanelAPI `[ÁNO/NIE]` dialogs use asynchronous callback structures without freezing background monitors  
- **TimeCore & Guard Telemetry:** Execution timing and system health metrics operate non-intrusively with zero thread stalls  

---

# 3. Knowledge Graph & Multi-Alias Indexing Performance

Rules:

- primary entity labels and aliases share a hash-indexed lookup table (`O(1)` query complexity)  
- queries for synonyms (e.g., `ovcia vlna` vs. `Vlna (textil)`) resolve directly to the canonical node pointer  
- suppressed learning loops: query resolution checks the alias index first before invoking AUTONOMY proposal generators  
- atomic serialization: `autosave_kg.json` serializes asynchronously or during idle cycles to avoid blocking active workflows  
- graph export/import operations are streaming and chunk-validated to prevent memory spikes  
- relations and properties are pre-indexed; orbital searches avoid full-graph scans  

---

# 4. Multi-Word Parsing & NL Performance (`InputParser5`)

- single-pass grammatical tokenization: compound phrases (`ovcia vlna`, `mobilny telefon`) are matched using linear token grouping  
- copula verb isolation (`je`, `sú`) occurs prior to entity matching, preventing complex regex backtracking  
- diacritic normalization is performed in a single buffer traversal  
- parsing overhead must remain under 0.5ms for standard user inputs  
- unrecognized inputs transition cleanly to AUTONOMY without triggering retry loops  

---

# 5. Autonomous ENVOY & Triage Performance

- **Bounded External Fetching:** External lookups execute with strict HTTP connection and read timeouts  
- **Disambiguation Fast-Path:** Wikipedia disambiguation headers (*„môže byť...“*) are parsed via streaming text filters  
- **Anti-Prefix Verification:** Prefix string comparisons are performed in constant time, stopping semantic drift immediately  
- **Domain Normalizer:** The Non-Bio Domain Shield and sentence-bound extractor evaluate only immediate declarative sentences, avoiding full-page semantic parsing  
- **Quarantine Cleansing:** HTML and script stripping runs via linear text scanners without invoking browser engines  

---

# 6. 4-Panel UI Suite & Terminal Performance (Port 8080)

- browser dashboard on port 8080 uses lightweight, event-driven DOM updates  
- **Terminal Decoupling:** Clearing input resets `currentModule = "none"` instantly, freeing event listeners  
- **Duplicates Panel:** File hash comparisons utilize streaming block hashing, categorizing duplicates without disk saturation  
- **Triage Panel:** Live quarantine queue updates utilize delta payloads rather than full queue redraws  
- **Navigation Panel:** Switching modules updates UI state in constant time without reloading backend services  

---

# 7. Workflow Engine 5.9.0 & Orchestrator Performance

- workflow transitions are executed as O(1) state-machine transitions managed by `sirius_orchestrator.py`  
- workflows maintain cached operational contexts, avoiding redundant property lookups  
- deep explainability traces (`KG_EXPLAIN_DEEP`) compile proof trees lazily upon request  
- COLNIK-6.x customs checks and AUTONOMY approvals evaluate in constant time within the orchestration pipeline  
- long-running operations yield control cooperatively, ensuring the UI remains responsive  

---

# 8. Symbolic Reasoning & XAI Performance

- reasoning depth is bounded by maximum orbital traversal thresholds  
- rules (`MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`, `TranzitivneRelacieRule`, `AutoTypeInferenceRule`) execute against indexed graph subsets  
- proof trees are constructed deterministically without non-deterministic search heuristics  
- confidence scores are calculated in linear time relative to the active proof path length  
- explanation rendering (ASCII / HTML) is isolated from the reasoning core  

---

# 9. Security Family & Identity Performance

### Identity Engine 3.1
- identity evaluation is strictly O(1) based on active session profiles (OWNER / FAMILY / STRANGER)  
- no background tracking loops or heavy biometric processing  
- STRANGER lockdown mode activates instantly upon unrecognized input  

### Schoolwork Engine 5.8
- academic topic identification is pre-computed and pattern-matched  
- academic bypass logic operates in constant time, ensuring learning workflows are never delayed  

### Time-Limits Engine v3
- temporal quotas are evaluated via delta calculations against TimeCore timestamps  
- no active polling timers in tight execution loops  

---

# 10. Self-Repair Layer & Guard Supervision Performance

- Guard resource telemetry polls OS metrics (CPU, RAM, Disk) at bounded, low-frequency intervals  
- anomaly thresholds are evaluated using moving averages to prevent alert thrashing  
- Self-Repair integrity scans run during system idle states or startup  
- schema integrity checks on `autosave_kg.json` execute via fast streaming JSON validators  
- repair suggestions and rollback operations maintain deterministic fallbacks  

---

# 11. Performance Baseline Metrics

| Component / Action | Complexity | Latency Target | Resource Overhead |
|:---|:---:|:---:|:---:|
| `InputParser5` Token Parsing | O(N) | < 0.5ms | Negligible |
| Multi-Alias Graph Lookup | O(1) | < 1ms | In-memory RAM lookup |
| COLNIK-6.x Customs Clearance | O(1) | < 0.2ms | Zero thread blocking |
| PanelAPI Event Dispatch | O(1) | < 1ms | Non-blocking async |
| Terminal State Reset (`none`) | O(1) | < 0.1ms | Instant state clear |
| Single-Hop Symbolic Inference | O(1) | < 2ms | Bounded memory |
| Multi-Hop Orbit Proof Tree | O(D) (bounded) | < 8ms | Bounded tree depth |
| Guard Metric Polling | O(1) | < 1ms | < 1% CPU utilization |

---

# 📄 Document Status

**Version:** 5.9.0 UNIFIED  
Performance rules and architectural guarantees are fully aligned with the **Semantic Multi-Word Parsing, Autonomous Disambiguation Triage, 4-Panel UI Suite & Multi-Alias KG Persistence Architecture 5.9.0**, ensuring maximum responsiveness and determinism on local hardware.
