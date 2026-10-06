# ⚙️ Automatic Input Triage Engine (AITE) — v5.9.1  
SIRIUS‑LOCAL‑AI Runtime 5.9.1 — Dual-Language KG Architecture, Native Merge & Orchestrated Protection

AITE v5.9.1 is the latest production generation of the triage, routing, and semantic input processing layer engineered for the SIRIUS Runtime ecosystem.  
It serves as the mission-critical gateway that parses multi-word queries, isolates copula grammatical terms, performs strict trailing punctuation stripping, binds active queries to language-isolated Knowledge Graphs (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN), and directs deterministic module execution under the central supervision of `sirius_orchestrator.py` and the COLNÍK Guard layer[cite: 1, 2, 3].

AITE 5.9.1 is fully offline, deterministic, and natively synchronized across Runtime 5.9.1 components and the embedded IPC Bridge daemon on port 8080[cite: 1, 3].

---

# 🚀 MODULE STATUS — v5.9.1 (PRODUCTION & INTEGRATED)

AITE 5.9.1 is fully aligned with the unified Runtime 5.9.1 production architecture:

- **Dual-Language Isolated Knowledge Stores:** Physical and logical partition across Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) graphs with dynamic language context switching.
- **Native Lossless KG Merge Engine:** Full runtime support for `kg merge <src> into <tgt>` with attribute retention and automatic alias mapping.
- **Taxonomical & Marsupial Inference (`KG_VERIFY`):** Hierarchical deduction recognizing sub-taxa (e.g., marsupials and macropods committed under mammals).
- **Non-Destructive Reverse Location Engine:** Multi-stem location parsing with anti-collision flora shielding protecting tree-dwelling fauna (e.g., *Koala*, *Macropus*)[cite: 1, 2].
- **Resilient Trailing Punctuation Stripping:** Greedy punctuation trimming (`.rstrip("?")`) preventing entity key mismatches[cite: 1, 2].
- **Confirmation State Latching:** Deterministic proposal preservation ensuring `[ÁNO/NIE]` / `[YES/NO]` inputs never lose context[cite: 1, 2].
- **Hard Token Guard:** Instant entry-level rejection of corrupted and malicious symbol sequences (`@#$%^&*`).
- **Envoy Sliding-Window Quarantine:** Automated rotation limiting log files to a maximum ceiling of 100 JSON records[cite: 2, 3].
- **COLNÍK Guard Shell Validation:** 0.0s hard blocking of forbidden system routines (`format`, `diskpart`) alongside telemetric profiling via TimeCore `cycle_delta()`[cite: 2, 3].
- **Safe UI Trash & Human-in-the-Loop (HitL):** Zero automated disk deletions; quarantine routing for user verification[cite: 2, 3].
- **Integrated IPC Bridge:** Single-process HTTP/OPTIONS server operating inside `sirius_orchestrator.py` on port 8080[cite: 1, 3].

---

# 🔥 What’s New in v5.9.1

### Dual-Language Graph Binding (`autosave_kg.json` & `autosave_kg_en.json`)
- **Strict Linguistic Isolation:** Total runtime and filesystem segregation between the Slovak knowledge base (`autosave_kg.json`) and the English knowledge base (`autosave_kg_en.json`), preventing cross-lingual contamination, mixed summaries, and bilingual hallucinations[cite: 1, 2].
- **Dynamic Context Dispatch:** `RuntimeCore` dynamically routes entity resolutions, attributes, relations, and atomic autosaves according to the active language flag received from the UI (`SK` / `EN`)[cite: 1, 2].

### Native Lossless Entity Merge (`kg merge`)
- **Direct Runtime Interceptor:** Integrated directly into `RuntimeCore` without external script invocations or brittle import paths[cite: 1, 2].
- **Zero-Loss Attribute Relocation:** Migrates all properties, descriptions, and habitat definitions from the source node directly to the target node[cite: 1, 2].
- **Automatic Alias Node Transition:** Source entities are preserved as lightweight alias nodes (`src -[alias]-> tgt`), maintaining bi-directional discovery[cite: 1, 2].

### Ontological & Taxonomical Reasoning (`KG_VERIFY`)
- **Contextual Taxa Deduction:** Accurately deduces higher-order biological categories directly from summary records (e.g., recognizing that marsupials and macropods belong to mammals)[cite: 1, 2].
- **Persistent Edge Auto-Commit:** Once verified via Envoy or contextual extraction, taxonomical edges (`kangaroo -[is_a]-> mammal`, `macropus -[je]-> cicavec`) are committed to the active knowledge graph, resulting in zero proposal recurrence on subsequent queries[cite: 1, 2].

