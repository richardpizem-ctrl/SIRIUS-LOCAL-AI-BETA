# 🌐 SIRIUS ENVOY 5 — Tutorial & Concept Guide (Runtime 5.9.1 Unified)
### Safe External Retrieval, Dual-Language KG Dispatch & Autonomous Triage Layer for SIRIUS LOCAL AI (Dual-Language KG Architecture, Lossless Entity Merge, Ontological Habitat Reasoning & COLNÍK Guard Security Protocol)

SIRIUS ENVOY 5 is an isolated external-retrieval, language-contextual normalization, and semantic triage subsystem that allows SIRIUS LOCAL AI to safely obtain, disambiguate, and structure information from external sources without exposing the local AI runtime to open network communication or data leaks[cite: 1, 2].

This v5.9.1 unified edition reflects the upgraded Runtime 5.9.1 architecture, including:

- Unified Single-Process Orchestrator (sirius_orchestrator.py on Port 8080 with embedded TerminalAssistant + TimeCore)[cite: 1, 2]
- Dual-Language Isolated Knowledge Stores (autosave_kg.json for SK and autosave_kg_en.json for EN)[cite: 1, 2]
- Dynamic Language Context Dispatching (routing requests and external endpoints strictly based on UI language flag SK / EN)[cite: 1, 2]
- Native Lossless KG Merge Engine (kg merge <src> into <tgt> with full property migration and alias tracking)[cite: 1, 2]
- Ontological & Taxonomical Category Deduction (KG_VERIFY automatically committing sub-taxa relations like marsupials -> mammals)[cite: 1, 2]
- Non-Destructive Reverse Location Engine (_execute_reverse_location_query with anti-flora classification guards)[cite: 1, 2]
- Greedy Trailing Punctuation Stripping (.rstrip("?")) preventing entity matching fragmentation[cite: 1, 2]
- Confirmation State Latching preserving pending proposal targets across conversation turns[cite: 1, 2]
- Entry-Level Token Guard blocking malicious character sequences (@#$%^&*)[cite: 2]
- Automatic Sliding-Window Quarantine Rotation enforcing a 100-file ceiling[cite: 2]
- COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like format and diskpart)[cite: 2]
- Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction[cite: 2]
- Multi-Word Compound Parser (InputParser5 preserving compound noun phrases)[cite: 1]
- Autonomous Disambiguation Triage & Strip-Bracket Fallback (EnvoyExecutionLayer5)[cite: 1]
- Anti-Prefix & Phonetic Guard (preventing erroneous fuzzy query shifts)[cite: 1]
- Contextual Domain Shield & Sentence-Bound Bio Extractor (EnvoyNormalizer5)[cite: 1]
- Zero Proposal Recurrence (suppressing duplicate learning prompts once confirmed or deduced)[cite: 1, 2]
- 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with deterministic state clearance)[cite: 1]
- PanelAPI interactive loops with [ÁNO/NIE] / [YES/NO] confirmation prompts[cite: 1, 2]
- TimeCore temporal tracking (cycle_delta()) & Guard security supervision (CPU, RAM, Disk)[cite: 2]
- COLNIK‑6.x Validation Layer (Standard & High-Performance IPC Mode)[cite: 1]
- AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Trash Governance)[cite: 1, 2]
- KG_EXPLAIN & KG_EXPLAIN_DEEP (Hierarchical proof trees & XAI attribution)[cite: 1]
- Reasoning Engine 5.9.1 (Multi-hop, inheritance, transitivity, orbital & taxonomical rules)[cite: 1, 2]

This document explains:

- what ENVOY is[cite: 1]
- why it exists[cite: 1]
- how dual-language graph isolation routes external queries to the appropriate knowledge partition[cite: 1, 2]
- how multi-word semantic parsing and autonomous disambiguation triage work[cite: 1]
- how domain shielding blocks inaccurate cross-domain attributes[cite: 1]
- how the quarantine sandbox functions under sliding-window limits[cite: 2]
- how data flows safely into the isolated Knowledge Graphs with multi-alias mapping[cite: 1, 2]
- what ENVOY is strictly forbidden from doing[cite: 1]
- how ENVOY integrates with Runtime 5.9.1 Unified Architecture[cite: 1, 2]

---

# 🧩 1. What Is SIRIUS ENVOY 5?

ENVOY is a sandboxed retrieval, language-aware normalization, and quarantine pipeline with a single purpose[cite: 1, 2]:

> Execute outbound-only semantic queries, bind to active language targets (SK/EN), resolve disambiguation branches, filter domain-specific facts, pass all content through quarantine under sliding-window limits, and deliver clean, isolated knowledge to the offline SIRIUS runtime[cite: 1, 2].

