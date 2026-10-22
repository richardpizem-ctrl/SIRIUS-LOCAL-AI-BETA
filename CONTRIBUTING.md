# 🤝 Contributing Guidelines – SIRIUS LOCAL AI (v5.9.5 UNIFIED)

Thank you for your interest in contributing to SIRIUS LOCAL AI.  
This document defines the rules, processes, and expectations for all contributors.  
The goal is to maintain a clean, safe, modular, deterministic, explainable, and intelligent local AI system built on the Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning, SafeRollback Crash Resilience, Professor Validator Middleware & COLNÍK Guard Security Protocol.

All processing is fully local.  
No data leaves your device.

Version 5.9.5 updates these guidelines to include:

- Unified Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)  
- Dual-Language Isolated Knowledge Stores (`autosave_kg.json` for SK & `autosave_kg_en.json` for EN)  
- Native Lossless KG Merge Engine (`kg merge <src> into <tgt>`)  
- Taxonomical & Marsupial Inference (`KG_VERIFY`) with persistent edge auto-commits  
- Non-Destructive Reverse Location Engine (`_execute_reverse_location_query`) with anti-flora classification guard  
- Punctuation Hygiene (`.rstrip("?")`) and Confirmation State Latching  
- Entry-Level Token Guard blocking malicious character sequences (`@#$%^&*`)  
- Sliding-Window Quarantine Ceiling Rotation (100 JSON file maximum)  
- SafeRollback Crash Resilience (`safe_rollback.py` with granular `shutil.copytree` backups and `shutil.rmtree` restorations)  
- Professor Validator Middleware enforcing strict `PASS / WARN / REJECT` cognitive verification  
- COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like `format` and `diskpart`)  
- Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with deterministic state release)  
- Multi-Word Semantic Engine (`InputParser5` preserving compound noun phrases)  
- Autonomous Disambiguation Triage & Anti-Prefix Guard (`EnvoyExecutionLayer5`)  
- Contextual Domain Shield & Sentence-Bound Bio Filter (`EnvoyNormalizer5`)  
- PanelAPI & Native Integrated IPC Bridge  
- TimeCore Latency Telemetry (`cycle_delta()`) & Guard Security/Metric Supervision  
- Reasoning Engine 5.9.5 & Workflow Engine 5.9.5  
- KG_EXPLAIN & KG_EXPLAIN_DEEP (Explainability Engines)  
- Proof Tree & Evidence Tree Foundations  
- COLNIK‑6.x Validation Layer (Standard & High-Performance IPC Mode)  
- AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Safe Trash Governance)  
- Identity Engine 3.1 & SECURITY FAMILY 5.x  
- Hardened deterministic routing and state decoupling rules  

---

# 1. 🔐 Core Principles