### Resilient Question Interceptor & Punctuation Hygiene
- **Greedy Trailing Punctuation Stripping:** Sanitizes input strings by trimming trailing question marks and punctuation, preventing entity lookup failures (e.g., `CO JE MACROPUS?` cleanly resolves to node `macropus`)[cite: 1, 2].
- **Latching of Confirmation States:** Fallback workflows strictly maintain pending entity identifiers in memory, ensuring user confirmations (`ÁNO`, `ANO`, `YES`, `Y`) correctly trigger Envoy execution rather than encountering a detached state[cite: 1, 2].

### Robust Reverse Habitat Querying (`_execute_reverse_location_query`)
- **Multi-Stem Regional Matching:** Supports inflected geographic terms across both languages (*Austrálii*, *Austrália*, *Australia*)[cite: 1, 2].
- **False-Positive Flora Guard:** Replaced naive substring lookups to prevent tree-dwelling animals (*„stromový vačkovec“*) from being discarded as plants. *Koala medvedíkovitá*, *Macropus*, and *Krokodíl morský* reliably resolve under Australian fauna[cite: 1, 2].
- **Uniform Attribute Retrieval:** Standardized all graph iterations via `self.kg.get_attributes()`, preventing missed property detections[cite: 1, 2].

### COLNÍK Guard & Token Hard Shield
- **Token Guard:** Immediate rejection of dangerous or corrupted inputs containing forbidden special characters (`@`, `#`, `$`, `%`, `^`, `&`, `*`) upon receiving `kg query` commands[cite: 2, 3].
- **Quarantine Sliding Window:** Maintains storage integrity by enforcing a 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`, automatically pruning older JSON payloads upon new arrivals[cite: 2, 3].
- **Command Access Control:** Enforces strict boundary verification for shell commands (blocking `format`, `rmdir /s`, `diskpart` in 0.0s)[cite: 2, 3].

---

# 1. Module Purpose

AITE 5.9.1 automatically determines:

- input category, structural layout, and trailing punctuation cleanup[cite: 1, 2]
- whether compound noun tokens form an indivisible semantic concept[cite: 1]
- which language store (`autosave_kg.json` vs. `autosave_kg_en.json`) is bound to the transaction[cite: 1, 2]
- the canonical concept intended when processing disambiguations or alias structures[cite: 1, 2]
- whether a query represents a reverse habitat query (fauna/flora), a category verification (`is_a`), or a factual definition[cite: 1, 2]
- whether an incoming administrative command is permitted, risky, or forbidden by COLNÍK Guard[cite: 2, 3]
- whether an affirmative response (`ÁNO` / `YES`) maps to an active pending proposal[cite: 1, 2]
- whether non-destructive file disposal must be routed to the HitL Quarantine Trash rather than executing raw file deletion[cite: 2, 3]

Supported inputs:

- natural language text (single-word, compound phrases, questions with trailing punctuation)[cite: 1, 2]
- administrative KG instructions (`kg set`, `kg relate`, `kg delete`, `kg merge`)[cite: 1, 2]
- shell diagnostics and telemetric requests (`mem`, `ps`, `sys`)[cite: 2, 3]
- autonomy proposal confirmations (`ÁNO`, `ANO`, `NIE`, `YES`, `NO`)[cite: 1, 2]
- visual documents and structured data files[cite: 1]

---

# 2. Module Functions

## 2.1 Input Recognition & Sanitization (Engine 5.9.1)
AITE 5.9.1 recognizes and normalizes:

- multi-word compound phrases (`mobilny telefon`, `ovcia vlna`)[cite: 1]
- trailing question punctuation via `.rstrip("?")`[cite: 1, 2]
- linguistic context tags (`language: "SK"` or `"EN"`)[cite: 1, 2]
- structural command formats (`kg merge <src> into <tgt>`, `kg set entity.attr = val`)[cite: 1, 2]
- verification structures (`je <subjekt> <kategória>?` / `is <subject> <category>?`)[cite: 1, 2]
- reverse habitat questions (`čo žije v...`, `what animals live in...`)[cite: 1, 2]
- affirmative and negative tokens across both languages (`ÁNO`, `ANO`, `YES`, `NIE`, `NO`)[cite: 1, 2]

## 2.2 Semantic Routing & Isolation Logic
AITE 5.9.1 determines:

- binding to `self.kg_sk` or `self.kg_en` based on caller language headers[cite: 1, 2]
- alias pathfinding to canonical nodes with attribute inheritance[cite: 1, 2]
- taxonomical validation via relation traversal and text-record deduction[cite: 1, 2]
- non-destructive flora/fauna separation during habitat checks[cite: 1, 2]
- execution dispatch to `WorkflowEngine5`, `ReasoningEngine5`, or direct graph retrieval[cite: 1, 2]
- evaluation of system commands against the COLNÍK Guard policy table[cite: 2, 3]

## 2.3 Subsystem Integration Matrix

### InputParser5 & Token Guard
- executes entry-level token sanitization[cite: 2, 3]
- strips trailing question punctuation and normalizes accents[cite: 1, 2]
- isolates copula verbs (`je`, `sú`, `is`, `are`) from compound subjects[cite: 1]

### RuntimeCore & Dual KnowledgeGraph
- dynamically points to `autosave_kg.json` (SK) or `autosave_kg_en.json` (EN)[cite: 1, 2]
- executes native `kg merge` operations and maintains canonical alias edges[cite: 1, 2]
- enforces atomic serialization during system shutdown and post-enrichment steps[cite: 1, 2]

### EnvoyExecutionLayer5, EnvoyNormalizer5 & Quarantine
- triggers Wikipedia extraction only upon user confirmation[cite: 1, 2]
- extracts clean declarative habitat indicators and assigns taxonomic links[cite: 1, 2]
- commits raw payloads to `COLNIK-6.x/envoy/quarantine/` with 100-file sliding-window pruning[cite: 2, 3]

### COLNÍK 6.x & TerminalAssistant
- validates console inputs and enforces the Human-in-the-Loop Safe Trash pipeline[cite: 2, 3]
- records latency telemetries via TimeCore `cycle_delta()`[cite: 2, 3]

---

# 3. Module Architecture

## 3.1 Components (v5.9.1)

- **InputClassifier 5.9.1** — categorizes commands, queries, and multi-word compounds[cite: 1]
- **TokenGuard 5.9.1** — blocks malformed or malicious symbolic payloads[cite: 2, 3]
- **LanguageContextRouter 5.9.1** — binds runtime instances to `kg_sk` or `kg_en`[cite: 1, 2]
- **PunctuationSanitizer 5.9.1** — strips trailing question marks to prevent entity fragmentation[cite: 1, 2]
- **TaxonomyReasoner 5.9.1** — deduces biological hierarchies (e.g., marsupials -> mammals)[cite: 1, 2]
- **ReverseHabitatEngine 5.9.1** — conducts robust multi-stem geographical queries[cite: 1, 2]
- **MergeInterceptor 5.9.1** — manages in-memory entity consolidation and alias formation[cite: 1, 2]
- **ConfirmationLatch 5.9.1** — tracks pending proposal states across interactive turns[cite: 1, 2]
- **COLNIKBridge 5.9.1** — coordinates terminal security and HitL quarantine deletion[cite: 2, 3]
- **QuarantineRotator 5.9.1** — enforces sliding-window ceiling limits on stored cache files[cite: 2, 3]

## 3.2 Processing Flow (v5.9.1)
```text
User Input via UI Panel / Web Client (Port 8080)
↓
 sirius_orchestrator.py IPC Bridge (Language Header: SK / EN)
