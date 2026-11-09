# ⚙️ Automatic Input Triage Engine (AITE) — v6.0.1  
SIRIUS‑LOCAL‑AI Runtime 5.x — Dual-Language KG Architecture, Native Merge & Orchestrated Protection

AITE v6.0.1 is the latest production generation of the triage, routing, and semantic input processing layer engineered for the SIRIUS Runtime ecosystem.  
It serves as the mission-critical gateway that parses multi-word queries, isolates copula grammatical terms, performs strict trailing punctuation stripping, binds active queries to language-isolated Knowledge Graphs (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN), and directs deterministic module execution under the central supervision of `sirius_orchestrator.py` and the COLNÍK Guard layer.

AITE 6.0.1 is fully offline, deterministic, and natively synchronized across Runtime 5.x components and the embedded IPC Bridge daemon on port 8080.

---

# 🚀 MODULE STATUS — v6.0.1 (PRODUCTION & INTEGRATED)

AITE 6.0.1 is fully aligned with the unified Runtime 5.x production architecture:

- **Dual-Language Isolated Knowledge Stores:** Physical and logical partition across Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) graphs with dynamic language context switching.
- **Native Lossless KG Merge Engine:** Full runtime support for `kg merge <src> into <tgt>` with attribute retention and automatic alias mapping.
- **Taxonomical & Marsupial Inference (`KG_VERIFY`):** Hierarchical deduction recognizing sub-taxa (e.g., marsupials and macropods committed under mammals).
- **Non-Destructive Reverse Location Engine:** Multi-stem location parsing with anti-collision flora shielding protecting tree-dwelling fauna (e.g., *Koala*, *Macropus*).
- **Resilient Trailing Punctuation Stripping:** Greedy punctuation trimming (`.rstrip("?")`) preventing entity key mismatches.
- **Confirmation State Latching:** Deterministic proposal preservation ensuring `[ÁNO/NIE]` / `[YES/NO]` inputs never lose context.
- **Hard Token Guard:** Instant entry-level rejection of corrupted and malicious symbol sequences (`@#$%^&*`).
- **Envoy Sliding-Window Quarantine:** Automated rotation limiting log files to a maximum ceiling of 100 JSON records.
- **COLNÍK Guard Shell Validation:** 0.0s hard blocking of forbidden system routines (`format`, `diskpart`) alongside telemetric profiling via TimeCore `cycle_delta()`.
- **Safe UI Trash & Human-in-the-Loop (HitL):** Zero automated disk deletions; quarantine routing for user verification (tested in `dist_V6_CHECK`).
- **SafeRollback Integration:** Granular, module-level backup (`shutil.copytree`) and instant restoration (`shutil.rmtree`) for absolute crash and collision resilience.
- **Professor Validator Matrix:** Strict `PASS / WARN / REJECT` decision middleware governing all cognitive outputs.
- **Integrated IPC Bridge:** Single-process HTTP/OPTIONS server operating inside `sirius_orchestrator.py` on port 8080.

---

# 🔥 What’s New in v6.0.1

### Dual-Language Graph Binding (`autosave_kg.json` & `autosave_kg_en.json`)
- **Strict Linguistic Isolation:** Total runtime and filesystem segregation between the Slovak knowledge base (`autosave_kg.json`) and the English knowledge base (`autosave_kg_en.json`), preventing cross-lingual contamination, mixed summaries, and bilingual hallucinations.
- **Dynamic Context Dispatch:** `RuntimeCore` dynamically routes entity resolutions, attributes, relations, and atomic autosaves according to the active language flag received from the UI (`SK` / `EN`).

### Native Lossless Entity Merge (`kg merge`)
- **Direct Runtime Interceptor:** Integrated directly into `RuntimeCore` without external script invocations or brittle import paths.
- **Zero-Loss Attribute Relocation:** Migrates all properties, descriptions, and habitat definitions from the source node directly to the target node.
- **Automatic Alias Node Transition:** Source entities are preserved as lightweight alias nodes (`src -[alias]-> tgt`), maintaining bi-directional discovery.

### Ontological & Taxonomical Reasoning (`KG_VERIFY`)
- **Contextual Taxa Deduction:** Accurately deduces higher-order biological categories directly from summary records (e.g., recognizing that marsupials and macropods belong to mammals).
- **Persistent Edge Auto-Commit:** Once verified via Envoy or contextual extraction, taxonomical edges (`kangaroo -[is_a]-> mammal`, `macropus -[je]-> cicavec`) are committed to the active knowledge graph, resulting in zero proposal recurrence on subsequent queries.

### Resilient Question Interceptor & Punctuation Hygiene
- **Greedy Trailing Punctuation Stripping:** Sanitizes input strings by trimming trailing question marks and punctuation, preventing entity lookup failures (e.g., `CO JE MACROPUS?` cleanly resolves to node `macropus`).
- **Latching of Confirmation States:** Fallback workflows strictly maintain pending entity identifiers in memory, ensuring user confirmations (`ÁNO`, `ANO`, `YES`, `Y`) correctly trigger Envoy execution rather than encountering a detached state.

### Robust Reverse Habitat Querying (`_execute_reverse_location_query`)
- **Multi-Stem Regional Matching:** Supports inflected geographic terms across both languages (*Austrálii*, *Austrália*, *Australia*).
- **False-Positive Flora Guard:** Replaced naive substring lookups to prevent tree-dwelling animals (*„stromový vačkovec“*) from being discarded as plants. *Koala medvedíkovitá*, *Macropus*, and *Krokodíl morský* reliably resolve under Australian fauna.
- **Uniform Attribute Retrieval:** Standardized all graph iterations via `self.kg.get_attributes()`, preventing missed property detections.