- Security has absolute priority  
- Explainability must remain transparent and deterministic  
- No action may bypass user confirmations (PanelAPI `[ÁNO/NIE]` / `[YES/NO]`)  
- Strict linguistic partition: SK and EN graph stores must never merge into a single mixed schema  
- Human-in-the-Loop Safe Trash: files flagged for deletion must route to quarantine, never direct disk removal  
- Hard Token Guard: all inputs must be sanitized against forbidden symbolic injections  
- No duplicate confirmation prompts on confirmed entities or deduced taxonomies (zero proposal recurrence)  
- Compound natural language queries must preserve modifiers without arbitrary truncation  
- Modular architecture must remain clean and strictly separated  
- All contributions must respect existing module APIs and `sirius_orchestrator.py`  
- No network operations or external data transmission (100% offline-first)  
- No hidden automation or background tasks without TimeCore/Guard supervision  
- UI panels must remain decoupled; input clearing must reset module states (`currentModule = "none"`)  
- No global mutable state or circular imports  
- Deterministic, reversible behavior whenever possible  
- Safety-critical modules must never be weakened or bypassed, including:  
  - Token Guard & InputParser5  
  - Dual-Language Graph Isolation (`autosave_kg.json` & `autosave_kg_en.json`)  
  - Native Lossless KG Merge Engine  
  - Taxonomical & Reverse Location Engines  
  - SafeRollback Backup & Restore Module (`safe_rollback.py`)  
  - Professor Validator Middleware (`professor_validator.py`)  
  - EnvoyExecutionLayer5, EnvoyNormalizer5 & EnvoyQuarantine5  
  - COLNÍK Guard & TerminalAssistant  
  - Human-in-the-Loop Safe Trash  
  - 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal`)  
  - SECURITY FAMILY 5.x  
  - Identity Engine 3.1  
  - Schoolwork Engine 5.8  
  - Time-Limits Engine v3  
  - Self-Repair Layer 5.8  
  - System Agent 5  
  - COLNIK‑6.x Validation Layer (Standard & IPC Mode)  
  - AUTONOMY 6.x (Control, Guard & Triage Mode)  
  - PanelAPI & TimeCore/Guard Supervision  
- Reasoning Engine 5.9.5 must not be extended unsafely  
- KG_EXPLAIN & KG_EXPLAIN_DEEP must remain transparent and correct  

---

# 2. 🚀 How to Start

1. Fork the repository  
2. Create a new branch for your change  
3. Implement the change according to the Runtime 5.9.5 architecture  
4. Test it in your local environment (Windows 11, Port 8080)  
5. Submit a Pull Request with a clear description  

Recommended branch naming:
- `feature/<name>`  
- `fix/<name>`  
- `refactor/<name>`  
- `docs/<name>`  

---

# 3. 🧼 Code Style

All contributions must follow the project’s `STYLEGUIDE.md`.

Key rules:

- clean, readable, consistent  
- no magic constants  
- clear naming of functions and modules  
- comments explain why, not what  
- avoid unnecessary complexity  
- follow the architecture and module map  
- functions ideally 5–25 lines  
- no monolithic modules  
- no deep nesting — prefer early returns  
- imports grouped: standard → third-party → internal  
- compound noun logic must preserve full tokens (*ovcia vlna*, *mobilny telefon*)  
- linguistic partition must be maintained across `autosave_kg.json` and `autosave_kg_en.json`  
- KG merge operations must preserve all attributes and generate alias nodes  
- reverse habitat matching must uniform attribute getters (`self.kg.get_attributes()`)  
- trailing punctuation must be cleanly stripped via `.rstrip("?")`  
- Envoy triage must respect disambiguation checks and anti-prefix guards  
- SECURITY FAMILY 5.x code must follow safety-first design  
- SCHOOLWORK ENGINE 5.8 must remain intact and non-bypassable  
- Reasoning Engine 5.9.5 integrations must be deterministic and safe  
- Self-Repair Layer 5.8 must not be disabled or bypassed  
- System Agent 5 must validate all system-level actions  
- ENVOY 5 must sanitize all web queries and prevent non-bio habitat leakage  
- COLNIK‑6.x must validate all KG mutations, workflow steps, and IPC payloads  
- AUTONOMY 6.x must manage proposals, Guard supervision, and Triage Mode securely  
- PanelAPI and TimeCore/Guard components must remain active and uncompromised  
- SafeRollback and Professor Validator middleware must remain active  
- KG_EXPLAIN & KG_EXPLAIN_DEEP output must remain transparent and correct  

---

# 4. 🧪 Testing Requirements

Every change must include:

- basic functional tests  
- verification of security constraints  
- input validation, trailing punctuation stripping, and token preservation testing  
- error-state and disambiguation fallback testing  
- predictable behavior under invalid inputs  
- no silent failures  
- no destructive operations without confirmation  
- no reliance on external cloud APIs or network execution outside local IPC  

If your change affects:

- **InputParser5 & Token Guard** → test multi-word noun preservation, copula verb isolation, trailing punctuation stripping, and rejection of `@#$%^&*`  
- **Dual-Language Graph Architecture** → test complete isolation of `autosave_kg.json` and `autosave_kg_en.json`, dynamic language context dispatching, and independent autosaves  
- **KG Merge Engine** → test zero-loss attribute relocation, alias edge formation, and bidirectional alias query resolution  
- **Taxonomical Reasoning (`KG_VERIFY`)** → test higher-order category deduction (*marsupials/macropods -> mammals*) and persistent edge auto-commit  
- **Reverse Habitat Engine** → test multi-stem location parsing and anti-flora shielding on tree-dwelling fauna  
- **TerminalAssistant & COLNÍK Guard** → test 0.0s blocking of forbidden commands (`format`, `diskpart`), prompt handling for risky commands, and TimeCore `cycle_delta()` telemetry  
- **Safe UI Trash** → test file quarantine transitions and confirm zero direct unverified disk deletions  
- **EnvoyQuarantine5** → test sliding-window rotation ensuring the 100 JSON record ceiling is enforced  
- **EnvoyExecutionLayer5** → test disambiguation resolution, prefix guards, strip-bracket fallback  
- **EnvoyNormalizer5** → test habitat domain blocking for technological and abstract entities  
- **SafeRollback** → test module-level `copytree` backups and `rmtree` restorations  
- **Professor Validator** → test `PASS / WARN / REJECT` cognitive output verification  
- **4-Panel UI Suite & PanelAPI** → test state resets on input clearance (`currentModule = "none"`), interactive `[ÁNO/NIE]` / `[YES/NO]` loops, and confirmation state latching  
- **Workflow Engine 5.9.5 & Orchestrator** → test single-process routing via `sirius_orchestrator.py` on port 8080  
- **Reasoning Engine 5.9.5** →  
  - multi-hop inference  
  - inheritance reasoning  
  - transitive reasoning  
  - taxonomical category reasoning  
  - deterministic rule chaining  
  - proof tree nodes  
  - evidence trees  
  - confidence scoring  