The local SIRIUS runtime:

- never connects directly to open socket channels[cite: 1]
- never sends local files, personal data, or telemetry outward[cite: 1]
- never receives raw, unsanitized external payloads[cite: 1]
- never executes external scripts or uncontrolled code[cite: 1]

ENVOY acts as an isolated, outbound-only semantic customs portal, operating strictly under orchestrator supervision on port 8080 and requiring explicit confirmation via PanelAPI [ÁNO/NIE] / [YES/NO] prompts for unindexed concepts[cite: 1, 2].

---

# 🛡 2. Why Does ENVOY Exist?

SIRIUS is a 100% offline-first symbolic AI[cite: 1].  
However, when the local Knowledge Graph lacks specific entities, manual data entry would be tedious[cite: 1].  
ENVOY allows the system to autonomously locate, disambiguate, and structure missing concepts into their respective language stores[cite: 1, 2]:

- extracting compound definitions (ovcia vlna, mobilny telefon, pevna linka)[cite: 1]
- binding queries to the correct linguistic domain (autosave_kg.json for SK, autosave_kg_en.json for EN)[cite: 1, 2]
- resolving encyclopedic disambiguation structures („môže byť...“)[cite: 1]
- capturing structured attributes (descriptions, taxonomy, materials)[cite: 1]
- enriching Knowledge Graph entities without cloud dependencies[cite: 1]

### ENVOY guarantees:

- external retrieval without exposing the local engine online[cite: 1]
- strict separation between Slovak and English knowledge bases without cross-contamination[cite: 1, 2]
- zero leakage of personal files, identity context, or conversations[cite: 1]
- contextual domain guarding (blocking biological attributes on technological/abstract concepts)[cite: 1]
- anti-prefix protection (blocking drifts like Káva -> Kavala)[cite: 1]
- zero proposal recurrence (confirmed entities and deduced taxonomies auto-commit to disk and never prompt the user again)[cite: 1, 2]

---

