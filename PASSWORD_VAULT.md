# 🔐 PASSWORD VAULT 5.9.0 — Secure Local Credential Module
### Fully Offline • AES‑256‑GCM • Identity‑Aware • Deterministic • Multi-Alias Ready • Single-Process Orchestrator • COLNIK‑Validated • AUTONOMY‑Supervised

PASSWORD VAULT 5.9.0 is the official secure credential storage module of  
**SIRIUS LOCAL AI — Semantic Multi-Word Parsing, Autonomous Disambiguation Triage, 4-Panel UI Suite & Multi-Alias KG Persistence Architecture 5.9.0**.

It provides **fully offline, encrypted, identity‑aware, deterministic** password and secret storage  
with strict OWNER/FAMILY/STRANGER access rules, terminal input decoupling, and complete integration with:

- Single-Process Orchestrator (`sirius_orchestrator.py` on Port 8080)  
- Multi-Word Semantic Engine (`InputParser5` preserving compound service names)  
- PanelAPI interactive loops (`[ÁNO/NIE]` confirmation prompts)  
- TimeCore temporal tracking & Guard security/resource supervision (CPU, RAM, Disk)  
- 4-Panel UI Suite (`Duplicates`, `Triage`, `Navigation`, `Terminal` with automatic `currentModule = "none"` state clearance)  
- Runtime Core 5.9.0  
- Workflow Engine 5.9.0  
- Reasoning Engine 5.9.0  
- KG_EXPLAIN & KG_EXPLAIN_DEEP (Hierarchical proof trees & XAI attribution)  
- Security Family 5.x & Identity Engine 3.1  
- System Agent 5  
- Self‑Repair Layer 5.8  
- **COLNIK‑6.x Validation Layer (Standard & High-Performance IPC Mode)**  
- **AUTONOMY 6.x (Control, Guard & Triage Mode in `COLNIK-6.x/triage`)**  

All vault operations are **strictly local‑first**, never transmitted over open networks, never cloud-synced, and never exposed to host process capture.

---

# 🧩 1. Purpose

The PASSWORD VAULT 5.9.0 module provides:

- secure offline credential storage with tamper-evident cryptographic sealing  
- deterministic access rules managed centrally by `sirius_orchestrator.py` on port 8080  
- compound service identification via `InputParser5` (e.g., preserving full multi-word tokens like `lokalny spravca uctu` without truncation)  
- identity‑aware protection with `PanelAPI` human-in-the-loop gating (`[ÁNO/NIE]`)  
- terminal isolation: clearing input forces immediate context release (`currentModule = "none"`), ensuring credential commands never leak into host shell commands  
- OWNER‑only write and delete access  
- FAMILY read‑only access for designated household items  
- STRANGER blocked completely with instant safe-mode quarantine  
- deep symbolic explainability for every vault access attempt  
- full compatibility with `KG_EXPLAIN` & `KG_EXPLAIN_DEEP` evidence trees  
- **COLNIK‑validated access decisions (Standard & High-Performance IPC Mode)**  
- **AUTONOMY‑aware proposal governance, Guard telemetry auditing, and Triage Mode containment**  

It is engineered for **maximum security**, **absolute zero-cloud reliance**, and **reproducible, audit-ready behavior**.

---

# 🔐 2. Security Model (v5.9.0)

### Cryptographic Foundation
- **AES‑256‑GCM** authenticated symmetric encryption with integrity tags  
- **PBKDF2‑HMAC‑SHA256** key derivation (600,000+ iterations)  
- cryptographically secure, random 256-bit salt per vault instance (`vault_salt.bin`)  
- deterministic decryption pipeline with memory wiping of plaintext buffers post-operation  
- atomic writing of encrypted vault containers (`vault.dat`) via temporary shadow files to prevent write corruption  

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
- **PanelAPI confirmation log (`[ÁNO/NIE]`)**  
- **TimeCore execution timestamp and Guard system metric snapshot**  

---

# 🧱 3. Module Responsibilities

### Core Responsibilities
- secure credential encryption, storage, and retrieval  
- deterministic AES-256-GCM encryption/decryption execution  
- identity‑aware access control and caller verification  
- safe atomic vault updates and rollbacks  
- safe credential deletion with zero-fill overwriting  
- single-process orchestration via `sirius_orchestrator.py`  
- input processing via `InputParser5` preserving multi-word service labels  
- terminal decoupling: ensuring module release (`currentModule = "none"`) upon command clearing  
- System Agent 5 validation and logging  
- explainability trace generation for all operations  
- **COLNIK‑validated access gating (Standard & High-Performance IPC Mode)**  
- **AUTONOMY‑aware proposal supervision and Guard resource tracking**  

### Additional Responsibilities (v5.9.0)
- compound noun preservation for custom services (`InputParser5`)  
- multi-alias linkage: credentials can link to primary service entities or aliases stored in `autosave_kg.json`  
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
