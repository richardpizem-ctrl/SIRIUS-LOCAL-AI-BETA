# ⭐ 12. NEW IN VERSION 5.9.0 UNIFIED — Semantic Multi-Word Parsing, 4-Panel UI Suite, Multi-Alias KG & AUTONOMY‑Supervised Styleguide Expansion

Version 5.9.0 UNIFIED expands the original STYLEGUIDE with new architectural rules for:

- Single-Process Orchestrator (sirius_orchestrator.py on Port 8080)
- Multi-Word Semantic Engine (InputParser5 preserving compound noun phrases and copula verb separation)
- Autonomous Disambiguation Triage and Anti-Prefix Guard (EnvoyExecutionLayer5)
- Contextual Domain Shield and Sentence-Bound Habitat Extractor (EnvoyNormalizer5)
- Multi-Alias Knowledge Graph Persistence (autosave_kg.json) with Zero Proposal Recurrence
- 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with automatic currentModule = "none" state clearance)
- Terminal State Decoupling (preventing shell capture and command injection)
- Integrated High-Performance IPC Bridge eliminating file locking bottlenecks and socket contention
- PanelAPI interactive loops ([ÁNO/NIE] confirmation prompts)
- TimeCore Temporal Tracking and Guard Resource/Security Supervision (CPU, RAM, Disk)
- COLNIK‑6.x Enterprise Customs Decision Gate (Standard and High-Performance IPC Mode)
- AUTONOMY‑6.x Supervised Proposal/Confirmation Layer (Control, Guard and Triage Mode)
- System Agent 5 (Hardened OS‑Level Gatekeeper and Reversibility Enforcer)
- Reasoning Engine 5.9.0 and Proof Trees (KG_EXPLAIN + KG_EXPLAIN_DEEP)
- Self‑Repair Layer 5.8 (Cryptographic Hash Sealing and Shadow Baseline Restoration)

All previous rules remain valid. Version 5.9.0 UNIFIED adds mandatory norms for deterministic, explainable, single-process orchestrated, multi-word compound preserving, domain-shielded, multi-alias persistent, terminal-decoupled, and customs-validated architecture.

---

# 12.1 Core Principles (Expanded for 5.9.0 UNIFIED)

### NEW (5.9.0)
- All module interactions, web services, and execution streams must be managed centrally by the single-process daemon sirius_orchestrator.py on port 8080.
- Natural language concept extraction must preserve compound noun phrases (ovcia vlna, mobilny telefon) in full via InputParser5, strictly isolating Slovak copula verbs (je, sú).
- Knowledge Graph mutations must record both raw colloquial query terms and formal encyclopedic titles under a dual-key structure committed atomically to autosave_kg.json.
- Once confirmed via PanelAPI ([ÁNO/NIE]), subsequent queries for registered entities or aliases must resolve directly from graph memory in O(1) time without triggering redundant learning proposals (Zero Proposal Recurrence).
- Clearing terminal input or completing a query must immediately reset active context (currentModule = "none"), permanently isolating web UI input from host OS shell execution.
- External retrieval via ENVOY must autonomously resolve disambiguation structures ("môže byť...") and enforce the Anti-Prefix Guard to prevent query drift (Káva -> Kavala).
- External facts must clear the Non-Bio Domain Shield (EnvoyNormalizer5), strictly barring technical, physical, or abstract concepts from receiving biological habitat metadata.
- Duplicate file scans must enforce a strict REPORT_ONLY policy; destructive bulk deletions are barred.
- Host hardware telemetry (CPU, RAM, Disk) must be monitored asynchronously via Guard with less than 1% overhead.
- All mutations and workflows must clear the primitive ALLOW / DENY / TRIAGE decision matrix of COLNIK-6.x; unverified or malformed payloads must route to COLNIK-6.x/triage.

---

# 12.2 Naming Conventions (Expanded for 5.9.0 UNIFIED)

### NEW Reserved Names (5.9.0)
- SiriusOrchestratorDaemon
- InputParser5
- MultiWordCompoundExtractor
- CopulaVerbSeparator
- MultiAliasRegistry
- DualKeyMappingCore
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

These names are reserved and must not be used for unrelated modules.

---

# 12.3 File and Folder Structure (Expanded for 5.9.0 UNIFIED)

