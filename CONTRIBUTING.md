# 🤝 Contributing Guidelines – SIRIUS LOCAL AI (v5.9.1 UNIFIED)

Thank you for your interest in contributing to SIRIUS LOCAL AI[cite: 1].  
This document defines the rules, processes, and expectations for all contributors[cite: 1].  
The goal is to maintain a clean, safe, modular, deterministic, explainable, and intelligent local AI system built on the Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & COLNÍK Guard Security Protocol[cite: 1, 2].

All processing is fully local[cite: 1].  
No data leaves your device[cite: 1].

Version 5.9.1 updates these guidelines to include:

- Unified Single-Process Orchestrator (sirius_orchestrator.py on Port 8080 with embedded TerminalAssistant + TimeCore)[cite: 1]  
- Dual-Language Isolated Knowledge Stores (autosave_kg.json for SK & autosave_kg_en.json for EN)[cite: 1, 2]  
- Native Lossless KG Merge Engine (kg merge <src> into <tgt>)[cite: 1, 2]  
- Taxonomical & Marsupial Inference (KG_VERIFY) with persistent edge auto-commits[cite: 1, 2]  
- Non-Destructive Reverse Location Engine (_execute_reverse_location_query) with anti-flora classification guard[cite: 1, 2]  
- Punctuation Hygiene (.rstrip("?")) and Confirmation State Latching[cite: 1, 2]  
- Entry-Level Token Guard blocking malicious character sequences (@#$%^&*)[cite: 2]  
- Sliding-Window Quarantine Ceiling Rotation (100 JSON file maximum)[cite: 2]  
- COLNÍK Guard Shell Access Control (0.0s hard blocking of forbidden commands like format and diskpart)[cite: 2]  
- Human-in-the-Loop Safe UI Trash preventing direct unverified disk destruction[cite: 2]  
- 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal with deterministic state release)[cite: 1]  
- Multi-Word Semantic Engine (InputParser5 preserving compound noun phrases)[cite: 1]  
- Autonomous Disambiguation Triage & Anti-Prefix Guard (EnvoyExecutionLayer5)[cite: 1]  
- Contextual Domain Shield & Sentence-Bound Bio Filter (EnvoyNormalizer5)[cite: 1]  
- PanelAPI & Native Integrated IPC Bridge[cite: 1]  
- TimeCore Latency Telemetry (cycle_delta()) & Guard Security/Metric Supervision[cite: 2]  
- Reasoning Engine 5.9.1 & Workflow Engine 5.9.1[cite: 1]  
- KG_EXPLAIN & KG_EXPLAIN_DEEP (Explainability Engines)[cite: 1]  
- Proof Tree & Evidence Tree Foundations[cite: 1]  
- COLNIK‑6.x Validation Layer (Standard & High-Performance IPC Mode)[cite: 1]  
- AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Safe Trash Governance)[cite: 1, 2]  
- Identity Engine 3.1 & SECURITY FAMILY 5.x[cite: 1]  
- Hardened deterministic routing and state decoupling rules[cite: 1]  

---

# 1. 🔐 Core Principles