- **SECURITY FAMILY 5.x** →  
  - identity classification (`OWNER / FAMILY / STRANGER`)  
  - time-limit enforcement v3  
  - schoolwork bypass logic  
  - safe-mode restrictions  
  - STRANGER-mode protections  
- **Schoolwork Engine 5.8** →  
  - subject detection  
  - difficulty scoring  
  - bypass logic  
- **Self-Repair Layer 5.8** →  
  - integrity checks  
  - fallback behavior  
- **System Agent 5** →  
  - validation of all system actions  
  - deterministic safety enforcement  
- **COLNIK‑6.x Validation Layer (Standard & IPC Mode)** →  
  - KG mutation validation  
  - workflow step authorization  
  - anomaly detection  
  - IPC synchronization with AUTONOMY  
- **AUTONOMY 6.x (Control, Guard & Triage Mode)** →  
  - proposal generation  
  - confirmation latching logic  
  - Triage Mode execution (`COLNIK-6.x/triage`)  
  - safe autonomous routing  
- **TimeCore & Guard** →  
  - temporal execution timing  
  - system metrics monitoring (CPU, RAM, Disk)  
  - runtime anomaly supervision  
- **KG_EXPLAIN & KG_EXPLAIN_DEEP** →  
  - correct inference history  
  - deterministic explanation output  

---

# 5. 📥 Pull Request Rules

A valid PR must include:

- clear description of the change  
- explanation of why the change is needed  
- reference to related Issues (if applicable)  
- test results or manual test notes  

Restrictions:

- no large PRs — prefer smaller, well-structured steps  
- PRs must not modify the architecture without prior discussion  
- PRs must follow module boundaries  
- PRs must not introduce new external dependencies without approval  
- PRs must not break determinism or safety guarantees  
- PRs must not merge or cross-contaminate `autosave_kg.json` and `autosave_kg_en.json`  
- PRs must not bypass Token Guard or COLNÍK Guard shell security  
- PRs must not bypass the Human-in-the-Loop Safe Trash pipeline  
- PRs must not bypass SafeRollback or Professor Validator checks  
- PRs must not weaken SECURITY FAMILY 5.x protections  
- PRs must not interfere with SCHOOLWORK ENGINE 5.8  
- PRs must not disable or bypass the Self-Repair Layer  
- PRs must not misuse Reasoning Engine 5.9.5  
- PRs must not introduce prefix drift or bypass disambiguation guards  
- PRs must not bypass System Agent 5 validation  
- PRs must not bypass ENVOY Execution/Permission Layers 5  
- PRs must not bypass COLNIK‑6.x validation or IPC synchronization  
- PRs must not bypass PanelAPI user confirmation gates  
- PRs must not disable TimeCore/Guard supervision  
- PRs must not distort or hide KG_EXPLAIN or KG_EXPLAIN_DEEP inference history  
- PRs must not misuse AUTONOMY 6.x decision logic or Triage Mode  

---

# 6. ❌ What We Do Not Accept