User Query (e.g., "CO JE MACROPUS?" / "MACROPUS" [Language: SK / EN])
│
▼
[Token Guard] ──────────► Rejects malformed symbolic inputs (@#$%^&*) at entry[cite: 2]
│
▼
[InputParser5] ─────────► Trims trailing punctuation (.rstrip("?")), preserves noun phrases, isolates copula verbs[cite: 1, 2]
│
▼
[Language Context] ─────► Evaluates UI language flag (SK ──> kg_sk; EN ──> kg_en)[cite: 1, 2]
│
▼
[EnvoyPermissionLayer5] ─► Audits identity, checks confirmation latch, prompts [ÁNO/NIE] or [YES/NO][cite: 1, 2]
│
▼
[EnvoyExecutionLayer5] ──► Targets Wikipedia API (sk.wikipedia.org or en.wikipedia.org), applies Anti-Prefix & Strip-Bracket guards[cite: 1]
│
▼
[Quarantine Sandbox] ────► Saves raw JSON to COLNIK-6.x/envoy/quarantine/ with 100-file sliding-window rotation[cite: 2]
│
▼
[EnvoyNormalizer5] ──────► Enforces Non-Bio Domain Shield & sentence-bound habitat extraction[cite: 1]
│
▼
[COLNIK-6.x Customs] ────► Validates schema consistency, reversibility, and threat boundaries[cite: 1]
│
▼
[RuntimeCore / KG] ──────► Atomic commit to designated store (autosave_kg.json or autosave_kg_en.json)[cite: 1, 2]

---

## 3.1 InputParser5 & Token Guard (Sanitization & Extraction)
- performs entry-level sanitization, rejecting malformed injection strings (@#$%^&*)[cite: 2]
- trims trailing question marks (.rstrip("?")) to guarantee clean entity token resolution[cite: 1, 2]
- extracts full noun phrases without dropping modifying adjectives (e.g., ovcia vlna)[cite: 1]
- isolates copula verbs (je, sú, is, are) from subject entities, preventing linguistic corruptions[cite: 1]

## 3.2 ENVOY Permission Layer 5 & Confirmation Latching
- checks identity profile (OWNER / FAMILY / STRANGER)[cite: 1]
- maintains confirmation state latching in memory so affirmative replies (ÁNO, ANO, YES, Y) cleanly execute pending requests[cite: 1, 2]
- checks existing language graphs: if an entity or alias already exists in autosave_kg.json (SK) or autosave_kg_en.json (EN), retrieval is bypassed to prevent redundant user prompts[cite: 1, 2]
- interfaces with COLNIK‑6.x for outbound authorization[cite: 1]

## 3.3 Envoy Execution Layer 5 (Autonomous Disambiguation & Anti-Prefix Guard)
- Autonomous Disambiguation Triage: automatically detects Wikipedia disambiguation pages („môže byť...“) and follows the precise contextual target[cite: 1]
- Phonetic & Anti-Prefix Guard: neutralizes overly aggressive prefix matching, stopping semantic query drift (e.g., preventing Káva from jumping to Kavala, or Skript to soap operas)[cite: 1]
- Strip-Bracket Fallback: automatically attempts root lemma lookups when encountering parenthetical subtitle pages that fail to resolve[cite: 1]
- Target Endpoint Isolation: routes English queries strictly to en.wikipedia.org and Slovak queries strictly to sk.wikipedia.org[cite: 2]

## 3.4 Quarantine Sandbox & Sliding-Window Rotation (EnvoyQuarantine5)
- completely isolated execution perimeter[cite: 1]
- stores raw extraction payloads in COLNIK-6.x/envoy/quarantine/
- automatically applies sliding-window rotation: prunes the oldest files upon new arrivals to enforce a strict 100-record ceiling[cite: 2]
- strips HTML, CSS, JavaScript, tracking beacons, and ads[cite: 1]
- extracts declarative sentences and factual bullet points[cite: 1]
- blocks binary payloads, executable scripts, and unknown media formats[cite: 1]

## 3.5 Envoy Normalizer 5 (Contextual Domain & Bio Filtering)
- Non-Bio Domain Shield: strictly checks taxonomy, barring abstract, formal, and technological concepts (ekológia, architektúra, fyzika) from receiving inaccurate geographic habitat attributes[cite: 1]
- Sentence-Bound Extractor: requires declarative presence of occurrence verbs (žije, obýva, lives, occurs) within the exact sentence before binding habitat relations[cite: 1, 2]

## 3.6 COLNIK‑6.x Validation Layer (Standard & IPC Mode)
- acts as the internal customs gatekeeper[cite: 1]
- inspects parsed KG mutations for structural integrity and cycle safety[cite: 1]
- validates that proposed additions adhere to Knowledge Graph schemas[cite: 1]
- routes suspicious or malformed records into COLNIK-6.x/triage for quarantine review[cite: 1]

## 3.7 RuntimeCore Dual-Graph Persistence & Lossless Merge
- indexes new knowledge strictly into the active language store: autosave_kg.json (SK) or autosave_kg_en.json (EN)[cite: 1, 2]
- supports native lossless merging (kg merge <src> into <tgt>), consolidating properties and creating alias edges[cite: 1, 2]
- commits updates atomically to disk[cite: 1, 2]
- guarantees zero proposal recurrence: future queries for any stored alias resolve instantly from memory[cite: 1, 2]

---

# 🔄 4. How ENVOY Works – Step by Step (Runtime 5.9.1)

## 1️⃣ User submits a query
User inputs via UI Panel: CO JE MACROPUS? (Language: SK) or MACROPUS (Language: EN).

## 2️⃣ InputParser5 & Token Guard sanitize input
Token Guard confirms absence of forbidden characters[cite: 2]. InputParser5 trims trailing question marks (.rstrip("?")), resolving clean token macropus[cite: 1, 2].

## 3️⃣ Context dispatch & graph verification
RuntimeCore checks the corresponding graph (autosave_kg.json for SK, autosave_kg_en.json for EN)[cite: 1, 2]. If the entity exists but lacks detailed text or does not exist, AUTONOMY generates a proposal and latches the entity state in memory[cite: 1, 2].

## 4️⃣ PanelAPI interactive confirmation
The UI displays: Entity 'Macropus' is in memory, but lacks details. Search via Envoy? [YES/NO] (or Slovak equivalent). The user confirms with ÁNO / YES[cite: 2].

## 5️⃣ Outbound fetch & disambiguation triage
ENVOY queries external reference sources (e.g., en.wikipedia.org for EN, sk.wikipedia.org for SK):
- checks if the response is an encyclopedic disambiguation index[cite: 1]
- resolves technical / biological sub-articles[cite: 1]
- verifies against phonetic prefix over-matching[cite: 1]

## 6️⃣ Quarantine sanitization & sliding-window rotation
The raw payload is stored in COLNIK-6.x/envoy/quarantine/ (automatically rotated to ensure ≤ 100 JSON records) and stripped of HTML, scripts, and trackers[cite: 2].

## 7️⃣ Contextual domain normalization
EnvoyNormalizer5 audits the text:
- classifies Macropus as a biological/marsupial genus[cite: 1]
- extracts core factual summary, taxonomy, and habitat attributes[cite: 1]

## 8️⃣ COLNIK-6.x customs clearance
COLNIK audits the structured graph nodes and relations, approving the commit[cite: 1].

## 9️⃣ Commit to designated language store
RuntimeCore records the entity and its attributes into autosave_kg.json or autosave_kg_en.json, executing an atomic serialization[cite: 1, 2].

## 🔟 Immediate response & zero future prompts
The answer is rendered in the UI. Subsequent queries for Macropus in that language are served instantly from graph memory without confirmation prompts[cite: 1, 2].

---

# 🚫 5. What ENVOY Never Does

ENVOY is strictly forbidden from:

- mixing Slovak and English articles into a single shared graph[cite: 1, 2]
- transmitting local files, directory trees, or source code outward[cite: 1]
- exposing user conversations or personal identifiers[cite: 1]
- executing unverified scripts, downloaded code, or binaries[cite: 1]
- storing raw HTML, active web content, or cookies[cite: 1]
- allowing quarantine storage in COLNIK-6.x/envoy/quarantine/ to exceed 100 files without sliding-window pruning[cite: 2]
- modifying the Knowledge Graph without COLNIK-6.x verification[cite: 1]
- bypassing user confirmation loops ([ÁNO/NIE] / [YES/NO]) for unindexed concepts[cite: 1, 2]
- triggering repetitive learning proposals for already indexed aliases or deduced categories[cite: 1, 2]
- assigning geographic habitats to non-biological entities[cite: 1]
- drifting across unrelated topics via loose prefix matching[cite: 1]
- interacting directly with host terminal shells or executing OS commands[cite: 1]
- capturing input focus without releasing module state (currentModule = "none")[cite: 1]

ENVOY is a strictly bounded, outbound-only, quarantined semantic bridge[cite: 1].

---

# 🧠 6. Knowledge Graph & Reasoning Integration

ENVOY directly enriches the dual Knowledge Graph platform:

- feeds structured facts into multi-hop symbolic reasoning rules (MultiHopOrbitInferenceRule, DedicsnostVlastnostiRule)[cite: 1]
- enables taxonomical category deduction (KG_VERIFY), allowing the system to deduce that marsupials/macropods belong to mammals and committing the relation directly to disk[cite: 1, 2]
- provides unambiguous entities for proof tree generation in KG_EXPLAIN and KG_EXPLAIN_DEEP[cite: 1]
- eliminates redundant external network calls via persistent multi-alias mapping[cite: 1]
- supplies sanitized domain definitions for offline academic and technical inquiries[cite: 1]

All external enrichment is permanently consolidated into autosave_kg.json (SK) or autosave_kg_en.json (EN), expanding the system's offline capability with every confirmed interaction[cite: 1, 2].

---

# 🖥 7. Integration with the 4-Panel UI Suite

ENVOY operates in direct synchronization with the web dashboard on port 8080:

- Triage Panel: live visual tracking of quarantine items, unclassified entities, and parsing logs (COLNIK-6.x/triage)[cite: 1]
- Duplicates Panel: live resource auditing ensuring retrieval tasks do not cause memory or storage spikes[cite: 1]
- Navigation Panel: deterministic routing across Runtime Core, KG, Envoy, and Autonomy layers[cite: 1]
- Terminal Panel: complete input decoupling ensuring conversational questions never lock up the terminal or execute as host commands[cite: 1]

---

# 🔐 8. Security & Operational Guarantees

- 100% Offline-First Core: The central reasoning engine never binds to external sockets[cite: 1].
- Dual-Language Isolation: Independent knowledge files eliminate bilingual hallucinations and mixed responses[cite: 1, 2].
- Token Guard Security: Immediate rejection of malformed or malicious symbolic inputs[cite: 2].
- Sliding-Window Quarantine: Strict 100-file ceiling maintained in quarantine storage[cite: 2].
- Confirmation Latching: State preservation prevents dropped confirmation responses[cite: 1, 2].
- Compound Integrity: Multi-word concepts are preserved and protected from fragmenting[cite: 1].
- Disambiguation Guard: Encyclopedic index pages are traversed contextually to accurate targets[cite: 1].
- Domain Shielding: Technical and abstract concepts cannot receive false biological properties[cite: 1].
- Zero Recurrence: Confirmed knowledge is permanently accessible across multiple aliases without duplicate prompts[cite: 1, 2].
- Deterministic Customs Inspection: All graph mutations are authorized by COLNIK-6.x[cite: 1].
- Supervised Human Oversight: Sensitive operations and learning tasks mandate PanelAPI [ÁNO/NIE] / [YES/NO] approval[cite: 1, 2].

---

# 📄 Document Status

Version: 5.9.1 (Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & Comprehensive Security Protocol)[cite: 1, 2]  
This tutorial specifies the design, operational pipeline, and safety boundaries of SIRIUS ENVOY 5 within the unified Runtime 5.9.1 framework[cite: 1, 2].
