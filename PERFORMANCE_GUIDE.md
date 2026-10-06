# ⚡ PERFORMANCE GUIDE – SIRIUS LOCAL AI (v5.9.1 UNIFIED)

This document defines the performance model, optimization rules, and runtime guarantees of the  
**Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & COLNÍK Guard Security Protocol 5.9.1**.

Version **5.9.1 UNIFIED** expands and optimizes the runtime profile with:

- **Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080) (embedded TerminalAssistant + TimeCore, zero IPC socket overhead, no file contention)**
- **Dual-Language Isolated Knowledge Stores (`autosave_kg.json` & `autosave_kg_en.json`) (O(1) memory lookup with zero cross-lingual contamination)**
- **Native Lossless KG Merge Engine (`kg merge <src> into <tgt>`) (in-memory property relocation and alias pointer binding)**
- **Ontological & Taxonomical Reasoning (`KG_VERIFY`) (hierarchical sub-taxa deduction with persistent edge auto-commits)**
- **Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`) (multi-stem matching, uniform `get_attributes()` traversal, and anti-flora shielding)**
- **Input Sanitization & Hygiene (Token Guard O(1) symbol check, `.rstrip("?")` trailing punctuation stripping)**
- **Confirmation State Latching (deterministic O(1) state preservation across interactive conversation turns)**
- **Sliding-Window Quarantine Ceiling Rotation (100 JSON file ceiling in `COLNIK-6.x/envoy/quarantine/`, constant-time sliding window)**
- **COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like `format` and `diskpart`)**
- **Human-in-the-Loop Safe UI Trash (non-destructive quarantine diversion preventing unverified disk I/O)**
- **Character Encoding Fallback (UTF-8 -> CP1250 -> CP852 pipeline with zero diacritic corruption)**
- **Multi-Word Semantic Engine (`InputParser5`) (constant-time token grouping and copula isolation)**
- **Autonomous Disambiguation Triage (`EnvoyExecutionLayer5`) (bounded network timeouts and prefix checks)**
- **Contextual Domain & Bio Filtering (`EnvoyNormalizer5`) (sentence-bound declarative parsing)**
- **4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`) (asynchronous state decoupling, non-blocking)**
- **Terminal State Decoupling (`currentModule = "none"`) (zero input lockups or CLI stalling)**
- **PanelAPI & Interactive [ÁNO/NIE] / [YES/NO] Confirmation Loops (non-blocking async polling)**
- **TimeCore Temporal Tracking (`cycle_delta()`) & Guard Resource Telemetry (lightweight CPU/RAM/Disk metrics)**
- **Workflow Engine 5.9.1 (constant-time transitions, COLNIK-validated and AUTONOMY-aware routing)**
- **Reasoning Engine 5.9.1 (bounded multi-hop derivation, property inheritance, orbital & taxonomical rules)**
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (deterministic proof-tree generation under bounded memory constraints)**
- **COLNIK-6.x Customs Decision Gate (constant-time allow/deny evaluation — Standard & High-Performance IPC Mode)**
- **AUTONOMY 6.x (supervised proposal cycle, Guard metric integration, and bounded Triage Mode)**

All processing is fully local; no data leaves the user's device.

---

# 1. Performance Philosophy

- predictable, deterministic execution > unconstrained throughput  
- single-process orchestration: eliminate disk-based IPC locks, process spawning, and inter-process polling latency  
- zero proposal recurrence: once an alias or taxonomical relation is indexed, subsequent queries resolve in O(1)  
- strict language partition: Slovak and English queries access dedicated in-memory graphs without cross-lingual collision overhead  
- immediate security filtering: Token Guard symbol checks and COLNÍK Guard command interceptions resolve at runtime boundary in 0.0s  
- no uncontrolled conversational loops or terminal command captures  
- compound noun preservation and punctuation trimming must not degrade parsing time (`O(N)` linear token scan)  
- strict boundaries for autonomous web triage: fast timeouts, anti-prefix guards, 100-file sliding-window ceilings, and non-bio domain checks  
- minimal overhead across all modules: complete cycle response under 10ms for local graph queries  
- SCHOOLWORK workflows must remain instant and non-bypassable  
- **Token Guard validation must remain strictly O(1)**  
- **COLNÍK Guard shell access checks must evaluate in 0.0s**  
- **Security Family 5.x checks must remain strictly O(1)**  
- **System Agent 5 validation must remain O(1)**  
- **COLNIK-6.x Customs inspection (Standard & IPC Mode) must remain constant-time**  
- **Guard system resource monitoring must operate asynchronously with < 1% CPU utilization**  
- **Orchestrator and PanelAPI loop latency must remain < 1ms per event**  