- cloud-dependent or network-based execution pipelines  
- automatic destructive file deletions without HitL quarantine routing  
- bridging or mixing Slovak and English knowledge graphs  
- bypassing security, customs, Token Guard, or permission layers  
- truncation of compound multi-word queries down to single tokens  
- leaking biological attributes into abstract or technological entities  
- PRs causing terminal input deadlocks or omitting state reset logic  
- monolithic modules or circular dependencies  
- undocumented API alterations  
- hidden background tasks without Guard supervision  
- features breaking modular isolation  
- attempts to disable FAMILY mode, time limits, or Schoolwork Engine  
- attempts to weaken STRANGER-mode protections  
- attempts to bypass Identity Engine 3.1  
- attempts to disable Self-Repair Layer  
- unsafe Reasoning Engine extensions  
- attempts to bypass System Agent 5, ENVOY 5, or COLNIK-6.x  
- attempts to manipulate KG_EXPLAIN or KG_EXPLAIN_DEEP output  

---

# 7. 💬 Communication

All discussions take place through:

- GitHub Issues  
- Pull Request comments  

Guidelines:

- be respectful and constructive  
- provide technical reasoning  
- avoid vague or incomplete reports  
- include reproduction steps and environment logs when reporting issues  

---

# 8. 🧭 Architecture Compliance

All contributions must respect:

- `ARCHITECTURE.md` (v5.9.5)  
- `MODULE_MAP.md`  
- `STYLEGUIDE.md`  
- `SECURITY.md`  
- Dual-Language Knowledge Graph isolation rules  
- Native Lossless Entity Merge specifications  
- COLNÍK Guard & Token Guard security rules  
- SafeRollback & Professor Validator rules  
- Human-in-the-Loop Safe Trash requirements  
- SECURITY FAMILY 5.x design rules  
- Schoolwork Engine 5.8 rules  
- Self-Repair Layer 5.8 requirements  
- System Agent 5 safety model  
- InputParser5 & Semantic preservation specifications  
- ENVOY 5 sanitization, disambiguation & domain filtering rules  
- COLNIK‑6.x validation rules (Standard & IPC Mode)  
- AUTONOMY 6.x Control, Guard & Triage Mode rules  
- 4-Panel UI Suite state management rules  
- PanelAPI, TimeCore & Guard supervision rules  
- KG_EXPLAIN & KG_EXPLAIN_DEEP explainability rules  
- Unified Orchestrator (`sirius_orchestrator.py`) execution rules  

Breaking architectural boundaries requires prior discussion and approval.

---

# 9. 📝 Commit Message Style

Use clear, structured commit messages:

- `feat: implement dual-language graph isolation for SK and EN`  
- `feat: integrate native kg merge command in RuntimeCore`  
- `fix: resolve reverse habitat fauna filtering with anti-flora guard`  
- `sec: enforce Token Guard and COLNIK Guard 0.0s command blocking`  
- `refactor: integrate SafeRollback backup and Professor Validator middleware`  
- `docs: update CONTRIBUTING.md for v5.9.5`  

Avoid vague messages like “update”, “fix stuff”, “misc changes”.

---

# 10. 🧒 Family Safety Requirements (v5.9.5)

Contributors must respect the integrity of the SECURITY FAMILY 5.x module:

- behavior-based identity must remain deterministic  
- FAMILY mode must remain safe and restricted  
- time-limits v3 must not be bypassable  
- schoolwork must always be allowed  
- stranger-mode must remain locked down  
- OWNER-level actions must remain protected  
- Identity Engine 3.1 must not be weakened  
- Schoolwork Engine 5.8 must remain intact  
- System Agent 5 must validate all system-level actions  
- ENVOY 5 must sanitize all web queries and verify target content  
- COLNIK‑6.x must validate all KG mutations, workflow steps, and IPC payloads  
- AUTONOMY 6.x must remain safe in Control, Guard & Triage Mode  
- PanelAPI must maintain required user confirmation gates  
- TimeCore & Guard must oversee runtime stability and system metrics  
- SafeRollback must provide reliable state recovery  
- Professor Validator must verify cognitive output integrity  
- KG_EXPLAIN & KG_EXPLAIN_DEEP must provide transparent inference history  
- reasoning rules must remain deterministic and safe  

Any PR affecting SECURITY FAMILY, SCHOOLWORK ENGINE, ENVOY, System Agent, COLNIK, AUTONOMY, PanelAPI, TimeCore/Guard, SafeRollback, Professor Validator, or KG_EXPLAIN must include explicit safety tests.

---

# 11. 📄 License

All contributions are accepted only in accordance with the project’s SUL-3.2.0 License.

---

# 📌 Document Status

Current version: **5.9.5** (Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning, SafeRollback, Professor Validator & Comprehensive Security Protocol)