### NEW Folders and Locations (5.9.0)
/orchestrator
/orchestrator/server_8080
/runtime5/parsers/input_parser_5
/kg/multi_alias_core
/envoy_v5/disambiguation
/envoy_v5/anti_prefix_guard
/envoy_v5/domain_shields
/ui_suite_8080
/ui_suite_8080/duplicates_panel
/ui_suite_8080/triage_panel
/ui_suite_8080/navigation_panel
/ui_suite_8080/terminal_panel
/colnik_6_x/triage
/supervision/hardware_metrics
/security_family_v3_1/academic_bypass

### NEW Rules (5.9.0)
- Execution entry point is exclusively python sirius_orchestrator.py (spawns daemon and UI on port 8080).
- All inter-module communication must use memory-based IPC pipelines hosted within sirius_orchestrator.py, completely avoiding disk-based file locking contention.
- Terminal input clearing in terminal_panel must execute an explicit event dispatch setting currentModule = "none".
- autosave_kg.json must always be staged through temporary shadow files (autosave_kg.tmp) before atomic rename/commit.
- External web payload normalization must pass through NonBioDomainShield before reaching Knowledge Graph staging.
- Unverified proposals, parsing anomalies, or unclassified files must be quarantined inside COLNIK-6.x/triage for review in the Triage Panel.

---

# 12.4 Function Length and Modular Prechecks (Expanded for 5.9.0 UNIFIED)

### NEW (5.9.0)
OS-level, Knowledge Graph mutation, and external triage functions must be decomposed into explicit lifecycle phases:

- precheck_identity()
- precheck_semantic_compound_integrity()
- precheck_alias_registry_recurrence()
- precheck_non_bio_domain_shield()
- precheck_anti_prefix_drift()
- precheck_system_resource_state()
- precheck_terminal_decoupling_state()
- precheck_colnik_customs_clearance()
- precheck_panel_api_consent()
- execute_action()
- postcheck_atomic_kg_commit()
- postcheck_zero_recurrence_indexing()
- postcheck_terminal_state_reset()
- postcheck_reversibility_guarantee()
- postcheck_explainability_proof_tree()
- postcheck_guard_metric_stability()

Maximum length of any orchestration or execution function: 45 lines.

---

# 12.5 Comments and Documentation Standards (Expanded for 5.9.0 UNIFIED)

### NEW (5.9.0)
Code comments must explicitly document:

- Orchestrator routing path within port 8080 runloop.
- Compound noun phrase preservation logic (InputParser5).
- Why an entity was routed through dual-key multi-alias persistence.
- Confirmation that Zero Proposal Recurrence is preserved for the target entity.
- Disambiguation branch selection rationale ("môže byť...").
- Validation proof that Non-Bio Domain Shield cleared the payload.
- Terminal state reset verification (currentModule = "none").
- Guard hardware telemetry impact (CPU, RAM, Disk).
- COLNIK-6.x customs evaluation verdict (ALLOW / DENY / TRIAGE).
- KG_EXPLAIN_DEEP derivation node hierarchy.

---

# 12.6 Error Messages (Expanded for 5.9.0 UNIFIED)

### NEW (5.9.0)
- "Orchestrator daemon failed to bind port 8080 – port already in use or socket restricted."
- "InputParser5 error – copula verb concatenation detected; tokenization aborted."
- "Knowledge Graph error – dual-key mapping failed; multi-alias commit rejected."
- "Zero Recurrence violation – redundant proposal generated for indexed alias."
- "Disambiguation failed – Wikipedia disambiguation branch unresolved; fallback engaged."
- "Anti-Prefix Guard triggered – prefix drift detected; query target halted."
- "Non-Bio Domain Shield violation – biological habitat attribute rejected for non-biological concept."
- "Terminal state reset enforced – input decoupled; currentModule set to 'none'."
- "Duplicates Panel error – destructive operation attempted; REPORT_ONLY policy enforced."
- "Guard supervision alert – hardware resource threshold exceeded (> 1% CPU spike)."
- "COLNIK customs inspection failed – payload quarantined to COLNIK-6.x/triage."
- "PanelAPI consent required – novel entity proposal awaiting user [ÁNO/NIE] confirmation."

---

# 12.7 Security Rules in Code (Expanded for 5.9.0 UNIFIED)