---

# 2. Runtime Guarantees (Runtime 5.9.1)

- **Zero Socket Contention:** Single-process architecture hosting HTTP/WebSocket on port 8080 eliminates socket conflicts  
- **Dual-Language Memory Isolation:** `self.kg_sk` and `self.kg_en` maintain isolated node registries, preventing cross-language graph pollution  
- **Zero Proposal Recurrence:** Confirmed knowledge and deduced taxonomical categories are committed to disk and served with zero interactive prompt latency  
- **Terminal & Shell Isolation:** Clearing input immediately resets active execution context to `currentModule = "none"` in O(1) time; forbidden shell commands are halted in 0.0s  
- **Safe Storage Maintenance:** Quarantine file count is capped at 100 records via automated sliding-window pruning  
- **Cycle-Safe Reasoning:** Multi-hop graph traversal and orbital rules are bounded to fixed recursion depths, preventing runaway inference  
- **Atomic Persistence:** Graph mutations are written atomically to `autosave_kg.json` and `autosave_kg_en.json` without corrupting active memory snapshots  
- **Deterministic Tokenization:** `InputParser5` separates copula verbs (`je`, `sú`, `is`, `are`), strips trailing punctuation (`.rstrip("?")`), and retains compound entities without backtracking  
- **No Blocking Operations:** PanelAPI `[ÁNO/NIE]` / `[YES/NO]` dialogs use confirmation state latching without freezing background monitors  
- **TimeCore & Guard Telemetry:** Execution timing via `cycle_delta()` and system health metrics operate non-intrusively with zero thread stalls  

---

# 3. Knowledge Graph, Dual Stores & Native Merge Performance

Rules:

- primary entity labels and aliases share a hash-indexed lookup table (`O(1)` query complexity) across both `autosave_kg.json` and `autosave_kg_en.json`  
- native merge operations (`kg merge <src> into <tgt>`) execute in-memory in `O(A + E)` time (attributes + edges), updating alias pointers without reloading graph state  
- taxonomical deductions (`KG_VERIFY`) evaluate linear inheritance chains and auto-commit edges in `O(1)` to permanently eliminate prompt cycles  
- reverse location queries (`_execute_reverse_location_query`) execute uniform attribute scans (`get_attributes()`) using pre-filtered stem sets (*Austrálii*, *Austrália*, *Australia*) without regex backtracking  
- suppressed learning loops: query resolution checks active language graph and alias index first before invoking AUTONOMY proposal generators  
- atomic serialization: `autosave_kg.json` and `autosave_kg_en.json` serialize independently during idle cycles or immediately after approved enrichment  
- graph export/import operations are streaming and chunk-validated to prevent memory spikes  
- relations and properties are pre-indexed; orbital searches avoid full-graph scans  

---

# 4. Multi-Word Parsing, Input Hygiene & Token Guard Performance

- **Token Guard Sanitization:** Single-pass character check detects forbidden symbols (`@`, `#`, `$`, `%`, `^`, `&`, `*`) in `O(N)` time, rejecting invalid requests before parsing starts  
- **Punctuation Trimming:** Trailing question marks are stripped in `O(1)` time via `.rstrip("?")`, avoiding regular expression engine overhead  
- **Single-Pass Grammatical Tokenization:** Compound phrases (`ovcia vlna`, `mobilny telefon`) are matched using linear token grouping  
- **Copula Verb Isolation:** Extraction of (`je`, `sú`, `is`, `are`) occurs prior to entity matching, preventing complex linguistic backtracking  
- **Diacritic Normalization:** Single buffer traversal across Slovak and English character sets  
- parsing overhead must remain under 0.5ms for standard user inputs  
- confirmation latching preserves target entity state across turns with zero memory reallocation overhead  

---

# 5. Autonomous ENVOY, Quarantine & Security Performance

