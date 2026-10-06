# 🛡 Security Architecture – SIRIUS LOCAL AI (v5.9.1 UNIFIED)
### Fully Offline • Deterministic • Dual-Language Isolated • Domain-Shielded • Single-Process Orchestrated • COLNÍK Guard Hardened • HitL Safe Trash • AUTONOMY‑Supervised

The **Security Architecture 5.9.1** defines all identity‑aware, OS‑aware, workflow‑aware, domain-shielded, semantic-aware, input-sanitized, shell-protected, and fetch‑aware protections inside the  
**Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & COLNÍK Guard Security Protocol 5.9.1**.

Version **5.9.1 UNIFIED** introduces major upgrades across all security layers:

- **Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)**  
- **Dual-Language Isolated Knowledge Stores (`autosave_kg.json` for SK & `autosave_kg_en.json` for EN)**  
- **Native Lossless KG Merge Engine (`kg merge <src> into <tgt>` directly in RuntimeCore)**  
- **Taxonomical Category Deduction (`KG_VERIFY`) with zero confirmation recurrence**  
- **Non-Destructive Reverse Location Engine (`_execute_reverse_location_query` with anti-flora classification guard)**  
- **Entry-Level Token Guard (hard blocking of malicious symbol injections `@#$%^&*`)**  
- **Punctuation Hygiene (`.rstrip("?")`) and Confirmation State Latching across turns**  
- **COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like `format` and `diskpart`)**  
- **Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction (`GET /trash`)**  
- **Sliding-Window Quarantine Rotation (100 JSON file ceiling in `COLNIK-6.x/envoy/quarantine/`)**  
- **Character Encoding Fallback (UTF-8 -> CP1250 -> CP852 pipeline with zero diacritic corruption)**  
- **Multi-Word Semantic Integrity (`InputParser5` compound phrase preservation)**  
- **Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)**  
- **Contextual Domain Shield & Sentence-Bound Bio Filter (`EnvoyNormalizer5`)**  
- **4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)**  
- **Terminal State Decoupling (preventing shell capture & command injection)**  
- **TimeCore Temporal Tracking (`cycle_delta()`) & Guard Resource/Security Supervision (CPU, RAM, Disk)**  
- **Security Family 5.x (Identity Engine 3.1 with O(1) classification)**  
- **System Agent 5 (Hardened OS‑Level Gatekeeper)**  
- **Self‑Repair Layer 5.8 (hash-sealed integrity enforcement)**  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP (Hierarchical proof trees & XAI attribution)**  
- **COLNIK‑6.x Enterprise Customs Decision Gate (Standard, High-Performance IPC Mode & COLNÍK Guard)**  
- **AUTONOMY 6.x (Control, Guard, Safe Trash & Triage Mode in `COLNIK-6.x/triage`)**  

All processing is fully local.  
No data leaves the device unless explicitly permitted through:

**TOKEN GUARD → ASK → CONTEXT BIND (SK/EN) → DISAMBIGUATE → FETCH → ROTATING QUARANTINE → SHIELD → CUSTOMS → DUAL KG COMMIT**  
(ENVOY 5 secure pipeline, orchestrated on port 8080 with TerminalAssistant, COLNIK‑validated, domain-shielded, sliding-window capped, and human-confirmed via `PanelAPI` [ÁNO/NIE] / [YES/NO] with confirmation state latching)

---

# 🛡 5.9.1 Security Family 5.x – Identity Engine 3.1 (UPDATED)

Security Family 5.x strengthens the identity model and optimizes it for:

