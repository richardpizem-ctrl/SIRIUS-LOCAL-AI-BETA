# 🚀 SIRIUS LOCAL AI 5.9.1  
### Enterprise‑Grade Symbolic Intelligence — Deterministic, Dual-Language KG, Native Lossless Merge, Ontological Habitat Reasoning, COLNÍK Guard Hardened, HitL Safe Trash, 4-Panel UI Suite, AUTONOMY‑Supervised

SIRIUS LOCAL AI 5.9.1 represents the premier generation of symbolic AI runtime engineered for enterprise and workstation environments where **absolute predictability, cryptographic security, linguistic integrity, complete transparency, human-in-the-loop oversight, and 100% offline isolation** are non-negotiable requirements.  
Unlike generative neural systems vulnerable to hallucinations, token mutilation, and unpredictable probabilistic drifts, SIRIUS operates on an **isolated Dual-Language Knowledge Graph architecture (`autosave_kg.json` for SK, `autosave_kg_en.json` for EN)**, a **native in-memory entity consolidation engine (`kg merge`)**, an **ontological & taxonomical category deduction reasoner (`KG_VERIFY`)**, a **non-destructive reverse location engine with anti-flora protection**, a **compound-preserving semantic engine (`InputParser5`) with greedy trailing punctuation hygiene (`.rstrip("?")`)**, an **entry-level Token Guard**, a **single-process orchestrator daemon (`sirius_orchestrator.py` on local port 8080 with embedded `TerminalAssistant` and `TimeCore`)**, a **COLNÍK Guard shell access controller with 0.0s hard blocking**, a **Human-in-the-Loop Safe UI Trash pipeline**, an **automated sliding-window quarantine rotator (100-file ceiling)**, an **autonomous encyclopedic disambiguation triager with contextual domain shielding (`EnvoyExecutionLayer5` / `EnvoyNormalizer5`)**, an **isolated 4-Panel UI Suite**, interactive **PanelAPI `[ÁNO/NIE]` / `[YES/NO]` confirmation loops with confirmation state latching**, hardware/security telemetry via **TimeCore (`cycle_delta()`) & Guard**, and a **customs-grade validation pipeline (COLNIK‑6.x)**.

This document provides a **comprehensive, enterprise-ready architectural overview** of the entire 5.9.1 platform.

---

# 🌐 Vision & Philosophy

Modern AI architectures behave like stochastic black boxes — deceptively capable yet structurally unaccountable, prone to semantic hallucination, and dependent on cloud transmission.  
SIRIUS completely rejects this paradigm.

Its non-negotiable foundational pillars:

- **Determinism** — Identical inputs yield identical deductions and execution paths, every single time ($O(1)$ to bounded polynomial complexity).  
- **Dual-Language Semantic Sovereignty** — Complete physical and logical partition across Slovak and English knowledge graphs, eliminating cross-lingual contamination and translation hallucinations.  
- **Native Lossless Entity Consolidation** — Direct in-memory property relocation and alias edge creation without data loss.  
- **Taxonomical & Habitat Soundness** — Biological sub-taxa deduction with edge auto-commits and reverse location matching protected by anti-flora classification guards.  
- **Multi-Word Semantic Integrity** — Preserves compound noun phrases in full; isolates copula verbs deterministically; strips trailing punctuation greedily.  
- **Multi-Tiered Local Protection** — Token Guard input sanitization, COLNÍK Guard 0.0s command blocking, Human-in-the-Loop Safe Trash, and sliding-window quarantine rotation.  
- **Confirmation State Latching** — State preservation across conversation turns ensures user confirmation prompts never drop execution context.  
- **Persistent Memory & Zero Recurrence** — Binds colloquial queries directly to canonical concepts; zero proposal recurrence once verified or deduced.  
- **Auditable Explainability (XAI)** — Every single inference, classification, and repair compiles a formal proof tree and evidence derivation chain.  
- **Terminal Isolation & Decoupling** — Interactive queries reset context to none upon clearance, ensuring zero host shell leakage.  
- **100% Offline Sovereignty** — Complete zero-cloud isolation; no external telemetry, tracking, or network dependency.  
- **Supervised Autonomy** — Orchestrated pipeline linking autonomous proposal governance with active human verification.  