- Security has absolute priority[cite: 1]  
- Explainability must remain transparent and deterministic[cite: 1]  
- No action may bypass user confirmations (PanelAPI [ÁNO/NIE] / [YES/NO])[cite: 1, 2]  
- Strict linguistic partition: SK and EN graph stores must never merge into a single mixed schema[cite: 1, 2]  
- Human-in-the-Loop Safe Trash: files flagged for deletion must route to quarantine, never direct disk removal[cite: 2]  
- Hard Token Guard: all inputs must be sanitized against forbidden symbolic injections[cite: 2]  
- No duplicate confirmation prompts on confirmed entities or deduced taxonomies (zero proposal recurrence)[cite: 1, 2]  
- Compound natural language queries must preserve modifiers without arbitrary truncation[cite: 1]  
- Modular architecture must remain clean and strictly separated[cite: 1]  
- All contributions must respect existing module APIs and sirius_orchestrator.py[cite: 1]  
- No network operations or external data transmission (100% offline-first)[cite: 1]  
- No hidden automation or background tasks without TimeCore/Guard supervision[cite: 1]  
- UI panels must remain decoupled; input clearing must reset module states (currentModule = "none")[cite: 1]  
- No global mutable state or circular imports[cite: 1]  
- Deterministic, reversible behavior whenever possible[cite: 1]  
- Safety-critical modules must never be weakened or bypassed, including:[cite: 1]  
  - Token Guard & InputParser5[cite: 1, 2]  
  - Dual-Language Graph Isolation (autosave_kg.json & autosave_kg_en.json)[cite: 1, 2]  
  - Native Lossless KG Merge Engine[cite: 1, 2]  
  - Taxonomical & Reverse Location Engines[cite: 1, 2]  
  - EnvoyExecutionLayer5, EnvoyNormalizer5 & EnvoyQuarantine5[cite: 1, 2]  
  - COLNÍK Guard & TerminalAssistant[cite: 2]  
  - Human-in-the-Loop Safe Trash[cite: 2]  
  - 4-Panel UI Suite (Duplicates, Triage, Navigation, Terminal)[cite: 1]  
  - SECURITY FAMILY 5.x[cite: 1]  
  - Identity Engine 3.1[cite: 1]  
  - Schoolwork Engine 5.8[cite: 1]  
  - Time-Limits Engine v3[cite: 1]  
  - Self-Repair Layer 5.8[cite: 1]  
  - System Agent 5[cite: 1]  
  - COLNIK‑6.x Validation Layer (Standard & IPC Mode)[cite: 1]  
  - AUTONOMY 6.x (Control, Guard & Triage Mode)[cite: 1]  
  - PanelAPI & TimeCore/Guard Supervision[cite: 1]  
- Reasoning Engine 5.9.1 must not be extended unsafely[cite: 1]  
- KG_EXPLAIN & KG_EXPLAIN_DEEP must remain transparent and correct[cite: 1]  

---

# 2. 🚀 How to Start

1. Fork the repository[cite: 1]  
2. Create a new branch for your change[cite: 1]  
3. Implement the change according to the Runtime 5.9.1 architecture[cite: 1, 2]  
4. Test it in your local environment (Windows 11, Port 8080)[cite: 1, 2]  
5. Submit a Pull Request with a clear description[cite: 1]  

Recommended branch naming:
- feature/<name>[cite: 1]  
- fix/<name>[cite: 1]  
- refactor/<name>[cite: 1]  
- docs/<name>[cite: 1]  

---

# 3. 🧼 Code Style

All contributions must follow the project’s STYLEGUIDE.md[cite: 1].

Key rules:

- clean, readable, consistent[cite: 1]  
- no magic constants[cite: 1]  
- clear naming of functions and modules[cite: 1]  
- comments explain why, not what[cite: 1]  
- avoid unnecessary complexity[cite: 1]  
- follow the architecture and module map[cite: 1]  
- functions ideally 5–25 lines[cite: 1]  
- no monolithic modules[cite: 1]  
- no deep nesting — prefer early returns[cite: 1]  
- imports grouped: standard → third-party → internal[cite: 1]  
- compound noun logic must preserve full tokens (ovcia vlna, mobilny telefon)[cite: 1]  
- linguistic partition must be maintained across autosave_kg.json and autosave_kg_en.json[cite: 1, 2]  
- KG merge operations must preserve all attributes and generate alias nodes[cite: 1, 2]  
- reverse habitat matching must utilize uniform attribute getters (self.kg.get_attributes())[cite: 1, 2]  
- trailing punctuation must be cleanly stripped via .rstrip("?")[cite: 1, 2]  
- Envoy triage must respect disambiguation checks and anti-prefix guards[cite: 1]  
- SECURITY FAMILY 5.x code must follow safety-first design[cite: 1]  
- SCHOOLWORK ENGINE 5.8 must remain intact and non-bypassable[cite: 1]  
- Reasoning Engine 5.9.1 integrations must be deterministic and safe[cite: 1]  
- Self-Repair Layer 5.8 must not be disabled or bypassed[cite: 1]  
- System Agent 5 must validate all system-level actions[cite: 1]  
- ENVOY 5 must sanitize all web queries and prevent non-bio habitat leakage[cite: 1]  
- COLNIK‑6.x must validate all KG mutations, workflow steps, and IPC payloads[cite: 1]  
- AUTONOMY 6.x must manage proposals, Guard supervision, and Triage Mode securely[cite: 1]  
- PanelAPI and TimeCore/Guard components must remain active and uncompromised[cite: 1]  
- KG_EXPLAIN & KG_EXPLAIN_DEEP output must remain transparent and correct[cite: 1]  