- **Bounded External Fetching:** External lookups execute with strict HTTP connection and read timeouts  
- **Sliding-Window Quarantine Maintenance:** `COLNIK-6.x/envoy/quarantine/` tracks file counts and purges oldest records in `O(log N)` file-time sorting, never exceeding 100 JSON payloads  
- **COLNÍK Guard Shell Filtering:** Exact string and prefix matching against FORBIDDEN commands executes in 0.0s before OS process creation  
- **HitL Safe Trash Diversion:** File deletion interception moves files to quarantine without triggering destructive disk deletion routines  
- **Disambiguation Fast-Path:** Wikipedia disambiguation headers (*„môže byť...“*) are parsed via streaming text filters  
- **Anti-Prefix Verification:** Prefix string comparisons are performed in constant time, stopping semantic drift immediately  
- **Domain Normalizer:** Non-Bio Domain Shield evaluates only immediate declarative sentences, avoiding full-page semantic parsing  
- **Quarantine Cleansing:** HTML and script stripping runs via linear text scanners without invoking browser engines  

---

# 6. 4-Panel UI Suite & Terminal Performance (Port 8080)

- browser dashboard on port 8080 uses lightweight, event-driven DOM updates  
- **Terminal Decoupling:** Clearing input resets `currentModule = "none"` instantly, freeing event listeners and preventing shell capture  
- **Duplicates Panel:** File hash comparisons utilize streaming block hashing, categorizing duplicates into safe vs. critical (`REPORT_ONLY`) without disk saturation  
- **Triage Panel:** Live quarantine queue updates utilize delta payloads rather than full queue redraws  
- **Navigation Panel:** Switching modules updates UI state in constant time without reloading backend services  

---

# 7. Workflow Engine 5.9.1 & Orchestrator Performance

- workflow transitions are executed as O(1) state-machine transitions managed by `sirius_orchestrator.py`  
- workflows maintain cached operational contexts, avoiding redundant property lookups  
- deep explainability traces (`KG_EXPLAIN_DEEP`) compile proof trees lazily upon request  
- COLNIK-6.x customs checks, COLNÍK Guard filters, and AUTONOMY approvals evaluate in constant time within the orchestration pipeline  
- long-running operations yield control cooperatively, ensuring the UI remains responsive  

---

# 8. Symbolic Reasoning & XAI Performance

- reasoning depth is bounded by maximum orbital traversal thresholds  
- rules (`MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`, `TranzitivneRelacieRule`, `AutoTypeInferenceRule`, `TaxonomyRule`) execute against indexed graph subsets  
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
- schema integrity checks on `autosave_kg.json` and `autosave_kg_en.json` execute via fast streaming JSON validators  
- repair suggestions and rollback operations maintain deterministic fallbacks  

---

# 11. Performance Baseline Metrics

| Component / Action | Complexity | Latency Target | Resource Overhead |
|:---|:---:|:---:|:---:|
| Token Guard Input Sanitization | O(N) | < 0.1ms | Negligible |
| Punctuation Stripping (`.rstrip("?")`) | O(1) | < 0.05ms | Negligible |
| `InputParser5` Token Parsing | O(N) | < 0.5ms | Negligible |
| Dual-Language Graph Lookup (SK/EN) | O(1) | < 1ms | In-memory RAM lookup |
| Native Entity Merge (`kg merge`) | O(A + E) | < 3ms | In-memory property migration |
| Taxonomical Deduction (`KG_VERIFY`) | O(1) | < 2ms | In-memory inference + commit |
| COLNÍK Guard Shell Interception | O(1) | 0.0s (instant block) | Zero process spawn |
| COLNIK-6.x Customs Clearance | O(1) | < 0.2ms | Zero thread blocking |
| PanelAPI Event Dispatch & Latch | O(1) | < 1ms | Non-blocking async |
| Terminal State Reset (`none`) | O(1) | < 0.1ms | Instant state clear |
| Quarantine Sliding-Window Prune | O(log N) | < 5ms | Capped at 100 JSON files |
| Single-Hop Symbolic Inference | O(1) | < 2ms | Bounded memory |
| Multi-Hop Orbit Proof Tree | O(D) (bounded) | < 8ms | Bounded tree depth |
| Guard Metric Polling (`cycle_delta()`) | O(1) | < 1ms | < 1% CPU utilization |

---

# 📄 Document Status

**Version:** 5.9.1 UNIFIED  
Performance rules and architectural guarantees are fully aligned with the **Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & COLNÍK Guard Security Protocol 5.9.1**, ensuring maximum responsiveness, zero unverified I/O, and determinism on local hardware.
