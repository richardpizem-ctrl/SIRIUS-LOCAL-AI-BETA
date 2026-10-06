# 🔐 PASSWORD VAULT 5.9.1 — Secure Local Credential Module
### Fully Offline • AES‑256‑GCM • Identity‑Aware • Deterministic • Dual-Language KG Ready • Token Guard Protected • COLNÍK Guard Hardened • Single-Process Orchestrator • AUTONOMY‑Supervised

PASSWORD VAULT 5.9.1 is the official secure credential storage module of  
**SIRIUS LOCAL AI — Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & Comprehensive Security Protocol 5.9.1**.

It provides **fully offline, encrypted, identity‑aware, deterministic** password and secret storage  
with strict OWNER/FAMILY/STRANGER access rules, terminal input decoupling, entry-level Token Guard sanitization, and complete integration with:

- Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080 with embedded TerminalAssistant + TimeCore)
- Dual-Language Knowledge Graph Stores (`autosave_kg.json` for SK & `autosave_kg_en.json` for EN)
- Token Guard input filter (immediately rejecting inputs containing forbidden characters `@#$%^&*`)
- Trailing punctuation hygiene (`.rstrip("?")`) and confirmation state latching
- COLNÍK Guard Shell Filter (0.0s hard blocking of forbidden commands like `format` and `diskpart`)
- Human-in-the-Loop Safe Trash pipeline (routing deletion targets to quarantine, preventing unverified disk removal)
- Multi-Word Semantic Engine (`InputParser5` preserving compound service names)
- PanelAPI interactive loops (`[ÁNO/NIE]` / `[YES/NO]` confirmation prompts)
- TimeCore temporal tracking (`cycle_delta()`) & Guard security/resource supervision (CPU, RAM, Disk)
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)
- Runtime Core 5.9.1
- Workflow Engine 5.9.1
- Reasoning Engine 5.9.1
- KG_EXPLAIN & KG_EXPLAIN_DEEP (Hierarchical proof trees & XAI attribution)
- Security Family 5.x & Identity Engine 3.1
- System Agent 5
- Self‑Repair Layer 5.8
- **COLNIK‑6.x Validation Layer (Standard, High-Performance IPC Mode & COLNÍK Guard)**
- **AUTONOMY 6.x (Control, Guard, Triage Mode & HitL Trash Governance in `COLNIK-6.x/triage`)**

All vault operations are **strictly local‑first**, never transmitted over open networks, never cloud-synced, and never exposed to host process capture.

---

# 🧩 1. Purpose

The PASSWORD VAULT 5.9.1 module provides:

- secure offline credential storage with tamper-evident cryptographic sealing  
- deterministic access rules managed centrally by `sirius_orchestrator.py` on port 8080
- Token Guard input protection rejecting malformed injection strings (`@#$%^&*`) at entry
- compound service identification via `InputParser5` (e.g., preserving full multi-word tokens like `lokalny spravca uctu` without truncation)
- identity‑aware protection with `PanelAPI` human-in-the-loop gating (`[ÁNO/NIE]` / `[YES/NO]`) and state latching
- terminal isolation: clearing input forces immediate context release (`currentModule = "none"`), ensuring credential commands never leak into host shell commands
- OWNER‑only write and delete access  
- FAMILY read‑only access for designated household items  
- STRANGER blocked completely with instant safe-mode quarantine  
- deep symbolic explainability for every vault access attempt
- full compatibility with `KG_EXPLAIN` & `KG_EXPLAIN_DEEP` evidence trees
- **COLNIK‑validated access decisions and COLNÍK Guard shell execution checks (0.0s block on destructive commands)**
- **AUTONOMY‑aware proposal governance, Guard telemetry auditing, and HitL Safe Trash quarantine routing**

It is engineered for **maximum security**, **absolute zero-cloud reliance**, and **reproducible, audit-ready behavior**.

---

# 🔐 2. Security Model (v5.9.1)

### Cryptographic Foundation
- **AES‑256‑GCM** authenticated symmetric encryption with integrity tags  
- **PBKDF2‑HMAC‑SHA256** key derivation (600,000+ iterations)  
- cryptographically secure, random 256-bit salt per vault instance (`vault_salt.bin`)  
- deterministic decryption pipeline with memory wiping of plaintext buffers post-operation  
- atomic writing of encrypted vault containers (`vault.dat`) via temporary shadow files to prevent write corruption  