---

# 4. 🧪 Testing Requirements

Every change must include:

- basic functional tests[cite: 1]  
- verification of security constraints[cite: 1]  
- input validation, trailing punctuation stripping, and token preservation testing[cite: 1, 2]  
- error-state and disambiguation fallback testing[cite: 1]  
- predictable behavior under invalid inputs[cite: 1]  
- no silent failures[cite: 1]  
- no destructive operations without confirmation[cite: 1]  
- no reliance on external cloud APIs or network execution outside local IPC[cite: 1]  

If your change affects:

- InputParser5 & Token Guard → test multi-word noun preservation, copula verb isolation, trailing punctuation stripping, and rejection of @#$%^&*[cite: 1, 2]  
- Dual-Language Graph Architecture → test complete isolation of autosave_kg.json and autosave_kg_en.json, dynamic language context dispatching, and independent autosaves[cite: 1, 2]  
- KG Merge Engine → test zero-loss attribute relocation, alias edge formation, and bidirectional alias query resolution[cite: 1, 2]  
- Taxonomical Reasoning (KG_VERIFY) → test higher-order category deduction (marsupials/macropods -> mammals) and persistent edge auto-commit[cite: 1, 2]  
- Reverse Habitat Engine → test multi-stem location parsing and anti-flora shielding on tree-dwelling fauna[cite: 1, 2]  
- TerminalAssistant & COLNÍK Guard → test 0.0s blocking of forbidden commands (format, diskpart), prompt handling for risky commands, and TimeCore cycle_delta() telemetry[cite: 2]  
- Safe UI Trash → test file quarantine transitions and confirm zero direct unverified disk deletions[cite: 2]  
- EnvoyQuarantine5 → test sliding-window rotation ensuring the 100 JSON record ceiling is enforced[cite: 2]  
- EnvoyExecutionLayer5 → test disambiguation resolution, prefix guards, strip-bracket fallback[cite: 1]  
- EnvoyNormalizer5 → test habitat domain blocking for technological and abstract entities[cite: 1]  
- 4-Panel UI Suite & PanelAPI → test state resets on input clearance (currentModule = "none"), interactive [ÁNO/NIE] / [YES/NO] loops, and confirmation state latching[cite: 1, 2]  
- Workflow Engine 5.9.1 & Orchestrator → test single-process routing via sirius_orchestrator.py on port 8080[cite: 1]  
- Reasoning Engine 5.9.1 →[cite: 1]  
  - multi-hop inference[cite: 1]  
  - inheritance reasoning[cite: 1]  
  - transitive reasoning[cite: 1]  
  - taxonomical category reasoning[cite: 1, 2]  
  - deterministic rule chaining[cite: 1]  
  - proof tree nodes[cite: 1]  
  - evidence trees[cite: 1]  
  - confidence scoring[cite: 1]  
- SECURITY FAMILY 5.x →[cite: 1]  
  - identity classification (OWNER / FAMILY / STRANGER)[cite: 1]  
  - time-limit enforcement v3[cite: 1]  
  - schoolwork bypass logic[cite: 1]  
  - safe-mode restrictions[cite: 1]  
  - STRANGER-mode protections[cite: 1]  
- Schoolwork Engine 5.8 →[cite: 1]  
  - subject detection[cite: 1]  
  - difficulty scoring[cite: 1]  
  - bypass logic[cite: 1]  
- Self-Repair Layer 5.8 →[cite: 1]  
  - integrity checks[cite: 1]  
  - fallback behavior[cite: 1]  
- System Agent 5 →[cite: 1]  
  - validation of all system actions[cite: 1]  
  - deterministic safety enforcement[cite: 1]  
- COLNIK‑6.x Validation Layer (Standard & IPC Mode) →[cite: 1]  
  - KG mutation validation[cite: 1]  
  - workflow step authorization[cite: 1]  
  - anomaly detection[cite: 1]  
  - IPC synchronization with AUTONOMY[cite: 1]  
