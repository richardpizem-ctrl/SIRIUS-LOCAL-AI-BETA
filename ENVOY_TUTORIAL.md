# 🌐 SIRIUS ENVOY 5 — Tutorial & Concept Guide (Runtime 5.9.5 Unified)
### Safe External Retrieval, Dual-Language KG Dispatch & Autonomous Triage Layer for SIRIUS LOCAL AI (Dual-Language KG Architecture, Lossless Entity Merge, Ontological Habitat Reasoning, SafeRollback Crash Resilience, Professor Validator Middleware & COLNÍK Guard Security Protocol)

SIRIUS ENVOY 5 is an isolated external-retrieval, language-contextual normalization, and semantic triage subsystem that allows SIRIUS LOCAL AI to safely obtain, disambiguate, and structure information from external sources without exposing the local AI runtime to open network communication or data leaks.

This v5.9.5 unified edition reflects the upgraded Runtime 5.9.5 architecture, including:

- Unified Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)  
- Dual-Language Isolated Knowledge Stores (`autosave_kg.json` for SK and `autosave_kg_en.json` for EN)  
- Dynamic Language Context Dispatching (routing requests and external endpoints strictly based on UI language flag SK / EN)  
- Native Lossless KG Merge Engine (`kg merge <src> into <tgt>` with full property migration and alias tracking)  
- Ontological & Taxonomical Category Deduction (`KG_VERIFY` automatically committing sub-taxa relations like marsupials -> mammals)  
- Non-Destructive Reverse Location Engine (`_execute_reverse_location_query` with anti-flora classification guards)  
- Greedy Trailing Punctuation Stripping (`.rstrip("?")`) preventing entity matching fragmentation  
- Confirmation State Latching preserving pending proposal targets across conversation turns  
- Entry-Level Token Guard blocking malicious character sequences (`@#$%^&*`)  
- Automatic Sliding-Window Quarantine Rotation enforcing a 100-file ceiling  
- SafeRollback Crash Resilience (`safe_rollback.py` with granular `shutil.copytree` backups and `shutil.rmtree` restorations)  
- Professor Validator Middleware enforcing strict `PASS / WARN / REJECT` cognitive verification  
- COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like `format` and `diskpart`)  
- Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction  
- Multi-Word Compound Parser (`InputParser5` preserving compound noun phrases)  
- Autonomous Disambiguation Triage & Strip-Bracket Fallback (`EnvoyExecutionLayer5`)  
- Anti-Prefix & Phonetic Guard (preventing erroneous fuzzy query shifts)  
- Contextual Domain Shield & Sentence-Bound Bio Extractor (`EnvoyNormalizer5`)  
- Zero Proposal Recurrence (suppressing duplicate learning prompts once confirmed or deduced)  
- 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with deterministic state clearance)  
- PanelAPI interactive loops with `[ÁNO/NIE]` / `[YES/NO]` confirmation prompts  
- TimeCore temporal tracking (`cycle_delta()`) & Guard security supervision (CPU, RAM, Disk)  
- COLNIK‑6.x Validation Layer (Standard & High-Performance IPC Mode)  
- AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Trash Governance)  
- KG_EXPLAIN & KG_EXPLAIN_DEEP (Hierarchical proof trees & XAI attribution)  
- Reasoning Engine 5.9.5 (Multi-hop, inheritance, transitivity, orbital & taxonomical rules)  

This document explains:

- what ENVOY is  
- why it exists  
- how dual-language graph isolation routes external queries to the appropriate knowledge partition  
- how multi-word semantic parsing and autonomous disambiguation triage work  
- how domain shielding blocks inaccurate cross-domain attributes  
- how the quarantine sandbox functions under sliding-window limits  
- how data flows safely into the isolated Knowledge Graphs with multi-alias mapping  
- what ENVOY is strictly forbidden from doing  
- how ENVOY integrates with Runtime 5.9.5 Unified Architecture  

---

# 🧩 1. What Is SIRIUS ENVOY 5?

ENVOY is a sandboxed retrieval, language-aware normalization, and quarantine pipeline with a single purpose:

> Execute outbound-only semantic queries, bind to active language targets (SK/EN), resolve disambiguation branches, filter domain-specific facts, pass all content through quarantine under sliding-window limits, and deliver clean, isolated knowledge to the offline SIRIUS runtime.

The local SIRIUS runtime:

- never connects directly to open socket channels  
- never sends local files, personal data, or telemetry outward  
- never receives raw, unsanitized external payloads  
- never executes external scripts or uncontrolled code  

ENVOY acts as an isolated, outbound-only semantic customs portal, operating strictly under orchestrator supervision on port 8080 and requiring explicit confirmation via PanelAPI `[ÁNO/NIE]` / `[YES/NO]` prompts for unindexed concepts.

---

# 🛡 2. Why Does ENVOY Exist?

SIRIUS is a 100% offline-first symbolic AI.  
However, when the local Knowledge Graph lacks specific entities, manual data entry would be tedious.  
ENVOY allows the system to autonomously locate, disambiguate, and structure missing concepts into their respective language stores:

- extracting compound definitions (*ovcia vlna*, *mobilny telefon*, *pevna linka*)  
- binding queries to the correct linguistic domain (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN)  
- resolving encyclopedic disambiguation structures (*„môže byť...“*)  
- capturing structured attributes (descriptions, taxonomy, materials)  
- enriching Knowledge Graph entities without cloud dependencies  

### ENVOY guarantees:

- external retrieval without exposing the local engine online  
- strict separation between Slovak and English knowledge bases without cross-contamination  
- zero leakage of personal files, identity context, or conversations  
- contextual domain guarding (blocking biological attributes on technological/abstract concepts)  
- anti-prefix protection (blocking drifts like *Káva* -> *Kavala*)  
- zero proposal recurrence (confirmed entities and deduced taxonomies auto-commit to disk and never prompt the user again)  

---

