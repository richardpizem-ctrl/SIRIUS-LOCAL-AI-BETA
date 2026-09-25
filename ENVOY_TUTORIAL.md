# 🌐 SIRIUS ENVOY 5 — Tutorial & Concept Guide (Runtime 5.9.0 Unified)
### Safe External Retrieval & Autonomous Triage Layer for SIRIUS LOCAL AI (Semantic Multi-Word Parsing, Disambiguation Triage, 4-Panel UI Suite & Multi-Alias KG Persistence)

SIRIUS ENVOY 5 is an **isolated external-retrieval and semantic triage subsystem** that allows SIRIUS LOCAL AI to safely obtain, disambiguate, and structure information from external sources **without exposing the local AI runtime to open network communication or data leaks**.

This **v5.9.0 unified edition** reflects the upgraded Runtime 5.9.0 architecture, including:

- Unified Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)  
- Multi-Word Compound Parser (`InputParser5` preserving compound noun phrases)  
- Autonomous Disambiguation Triage & Strip-Bracket Fallback (`EnvoyExecutionLayer5`)  
- Anti-Prefix & Phonetic Guard (preventing erroneous fuzzy query shifts)  
- Contextual Domain Shield & Sentence-Bound Bio Extractor (`EnvoyNormalizer5`)  
- Multi-Alias Knowledge Graph Persistence (`RuntimeCore` writing to `autosave_kg.json`)  
- Zero Proposal Recurrence (suppressing duplicate learning prompts once confirmed)  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with deterministic state clearance)  
- Native High-Performance IPC Bridge eliminating file locking bottlenecks  
- PanelAPI interactive loops with [ÁNO/NIE] confirmation prompts  
- TimeCore temporal tracking & Guard security supervision (CPU, RAM, Disk)  
- COLNIK‑6.x Validation Layer (Standard & High-Performance IPC Mode)  
- AUTONOMY 6.x (Control, Guard & Triage Mode in `COLNIK-6.x/triage`)  
- KG_EXPLAIN & KG_EXPLAIN_DEEP (Hierarchical proof trees & XAI attribution)  
- Reasoning Engine 5.9.0 (Multi-hop, inheritance, transitivity, orbital rules)  

This document explains:

- what ENVOY is  
- why it exists  
- how multi-word semantic parsing and autonomous disambiguation triage work  
- how domain shielding blocks inaccurate cross-domain attributes  
- how the quarantine sandbox functions  
- how data flows safely into the local Knowledge Graph with multi-alias mapping  
- what ENVOY is strictly forbidden from doing  
- how ENVOY integrates with Runtime 5.9.0 Unified Architecture  

---

# 🧩 1. What Is SIRIUS ENVOY 5?

ENVOY is a **sandboxed retrieval and normalization pipeline** with a single purpose:

> **Execute outbound-only semantic queries, resolve disambiguation branches, filter domain-specific facts, pass all content through quarantine, and deliver clean, multi-alias knowledge to the offline SIRIUS runtime.**

The local SIRIUS runtime:

- never connects directly to open socket channels  
- never sends local files, personal data, or telemetry outward  
- never receives raw, unsanitized external payloads  
- never executes external scripts or uncontrolled code  

ENVOY acts as an **isolated, outbound-only semantic customs portal**, operating strictly under orchestrator supervision on port 8080 and requiring explicit confirmation via PanelAPI `[ÁNO/NIE]` prompts for unindexed concepts.

---

# 🛡 2. Why Does ENVOY Exist?

SIRIUS is a 100% offline-first symbolic AI.  
However, when the local Knowledge Graph lacks specific entities, manual data entry would be tedious.  
ENVOY allows the system to autonomously locate, disambiguate, and structure missing concepts:

- extracting compound definitions (`ovcia vlna`, `mobilny telefon`, `pevna linka`)  
- resolving encyclopedic disambiguation structures (*„môže byť...“*)  
- capturing structured attributes (descriptions, taxonomy, materials)  
- enriching Knowledge Graph entities without cloud dependencies  

### ENVOY guarantees:

- **external retrieval without exposing the local engine online**  
- **zero leakage of personal files, identity context, or conversations**  
- **contextual domain guarding** (blocking biological attributes on technological/abstract concepts)  
- **anti-prefix protection** (blocking drifts like *Káva* -> *Kavala*)  
- **zero proposal recurrence** (confirmed entities are indexed across aliases and never prompt the user again)  

