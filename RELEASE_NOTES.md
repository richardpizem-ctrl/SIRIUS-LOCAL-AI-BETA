# 🟦 RELEASE NOTES – SIRIUS LOCAL AI v5.9.0 UNIFIED
### Semantic Multi-Word Parsing, Autonomous Disambiguation Triage, 4-Panel UI Suite & Multi-Alias KG Persistence

Version **5.9.0 UNIFIED** marks a decisive evolutionary milestone in the SIRIUS LOCAL AI runtime architecture.  
It solves fundamental challenges in natural language noun extraction, eliminates repetitive learning prompts via multi-alias persistence, introduces autonomous encyclopedic disambiguation with domain shielding, and deploys a fully decoupled 4-Panel UI Suite served over a native, single-process orchestrator daemon on port 8080.

Building on the unified foundations of **v5.8**, this release introduces:

- **Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)**  
- **Multi-Word Semantic Engine (`InputParser5` preserving compound noun phrases)**  
- **Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)**  
- **Contextual Domain Shield & Bio Filtering (`EnvoyNormalizer5`)**  
- **Multi-Alias Knowledge Graph Persistence (`autosave_kg.json`)**  
- **Permanent Elimination of Interactive Proposal Recurrence on Confirmed Knowledge**  
- **4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)**  
- **Integrated High-Performance IPC Bridge eliminating file locking bottlenecks and socket contention**  
- **PanelAPI & Interactive `[ÁNO/NIE]` Confirmation Loops**  
- **TimeCore Temporal Tracking & Guard Security/Metric Supervision (CPU, RAM, Disk)**  
- **COLNIK‑6.x Customs Decision Gate (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x (Control, Guard & Triage Mode in `COLNIK-6.x/triage`)**  
- **Reasoning Engine 5.9.0 & Workflow Engine 5.9.0**  
- **Hierarchical Proof Trees in `KG_EXPLAIN` & `KG_EXPLAIN_DEEP` (XAI)**  

---

# 🚀 What’s New in v5.9.0 UNIFIED

## 🔥 1. Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)
The orchestration runtime has been consolidated into a unified single-process architecture.

- runs an integrated local HTTP/WebSocket IPC daemon on port 8080  
- eliminates disk file-locking contention, race conditions, and external socket collisions  
- directly coordinates `InputParser5`, `RuntimeCore`, `COLNIK-6.x`, `AUTONOMY 6.x`, and the web suite  
- provides a single, deterministic execution loop across all modules  

---

## 🔥 2. Multi-Word Semantic Parsing (`InputParser5`)
Natural language concept extraction is now fully context- and modifier-preserving.

- native preservation of compound noun phrases (e.g., `ovcia vlna`, `mobilny telefon`, `pevna linka`) without truncating modifiers down to single words  
- strict isolation of copula verbs (`je`, `sú`) from subject entities, preventing linguistic concatenations (e.g., `jeovcia vlna`)  
- diacritic-aware normalization producing clean lookup tokens for graph traversal and web triage  
- linear-time grammatical tokenization without regex backtracking overhead  

---

## 🔥 3. Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)
Encyclopedic web enrichment now operates with autonomous branch intelligence and strict semantic boundaries.

- **Autonomous Disambiguation Triage:** automatically detects Wikipedia disambiguation pages (*„môže byť...“*) and follows the exact contextual branch (e.g., categorizing `slon` into genus *Elephas*)  
- **Phonetic & Anti-Prefix Guard:** eliminates prefix over-matching anomalies, permanently stopping query drift (*Káva* -> *Kavala* or *Skript* -> telenovelas)  
- **Strip-Bracket Fallback:** recovers automatically from missing parenthetical articles by querying base root lemmas  
- **Quarantine Sandbox:** strips all HTML markup, scripts, trackers, and unverified binaries before normalization  

---

## 🔥 4. Contextual Domain Shield & Bio Filtering (`EnvoyNormalizer5`)
Guarantees domain boundary integrity for external facts before Knowledge Graph insertion.

- **Non-Bio Domain Shield:** strictly bars abstract, technical, or formal disciplines (*ekológia*, *architektúra*, *fyzika*) from receiving inaccurate geographic habitat attributes  
- **Sentence-Bound Extractor:** requires declarative presence of explicit occurrence verbs (*žije*, *obýva*, *prirodzený výskyt*) within the exact sentence before allowing habitat relation binding  
- prevents categorical property pollution across unrelated ontology branches  

---

## 🔥 5. Multi-Alias KG Persistence & Zero Proposal Recurrence (`autosave_kg.json`)
The Knowledge Graph engine introduces dual-key indexing and permanent prompt suppression.

- **Dual-Key Commitment:** records newly acquired entities simultaneously under the user's raw query phrase (`ovcia vlna`) and the official encyclopedic title (`Vlna (textil)`)  
- **Atomic Serialization:** commits updates directly and atomically to `autosave_kg.json`  
- **Zero Proposal Recurrence:** once confirmed via `[ÁNO/NIE]`, subsequent requests for any registered alias resolve instantly from memory in O(1) without triggering repetitive learning prompts  

---

## 🔥 6. 4-Panel UI Suite & Terminal State Decoupling
A unified, browser-based management console running locally on port 8080.

- **Duplicates Panel:** live resource auditing and safe duplicate file categorization enforcing `REPORT_ONLY` to prevent data loss  
- **Triage Panel:** visual supervision of quarantine queues and unclassified payloads (`COLNIK-6.x/triage`)  
- **Navigation Panel:** deterministic module switching across Runtime, KG, Envoy, and Autonomy  
- **Terminal Panel:** decoupled command line interface that automatically resets `currentModule = "none"` when clearing input, permanently preventing conversational queries from locking the terminal or executing as host OS shell commands  

---

## 🔥 7. TimeCore & Guard Metric Supervision
System safety monitoring now tracks both temporal bounds and host hardware loads.

- TimeCore temporal tracking provides execution timeouts and runloop heartbeat management  
- Guard supervision audits real-time CPU, RAM, and Disk metrics (< 1% monitoring overhead)  
- automated execution throttling and anomaly isolation during erratic resource spikes  
- structured, asynchronous telemetry logging for audit trails  

---

## 🔥 8. COLNIK‑6.x Customs Decision Gate (Standard & High-Performance IPC Mode)
The final decision checkpoint operates with expanded domain verification.

- evaluates inputs across PermissionLayer5, PolicyEngine5, BehaviorFilter5, and EnvoyNormalizer5  
- native high-performance IPC synchronization with AUTONOMY 6.x  
- deterministic ALLOW / DENY / TRIAGE decision matrix  
- routes ambiguous or malformed payloads into `COLNIK-6.x/triage` for quarantine review  

---

## 🔥 9. AUTONOMY 6.x – Control, Guard & Triage Mode
Autonomous governance with active human-in-the-loop validation.

- generates structured learning proposals (`kg.learn_proposal`) for novel concepts  
- coordinates interactive confirmation prompts via `PanelAPI` (`[ÁNO/NIE]`)  
- enforces zero proposal recurrence on confirmed aliases  
- manages quarantine containment and isolation in `COLNIK-6.x/triage`  

---

## 🔥 10. Reasoning Engine 5.9.0 – Multi-Hop Symbolic Proof Trees
Auditable, deterministic symbolic deduction with zero probabilistic hallucination.

- multi-hop inference, orbital leaps, and taxonomic inheritance rules (`DedicsnostVlastnostiRule`, `TranzitivneRelacieRule`, `MultiHopOrbitInferenceRule`)  
- hierarchical ASCII and HTML proof-tree generation in `KG_EXPLAIN` & `KG_EXPLAIN_DEEP`  
- linear-time confidence scoring relative to derivation path depth  
- bounded recursion depths preventing cyclic graph traversal loops  

---

## 🔥 11. Security Family 5.x & Identity Engine 3.1
Household protections and academic priority.

- constant-time (O(1)) identity classification across OWNER, FAMILY, and STRANGER tiers  
- STRANGER lockdown mode immediately isolates terminal access upon unrecognized commands  
- Schoolwork Engine 5.8: academic queries bypass restrictions with zero delay  
- deterministic time-limit quotas tracked via TimeCore deltas  

---

## 🔥 12. Self‑Repair Layer 5.8 – Hash Sealing & Recovery
- continuous checksum auditing of core configuration files and `autosave_kg.json`  
- automated reconstruction of damaged metadata from verified integrity seals  
- isolated shadow vault fallback when disk storage anomalies are detected  
- deterministic repair suggestions dispatched directly to `COLNIK-6.x/triage`  

---

# 🧩 Additional Improvements in v5.9.0 UNIFIED

### ✔ Single-process daemon execution on port 8080 (`sirius_orchestrator.py`)  
### ✔ Terminal input decoupling (`currentModule = "none"`) preventing shell capture  
### ✔ Multi-word compound preservation in `InputParser5`  
### ✔ Wikipedia disambiguation handling (*„môže byť...“*) in `EnvoyExecutionLayer5`  
### ✔ Anti-prefix guard neutralizing query drifts (*Káva* -> *Kavala*)  
### ✔ Non-Bio Domain Shield blocking habitat leakage onto technical concepts  
### ✔ Multi-alias graph persistence with zero repetitive proposal loops  
### ✔ Real-time hardware telemetry monitoring in Guard (CPU, RAM, Disk)  
### ✔ 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`)  
### ✔ Cycle-safe orbital inference rules in `ReasoningEngine5.9.0`  
### ✔ Hierarchical proof-tree generation in `KG_EXPLAIN_DEEP`  
### ✔ High-Performance IPC synchronization between COLNIK-6.x and AUTONOMY 6.x  

---

# ⚙ Execution (IMPORTANT)
SIRIUS Runtime 5.9.0 is launched via the unified single-process orchestrator:

```bash
python sirius_orchestrator.py
Access the interactive 4-Panel UI Suite via browser:
[http://127.0.0.1:8080](http://127.0.0.1:8080)