### COLNÍK Guard & Token Hard Shield
- **Token Guard:** Immediate rejection of dangerous or corrupted inputs containing forbidden special characters (`@`, `#`, `$`, `%`, `^`, `&`, `*`) upon receiving `kg query` commands.
- **Quarantine Sliding Window:** Maintains storage integrity by enforcing a 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`, automatically pruning older JSON payloads upon new arrivals.
- **Command Access Control:** Enforces strict boundary verification for shell commands (blocking `format`, `rmdir /s`, `diskpart` in 0.0s).

---

# 1. Module Purpose

AITE 6.0.1 automatically determines:

- input category, structural layout, and trailing punctuation cleanup
- whether compound noun tokens form an indivisible semantic concept
- which language store (`autosave_kg.json` vs. `autosave_kg_en.json`) is bound to the transaction
- the canonical concept intended when processing disambiguations or alias structures
- whether a query represents a reverse habitat query (fauna/flora), a category verification (`is_a`), or a factual definition
- whether an incoming administrative command is permitted, risky, or forbidden by COLNÍK Guard
- whether an affirmative response (`ÁNO` / `YES`) maps to an active pending proposal
- whether non-destructive file disposal must be routed to the HitL Quarantine Trash rather than executing raw file deletion

Supported inputs:

- natural language text (single-word, compound phrases, questions with trailing punctuation)
- administrative KG instructions (`kg set`, `kg relate`, `kg delete`, `kg merge`)
- shell diagnostics and telemetric requests (`mem`, `ps`, `sys`)
- autonomy proposal confirmations (`ÁNO`, `ANO`, `NIE`, `YES`, `NO`)
- visual documents and structured data files

---

# 2. Module Functions

## 2.1 Input Recognition & Sanitization (Engine 6.0.1)
AITE 6.0.1 recognizes and normalizes:

- multi-word compound phrases (`mobilny telefon`, `ovcia vlna`)
- trailing question punctuation via `.rstrip("?")`
- linguistic context tags (`language: "SK"` or `"EN"`)
- structural command formats (`kg merge <src> into <tgt>`, `kg set entity.attr = val`)
- verification structures (`je <subjekt> <kategória>?` / `is <subject> <category>?`)
- reverse habitat questions (`čo žije v...`, `what animals live in...`)
- affirmative and negative tokens across both languages (`ÁNO`, `ANO`, `YES`, `NIE`, `NO`)

## 2.2 Semantic Routing & Isolation Logic
AITE 6.0.1 determines:

- binding to `self.kg_sk` or `self.kg_en` based on caller language headers
- alias pathfinding to canonical nodes with attribute inheritance
- taxonomical validation via relation traversal and text-record deduction
- non-destructive flora/fauna separation during habitat checks
- execution dispatch to `WorkflowEngine5`, `ReasoningEngine5`, or direct graph retrieval
- evaluation of system commands against the COLNÍK Guard policy table

## 2.3 Subsystem Integration Matrix

### InputParser5 & Token Guard
- executes entry-level token sanitization
- strips trailing question punctuation and normalizes accents
- isolates copula verbs (`je`, `sú`, `is`, `are`) from compound subjects

### RuntimeCore & Dual KnowledgeGraph
- dynamically points to `autosave_kg.json` (SK) or `autosave_kg_en.json` (EN)
- executes native `kg merge` operations and maintains canonical alias edges
- enforces atomic serialization during system shutdown and post-enrichment steps

### EnvoyExecutionLayer5, EnvoyNormalizer5 & Quarantine
- triggers Wikipedia extraction only upon user confirmation
- extracts clean declarative habitat indicators and assigns taxonomic links
- commits raw payloads to `COLNIK-6.x/envoy/quarantine/` with 100-file sliding-window pruning

### COLNÍK 6.x & TerminalAssistant
- validates console inputs and enforces the Human-in-the-Loop Safe Trash pipeline (tested in `dist_V6_CHECK`)
- records latency telemetries via TimeCore `cycle_delta()`

---

# 3. Module Architecture

## 3.1 Components (v6.0.1)

- **InputClassifier 6.0.1** — categorizes commands, queries, and multi-word compounds
- **TokenGuard 6.0.1** — blocks malformed or malicious symbolic payloads
- **LanguageContextRouter 6.0.1** — binds runtime instances to `kg_sk` or `kg_en`
- **PunctuationSanitizer 6.0.1** — strips trailing question marks to prevent entity fragmentation
- **TaxonomyReasoner 6.0.1** — deduces biological hierarchies (e.g., marsupials -> mammals)
- **ReverseHabitatEngine 6.0.1** — conducts robust multi-stem geographical queries
- **MergeInterceptor 6.0.1** — manages in-memory entity consolidation and alias formation
- **ConfirmationLatch 6.0.1** — tracks pending proposal states across interactive turns
- **COLNIKBridge 6.0.1** — coordinates terminal security and HitL quarantine deletion
- **QuarantineRotator 6.0.1** — enforces sliding-window ceiling limits on stored cache files

## 3.2 Processing Flow (v6.0.1)
```text
User Input via UI Panel / Web Client (Port 8080)
↓
 sirius_orchestrator.py IPC Bridge (Language Header: SK / EN)
↓
 Token Guard (Checks for forbidden special characters @#\$%^&*)
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