---
User Query (e.g., "Čo je ovcia vlna?")
│
▼
[InputParser5] ────────► Preserves multi-word noun phrases & separates copula verbs
│
▼
[EnvoyPermissionLayer5] ► Audits identity, caller scope, and PanelAPI [ÁNO/NIE] confirmation
│
▼
[EnvoyExecutionLayer5] ─► Resolves disambiguation pages, applies Anti-Prefix Guard & Strip-Bracket Fallback
│
▼
[Quarantine Sandbox] ───► Strips HTML, scripts, trackers, and unverified binary objects
│
▼
[EnvoyNormalizer5] ─────► Enforces Non-Bio Domain Shield & sentence-bound habitat checks
│
▼
[COLNIK-6.x Customs] ───► Validates schema consistency, reversibility, and threat boundaries
│
▼
[RuntimeCore / KG] ─────► Multi-Alias commitment to autosave_kg.json (raw query + encyclopedic title)
## 3.1 InputParser5 (Semantic Multi-Word Extraction)
- extracts full noun phrases without dropping modifying adjectives (e.g., `ovcia vlna`)  
- isolates copula verbs (`je`, `sú`) from subject entities, preventing linguistic corruptions  
- provides normalized query tokens directly to the triage pipeline  

## 3.2 ENVOY Permission Layer 5
- checks identity profile (OWNER / FAMILY / STRANGER)  
- manages interactive learning proposals (`kg.learn_proposal`) via PanelAPI `[ÁNO/NIE]`  
- checks existing multi-alias registries: if an entity or alias already exists in `autosave_kg.json`, retrieval is bypassed to prevent redundant user prompts  
- interfaces with COLNIK‑6.x for outbound authorization  

## 3.3 Envoy Execution Layer 5 (Autonomous Disambiguation & Anti-Prefix Guard)
- **Autonomous Disambiguation Triage:** automatically detects Wikipedia disambiguation pages (*„môže byť...“*) and follows the precise contextual target (e.g., resolving `slon` into genus *Elephas*)  
- **Phonetic & Anti-Prefix Guard:** neutralizes overly aggressive prefix matching, stopping semantic query drift (e.g., preventing *Káva* from jumping to *Kavala*, or *Skript* to soap operas)  
- **Strip-Bracket Fallback:** automatically attempts root lemma lookups when encountering parenthetical subtitle pages that fail to resolve  

## 3.4 Quarantine Sandbox
- completely isolated execution perimeter  
- removes HTML, CSS, JavaScript, tracking beacons, and ads  
- extracts declarative sentences and factual bullet points  
- blocks binary payloads, executable scripts, and unknown media formats  
- emits provenance logs for auditability  

## 3.5 Envoy Normalizer 5 (Contextual Domain & Bio Filtering)
- **Non-Bio Domain Shield:** strictly checks taxonomy, barring abstract, formal, and technological concepts (*ekológia*, *architektúra*, *fyzika*) from receiving inaccurate geographic habitat attributes  
- **Sentence-Bound Extractor:** requires declarative presence of occurrence verbs (*žije*, *obýva*, *prirodzený výskyt*) within the exact sentence before binding habitat relations  

## 3.6 COLNIK‑6.x Validation Layer (Standard & IPC Mode)
- acts as the internal customs gatekeeper  
- inspects parsed KG mutations for structural integrity and cycle safety  
- validates that proposed additions adhere to Knowledge Graph schemas  
- routes suspicious or malformed records into `COLNIK-6.x/triage` for quarantine review  

## 3.7 RuntimeCore Multi-Alias Persistence
- indexes new knowledge simultaneously under:  
  1. the user's raw query term (`ovcia vlna`)  
  2. the normalized encyclopedic title (`Vlna (textil)`)  
- commits updates directly to `autosave_kg.json`  
- guarantees zero proposal recurrence: future queries for any stored alias resolve instantly from memory  

---

# 🔄 4. How ENVOY Works – Step by Step (Runtime 5.9.0)

## 1️⃣ User submits a query
User inputs via Web UI or Terminal: `ČO JE MOBILNÝ TELEFÓN?`

## 2️⃣ InputParser5 preserves compound structure
The parser identifies `mobilný telefón` as a single multi-word entity, strips punctuation, and isolates the copula verb.

## 3️⃣ Graph existence & alias verification
`RuntimeCore` checks `autosave_kg.json`. If missing, AUTONOMY generates a `kg.learn_proposal`.