- speed (O(1) constant-time profile evaluation)  
- determinism and predictable security boundaries  
- deep symbolic explainability  
- **COLNIK‑validated identity enforcement (Standard, IPC Mode & COLNÍK Guard)**  
- **AUTONOMY‑aware identity governance (Control, Guard, Safe Trash & Triage Mode)**  
- **PanelAPI human-in-the-loop gating (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching**  
- **Terminal safety isolation via state decoupling and 0.0s command blocking**  

### Purpose
Ensure that all OS‑level, UI‑level, workflow‑level, reasoning‑level, and ENVOY‑level actions are:

- deterministically validated via `sirius_orchestrator.py` on port 8080 with embedded TerminalAssistant + TimeCore  
- identity‑controlled under OWNER / FAMILY / STRANGER access tiers  
- safely restricted with instant safe-mode locking for ambiguous callers  
- reversible and non-destructive via Human-in-the-Loop Safe Trash  
- sanitized at entry via Token Guard against malicious symbols (`@#$%^&*`)  
- fully audited with verifiable derivation traces  
- explainable via `KG_EXPLAIN` & `KG_EXPLAIN_DEEP` proof trees  
- customs-validated by COLNIK-6.x  
- autonomy-supervised without proposal recurrence  

### Security Enhancements (5.9.1 Upgrade)
- **Token Guard Entry Enforcement:** Raw inputs containing malicious or corrupted symbols (`@#$%^&*`) are dropped immediately at runtime threshold.  
- **Punctuation Stripping & Confirmation Latching:** Trailing punctuation is stripped via `.rstrip("?")` to avoid entity lookup corruption, and pending proposal targets remain latched in memory across conversation turns.  
- **COLNÍK Guard Command Interception:** TerminalAssistant intercepts forbidden shell instructions in 0.0s (`format`, `diskpart`, `rmdir /s`, etc.) before OS process execution.  
- **Human-in-the-Loop Safe Trash:** Direct unverified disk deletions are blocked; removals route to quarantine awaiting explicit manual review via `GET /trash`.  
- **Identity-Aware Dual-Language Resolution:** Access rules evaluate within the active linguistic graph (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN) without cross-lingual contamination.  
- **SCHOOLWORK Bypass 5.x:** Academic research tasks unconditionally bypass time and family restrictions while remaining explainable and auditable.  
- **Terminal Lockdown on STRANGER:** Unrecognized users trigger immediate interface lockdown and terminal detachment (`currentModule = "none"`).  
- **Constant-Time Verification:** Zero background biometric training loops; identity checks evaluate in O(1) time.  
- **Audit Integration:** Direct telemetry feed into Guard supervision and `TimeCore` latency profiling (`cycle_delta()`).  

### Threat Protections
- blocking OS‑level actions outside identity scope  
- 0.0s hard blocking of forbidden system routines (`format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`)  
- blocking unauthorized workflow state transitions  
- blocking UI terminal manipulation attempts  
- protection against rapid-fire execution anomalies and loop attacks  
- blocking unauthorized external fetch attempts  
- deep explainability metadata generated for every blocked operation  
- **COLNIK‑validated threat classification and quarantine dispatch**  

---

# 🛡 5.9.1 Semantic Integrity, Dual-Language Partitioning & Domain Shielding (NEW)

Runtime 5.9.1 introduces dedicated architectural guards against linguistic truncation, cross-lingual contamination, and cross-domain attribute pollution.

### Dual-Language Graph Isolation
- **Physical & Logical Segregation:** Slovak entities serialize into `autosave_kg.json`, while English entities persist into `autosave_kg_en.json`, eliminating bilingual query collisions, mixed summaries, and translation hallucinations.  
- **Dynamic Context Dispatching:** `RuntimeCore` binds queries, node retrieval, attributes, and relations dynamically based on the active UI language flag (`SK` / `EN`).  
- **Independent Atomic Dual Autosaves:** Serializes each partition independently on runtime shutdown or post-enrichment.  

### Native Lossless Entity Merge Security (`kg merge`)
- **Direct Runtime Consolidation:** Relocates properties, summaries, and habitat data from source to target without data loss directly inside `RuntimeCore`.  
- **Alias Link Integrity:** Converts source nodes into persistent directional aliases (`src -[alias]-> tgt`), preserving historical references without dangling pointers.  

### Ontological & Taxonomical Reasoning (`KG_VERIFY`)
- **Taxonomical Category Deduction:** Automatically recognizes biological sub-taxa (e.g., establishing that marsupials and macropods belong to mammals) without requiring rigid external Wikipedia exact matches.  
- **Edge Auto-Commit:** Inferred relationships are committed directly to disk with zero future confirmation recurrence.  

### Non-Destructive Reverse Location Engine
- **Multi-Stem Geographic Matching:** Evaluates inflected location names across both languages (*Austrálii*, *Austrália*, *Australia*).  
- **False-Positive Flora Guard:** Prevents tree-dwelling animals (*„stromový vačkovec“*) from being misclassified as plants, reliably confirming *Koala*, *Macropus*, and *Krokodíl morský* as Australian fauna.  
- **Standardized Traversal:** Direct attribute inspection standardized via `self.kg.get_attributes()`, preventing silent lookup failures.  

### InputParser5 & Token Guard Protection
- **Token Guard:** Drops inputs containing malicious characters (`@#$%^&*`) before runtime ingest.  
- **Trailing Punctuation Hygiene:** Strips trailing question marks via `.rstrip("?")`, guaranteeing that `CO JE MACROPUS?` cleanly resolves to node `macropus`.  
- **Compound Preservation:** Preserves multi-word noun phrases (`ovcia vlna`, `mobilny telefon`, `pevna linka`) in complete grammatical form.  
- **Copula Separation:** Strictly separates copula verbs (`je`, `sú`, `is`, `are`), preventing token concatenation and query corruption.  

### Contextual Domain Shield (`EnvoyNormalizer5`)
- **Non-Bio Domain Shield:** Strictly verifies ontological domains, barring technical, physical, formal, and architectural concepts (*ekológia*, *architektúra*, *fyzika*) from receiving biological habitat metadata.  
- **Sentence-Bound Extractor:** Requires the declarative presence of explicit occurrence verbs (*žije*, *obýva*, *lives*, *occurs*) within the exact sentence before allowing habitat relation binding.  

### Autonomous Disambiguation & Anti-Prefix Guard (`EnvoyExecutionLayer5`)
- **Disambiguation Triage:** Automatically detects Wikipedia disambiguation pages (*„môže byť...“*) and resolves specific context targets.  
- **Phonetic & Anti-Prefix Guard:** Eliminates prefix over-matching anomalies, permanently stopping query drift (*Káva* -> *Kavala*).  
- **Strip-Bracket Fallback:** Automatically attempts root lemma lookups when encountering unresolvable parenthetical articles.  
- **Endpoint Binding:** Directs requests strictly to `sk.wikipedia.org` or `en.wikipedia.org` based on caller context.  

---

# 🛡 5.9.1 4-Panel UI Suite, Terminal Decoupling & COLNÍK Guard (NEW)

A dedicated, decoupled browser interface running locally on port 8080 engineered to isolate host shells and protect system storage.

### COLNÍK Guard Shell Filter (TerminalAssistant)
- **Categorization Matrix:**  
  - **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs  
  - **RISKY (Explicit Prompt):** `rm`, `kill`, `taskkill`, `del`  
  - **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`  
- **Latency Profiling:** Every executed command is profiled via TimeCore `cycle_delta()`.  
- **Character Encoding Fallback:** Multi-stage shell decoding (UTF-8 -> CP1250 -> CP852 fallback) ensuring full diacritics integrity.  

### Terminal Decoupling Guard
- **Automatic State Reset:** Clearing input or finishing a conversational query automatically resets `currentModule = "none"`.  
- **Host Shell Isolation:** Conversational queries and entity searches cannot leak into the operating system terminal as executable shell commands.  
- **State Lock Prevention:** Guarantees the terminal panel never captures input focus in a locked, unresolvable state.  

### Duplicates Panel & Safe UI Trash (Human-in-the-Loop)
- **Safe UI Trash Pipeline:** File deletions (duplicates, empty folders, damaged files) route into quarantine storage; direct permanent removal is blocked without manual review via `GET /trash`.  
- **Hardware Telemetry:** Monitors host hardware telemetry via Guard.  
- **Report-Only Baseline:** Enforces strict **REPORT_ONLY** policies for detected duplicates, preventing unauthorized mass file deletions.  

### Triage Panel & Sliding-Window Quarantine
- **Quarantine Supervision:** Visual inspection queue of all quarantined files, unparsed web payloads, and held mutations (`COLNIK-6.x/triage`).  
- **Sliding-Window Rotation:** Enforces an automated 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`, pruning older records upon new arrivals to prevent disk bloat.  
- **Manual Clearance:** Manual release or disposal requires explicit OWNER authorization and confirmation.  

---

# 🛡 5.9.1 System Agent 5 – Hardened OS‑Level Gatekeeper

System Agent 5 is the final gatekeeper for all system-level operations under orchestrator supervision.

### Purpose
Ensure that **every host system action** is:

- non-destructive and verified safe  
- identity‑validated against active credentials  
- intercepted by COLNÍK Guard if matching forbidden patterns  
- routed to Safe Trash if attempting file deletion  
- reversible with automated rollback states  
- deterministic and auditable  
- explainable via proof trees  
- customs-validated by COLNIK-6.x  
- autonomy-supervised with zero recurrence  

### Security Guarantees (5.9.1 Upgrade)
- constant-time identity validation (O(1))  
- deep integration with `sirius_orchestrator.py` on port 8080 with embedded TerminalAssistant + TimeCore  
- 0.0s hard blocking of destructive commands via COLNÍK Guard  
- blocking of unverified process spawns or binary executions  
- ENVOY 5 outbound permission enforcement  
- `KG_EXPLAIN` & `KG_EXPLAIN_DEEP` derivation trees generated for all system decisions  
- **COLNIK‑validated OS‑level actions**  
- **AUTONOMY‑aware system validation**  

---

# 🛡 5.9.1 ENVOY 5 Quarantined Fetch Pipeline (UPDATED)

ENVOY 5 enforces an outbound-only, quarantined retrieval model with strict domain shielding, sliding-window limits, and zero local data leakage.

### Security Flow
**TOKEN GUARD → ASK → CONTEXT BIND (SK/EN) → PARSE (`InputParser5`) → DISAMBIGUATE (`ExecutionLayer5`) → FETCH → ROTATING QUARANTINE (100-File Limit) → SHIELD (`Normalizer5`) → CUSTOMS (`COLNIK-6.x`) → DUAL KG COMMIT (`autosave_kg.json` / `autosave_kg_en.json`)**

### Protections
- **Token Guard:** Drops malformed symbolic inputs (`@#$%^&*`) at entry.  
- **Punctuation Hygiene:** Strips trailing question marks (`.rstrip("?")`) to preserve pure entity identifiers.  
- **Confirmation State Latching:** Maintains pending proposal targets across turns, ensuring affirmative replies execute reliably.  
- **Sliding-Window Quarantine Rotation:** Automatically caps quarantine payloads to a maximum of 100 JSON records.  
- **Dual-Language Target Partition:** English queries persist to `autosave_kg_en.json`; Slovak queries persist to `autosave_kg.json`.  
- **Outbound-Only:** Strictly zero inbound listening ports; main runtime never binds to public network sockets.  
- **Quarantine Sandbox:** Strips all active scripts, trackers, cookies, HTML markup, and executable objects.  
- **Zero Local Leakage:** Local files, memory dumps, and conversation histories are never transmitted.  
- **Zero Recurrence:** Confirmed entities and deduced taxonomies are stored permanently, eliminating repeated learning prompts.  
- **PanelAPI Confirmation:** Unindexed concepts mandate user approval via `[ÁNO/NIE]` / `[YES/NO]` confirmation.  
- **COLNIK Validation:** All parsed payloads pass through customs inspection before graph commitment.  

---

# 🛡 5.9.1 Password Vault 5.9.1 Security Model

- **AES-256-GCM** authenticated symmetric encryption with random 256-bit salts  
- **PBKDF2-HMAC-SHA256** key stretching (600,000+ iterations)  
- Token Guard input filter rejecting injection symbols (`@#$%^&*`)  
- COLNÍK Guard shell filtering on diagnostic commands (0.0s block on forbidden shell operations)  
- Human-in-the-Loop Safe Trash for old credential backups  
- OWNER-only write/delete access; FAMILY read-only for shared items; STRANGER blocked  
- compound service name preservation via `InputParser5` with trailing punctuation stripping  
- terminal state decoupling preventing secret strings from leaking to the host shell  
- explainability traces generated for all vault access attempts  
- **COLNIK‑validated vault operations (Standard & High-Performance IPC Mode)**  
- **PanelAPI confirmation gating (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching**  

---

# 🛡 5.9.1 Self‑Repair & Integrity Guard (UPDATED)

Self‑Repair Layer 5.8 integrates directly with Guard resource telemetry, dual graph partitions, and the security stack.

### Capabilities
- cryptographic checksum auditing of `autosave_kg.json`, `autosave_kg_en.json`, core manifests, and vault containers  
- detection of corrupted entity schemas or broken relation trees  
- automated reconstruction of damaged metadata from verified integrity seals  
- isolated shadow container creation during disk storage anomalies  
- deterministic repair suggestions dispatched directly to `COLNIK-6.x/triage`  
- `KG_EXPLAIN_DEEP` generation for all repair and rollback actions  

---

# 📄 Document Status

**Version:** 5.9.1 UNIFIED  
This document reflects the comprehensive security model of Runtime 5.9.1:

- Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)  
- Dual-Language Isolated Knowledge Stores (`autosave_kg.json` & `autosave_kg_en.json`)  
- Native Lossless KG Merge Engine (`kg merge <src> into <tgt>`)  
- Ontological & Taxonomical Category Deduction (`KG_VERIFY`)  
- Non-Destructive Reverse Location Engine with Anti-Flora Guard  
- Entry-Level Token Guard (`@#$%^&*` rejection)  
- COLNÍK Guard Shell Access Control (0.0s hard block on forbidden commands)  
- Human-in-the-Loop Safe UI Trash Pipeline (`GET /trash`)  
- Sliding-Window Quarantine Rotation (100-file ceiling)  
- Greedy Trailing Punctuation Stripping (`.rstrip("?")`) & Confirmation State Latching  
- Multi-Word Compound Preservation (`InputParser5`)  
- Autonomous Disambiguation & Anti-Prefix Guard (`EnvoyExecutionLayer5`)  
- Contextual Domain Shield & Sentence-Bound Extractor (`EnvoyNormalizer5`)  
- 4-Panel UI Suite with Terminal State Decoupling (`currentModule = "none"`)  
- PanelAPI interactive loops (`[ÁNO/NIE]` / `[YES/NO]`)  
- TimeCore Temporal Tracking (`cycle_delta()`) & Guard Resource Monitoring (CPU, RAM, Disk)  
- Security Family 5.x & Identity Engine 3.1  
- System Agent 5  
- Password Vault 5.9.1  
- Self‑Repair Layer 5.8  
- Hierarchical Proof Trees (`KG_EXPLAIN` & `KG_EXPLAIN_DEEP`)  
- **COLNIK‑6.x Enterprise Customs Decision Gate (Standard, High-Performance IPC Mode & COLNÍK Guard)**  
- **AUTONOMY 6.x (Control, Guard, Safe Trash & Triage Mode in `COLNIK-6.x/triage`)**
