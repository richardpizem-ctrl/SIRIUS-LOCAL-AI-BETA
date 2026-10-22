# 🛃 COLNÍK 6.x — Customs & Security Validation Layer  
**Status:** ✔ Production-Enhanced  
**Version:** 6.x (Updated for Runtime 5.9.5 UNIFIED)  
**Component:** COLNÍK  
**Role:** Core security gatekeeper, IPC gateway, terminal command validator, Token Guard filter, quarantine rotator, SafeRollback protector, Professor Validator coordinator, and Human-in-the-Loop (HitL) Safe Trash supervisor.

---

## 🎯 1. Purpose  
The COLNÍK 6.x module is the mission-critical security and customs inspection gateway of the SIRIUS Local AI ecosystem (v5.9.5).  
Its primary mission is to intercept, audit, filter, and validate all incoming terminal commands, IPC messages, knowledge mutations, and file operations before they interact with the core runtime or persistent disk storage.

COLNÍK 6.x guarantees zero unauthorized system modifications, enforces strict command blacklists (0.0s hard blocks), manages the 100-file sliding window quarantine rotation, supervises SafeRollback crash resilience, coordinates Professor Validator decisions, and implements non-destructive Human-in-the-Loop (HitL) Safe Trash governance.

---

## 🧩 Architecture Overview  
**User Input / IPC Request (Port 8080) → Token Guard (@#\$%^&*) → COLNÍK Guard (Command Categorization) → Professor Validator (PASS/WARN/REJECT) → SafeRollback Protection → IPC Handshake (Standard & High-Performance Mode) → Workflow Engine / Dual-Language KG Commit**

### Core Responsibilities  
- **Token Guard Sanitization:** Immediate entry-level rejection of malformed or malicious symbolic inputs containing forbidden characters (`@#$%^&*`).
- **COLNÍK Guard Shell Security:** Real-time categorization of terminal inputs with instant 0.0s hard blocks on destructive routines (`format`, `diskpart`, `rmdir /s`).
- **Professor Validator Middleware:** Strict decision verification matrix (`PASS / WARN / REJECT`) evaluating all cognitive outputs before UI rendering.
- **SafeRollback Crash Resilience:** Granular module-level backups (`shutil.copytree`) and instant restorations (`shutil.rmtree`) ensuring absolute state integrity.
- **Human-in-the-Loop Safe Trash:** Rerouting all requested file removals into isolated quarantine storage awaiting manual user confirmation (`GET /trash`).
- **Quarantine Sliding-Window Rotation:** Automatically maintaining a strict 100-file ceiling inside `COLNIK-6.x/envoy/quarantine/` via automated pruning upon new arrivals.
- **Dual-Language IPC Gateway:** Orchestrating secure communications between the single-process HTTP IPC daemon (port 8080) and isolated Slovak (`autosave_kg.json`) / English (`autosave_kg_en.json`) knowledge graphs.

---

## 🛡️ 2. Security Rules & Command Matrix

### **Command Access Classification**
- 🛑 **FORBIDDEN (0.0s Hard Block):** `format`, `rmdir /s`, `del /f /s /q c:`, `diskpart`, `drop database`, fork-bombs.
- ⚠️ **RISKY (Explicit Prompt Required):** `rm`, `kill`, `taskkill`, `del`.
- ✅ **ALLOWED:** `ps`, `top`, `mem`, `sys`, `grep`, `info`, `cat`, `head`, `tail`, `check`, `template`, `python`, `git`, `pip`, `ls`, `dir`, `cd`, `pwd`, `mkdir`, `touch`, `help`.

---

## 📊 3. Module Status (v5.9.5)
- ✔ Fully updated & verified for Runtime 5.9.5 architecture  
- ✔ Dual-Language Graph Isolation (`autosave_kg.json` & `autosave_kg_en.json`) active  
- ✔ Token Guard input filtering operational  
- ✔ COLNÍK Guard shell security (0.0s hard block) active  
- ✔ SafeRollback backup & restore module integrated  
- ✔ Professor Validator decision matrix (`PASS / WARN / REJECT`) active  
- ✔ Human-in-the-Loop Safe Trash pipeline active  
- ✔ Envoy quarantine sliding-window rotation (100-file ceiling) active  
- ✔ Single-process IPC bridge on port 8080 synchronized