## 4️⃣ PanelAPI interactive confirmation
The UI displays: `[NÁVRH] Chcete vyhľadať a naučiť sa entitu 'mobilný telefón'? [ÁNO/NIE]`.  
The user confirms with `ÁNO`.

## 5️⃣ Outbound fetch & disambiguation triage
ENVOY queries external reference sources:  
- checks if the response is an encyclopedic disambiguation index  
- resolves technical / practical sub-articles  
- verifies against phonetic prefix over-matching  

## 6️⃣ Quarantine sanitization
The raw payload is stripped of HTML markup, scripts, and tracking code in the quarantine sandbox.

## 7️⃣ Contextual domain normalization
`EnvoyNormalizer5` audits the text:  
- classifies `mobilný telefón` as technological/device  
- prevents false habitat or biological attribute assignment  
- extracts core functional descriptions and categories  

## 8️⃣ COLNIK-6.x customs clearance
COLNIK audits the structured graph nodes and relations, approving the commit.

## 9️⃣ Multi-Alias commit to `autosave_kg.json`
`RuntimeCore` records the entity under both `mobilny telefon` and its formal title, saving the graph atomically.

## 🔟 Immediate response & zero future prompts
The answer is rendered in the UI. Next time the user asks `Čo je mobilný telefón?`, the system responds instantly from memory without prompting.

---

# 🚫 5. What ENVOY Never Does

ENVOY is strictly forbidden from:

- transmitting local files, directory trees, or source code outward  
- exposing user conversations or personal identifiers  
- executing unverified scripts, downloaded code, or binaries  
- storing raw HTML, active web content, or cookies  
- modifying the Knowledge Graph without COLNIK-6.x verification  
- bypassing user confirmation loops (`[ÁNO/NIE]`) for unindexed concepts  
- triggering repetitive learning proposals for already indexed aliases  
- assigning geographic habitats to non-biological entities  
- drifting across unrelated topics via loose prefix matching  
- interacting directly with host terminal shells or executing OS commands  
- capturing input focus without releasing module state (`currentModule = "none"`)  

ENVOY is a **strictly bounded, outbound-only, quarantined semantic bridge**.

---

# 🧠 6. Knowledge Graph & Reasoning Integration

ENVOY directly enriches the unified Knowledge Graph platform:

- feeds structured facts into multi-hop symbolic reasoning rules (`MultiHopOrbitInferenceRule`, `DedicsnostVlastnostiRule`)  
- provides unambiguous entities for proof tree generation in `KG_EXPLAIN` and `KG_EXPLAIN_DEEP`  
- eliminates redundant external network calls via persistent multi-alias mapping  
- supplies sanitized domain definitions for offline academic and technical inquiries  

All external enrichment is permanently consolidated into **`autosave_kg.json`**, expanding the system's offline capability with every confirmed interaction.

---

# 🖥 7. Integration with the 4-Panel UI Suite

ENVOY operates in direct synchronization with the web dashboard on port 8080:

- **Triage Panel:** live visual tracking of quarantine items, unclassified entities, and parsing logs (`COLNIK-6.x/triage`)  
- **Duplicates Panel:** live resource auditing ensuring retrieval tasks do not cause memory or storage spikes  
- **Navigation Panel:** deterministic routing across Runtime Core, KG, Envoy, and Autonomy layers  
- **Terminal Panel:** complete input decoupling ensuring conversational questions never lock up the terminal or execute as host commands  

---

# 🔐 8. Security & Operational Guarantees

- **100% Offline-First Core:** The central reasoning engine never binds to external sockets.  
- **Compound Integrity:** Multi-word concepts are preserved and protected from fragmenting.  
- **Disambiguation Guard:** Encyclopedic index pages are traversed contextually to accurate targets.  
- **Domain Shielding:** Technical and abstract concepts cannot receive false biological properties.  
- **Zero Recurrence:** Confirmed knowledge is permanently accessible across multiple aliases without duplicate prompts.  
- **Deterministic Customs Inspection:** All graph mutations are authorized by COLNIK-6.x.  
- **Supervised Human Oversight:** Sensitive operations and learning tasks mandate PanelAPI `[ÁNO/NIE]` approval.  

---

# 📄 Document Status

**Version:** 5.9.0 (Semantic Multi-Word Parsing, Disambiguation Triage, 4-Panel UI Suite & Multi-Alias KG Persistence)  
This tutorial specifies the design, operational pipeline, and safety boundaries of SIRIUS ENVOY 5 within the unified Runtime 5.9.0 framework.