### Token Guard & Host Shell Protection
- raw vault queries pass through **Token Guard**; input sequences containing forbidden characters (`@`, `#`, `$`, `%`, `^`, `&`, `*`) are blocked at runtime entry
- vault administrative actions invoking shell diagnostics are validated against **COLNÍK Guard**:
  - **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`
  - **RISKY (Explicit Prompt):** `rm`, `kill`, `taskkill`, `del`
  - **ALLOWED:** `ps`, `mem`, `sys`, `grep`, `cat`, etc.
- file removal operations (e.g., purging stale vault backups) route through the **Human-in-the-Loop Safe Trash** pipeline for manual review (`GET /trash`), prohibiting direct unverified deletion

### Identity Rules & Policy Tiers
- **OWNER** → full access (read / write / delete / export) with optional `PanelAPI` confirmation for critical keys
- **FAMILY** → restricted read‑only access to approved shared services; modification blocked
- **STRANGER** → completely blocked; access attempts log security events and trigger safe-mode
- **Unknown Identity** → immediate lockdown, session suspension, and Guard alert dispatch

### Deep Explainability & Supervision Integration
Every vault transaction produces audit traces and operational telemetry:

- why the action was permitted or denied
- matching Identity Engine 3.1 behavioral rule
- System Agent 5 policy check record
- Security Family 5.x restriction or authorization tag
- `KG_EXPLAIN` symbolic justification
- `KG_EXPLAIN_DEEP` hierarchical proof tree
- **COLNIK‑6.x customs inspection verdict (Standard & IPC Mode)**
- **AUTONOMY 6.x proposal/confirmation log without proposal recurrence**
- **PanelAPI confirmation log (`[ÁNO/NIE]` / `[YES/NO]`) with confirmation state latching**
- **TimeCore execution timestamp (`cycle_delta()`) and Guard system metric snapshot**

---

# 🧱 3. Module Responsibilities

### Core Responsibilities
- secure credential encryption, storage, and retrieval  
- deterministic AES-256-GCM encryption/decryption execution  
- identity‑aware access control and caller verification
- safe atomic vault updates and rollbacks  
- safe credential deletion with zero-fill overwriting and HitL Safe Trash quarantine routing
- single-process orchestration via `sirius_orchestrator.py` on port 8080
- input processing via `InputParser5` preserving multi-word service labels
- trailing question mark stripping via `.rstrip("?")` to ensure exact credential key matches
- terminal decoupling: ensuring module release (`currentModule = "none"`) upon command clearing
- System Agent 5 validation and logging
- explainability trace generation for all operations
- **COLNIK‑validated access gating and COLNÍK Guard shell command control**
- **AUTONOMY‑aware proposal supervision and Guard resource tracking**

### Additional Responsibilities (v5.9.1)
- Token Guard input filter enforcement
- compound noun preservation for custom services (`InputParser5`)
- dual-language linkage: credentials can link to service entities or aliases stored in either `autosave_kg.json` (SK) or `autosave_kg_en.json` (EN)
- zero proposal recurrence: established authorizations do not trigger repeated interactive confirmation prompts
- Self‑Repair Layer 5.8 vault integrity and schema validation
- integration with the 4-Panel UI Suite dashboard on port 8080
- deterministic fallback behavior and error routing

---

# 🗂️ 4. Vault Structure

The vault resides within an isolated directory tree:

```text
vault/  
├── vault.dat                 # encrypted AES-256-GCM credential container  
├── vault_meta.json           # non-sensitive metadata & operational markers  
├── vault_salt.bin            # cryptographically secure PBKDF2 salt  
└── vault_integrity.json      # Self‑Repair Layer hash seals & integrity markers

🔄 5. Operational Workflow (v5.9.1)
User / UI Vault Command
↓
Token Guard (Entry check: reject inputs with @#$%^&*)
↓
InputParser5 (.rstrip("?") trailing punctuation stripping & noun phrase preservation)
↓
sirius_orchestrator.py (Single-Process Daemon on Port 8080 with TerminalAssistant & TimeCore)
↓
Identity Gate & Security Family 5.x Verification
├─ [STRANGER / Unknown] ──> Reject with SECURITY_LOCKDOWN & Alert Guard
↓
COLNÍK Guard Inspection
├─ [Shell Operation] ─────> Verify Command (0.0s block on format/diskpart)
├─ [Deletion Request] ────> Route to Human-in-the-Loop Safe Trash (GET /trash)
↓
PanelAPI Confirmation Latch ([ÁNO/NIE] / [YES/NO] prompt if confirmation required)
↓
Vault Engine: Decrypt Shadow Buffer ──> Perform Action ──> Atomic Save to vault.dat
↓
Zero Plaintext Memory Wipe
↓
UI State Release (currentModule = "none") & Log Telemetry via TimeCore cycle_delta()

📌 Document Status
Version: 5.9.1 (Dual-Language KG Architecture, Native Lossless Entity Merge, Ontological Habitat Reasoning & Comprehensive Security Protocol)

This document specifies the operational credential vault of SIRIUS LOCAL AI, fully unifying AES-256-GCM security, Token Guard input hygiene, COLNÍK Guard shell protection, Human-in-the-Loop Safe Trash, and single-process orchestration on port 8080.

