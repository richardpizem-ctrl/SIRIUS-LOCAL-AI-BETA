# 📐 STYLEGUIDE – SIRIUS LOCAL AI (v5.9.1 UNIFIED)
### Mandatory Coding, Architecture, Security, Dual-Language KG & Quality Guidelines

This document defines the strict engineering guidelines, naming conventions, safety requirements, and architectural rules for all code written for **SIRIUS LOCAL AI**.

Version **5.9.1 UNIFIED** expands this styleguide with explicit rules for:
- Single-Process Orchestrator (sirius_orchestrator.py on Port 8080 with embedded TerminalAssistant + TimeCore)
- Dual-Language Isolated Knowledge Stores (autosave_kg.json for SK & autosave_kg_en.json for EN)
- Native Lossless Knowledge Graph Merge Engine (kg merge <src> into <tgt>)
- Ontological & Taxonomical Category Deduction (KG_VERIFY with persistent edge auto-commits)
- Non-Destructive Reverse Location Engine (_execute_reverse_location_query with False-Positive Flora Guard)
- Entry-Level Token Guard (hard rejection of malformed symbolic injection sequences @#$%^&*)
- Trailing Punctuation Hygiene (.rstrip("?")) preventing token lookup mismatch
- Confirmation State Latching preserving pending proposal targets across conversation turns
- COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like format and diskpart)
- Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction (GET /trash)
- Sliding-Window Quarantine Ceiling Rotation (100 JSON file maximum in COLNIK-6.x/envoy/quarantine/)
- Multi-Stage Character Encoding Fallback (UTF-8 -> CP1250 -> CP852 pipeline with zero diacritic corruption)
- Multi-Word Semantic Engine (InputParser5 compound phrase preservation & copula verb separation)
- Autonomous Disambiguation Triage and Anti-Prefix Guard (EnvoyExecutionLayer5)
- Contextual Domain Shield and Sentence-Bound Habitat Extractor (EnvoyNormalizer5)
- Permanent Elimination of Interactive Proposal Recurrence on Confirmed Knowledge
- 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with automatic currentModule = "none" state clearance)
- Terminal State Decoupling (preventing shell capture and command injection)
- Integrated High-Performance IPC Bridge eliminating file locking bottlenecks and socket contention
- PanelAPI interactive loops ([ÁNO/NIE] / [YES/NO] confirmation prompts)
- TimeCore Temporal Tracking (cycle_delta()) and Guard Resource/Security Supervision (CPU, RAM, Disk)
- COLNIK‑6.x Enterprise Customs Decision Gate (Standard, High-Performance IPC Mode & COLNÍK Guard)
- AUTONOMY‑6.x Supervised Proposal/Confirmation Layer (Control, Guard, Safe Trash & Triage Mode)
- System Agent 5 (Hardened OS‑Level Gatekeeper and Reversibility Enforcer)
- Reasoning Engine 5.9.1 and Proof Trees (KG_EXPLAIN + KG_EXPLAIN_DEEP)
- Self‑Repair Layer 5.8 (Cryptographic Hash Sealing, Dual KG Healing and Shadow Baseline Restoration)

---

# 12.1 Core Principles (Expanded for 5.9.1 UNIFIED)