SIRIUS is engineered for engineers, researchers, and enterprises that demand **verifiable control** over their intelligent infrastructure.

---

# 🧠 Dual-Language Isolated Knowledge Graph (KG) 5.9.1  
### The Core of Deterministic Intelligence & Zero Recurrence

The Knowledge Graph serves as the definitive semantic ontology of SIRIUS.  
In version 5.9.1, it organizes entities, attributes, relations, and orbital taxonomies within **independent, cycle-safe, schema-validated structures** serialized atomically to `autosave_kg.json` (SK) and `autosave_kg_en.json` (EN).

### Key Capabilities

- **Dual-Language Isolated Schema**  
  Maintains complete physical and logical partition between Slovak (`autosave_kg.json`) and English (`autosave_kg_en.json`) graphs. Dynamic context dispatching routes queries, node retrieval, attributes, and relations dynamically based on the active UI language flag (`SK` / `EN`), completely preventing bilingual query collisions, mixed summaries, and translation hallucinations.

- **Native Lossless Entity Merge (`kg merge <src> into <tgt>`)**  
  Built natively inside `RuntimeCore` without external scripts. Relocates all properties, descriptions, alternative summaries, and habitat data from source to target without data loss, while converting `<source>` into a persistent alias node with a directional edge pointing directly to `<target>` (`src -[alias]-> tgt`).

- **Ontological & Taxonomical Reasoning (`KG_VERIFY`)**  
  Deduces higher-order biological categories directly from summary records (recognizing that marsupials and macropods belong to mammals) and auto-commits verified relations directly to disk with zero confirmation recurrence.

- **Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`)**  
  Multi-stem regional matching (*Austrálii*, *Austrália*, *Australia*) combined with the False-Positive Flora Guard to ensure tree-dwelling animals (*„stromový vačkovec“*) are not misclassified as plants, reliably indexing *Koala*, *Macropus*, and *Krokodíl morský* under Australian fauna. Standardized attribute access via `self.kg.get_attributes()` eliminates silent lookup failures.

- **Multi-Alias Dual-Key Architecture**  
  Records newly verified knowledge simultaneously under the user's raw compound query (e.g., `ovcia vlna`) and the formal encyclopedic lemma (`Vlna (textil)`). Subsequent lookups for either key resolve instantly from memory in $O(1)$ time.

- **Permanent Proposal Recurrence Elimination**  
  Suppresses redundant AUTONOMY proposal loops. Once a concept, alias mapping, or taxonomical edge is confirmed, it never triggers an interactive re-learning prompt.

- **Compound-Phrase Entity Preservation & Punctuation Hygiene**  
  Natively ingests and indexes multi-word phrases extracted by `InputParser5` and applies greedy trailing punctuation stripping (`.rstrip("?")`), ensuring `CO JE MACROPUS?` cleanly matches node `macropus`.

- **Developer Comfort Commands**  
  Fast CLI shortcuts for manual inspection (`kg add entity`, `kg merge`, `kg verify`, `kg where`, `kg reverse location`, `kg switch language`, `kg list`, `kg search`, `kg debug stats`, `kg release`).

- **Atomic Dual Snapshot Persistence**  
  Guarantees zero file corruption through temporary shadow staging prior to committing updates independently to `autosave_kg.json` and `autosave_kg_en.json`.

---

# 🛡️ Enterprise Security Suite: COLNÍK Guard & HitL Safe Trash  
### Local Host Protection, Command Filtering & Quarantine Ceilings

Runtime 5.9.1 deploys a fortified multi-layered security matrix:

- **COLNÍK Guard Shell Interceptor (`TerminalAssistant`)**  
  - **FORBIDDEN (0.0s Hard Block):** Intercepts destructive commands (`format`, `diskpart`, `rmdir /s`, `del /f /s /q c:`, `drop database`, fork-bombs) in 0.0s before OS process creation.  
  - **RISKY (Explicit Prompt):** Prompts user confirmation for `rm`, `kill`, `taskkill`, `del`.  
  - **ALLOWED:** Safe execution for telemetry and operational inspection (`ps`, `top`, `mem`, `sys`, `grep`, `cat`, `ls`, `dir`, etc.).  
  - **Latency Profiling & Multi-Stage Decoding:** Profiles execution latency via TimeCore `cycle_delta()` and applies robust decoding fallback (UTF-8 -> CP1250 -> CP852) to guarantee diacritics integrity.

- **Human-in-the-Loop (HitL) Safe UI Trash**  
  Direct unverified disk deletions are blocked. Operations proposing file removal (duplicates, empty folders, damaged files) route into quarantine storage. Items remain securely held until explicit manual review and approval via `GET /trash`.

- **Token Guard Input Sanitization**  
  Audits raw input strings immediately at runtime threshold, instantly dropping requests containing dangerous character sequences (`@`, `#`, `$`, `%`, `^`, `&`, `*`).