↓
 Token Guard (Checks for forbidden special characters @#$%^&*)
├─ [Malicious/Corrupted] ──> Reject with TOKEN_GUARD_BLOCK
↓
 Clean Input & Trailing Punctuation Stripping (.rstrip("?"))
↓
 Language Context Switch:
   • Language == "EN" ──> Bind self.kg = self.kg_en (autosave_kg_en.json)
   • Language == "SK" ──> Bind self.kg = self.kg_sk (autosave_kg.json)
↓
 AITE Intent Classification:
 ├─ [Confirmation: ÁNO / YES] ──> Resolve Active Latch ──> Envoy Enrich ──> Atomic Save
 ├─ [KG Mutation: kg merge / set / relate] ──> Execute Native In-Memory Logic ──> Save
 ├─ [Habitat Query: where does X live?] ──> Resolve Alias ──> Direct Habitat Return
 ├─ [Reverse Query: what animals live in Y?] ──> Multi-Stem Search (Anti-Flora Guard)
 ├─ [Verification: is X a Y?] ──> Taxonomical Check (e.g. Marsupial -> Mammal)
 └─ [Entity Lookup: what is X?] ──> Check Local Graph
      ├─ [Found in KG] ──> Output Clean Summary
      └─ [Missing from KG] ──> Latch Confirmation State ──> Dispatch [ÁNO/NIE] Prompt