- AUTONOMY 6.x (Control, Guard & Triage Mode) →[cite: 1]  
  - proposal generation[cite: 1]  
  - confirmation latching logic[cite: 1, 2]  
  - Triage Mode execution (COLNIK-6.x/triage)[cite: 1]  
  - safe autonomous routing[cite: 1]  
- TimeCore & Guard →[cite: 1]  
  - temporal execution timing[cite: 1]  
  - system metrics monitoring (CPU, RAM, Disk)[cite: 1]  
  - runtime anomaly supervision[cite: 1]  
- KG_EXPLAIN & KG_EXPLAIN_DEEP →[cite: 1]  
  - correct inference history[cite: 1]  
  - deterministic explanation output[cite: 1]  

---

# 5. 📥 Pull Request Rules

A valid PR must include:

- clear description of the change[cite: 1]  
- explanation of why the change is needed[cite: 1]  
- reference to related Issues (if applicable)[cite: 1]  
- test results or manual test notes[cite: 1]  

Restrictions:

- no large PRs — prefer smaller, well-structured steps[cite: 1]  
- PRs must not modify the architecture without prior discussion[cite: 1]  
- PRs must follow module boundaries[cite: 1]  
- PRs must not introduce new external dependencies without approval[cite: 1]  
- PRs must not break determinism or safety guarantees[cite: 1]  
- PRs must not merge or cross-contaminate autosave_kg.json and autosave_kg_en.json[cite: 1, 2]  
- PRs must not bypass Token Guard or COLNÍK Guard shell security[cite: 2]  
- PRs must not bypass the Human-in-the-Loop Safe Trash pipeline[cite: 2]  
- PRs must not weaken SECURITY FAMILY 5.x protections[cite: 1]  
- PRs must not interfere with SCHOOLWORK ENGINE 5.8[cite: 1]  
- PRs must not disable or bypass the Self-Repair Layer[cite: 1]  
- PRs must not misuse Reasoning Engine 5.9.1[cite: 1]  
- PRs must not introduce prefix drift or bypass disambiguation guards[cite: 1]  
- PRs must not bypass System Agent 5 validation[cite: 1]  
- PRs must not bypass ENVOY Execution/Permission Layers 5[cite: 1]  
- PRs must not bypass COLNIK‑6.x validation or IPC synchronization[cite: 1]  
- PRs must not bypass PanelAPI user confirmation gates[cite: 1]  
- PRs must not disable TimeCore/Guard supervision[cite: 1]  
- PRs must not distort or hide KG_EXPLAIN or KG_EXPLAIN_DEEP inference history[cite: 1]  
- PRs must not misuse AUTONOMY 6.x decision logic or Triage Mode[cite: 1]  

---

# 6. ❌ What We Do Not Accept

- cloud-dependent or network-based execution pipelines[cite: 1]  
- automatic destructive file deletions without HitL quarantine routing[cite: 1, 2]  
- bridging or mixing Slovak and English knowledge graphs[cite: 1, 2]  
- bypassing security, customs, Token Guard, or permission layers[cite: 1, 2]  
- truncation of compound multi-word queries down to single tokens[cite: 1]  
- leaking biological attributes into abstract or technological entities[cite: 1]  
- PRs causing terminal input deadlocks or omitting state reset logic[cite: 1]  
- monolithic modules or circular dependencies[cite: 1]  
- undocumented API alterations[cite: 1]  
- hidden background tasks without Guard supervision[cite: 1]  
- features breaking modular isolation[cite: 1]  
- attempts to disable FAMILY mode, time limits, or Schoolwork Engine[cite: 1]  
- attempts to weaken STRANGER-mode protections[cite: 1]  
- attempts to bypass Identity Engine 3.1[cite: 1]  
- attempts to disable Self-Repair Layer[cite: 1]  
- unsafe Reasoning Engine extensions[cite: 1]  
- attempts to bypass System Agent 5, ENVOY 5, or COLNIK-6.x[cite: 1]  
- attempts to manipulate KG_EXPLAIN or KG_EXPLAIN_DEEP output[cite: 1]  

---

# 7. 💬 Communication

All discussions take place through:

- GitHub Issues[cite: 1]  
- Pull Request comments[cite: 1]  

Guidelines:

- be respectful and constructive[cite: 1]  
- provide technical reasoning[cite: 1]  
- avoid vague or incomplete reports[cite: 1]  
- include reproduction steps and environment logs when reporting issues[cite: 1]  

---

# 8. 🧭 Architecture Compliance

All contributions must respect:

- ARCHITECTURE.md (v5.9.1)[cite: 1, 2]  
- MODULE_MAP.md[cite: 1]  
- STYLEGUIDE.md[cite: 1]  
- SECURITY.md[cite: 1]  
- Dual-Language Knowledge Graph isolation rules[cite: 1, 2]  
- Native Lossless Entity Merge specifications[cite: 1, 2]  
- COLNÍK Guard & Token Guard security rules[cite: 2]  
- Human-in-the-Loop Safe Trash requirements[cite: 2]  
- SECURITY FAMILY 5.x design rules[cite: 1]  
- Schoolwork Engine 5.8 rules[cite: 1]  
- Self-Repair Layer 5.8 requirements[cite: 1]  
- System Agent 5 safety model[cite: 1]  
- InputParser5 & Semantic preservation specifications[cite: 1]  
- ENVOY 5 sanitization, disambiguation & domain filtering rules[cite: 1]  
- COLNIK‑6.x validation rules (Standard & IPC Mode)[cite: 1]  
- AUTONOMY 6.x Control, Guard & Triage Mode rules[cite: 1]  
- 4-Panel UI Suite state management rules[cite: 1]  
- PanelAPI, TimeCore & Guard supervision rules[cite: 1]  
- KG_EXPLAIN & KG_EXPLAIN_DEEP explainability rules[cite: 1]  
- Unified Orchestrator (sirius_orchestrator.py) execution rules[cite: 1]  

Breaking architectural boundaries requires prior discussion and approval[cite: 1].

---

# 9. 📝 Commit Message Style

Use clear, structured commit messages:

- feat: implement dual-language graph isolation for SK and EN[cite: 1, 2]  
- feat: integrate native kg merge command in RuntimeCore[cite: 1, 2]  
- fix: resolve reverse habitat fauna filtering with anti-flora guard[cite: 1, 2]  
- sec: enforce Token Guard and COLNIK Guard 0.0s command blocking[cite: 2]  
- docs: update CONTRIBUTING.md for v5.9.1[cite: 1, 2]  

Avoid vague messages like “update”, “fix stuff”, “misc changes”[cite: 1].

---

# 10. 🧒 Family Safety Requirements (v5.9.1)

Contributors must respect the integrity of the SECURITY FAMILY 5.x module:

- behavior-based identity must remain deterministic[cite: 1]  
- FAMILY mode must remain safe and restricted[cite: 1]  
- time-limits v3 must not be bypassable[cite: 1]  
- schoolwork must always be allowed[cite: 1]  
- stranger-mode must remain locked down[cite: 1]  
- OWNER-level actions must remain protected[cite: 1]  
- Identity Engine 3.1 must not be weakened[cite: 1]  
- Schoolwork Engine 5.8 must remain intact[cite: 1]  
- System Agent 5 must validate all system-level actions[cite: 1]  
- ENVOY 5 must sanitize all web queries and verify target content[cite: 1]  
- COLNIK‑6.x must validate all KG mutations, workflow steps, and IPC payloads[cite: 1]  
- AUTONOMY 6.x must remain safe in Control, Guard & Triage Mode[cite: 1]  
- PanelAPI must maintain required user confirmation gates[cite: 1]  
- TimeCore & Guard must oversee runtime stability and system metrics[cite: 1]  
- KG_EXPLAIN & KG_EXPLAIN_DEEP must provide transparent inference history[cite: 1]  
- reasoning rules must remain deterministic and safe[cite: 1]  

Any PR affecting SECURITY FAMILY, SCHOOLWORK ENGINE, ENVOY, System Agent, COLNIK, AUTONOMY, PanelAPI, TimeCore/Guard, or KG_EXPLAIN must include explicit safety tests[cite: 1].

---

# 11. 📄 License

All contributions are accepted only in accordance with the project’s SUL-3.2.0 License.

---

# 📌 Document Status

Current version: 5.9.1 (Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & Comprehensive Security Protocol)[cite: 1, 2]