- All module interactions, web services, and execution streams must be managed centrally by the single-process daemon sirius_orchestrator.py on port 8080 with embedded TerminalAssistant and TimeCore.
- Raw inputs must clear Token Guard immediately at runtime entry; any sequence containing forbidden characters (@, #, $, %, ^, &, *) must be rejected prior to tokenization.
- Query tokens must undergo greedy trailing punctuation stripping via .rstrip("?") to guarantee exact entity lookup matching (e.g., CO JE MACROPUS? -> macropus).
- Pending interactive proposal identifiers must be preserved in memory via Confirmation State Latching across conversation turns to ensure user approvals (ÁNO / YES) execute without losing target context.
- Knowledge Graph stores must maintain strict physical and logical isolation between Slovak (autosave_kg.json) and English (autosave_kg_en.json) partitions; cross-lingual merging or translation hallucination is prohibited.
- Entity consolidation must execute natively in-memory via kg merge <src> into <tgt> inside RuntimeCore, migrating all properties, summaries, and habitat data to <tgt> without data loss, and converting <src> into a persistent directional alias node (src -[alias]-> tgt).
- Taxonomical inferences (KG_VERIFY) must deduce higher-order biological categories directly from summary records (e.g., macropods -> mammals) and auto-commit edges directly to the active graph store with zero subsequent proposal recurrence.
- Reverse location queries (_execute_reverse_location_query) must implement multi-stem matching (Austrálii, Austrália, Australia), utilize standardized self.kg.get_attributes() traversal, and enforce the False-Positive Flora Guard to prevent tree-dwelling animals („stromový vačkovec“) from being misclassified as plants.
- Shell command execution through the terminal must be audited by COLNÍK Guard: forbidden commands (format, diskpart, rmdir /s, del /f /s /q c:, drop database) must be halted in 0.0s before OS process creation.
- File removal operations must route through the Human-in-the-Loop Safe Trash pipeline; direct unverified file unlinking is strictly prohibited, mandating user review via GET /trash.
- Quarantine log payloads in COLNIK-6.x/envoy/quarantine/ must be capped at a strict 100-file ceiling, automatically rotating and pruning the oldest records upon new arrivals.
- Shell output decoders must employ a multi-stage decoding pipeline (UTF-8 -> CP1250 -> CP852 fallback) to prevent diacritic character mangling.
- Natural language concept extraction must preserve compound noun phrases (ovcia vlna, mobilny telefon, pevna linka) in full via InputParser5, strictly isolating copula verbs (je, sú, is, are).
- Clearing terminal input or completing a query must immediately reset active context (currentModule = "none"), permanently isolating web UI input from host OS shell execution.
- External retrieval via ENVOY must dynamically bind to language-specific Wikipedia endpoints (sk.wikipedia.org vs. en.wikipedia.org), resolve disambiguation structures („môže byť...“), and enforce the Anti-Prefix Guard to prevent query drift (Káva -> Kavala).
- External facts must clear the Non-Bio Domain Shield (EnvoyNormalizer5), strictly barring technical, physical, or abstract concepts from receiving biological habitat metadata.
- Duplicate file scans must enforce a strict REPORT_ONLY policy; proposed removals must divert to the HitL Safe Trash quarantine.
- Host hardware telemetry (CPU, RAM, Disk) must be monitored asynchronously via Guard (< 1% overhead), with command latency profiled via TimeCore cycle_delta().
- All mutations, shell invocations, and workflows must clear the primitive ALLOW / DENY / TRIAGE decision matrix of COLNIK-6.x; unverified or malformed payloads must route to COLNIK-6.x/triage.

---

# 12.2 Naming Conventions (Expanded for 5.9.1 UNIFIED)

The following names are reserved and must strictly follow SIRIUS conventions:

- SiriusOrchestratorDaemon
- TerminalAssistant
- TimeCoreTelemetry
- TokenGuardSanitizer
- TrailingPunctuationSanitizer
- ConfirmationStateLatch
- DualLanguageStoreRouter
- NativeLosslessMergeEngine
- TaxonomicalCategoryDeductionEngine
- ReverseLocationReasoner
- FalsePositiveFloraGuard
- ColnikGuardShellFilter
- HumanInTheLoopSafeTrash
- QuarantineSlidingWindowRotator
- MultiStageEncodingFallback
- InputParser5
- MultiWordCompoundExtractor
- CopulaVerbSeparator
- MultiAliasRegistry
- ZeroRecurrenceGate
- DisambiguationTriager5
- AntiPrefixGuard
- StripBracketFallback
- NonBioDomainShield
- SentenceBoundHabitatExtractor
- TerminalDecouplingController
- FourPanelUiSuite
- DuplicatesReporter
- TriageQuarantineQueue
- GuardResourceSupervisor
- COLNIKCustomsGate6_x
- AutonomyGovernanceEngine6_x

---

# 12.3 File and Folder Structure (Expanded for 5.9.1 UNIFIED)

Directory hierarchy:

/orchestrator
/orchestrator/server_8080
/orchestrator/terminal_assistant
/runtime5/parsers/input_parser_5
/runtime5/token_guard
/runtime5/envoy_quarantine_5
/kg/dual_language_stores
/kg/merge_engine
/kg/taxonomical_reasoner
/kg/reverse_location_engine
/filesystem/safe_trash_quarantine
/envoy_v5/disambiguation
/envoy_v5/anti_prefix_guard
/envoy_v5/domain_shields
/colnik_6_x/colnik_guard
/colnik_6_x/triage
/colnik_6_x/envoy/quarantine
/ui_suite_8080
/ui_suite_8080/duplicates_panel
/ui_suite_8080/triage_panel
/ui_suite_8080/navigation_panel
/ui_suite_8080/terminal_panel
/supervision/hardware_metrics
/security_family_v3_1/academic_bypass

Rules:
- Execution entry point is exclusively python sirius_orchestrator.py (spawns daemon, embedded TerminalAssistant, and UI on port 8080).
- Dual-language Knowledge Graphs must persist separately into autosave_kg.json (SK) and autosave_kg_en.json (EN).
- All inter-module communication must use memory-based IPC pipelines hosted within sirius_orchestrator.py, completely avoiding disk-based file locking contention.
- Terminal input clearing in terminal_panel must execute an explicit event dispatch setting currentModule = "none".
- Shell commands executed via the terminal must pass through COLNÍK Guard before dispatch to host processes.
- File removal operations must divert files to /filesystem/safe_trash_quarantine awaiting manual review via GET /trash.
- Quarantine logs in COLNIK-6.x/envoy/quarantine/ must be capped at 100 JSON payloads via automated sliding-window pruning.
- Both autosave_kg.json and autosave_kg_en.json must be staged through temporary shadow files (*.tmp) before atomic rename/commit.
- External web payload normalization must pass through NonBioDomainShield before reaching Knowledge Graph staging.
- Unverified proposals, parsing anomalies, or unclassified files must be quarantined inside COLNIK-6.x/triage for review in the Triage Panel.

---

# 12.4 Function Length and Modular Prechecks (Expanded for 5.9.1 UNIFIED)

OS-level, Knowledge Graph mutation, shell execution, and external triage functions must be decomposed into explicit lifecycle phases:

- precheck_token_guard_symbols()
- precheck_trailing_punctuation_hygiene()
- precheck_confirmation_state_latch()
- precheck_identity()
- precheck_language_context_partition()
- precheck_colnik_guard_shell_command()
- precheck_safe_trash_quarantine_path()
- precheck_quarantine_window_ceiling()
- precheck_semantic_compound_integrity()
- precheck_alias_registry_recurrence()
- precheck_non_bio_domain_shield()
- precheck_anti_prefix_drift()
- precheck_system_resource_state()
- precheck_terminal_decoupling_state()
- precheck_colnik_customs_clearance()
- precheck_panel_api_consent()
- execute_action()
- postcheck_atomic_dual_kg_commit()
- postcheck_zero_recurrence_indexing()
- postcheck_terminal_state_reset()
- postcheck_reversibility_guarantee()
- postcheck_explainability_proof_tree()
- postcheck_guard_metric_stability()
- postcheck_timecore_latency_profile()

Maximum length of any orchestration or execution function: 45 lines.

---

# 12.5 Comments and Documentation Standards (Expanded for 5.9.1 UNIFIED)

Code comments must explicitly document:
- Token Guard character inspection logic rejecting @#$%^&*.
- Greedy trailing punctuation trimming (.rstrip("?")).
- Confirmation state latch binding and restoration across conversation turns.
- Active language graph binding (autosave_kg.json vs. autosave_kg_en.json).
- In-memory property migration and alias pointer binding logic (kg merge).
- Taxonomical category deduction and edge auto-commit proof (KG_VERIFY).
- Reverse location search logic, multi-stem array, and False-Positive Flora Guard filtering.
- COLNÍK Guard command inspection rule (FORBIDDEN / RISKY / ALLOWED).
- Human-in-the-Loop Safe Trash diversion and review endpoint binding (GET /trash).
- Sliding-window quarantine pruning logic enforcing the 100-record maximum.
- Multi-stage character decoding fallback route (UTF-8 -> CP1250 -> CP852).
- Terminal state reset verification (currentModule = "none").
- TimeCore execution latency profile (cycle_delta()) and Guard hardware telemetry impact.
- COLNIK-6.x customs evaluation verdict (ALLOW / DENY / TRIAGE).
- KG_EXPLAIN_DEEP derivation node hierarchy.

---

# 12.6 Error Messages (Expanded for 5.9.1 UNIFIED)

- "Token Guard violation – malformed or forbidden characters (@#$%^&*) detected; input rejected."
- "Confirmation state latch error – pending proposal context lost; re-prompting required."
- "COLNÍK Guard security block – forbidden shell routine intercepted in 0.0s; command halted."
- "Safe Trash enforcement – direct file deletion blocked; item diverted to quarantine (GET /trash)."
- "Quarantine ceiling exceeded – sliding window triggered; pruning oldest JSON payloads to 100 limit."
- "Dual-Language partition mismatch – entity mutation attempted across mismatched language store."
- "KG Merge error – source entity relocation failed; merge aborted to prevent attribute loss."
- "Taxonomical verification failed – inconsistent ontology path detected during category deduction."
- "Flora Guard alert – reverse location classification blocked animal entity from botanical grouping."
- "Orchestrator daemon failed to bind port 8080 – port already in use or socket restricted."
- "InputParser5 error – copula verb concatenation detected; tokenization aborted."
- "Knowledge Graph error – dual-key mapping failed; multi-alias commit rejected."
- "Zero Recurrence violation – redundant proposal generated for indexed alias or deduced category."
- "Disambiguation failed – Wikipedia disambiguation branch unresolved; fallback engaged."
- "Anti-Prefix Guard triggered – prefix drift detected; query target halted."
- "Non-Bio Domain Shield violation – biological habitat attribute rejected for non-biological concept."
- "Terminal state reset enforced – input decoupled; currentModule set to 'none'."
- "Duplicates Panel error – destructive operation attempted; REPORT_ONLY policy enforced."
- "Guard supervision alert – hardware resource threshold exceeded (> 1% CPU spike)."
- "COLNIK customs inspection failed – payload quarantined to COLNIK-6.x/triage."
- "PanelAPI consent required – novel entity proposal awaiting user [ÁNO/NIE] confirmation."

---

# 12.7 Security Rules in Code (Expanded for 5.9.1 UNIFIED)

- All execution must originate from sirius_orchestrator.py on local port 8080.
- Raw input strings must be validated by Token Guard before reaching parser or workflow layers.
- Destructive shell routines (format, diskpart, rmdir /s, etc.) must be halted in 0.0s via COLNÍK Guard.
- File removal operations must route into quarantine storage for manual review via GET /trash; direct permanent unlinking is prohibited.
- Conversational natural language inputs must never be piped directly into OS shell execution environments.
- Every input clear or escape event in the web console must unconditionally assert currentModule = "none".
- Slovak and English entities must never be merged into a single mixed knowledge graph.
- No external data may be bound to Knowledge Graph entities without clearing EnvoyNormalizer5 domain filters.
- All file duplicate operations must default strictly to read-only reporting (REPORT_ONLY).
- Identity authorization must evaluate in constant time (O(1)) without background biometric tracking.
- Academic research queries must execute with zero restriction latency via Schoolwork Engine bypass rules.
- Knowledge Graph disk writes must execute atomically to prevent storage corruption.
- COLNIK-6.x customs inspection must evaluate all mutations across Standard and High-Performance IPC modes.
- Novel learning proposals must gate through interactive PanelAPI ([ÁNO/NIE] / [YES/NO]) confirmation loops with state latching.

---

# 12.8 Testing Requirements (Expanded for 5.9.1 UNIFIED)

Input Sanitization and Hygiene tests must include:
- Token Guard tests (asserting strings with @#$%^&* are dropped immediately).
- Trailing punctuation stripping tests (asserting CO JE MACROPUS? resolves to macropus).
- Confirmation state latch tests (asserting ÁNO / YES confirms the latched proposal across turns).

Dual-Language and Merge tests must include:
- Isolated partition tests (asserting SK queries persist to autosave_kg.json and EN queries to autosave_kg_en.json).
- Native kg merge tests (asserting source properties relocate to target without loss, and source transitions to alias pointer).
- Taxonomical deduction tests (KG_VERIFY asserting macropods are classified as mammals with edge auto-commits).
- Reverse location search tests with False-Positive Flora Guard (asserting tree-dwelling animals are not categorized as flora).

Shell and System Security tests must include:
- COLNÍK Guard 0.0s hard blocking tests (asserting format, diskpart, rmdir /s halt with zero execution).
- Human-in-the-Loop Safe Trash tests (asserting deletions divert to quarantine awaiting GET /trash).
- Sliding-window quarantine rotation tests (asserting log file count never exceeds 100 JSON payloads).
- Character encoding fallback tests (asserting diacritics integrity across UTF-8, CP1250, CP852).

Semantic and Parsing tests must include:
- Compound noun phrase preservation tests (e.g., verifying ovcia vlna does not truncate to vlna).
- Copula verb separation tests (e.g., asserting je, sú, is, are are completely isolated from entity tokens).
- Diacritic-aware normalization tests.

Disambiguation and Domain Shield tests must include:
- Wikipedia disambiguation page triage tests („môže byť...“).
- Anti-Prefix Guard tests (asserting Káva does not resolve to Kavala).
- Strip-Bracket Fallback tests.
- Non-Bio Domain Shield tests (asserting habitat tags fail on abstract/technical entities).
- Sentence-Bound Extractor tests (asserting occurrence verbs are strictly required for habitat links).

UI Suite and Terminal tests must include:
- Port 8080 HTTP/WebSocket IPC connection stability tests.
- Terminal state decoupling tests (verifying currentModule = "none" triggers upon clearing input).
- Host shell isolation tests (verifying conversational queries cannot execute shell binaries).
- Duplicates Panel REPORT_ONLY non-destructive enforcement tests.
- Triage Panel quarantine queue release/delete tests.

Supervision and Customs tests must include:
- Guard hardware telemetry polling tests (< 1% CPU overhead).
- TimeCore execution latency profiling tests (cycle_delta()).
- COLNIK-6.x customs decision tests (ALLOW / DENY / TRIAGE).
- KG_EXPLAIN and KG_EXPLAIN_DEEP hierarchical proof-tree compilation tests.

---

# 12.9 Logging Rules (Expanded for 5.9.1 UNIFIED)

- Log single-process daemon state transitions asynchronously to avoid blocking the main runloop.
- Log execution latency deltas (cycle_delta()) alongside hardware metrics (CPU, RAM, Disk).
- Never log sensitive user credentials, secret keys, or private identity profiles.
- Log input sanitization steps as: TOKEN_GUARD_INSPECTED -> PUNCTUATION_STRIPPED -> COMPOUND_PRESERVED.
- Log shell command interventions as: COLNIK_GUARD_INTERCEPT (FORBIDDEN_BLOCKED_0_0S / RISKY_PROMPTED / ALLOWED).
- Log file disposals as: SAFE_TRASH_DIVERTED -> QUARANTINE_STAGED (GET /trash).
- Log quarantine rotation events as: QUARANTINE_ROTATION_TRIGGERED (Pruned down to 100 files).
- Log dual-language mutations as: LANGUAGE_CONTEXT_BOUND (SK / EN) -> DUAL_KEY_MAPPED -> ZERO_RECURRENCE_VERIFIED -> ATOMIC_COMMITTED.
- Log entity merges as: KG_MERGE_EXECUTED (<src> -> <tgt> with alias pointer).
- Log taxonomical deductions as: KG_VERIFY_DEDUCED (<sub_taxon> -> <category> auto-committed).
- Log terminal decoupling events as: INPUT_CLEARED -> MODULE_RELEASED (none).
- Log customs verdicts as: COLNIK_CLEARANCE (ALLOW / DENY / TRIAGE -> COLNIK-6.x/triage).

---

# 12.10 Module Boundaries (Expanded for 5.9.1 UNIFIED)

- sirius_orchestrator.py on Port 8080 with embedded TerminalAssistant and TimeCore is the exclusive runtime orchestrator and daemon host.
- TokenGuard is the exclusive validator for entry-level character sequence sanitization (@#$%^&*).
- COLNÍK Guard is the exclusive gatekeeper for shell command inspection and 0.0s hard blocking.
- HitL Safe Trash is the exclusive pipeline for non-destructive file removals awaiting manual approval (GET /trash).
- EnvoyQuarantine5 is the exclusive manager for enforcing the 100-file sliding-window quarantine ceiling.
- InputParser5 is the exclusive parser for natural language compound noun extraction and trailing punctuation stripping.
- autosave_kg.json (SK) and autosave_kg_en.json (EN) are the exclusive atomic persistence targets for the Knowledge Graph.
- RuntimeCore is the exclusive engine for native in-memory entity consolidation (kg merge).
- ReasoningEngine5.9.1 is the exclusive reasoner for taxonomical deduction (KG_VERIFY) and reverse location queries.
- EnvoyNormalizer5 is the exclusive authority for Non-Bio Domain Shielding and sentence-bound extraction.
- terminal_panel on Port 8080 must strictly isolate user input and enforce currentModule = "none" decoupling.
- System Agent 5 is the exclusive validator of host OS actions and reversibility policies.
- Guard is the exclusive auditor of real-time hardware metrics (CPU, RAM, Disk).
- COLNIK‑6.x is the exclusive customs gate issuing ALLOW / DENY / TRIAGE verdicts.
- AUTONOMY‑6.x is the exclusive governance layer for proposals, enforcing Zero Proposal Recurrence and confirmation state latching.
- PanelAPI is the exclusive interface for interactive human confirmations ([ÁNO/NIE] / [YES/NO]).

---

# Document Status (Updated)

Version: 4.0.0 -> 4.2.0 -> 4.3.0 -> 4.4.0 PRO -> 4.5.0 PRO -> 5.0.0 UNIFIED -> 5.3.0 UNIFIED -> 5.5.0 UNIFIED -> 5.6.2 UNIFIED -> 5.7.0 UNIFIED -> 5.8 UNIFIED -> 5.9.0 UNIFIED -> 5.9.1 UNIFIED  
This styleguide establishes the complete, mandatory engineering rules for deterministic, dual-language segregated, natively merged, taxonomically deduced, input-sanitized, shell-protected, terminal-decoupled, domain-shielded, and COLNIK‑validated architecture in Runtime 5.9.1 UNIFIED.