- **Sliding-Window Quarantine Rotation (`EnvoyQuarantine5`)**  
  Monitors stored logs inside `COLNIK-6.x/envoy/quarantine/` and automatically prunes the oldest records upon new arrivals, strictly enforcing a 100-file ceiling.

---

# ⚙️ Reasoning Engine 5.9.1  
### Symbolic Multi-Hop Deduction with Bounded Derivation Trees

The Reasoning Engine performs deterministic deduction over the Knowledge Graph without neural approximations.

### Active Inference Rules

- **TaxonomicalCategoryDeductionRule (`KG_VERIFY`)** — Deduces class membership from relational and textual summaries (e.g., macropods -> mammals), committing edges directly to disk.  
- **MultiHopOrbitInferenceRule** — Traverses bounded orbital layers to uncover indirect relationships across disparate graph clusters.  
- **DedicsnostVlastnostiRule** — Propagates inherited attributes down class taxonomies while barring cross-domain leakage onto technical nodes.  
- **TranzitivneRelacieRule** — Verifies directed transitive equivalence chains, following directional alias links from native entity merges.  
- **AutoTypeInferenceRule** — Infers structural categorization dynamically based on verified attribute signatures.  

### Explainability Deliverables

Every deduction delivers:
- hierarchical ASCII & HTML proof trees  
- rule provenance tags and edge weights  
- confidence metrics calculated linearly relative to derivation depth  
- contextual attribution logs  

### COLNIK & AUTONOMY Integration

Reasoning outcomes feed directly into:
- AUTONOMY 6.x proposal governance and confirmation state latching  
- threat and risk classification matrices  
- interactive `[ÁNO/NIE]` / `[YES/NO]` gating loops  
- customs-validated payload delivery packets  

---

# 🔄 Single-Process Orchestration & Workflow Engine 5.9.1  
### Native Port 8080 Runloop & Terminal Decoupling

The Workflow Engine coordinates execution through a unified, single-process orchestrator daemon (`sirius_orchestrator.py`) hosting HTTP/WebSocket services on port 8080 with embedded `TerminalAssistant` and `TimeCore`:
User / Web UI / Shell Terminal (Port 8080)
│
▼
Token Guard (Immediate drop of @#$%^&*)
│
▼
InputParser5 (.rstrip("?") trailing punctuation stripping & compound noun extraction)
│
▼
Language Context Router (Binds to autosave_kg.json [SK] or autosave_kg_en.json [EN])
│
▼
sirius_orchestrator.py (Single-Process Daemon + TerminalAssistant)
├── 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal)
├── COLNÍK Guard (0.0s Hard Block on format, diskpart, rmdir /s)
├── HitL Safe Trash Pipeline (Quarantined removal via GET /trash)
├── TimeCore (cycle_delta()) & Guard (Resource supervision)
├── Dual KG Core (autosave_kg.json & autosave_kg_en.json)
├── Native Lossless Merge Engine (kg merge  into )
├── ReasoningEngine 5.9.1 (Taxonomical KG_VERIFY & Proof trees)
├── COLNIK-6.x Customs Decision Gate (Standard & IPC Mode)
├── AUTONOMY 6.x (Confirmation State Latching & Triage Mode)
├── PanelAPI ([ÁNO/NIE] / [YES/NO] Confirmation Loops)
└── EXECUTE 6.x (Dual KG Commits & Safe Execution)
### Key Features
- **Elimination of Socket & File Contention:** Single-process architecture replaces disk-based IPC polling, preventing file locking conflicts and port collisions.  
- **Terminal State Decoupling:** Clearing input or aborting an action immediately forces `currentModule = "none"`, permanently preventing conversational text from executing as host OS shell commands.  
- **Confirmation State Latching:** Pending proposal targets remain latched in memory across conversation turns, guaranteeing affirmative replies (`ÁNO` / `YES`) execute reliably.  
- **Hardware Telemetry Integration:** Continuous low-overhead tracking of CPU, RAM, and Disk metrics via Guard alongside TimeCore latency profiling (`cycle_delta()`).  