### NEW (5.9.0)
- All execution must originate from sirius_orchestrator.py on local port 8080.
- Conversational natural language inputs must never be piped directly into OS shell execution environments.
- Every input clear or escape event in the web console must unconditionally assert currentModule = "none".
- No external data may be bound to Knowledge Graph entities without clearing EnvoyNormalizer5 domain filters.
- All file duplicate operations must default strictly to read-only reporting (REPORT_ONLY).
- Identity authorization must evaluate in constant time (O(1)) without background biometric tracking.
- Academic research queries must execute with zero restriction latency via Schoolwork Engine bypass rules.
- All Knowledge Graph disk writes must execute atomically to prevent autosave_kg.json corruption.
- COLNIK-6.x customs inspection must evaluate all mutations across Standard and High-Performance IPC modes.
- Novel learning proposals must gate through interactive PanelAPI ([ÁNO/NIE]) confirmation loops.

---

# 12.8 Testing Requirements (Expanded for 5.9.0 UNIFIED)

### NEW (5.9.0)
Semantic and Parsing tests must include:
- Compound noun phrase preservation tests (e.g., verifying ovcia vlna does not truncate to vlna).
- Slovak copula verb separation tests (e.g., asserting je, sú are completely isolated from entity tokens).
- Diacritic-aware normalization tests.

Multi-Alias and Knowledge Graph tests must include:
- Dual-key mapping tests in autosave_kg.json.
- Zero Proposal Recurrence tests (asserting confirmed entities never re-trigger learning proposals).
- Atomic write and shadow backup recovery tests.

Disambiguation and Domain Shield tests must include:
- Wikipedia disambiguation page triage tests ("môže byť...").
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
- COLNIK-6.x customs decision tests (ALLOW / DENY / TRIAGE).
- KG_EXPLAIN and KG_EXPLAIN_DEEP hierarchical proof-tree compilation tests.

---

# 12.9 Logging Rules (Expanded for 5.9.0 UNIFIED)

### NEW (5.9.0)
- Log single-process daemon state transitions asynchronously to avoid blocking the main runloop.
- Buffer Guard hardware metrics (CPU, RAM, Disk) in memory, writing telemetry summaries periodically.
- Never log sensitive user credentials, secret keys, or private identity profiles.
- Log natural language parsing steps as: TOKENIZED -> COPULA_ISOLATED -> COMPOUND_PRESERVED.
- Log external triage as: FETCHED -> DISAMBIGUATED -> QUARANTINED -> DOMAIN_SHIELDED -> CLEARED.
- Log Knowledge Graph mutations as: DUAL_KEY_MAPPED -> ZERO_RECURRENCE_VERIFIED -> ATOMIC_COMMITTED.
- Log terminal decoupling events as: INPUT_CLEARED -> MODULE_RELEASED (none).
- Log customs verdicts as: COLNIK_CLEARANCE (ALLOW / DENY / TRIAGE -> COLNIK-6.x/triage).

---

# 12.10 Module Boundaries (Expanded for 5.9.0 UNIFIED)

### NEW (5.9.0)
- sirius_orchestrator.py on Port 8080 is the exclusive runtime orchestrator and daemon host.
- InputParser5 is the exclusive parser for natural language compound noun extraction.
- autosave_kg.json is the exclusive atomic persistence target for the multi-alias Knowledge Graph.
- EnvoyNormalizer5 is the exclusive authority for Non-Bio Domain Shielding and sentence-bound extraction.
- terminal_panel on Port 8080 must strictly isolate user input and enforce currentModule = "none" decoupling.
- System Agent 5 is the exclusive validator of host OS actions and reversibility policies.
- Guard is the exclusive auditor of real-time hardware metrics (CPU, RAM, Disk).
- COLNIK‑6.x is the exclusive customs gate issuing ALLOW / DENY / TRIAGE verdicts.
- AUTONOMY‑6.x is the exclusive governance layer for proposals, enforcing Zero Proposal Recurrence.
- PanelAPI is the exclusive interface for interactive human confirmations ([ÁNO/NIE]).

---

# Document Status (Updated)

Version: 4.0.0 -> 4.2.0 -> 4.3.0 -> 4.4.0 PRO -> 4.5.0 PRO -> 5.0.0 UNIFIED -> 5.3.0 UNIFIED -> 5.5.0 UNIFIED -> 5.6.2 UNIFIED -> 5.7.0 UNIFIED -> 5.8 UNIFIED -> 5.9.0 UNIFIED  
This styleguide establishes the complete, mandatory engineering rules for deterministic, compound-preserving, multi-alias persistent, single-process orchestrated, terminal-decoupled, domain-shielded, and COLNIK‑validated architecture in Runtime 5.9.0 UNIFIED.