```text
User Query (e.g., "CO JE MACROPUS?" / "MACROPUS" [Language: SK / EN])
│
▼
[Token Guard] ──────────► Rejects malformed symbolic inputs (@#$%^&*) at entry
│
▼
[InputParser5] ─────────► Trims trailing punctuation (.rstrip("?")), preserves noun phrases, isolates copula verbs
│
▼
[Language Context] ─────► Evaluates UI language flag (SK ──> kg_sk; EN ──> kg_en)
│
▼
[EnvoyPermissionLayer5] ─► Audits identity, checks confirmation latch, prompts [ÁNO/NIE] or [YES/NO]
│
▼
[EnvoyExecutionLayer5] ──► Targets Wikipedia API (sk.wikipedia.org or en.wikipedia.org), applies Anti-Prefix & Strip-Bracket guards
│
▼
[Quarantine Sandbox] ────► Saves raw JSON to COLNIK-6.x/envoy/quarantine/ with 100-file sliding-window rotation
│
▼
[EnvoyNormalizer5] ──────► Enforces Non-Bio Domain Shield & sentence-bound habitat extraction
│
▼
[COLNIK-6.x Customs] ────► Validates schema consistency, reversibility, and threat boundaries
│
▼
[RuntimeCore / KG] ──────► Atomic commit to designated store (autosave_kg.json or autosave_kg_en.json)
3.1 InputParser5 & Token Guard (Sanitization & Extraction)
performs entry-level sanitization, rejecting malformed injection strings (@#$%^&*)

trims trailing question marks (.rstrip("?")) to guarantee clean entity token resolution

extracts full noun phrases without dropping modifying adjectives (e.g., ovcia vlna)

isolates copula verbs (je, sú, is, are) from subject entities, preventing linguistic corruptions

3.2 ENVOY Permission Layer 5 & Confirmation Latching
checks identity profile (OWNER / FAMILY / STRANGER)

maintains confirmation state latching in memory so affirmative replies (ÁNO, ANO, YES, Y) cleanly execute pending requests

checks existing language graphs: if an entity or alias already exists in autosave_kg.json (SK) or autosave_kg_en.json (EN), retrieval is bypassed to prevent redundant user prompts

interfaces with COLNIK‑6.x for outbound authorization

3.3 Envoy Execution Layer 5 (Autonomous Disambiguation & Anti-Prefix Guard)
Autonomous Disambiguation Triage: automatically detects Wikipedia disambiguation pages („môže byť...“) and follows the precise contextual target

Phonetic & Anti-Prefix Guard: neutralizes overly aggressive prefix matching, stopping semantic query drift (e.g., preventing Káva from jumping to Kavala, or Skript to soap operas)

Strip-Bracket Fallback: automatically attempts root lemma lookups when encountering parenthetical subtitle pages that fail to resolve

Target Endpoint Isolation: routes English queries strictly to en.wikipedia.org and Slovak queries strictly to sk.wikipedia.org

4. Quarantine Sandbox, Sliding-Window Rotation & SafeRollback (EnvoyQuarantine5 & SafeRollback)
completely isolated execution perimeter

stores raw extraction payloads in COLNIK-6.x/envoy/quarantine/

automatically applies sliding-window rotation: prunes the oldest files upon new arrivals to enforce a strict 100-record ceiling

supervises granular module-level backups (shutil.copytree) and instant restorations (shutil.rmtree) via safe_rollback.py

strips HTML, CSS, JavaScript, tracking beacons, and ads

extracts declarative sentences and factual bullet points

blocks binary payloads, executable scripts, and unknown media formats

3.5 Envoy Normalizer 5 (Contextual Domain & Bio Filtering)
Non-Bio Domain Shield: strictly checks taxonomy, barring abstract, formal, and technological concepts (ekológia, architektúra, fyzika) from receiving inaccurate geographic habitat attributes

Sentence-Bound Extractor: requires declarative presence of occurrence verbs (žije, obýva, lives, occurs) within the exact sentence before binding habitat relations

3.6 Professor Validator Middleware (professor_validator.py)
evaluates all cognitive outputs against strict PASS / WARN / REJECT decision matrices before UI presentation or graph commits

3.7 COLNIK‑6.x Validation Layer (Standard & IPC Mode)
acts as the internal customs gatekeeper

inspects parsed KG mutations for structural integrity and cycle safety

validates that proposed additions adhere to Knowledge Graph schemas

routes suspicious or malformed records into COLNIK-6.x/triage for quarantine review

3.8 RuntimeCore Dual-Graph Persistence & Lossless Merge
indexes new knowledge strictly into the active language store: autosave_kg.json (SK) or autosave_kg_en.json (EN)

supports native lossless merging (kg merge <src> into <tgt>), consolidating properties and creating alias edges

commits updates atomically to disk

guarantees zero proposal recurrence: future queries for any stored alias resolve instantly from memory

🔄 4. How ENVOY Works – Step by Step (Runtime 5.9.5)
1️⃣ User submits a query
User inputs via UI Panel: CO JE MACROPUS? (Language: SK) or MACROPUS (Language: EN).

2️⃣ InputParser5 & Token Guard sanitize input
Token Guard confirms absence of forbidden characters. InputParser5 trims trailing question marks (.rstrip("?")), resolving clean token macropus.

3️⃣ Context dispatch & graph verification
RuntimeCore checks the corresponding graph (autosave_kg.json for SK, autosave_kg_en.json for EN). If the entity exists but lacks detailed text or does not exist, AUTONOMY generates a proposal and latches the entity state in memory.

4️⃣ PanelAPI interactive confirmation
The UI displays: Entity 'Macropus' is in memory, but lacks details. Search via Envoy? [YES/NO] (or Slovak equivalent). The user confirms with ÁNO / YES.

5️⃣ Outbound fetch & disambiguation triage
ENVOY queries external reference sources (e.g., en.wikipedia.org for EN, sk.wikipedia.org for SK):

checks if the response is an encyclopedic disambiguation index

resolves technical / biological sub-articles

verifies against phonetic prefix over-matching

6️⃣ Quarantine sanitization, SafeRollback & sliding-window rotation
The raw payload is stored in COLNIK-6.x/envoy/quarantine/ (automatically rotated to ensure <= 100 JSON records) and stripped of HTML, scripts, and trackers, backed up securely via SafeRollback.

7️⃣ Contextual domain normalization & Professor Validator check
EnvoyNormalizer5 audits the text:

classifies Macropus as a biological/marsupial genus

extracts core factual summary, taxonomy, and habitat attributes

verifies output validity through Professor Validator (PASS / WARN / REJECT)

8️⃣ COLNIK-6.x customs clearance
COLNIK audits the structured graph nodes and relations, approving the commit.

9️⃣ Commit to designated language store
RuntimeCore records the entity and its attributes into autosave_kg.json or autosave_kg_en.json, executing an atomic serialization.

🔟 Immediate response & zero future prompts
The answer is rendered in the UI. Subsequent queries for Macropus in that language are served instantly from graph memory without confirmation prompts.

🚫 5. What ENVOY Never Does
ENVOY is strictly forbidden from:

mixing Slovak and English articles into a single shared graph

transmitting local files, directory trees, or source code outward

exposing user conversations or personal identifiers

executing unverified scripts, downloaded code, or binaries

storing raw HTML, active web content, or cookies

allowing quarantine storage in COLNIK-6.x/envoy/quarantine/ to exceed 100 files without sliding-window pruning

modifying the Knowledge Graph without COLNIK-6.x verification

bypassing user confirmation loops ([ÁNO/NIE] / [YES/NO]) for unindexed concepts

triggering repetitive learning proposals for already indexed aliases or deduced categories

assigning geographic habitats to non-biological entities

drifting across unrelated topics via loose prefix matching

interacting directly with host terminal shells or executing OS commands

capturing input focus without releasing module state (currentModule = "none")

ENVOY is a strictly bounded, outbound-only, quarantined semantic bridge.

🧠 6. Knowledge Graph & Reasoning Integration
ENVOY directly enriches the dual Knowledge Graph platform:

feeds structured facts into multi-hop symbolic reasoning rules (MultiHopOrbitInferenceRule, DedicsnostVlastnostiRule)

enables taxonomical category deduction (KG_VERIFY), allowing the system to deduce that marsupials/macropods belong to mammals and committing the relation directly to disk

provides unambiguous entities for proof tree generation in KG_EXPLAIN and KG_EXPLAIN_DEEP

eliminates redundant external network calls via persistent multi-alias mapping

supplies sanitized domain definitions for offline academic and technical inquiries

All external enrichment is permanently consolidated into autosave_kg.json (SK) or autosave_kg_en.json (EN), expanding the system's offline capability with every confirmed interaction.

🖥 7. Integration with the 4-Panel UI Suite
ENVOY operates in direct synchronization with the web dashboard on port 8080:

Triage Panel: live visual tracking of quarantine items, unclassified entities, and parsing logs (COLNIK-6.x/triage)

Duplicates Panel: live resource auditing ensuring retrieval tasks do not cause memory or storage spikes

Navigation Panel: deterministic module switching across Runtime Core, KG, Envoy, and Autonomy layers

Terminal Panel: complete input decoupling ensuring conversational questions never lock up the terminal or execute as host commands

🔐 8. Security & Operational Guarantees
100% Offline-First Core: The central reasoning engine never binds to external sockets.

Dual-Language Isolation: Independent knowledge files eliminate bilingual hallucinations and mixed responses.

Token Guard Security: Immediate rejection of malformed or malicious symbolic inputs.

Sliding-Window Quarantine: Strict 100-file ceiling maintained in quarantine storage.

SafeRollback Crash Resilience: Granular module-level backups and restorations protecting state integrity.

Professor Validator Verification: Strict cognitive output filtering (PASS / WARN / REJECT).

Confirmation Latching: State preservation prevents dropped confirmation responses.

Compound Integrity: Multi-word concepts are preserved and protected from fragmenting.

Disambiguation Guard: Encyclopedic index pages are traversed contextually to accurate targets.

Domain Shielding: Technical and abstract concepts cannot receive false biological properties.

Zero Recurrence: Confirmed knowledge is permanently accessible across multiple aliases without duplicate prompts.

Deterministic Customs Inspection: All graph mutations are authorized by COLNIK-6.x.

Supervised Human Oversight: Sensitive operations and learning tasks mandate PanelAPI [ÁNO/NIE] / [YES/NO] approval.

📄 Document Status
Version: 5.9.5 (Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning, SafeRollback, Professor Validator & Comprehensive Security Protocol)

This tutorial specifies the design, operational pipeline, and safety boundaries of SIRIUS ENVOY 5 within the unified Runtime 5.9.5 framework.