---

# 🛡️ ENVOY 5 — Autonomous Retrieval & Domain Shielding  
### Quarantined External Retrieval with Sliding-Window Maintenance

When external enrichment is explicitly authorized, ENVOY 5 operates as an outbound-only, heavily sandboxed retrieval bridge bound to the active linguistic context.

### Security & Semantic Subsystems

- **Target Endpoint Isolation:** Routes English queries strictly to `en.wikipedia.org` and Slovak queries strictly to `sk.wikipedia.org`.  
- **Autonomous Disambiguation Triage (`ExecutionLayer5`):** Detects Wikipedia disambiguation structures (*„môže byť...“*) and contextually routes queries to specific sub-articles.  
- **Anti-Prefix & Phonetic Guard:** Neutralizes prefix over-matching anomalies, permanently halting semantic drift (*Káva* -> *Kavala*).  
- **Strip-Bracket Fallback:** Automatically queries base root lemmas when encountering unresolvable parenthetical articles.  
- **Non-Bio Domain Shield (`Normalizer5`):** Strictly prevents abstract, technical, physical, or architectural disciplines (*ekológia*, *architektúra*, *fyzika*) from receiving biological habitat attributes.  
- **Sentence-Bound Extractor:** Requires explicit occurrence verbs (*žije*, *obýva*, *lives*, *occurs*) within the exact sentence before allowing habitat relation extraction.  
- **Quarantine Sandbox & Sliding-Window Rotation (`EnvoyQuarantine5`):** Isolates incoming data, strips active HTML/scripts/trackers, and automatically enforces a 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/`.  

---

# 🧩 COLNIK‑6.x — Enterprise Customs Decision Gate  
### Standard, High-Performance IPC & COLNÍK Guard

COLNIK-6.x functions as the definitive internal customs authority and command firewall for every system mutation.

### Operational Responsibilities
- **Primitive Decision Gate:** Evaluates system requests to issue deterministic ALLOW, DENY, or TRIAGE verdicts.  
- **COLNÍK Guard Shell Interception:** Blocks dangerous shell routines in 0.0s (`format`, `diskpart`, etc.).  
- **Safe Trash Governance:** Diverts file deletions into quarantine awaiting manual approval via `GET /trash`.  
- **Token Guard Verification:** Confirms input strings are free of malicious symbols (`@#$%^&*`).  
- **Multi-Module Policy Auditing:** Aggregates outputs from PermissionLayer5, PolicyEngine5, BehaviorFilter5, FamilySafetyRules5_x, and EnvoyNormalizer5.  
- **Triage Quarantine Queue:** Routes malformed, ambiguous, or suspicious operations into `COLNIK-6.x/triage` for review via the Triage UI Panel.  

---

# 🖥️ 4-Panel UI Suite (Port 8080)  
### Visual Management & Secure Command Console

