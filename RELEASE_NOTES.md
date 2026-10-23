# 🟦 RELEASE NOTES – SIRIUS LOCAL AI v5.9.5 UNIFIED
### Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning, Pre-Processing Spellcheck, Professor Middleware Quality Gateway & Comprehensive Security Protocol
**Author & Architecture Lead:** Richard Pizem  

Version **5.9.5 UNIFIED** marks a decisive evolutionary milestone in the SIRIUS LOCAL AI runtime architecture.  
It solves fundamental challenges in cross-lingual knowledge contamination, introduces native in-memory entity consolidation (`kg merge`), deploys automated taxonomical category deduction (`KG_VERIFY`), enables robust reverse location querying with anti-flora protection, introduces an entry-level text pre-processing and spellcheck engine (`spellcheck_engine.py`), and implements the authoritative **Professor Middleware Layer** (`grammar_engine.py`, `professor_validator.py`, `professor_miner.py`) enforcing cognitive quality gating (`PASS / WARN / REJECT`).

The core architectural directive is strictly enforced:  
> **Runtime Core and symbolic reasoning mechanisms may retrieve or infer any fact from the Knowledge Graph, but the Professor Middleware Layer authoritatively determines whether the output is permitted to reach the UI or commit to persistent state.**

Building on the unified foundations of the **v5.9.x** series, this release introduces:

- **Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)**  
- **Dual-Language Isolated Knowledge Stores (`autosave_kg.json` for SK & `autosave_kg_en.json` for EN)**  
- **Pre-Processing & Spellcheck Layer (`spellcheck_engine.py` for diacritics and typo normalization)**  
- **Professor Middleware Layer (`grammar_engine.py`, `professor_validator.py`, `professor_miner.py`) with strict PASS / WARN / REJECT evaluation**  
- **Dynamic Language Context Dispatching (routing queries and external endpoints strictly based on UI language flag SK / EN)**  
- **Native Lossless KG Merge Engine (`kg merge <src> into <tgt>` directly in RuntimeCore)**  
- **Ontological & Taxonomical Category Deduction (`KG_VERIFY` with persistent edge auto-commits)**  
- **Non-Destructive Reverse Location Engine (`_execute_reverse_location_query` with anti-flora classification guard)**  
- **Greedy Trailing Punctuation Stripping (`.rstrip("?")`) preventing entity lookup mismatch**  
- **Confirmation State Latching preserving pending proposal targets across conversation turns**  
- **Entry-Level Token Guard blocking malicious character sequences (`@#$%^&*`)**  
- **Sliding-Window Quarantine Ceiling Rotation (100 JSON file maximum in `COLNIK-6.x/envoy/quarantine/`)**  
- **SafeRollback Crash Resilience (`safe_rollback.py` with granular `shutil.copytree` backups and instant rollback)**  
- **COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like `format` and `diskpart`)**  
- **Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction (`GET /trash`)**  
- **Multi-Word Semantic Engine (`InputParser5` preserving compound noun phrases)**  
- **Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)**  
- **Contextual Domain Shield & Bio Filtering (`EnvoyNormalizer5`)**  
- **Permanent Elimination of Interactive Proposal Recurrence on Confirmed Knowledge**  
- **4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)**  
- **Integrated High-Performance IPC Bridge eliminating file locking bottlenecks and socket contention**  
- **PanelAPI & Interactive `[ÁNO/NIE]` / `[YES/NO]` Confirmation Loops**  
- **TimeCore Temporal Tracking (`cycle_delta()`) & Guard Security/Metric Supervision (CPU, RAM, Disk)**  
- **COLNIK‑6.x Customs Decision Gate (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x (Control, Guard, Safe Trash & Triage Mode in `COLNIK-6.x/triage`)**  
- **Reasoning Engine 5.9.5 & Workflow Engine 5.9.5**  
- **Hierarchical Proof Trees in `KG_EXPLAIN` & `KG_EXPLAIN_DEEP` (XAI)**  

---

# 🚀 What’s New in v5.9.5 UNIFIED

## 🔥 1. Dual-Language Isolated KG Architecture (`autosave_kg.json` & `autosave_kg_en.json`)
Knowledge representation has been structurally segregated into dedicated linguistic domains.

- strict physical and logical partition: Slovak entities serialize into `autosave_kg.json`, while English entities persist into `autosave_kg_en.json`  
- eliminates cross-lingual contamination, mixed-language entity summaries, and hallucinated translation bridges  
- `RuntimeCore` performs dynamic context dispatching based on caller UI language parameters (`SK` / `EN`)  
- independent atomic dual autosaves triggered upon runtime exit or post-enrichment  

---

## 🔥 2. Pre-Processing Spellcheck & Diacritics Engine (`spellcheck_engine.py`)
Incoming natural language queries now pass through an automated spelling and accent normalization stage prior to graph ingestion.

- diacritic-insensitive entity resolution: queries submitted without accents (e.g., `urologia`) reliably match canonical nodes (e.g., `urológia`)  
- automatic typo correction and noise suppression preventing false misses in entity node traversal  
- sanitizes raw text prior to parsing without modifying semantic intent  

---

## 🔥 3. Professor Middleware Layer: Cognitive Quality Gateway
The foundational quality control bridge between Runtime Core and UI presentation.

- **Professor Cleaner (`grammar_engine.py`):**  
  - normalizes extracted triplets (`add_relation(source, relation, target)`)  
  - handles reflexive verbs and phrasal predicates (*sa zaoberá*, *zaoberá sa*, *deals with*, *focuses on*)  
  - isolates reflexive particles (*sa/si*) into relation edges instead of attaching them to entity subjects  
  - preserves essential conjunctions (*a*, *i*) in multi-word objects for Slovak while cleanly filtering English indefinite articles (*a*, *an*)  
- **Professor Validator (`professor_validator.py`):**  
  - **PASS:** 100% verified factual integrity; payload is released directly to the UI  
  - **WARN:** Facts meet baseline criteria but carry low confidence (`LOW_CONFIDENCE`); rendered with a distinct visual uncertainty indicator  
  - **REJECT:** Intercepts incomplete facts (`INCOMPLETE_FACTS`) or contradictory assertions (`CONTRADICTION`); blocks output rendering, returns structured error diagnostics, and routes payloads to quarantine  
- **Professor Summarizer (`professor_miner.py`):**  
  - synthesizes multi-node evidence into concise, human-readable summaries for UI Panel V2  

---

## 🔥 4. Native Lossless KG Merge Engine (`kg merge <src> into <tgt>`)
Entity consolidation is now built directly into the core runtime without external script invocations.

- relocates all node properties, descriptions, alternative summaries, and habitat metadata from source to target without data loss  
- converts `<source>` into a persistent alias node with a directional edge pointing directly to `<target>` (`src -[alias]-> tgt`)  
- supports bi-directional alias traversal, resolving future queries under either identifier instantly from memory  
- executes atomically within the active language store  

---

## 🔥 5. Ontological & Taxonomical Category Deduction (`KG_VERIFY`)
The symbolic reasoning layer deduces higher-order biological categories directly from stored text records.

- automatically recognizes biological sub-taxa (e.g., establishing that marsupials and macropods belong to mammals) without requiring rigid external Wikipedia matches  
- persistent edge auto-commit: verified relations (`kangaroo -[is_a]-> mammal`, `macropus -[je]-> cicavec`) are committed directly to disk  
- permanently suppresses repetitive proposal prompts (Zero Recurrence) for all inferred taxonomic links  

---

## 🔥 6. Non-Destructive Reverse Location Engine with Anti-Flora Guard
Reverse habitat querying reliably identifies regional fauna without misclassifications.

- multi-stem geographic matching handles inflected language variations seamlessly (*Austrálii*, *Austrália*, *Australia*)  
- False-Positive Flora Guard: eliminates naive substring collisions that previously classified tree-dwelling animals (*„stromový vačkovec“*) as flora  
- reliably indexes *Koala*, *Macropus*, and *Krokodíl morský* under Australian fauna  
- uniform attribute traversal standardized via `self.kg.get_attributes()`, preventing silent lookup failures  

---

## 🔥 7. Comprehensive Security Protocol: COLNÍK Guard & Safe UI Trash
Local host protection has been fortified with multi-tiered command and filesystem firewalls.

- **COLNÍK Guard Shell Interceptor:** 0.0s hard blocking of forbidden commands (`format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`), interactive prompt checks for risky commands, and safe execution for system telemetry (`mem`, `ps`, `sys`)  
- **Human-in-the-Loop Safe UI Trash:** direct unverified disk deletions are blocked; files flagged for removal route into quarantine storage and require explicit user review via `GET /trash`  
- **Token Guard Sanitization:** raw input is audited at runtime entry, instantly rejecting malformed symbolic injection sequences (`@#$%^&*`)  
- **Sliding-Window Quarantine Rotation:** automatically limits stored logs inside `COLNIK-6.x/envoy/quarantine/` to a strict 100-file ceiling by pruning oldest records upon new arrivals  
- **SafeRollback Crash Resilience:** granular module-level backups (`shutil.copytree`) and restorations (`shutil.rmtree`) guaranteeing state integrity across interrupted cycles  
- **Character Encoding Fallback:** multi-stage shell decoding (UTF-8 -> CP1250 -> CP852 fallback) ensuring full diacritics integrity  

---

## 🔥 8. Punctuation Hygiene & Confirmation State Latching
Interactive conversational stability is hardened against formatting noise and state drops.

- **Greedy Trailing Punctuation Stripping (`.rstrip("?")`):** guarantees that queries like `CO JE MACROPUS?` cleanly resolve to node `macropus` without key fragmentation  
- **Confirmation State Latching:** maintains pending entity proposal identifiers in memory across conversation turns, ensuring affirmative user inputs (`ÁNO` / `YES`) execute without detached states  

---

## 🔥 9. Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)
The orchestration runtime has been consolidated into a unified single-process architecture.

- embeds `TerminalAssistant` and `TimeCore` directly into `sirius_orchestrator.py` on port 8080  
- eliminates disk file-locking contention, race conditions, and external socket collisions  
- directly coordinates `InputParser5`, `RuntimeCore`, `COLNIK-6.x`, `AUTONOMY 6.x`, and the web suite  
- provides a single, deterministic execution loop across all modules  

---

## 🔥 10. Multi-Word Semantic Parsing (`InputParser5`)
Natural language concept extraction is now fully context- and modifier-preserving.

- native preservation of compound noun phrases (e.g., `ovcia vlna`, `mobilny telefon`, `pevna linka`) without truncating modifiers down to single words  
- strict isolation of copula verbs (`je`, `sú`, `is`, `are`) from subject entities, preventing linguistic concatenations  
- diacritic-aware normalization producing clean lookup tokens for graph traversal and web triage  
- linear-time grammatical tokenization without regex backtracking overhead  

---

## 🔥 11. Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)
Encyclopedic web enrichment now operates with autonomous branch intelligence and strict semantic boundaries.

- **Autonomous Disambiguation Triage:** automatically detects Wikipedia disambiguation pages (*„môže byť...“*) and follows the exact contextual branch  
- **Target Endpoint Isolation:** routes English queries strictly to `en.wikipedia.org` and Slovak queries strictly to `sk.wikipedia.org`  
- **Phonetic & Anti-Prefix Guard:** eliminates prefix over-matching anomalies, permanently stopping query drift (*Káva* -> *Kavala*)  
- **Strip-Bracket Fallback:** recovers automatically from missing parenthetical articles by querying base root lemmas  

---

## 🔥 12. Contextual Domain Shield & Bio Filtering (`EnvoyNormalizer5`)
Guarantees domain boundary integrity for external facts before Knowledge Graph insertion.

- **Non-Bio Domain Shield:** strictly bars abstract, technical, or formal disciplines (*ekológia*, *architektúra*, *fyzika*) from receiving inaccurate geographic habitat attributes  
- **Sentence-Bound Extractor:** requires declarative presence of explicit occurrence verbs (*žije*, *obýva*, *lives*, *occurs*) within the exact sentence before allowing habitat relation binding  
- prevents categorical property pollution across unrelated ontology branches  

---

## 🔥 13. 4-Panel UI Suite & Terminal State Decoupling
A unified, browser-based management console running locally on port 8080.

- **Duplicates Panel:** live resource auditing and safe duplicate file categorization enforcing `REPORT_ONLY` and routing deletions to HitL Safe Trash  
- **Triage Panel:** visual supervision of quarantine queues and unclassified payloads (`COLNIK-6.x/triage`)  
- **Navigation Panel:** deterministic module switching across Runtime, KG, Envoy, and Autonomy with real-time status telemetry  
- **Terminal Panel:** decoupled command line interface that automatically resets `currentModule = "none"` when clearing input, running shell commands through COLNÍK Guard security  

---

## 🔥 14. TimeCore & Guard Metric Supervision
System safety monitoring now tracks both temporal bounds and host hardware loads.

- TimeCore temporal tracking provides execution latency profiling via `cycle_delta()` and runloop heartbeat management  
- Guard supervision audits real-time CPU, RAM, and Disk metrics (< 1% monitoring overhead)  
- automated execution throttling and anomaly isolation during erratic resource spikes  
- structured, asynchronous telemetry logging for audit trails  

---

# 🧩 Additional Improvements in v5.9.5 UNIFIED

### ✔ Dual-language graph isolation (`autosave_kg.json` & `autosave_kg_en.json`)  
### ✔ Pre-processing spellcheck and diacritics normalization (`spellcheck_engine.py`)  
### ✔ Professor Middleware Layer (`grammar_engine.py`, `professor_validator.py`, `professor_miner.py`)  
### ✔ Strict cognitive validation matrix enforcing PASS / WARN / REJECT outputs  
### ✔ Native lossless entity merge engine (`kg merge <src> into <tgt>`)  
### ✔ Taxonomical category inference auto-commit (`KG_VERIFY`)  
### ✔ Non-destructive reverse habitat engine with False-Positive Flora Guard  
### ✔ Hard Token Guard entry-level sanitization rejecting `@#$%^&*`  
### ✔ COLNÍK Guard 0.0s hard blocking of forbidden commands (`format`, `diskpart`, `rmdir /s`)  
### ✔ Human-in-the-Loop Safe UI Trash pipeline with review via `GET /trash`  
### ✔ Sliding-window quarantine rotation enforcing 100-file ceiling  
### ✔ SafeRollback crash resilience engine (`safe_rollback.py`)  
### ✔ Trailing punctuation trimming (`.rstrip("?")`) and confirmation state latching  
### ✔ Multi-stage shell character decoding (UTF-8 -> CP1250 -> CP852 fallback)  
### ✔ Single-process daemon execution on port 8080 (`sirius_orchestrator.py`)  
### ✔ Terminal input decoupling (`currentModule = "none"`) preventing shell capture  
### ✔ Multi-word compound preservation in `InputParser5`  
### ✔ Autonomous disambiguation triage and Anti-Prefix Guard in `EnvoyExecutionLayer5`  
### ✔ Non-Bio Domain Shield blocking habitat leakage onto technical concepts  
### ✔ Zero repetitive proposal loops on confirmed knowledge  
### ✔ 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`)  

---

# ⚙ Execution
SIRIUS Runtime 5.9.5 is launched via the unified single-process orchestrator:

```bash
python src/sirius_orchestrator.py --port 8080
Access the interactive 4-Panel UI Suite via browser:
[http://127.0.0.1:8080](http://127.0.0.1:8080)