Accessible locally via browser (http://127.0.0.1:8080), the UI Suite provides four purpose-built management panels:

- **Duplicates Panel:** Displays duplicate file status, monitors Guard hardware metrics, enforces `REPORT_ONLY` policies, and routes deletions to the HitL Safe Trash pipeline.  
- **Triage Panel:** Real-time visual queue displaying quarantined payloads, unparsed web data, and held mutations (`COLNIK-6.x/triage`).  
- **Navigation Panel:** Deterministic, state-safe navigation across Runtime Core, Knowledge Graph, Envoy, and Autonomy modules.  
- **Terminal Panel:** Interactive command console featuring automatic context release (`currentModule = "none"`), ensuring that typing errors or conversational queries never capture the host OS shell, while command executions are validated against COLNÍK Guard.  

---

# 🔧 Self‑Repair Layer 5.8 & System Agent 5  
### Cryptographic Sealing & Host Gatekeeping

- **Cryptographic Hash Verification:** Continually scans `autosave_kg.json`, `autosave_kg_en.json`, configuration manifests, and system files against SHA-256 seals in `integrity_map.json`.  
- **Automated Reconstruction:** Restores corrupted JSON stores and missing configuration templates from baseline fallbacks.  
- **System Agent 5 Mediation:** Constant-time ($O(1)$) gatekeeper validating all OS-level actions; blocks privilege escalations and unverified process spawns.  

---

# 🛡️ Security Family 5.x & Identity Engine 3.1  
### Role-Based Access Control & Academic Priority

- **Access Tiers:** Strict policy separation across OWNER (full administration), FAMILY (safe household access), and STRANGER (zero-trust sandbox with immediate terminal lockout).  
- **Schoolwork Engine 5.8:** Guaranteed educational bypass allowing academic and homework queries to navigate the Knowledge Graph without restriction or delay.  
- **Password Vault 5.9.1:** Authenticated AES-256-GCM encrypted credential vault with PBKDF2 key stretching, Token Guard protection, and COLNÍK Guard shell filtering.  

---

# 🌟 Architectural Comparison: 5.9.0 vs. 5.9.1

| Architectural Feature | Version 5.9.0 UNIFIED | Version 5.9.1 UNIFIED (Current) |
|:---|:---|:---|
| **Knowledge Graph Schema** | Single unified `autosave_kg.json` | Dual-Language Isolated (`autosave_kg.json` [SK] & `autosave_kg_en.json` [EN]) |
| **Language Context Dispatch** | Monolingual focus / mixed | Dynamic Language Routing based on UI header |
| **Entity Merging** | Manual / external script | Native In-Memory Lossless Merge (`kg merge <src> into <tgt>`) |
| **Taxonomical Category Deduction** | Basic inheritance rules | Contextual Reasoner (`KG_VERIFY`) with edge auto-commits |
| **Reverse Location Engine** | Basic location lookup | Multi-stem matching with False-Positive Flora Guard |
| **Input Token Sanitization** | Regex tokenization | Hard Token Guard dropping `@#$%^&*` at runtime entry |
| **Punctuation Hygiene** | Standard whitespace trim | Greedy Trailing Stripping (`.rstrip("?")`) |
| **Confirmation State Handling** | Turn-dependent prompt loop | Deterministic Confirmation State Latching across turns |
| **Terminal Shell Security** | State decoupling (`none`) | COLNÍK Guard 0.0s Hard Blocking (`format`, `diskpart`, etc.) |
| **Filesystem Disposal Safety** | Report-only duplicates | Human-in-the-Loop Safe UI Trash (`GET /trash`) |
| **Quarantine Storage Maintenance** | Unbounded queue | Automated Sliding-Window Rotation (100 JSON file ceiling) |
| **Shell Output Encoding** | Default OS encoding | Multi-Stage Fallback (UTF-8 -> CP1250 -> CP852) |

---

# 🤖 AUTONOMY 6.x — Supervised Deterministic Intelligence  
### Supervised Autonomous Governance with Active Human-in-the-Loop Oversight

AUTONOMY 6.x operates as the supervisory intelligence layer within SIRIUS 5.9.1, bridging autonomous proposals with human verification.

### Core Autonomy Pipeline
1. **Telemetry & Resource Monitoring:** Evaluates CPU, RAM, and Disk loads via Guard alongside TimeCore latency profiling (`cycle_delta()`).  
2. **Analysis & Proposal Synthesis:** Identifies unindexed concepts and prepares structured proposal objects (`kg.learn_proposal`) targeted to the active language partition.  
3. **Loop Suppression Audit:** Verifies that candidate proposals or deduced taxonomies do not already exist in the active graph.  
4. **Customs Clearance:** Passes proposed actions through COLNIK-6.x validation and Token Guard.  
5. **Interactive Confirmation:** Dispatches human-in-the-loop prompts via PanelAPI (`[ÁNO/NIE]` / `[YES/NO]`) with active confirmation state latching.  
6. **Execution & State Clearance:** Dispatches approved actions to EXECUTE 6.x and resets terminal state (`currentModule = "none"`).  

---

# 🚀 Execution & Verification
SIRIUS Runtime 5.9.1 is launched via the unified single-process orchestrator:

```bash
python sirius_orchestrator.py
Access the interactive 4-Panel UI Suite via browser:
http://127.0.0.1:8080
