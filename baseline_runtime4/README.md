# File: baseline_runtime4/README.md
# Version: 4.5.0
# Purpose: Stores known‑good baseline copies of runtime4 modules

This directory contains clean, verified baseline versions of all
runtime4 modules. The Self‑Repair Layer uses these files to restore
corrupted or missing components during automatic repair.

Populate this folder with exact, unmodified copies of:

- src/runtime4/core/*
- src/runtime4/self_repair/*
- src/runtime4/security/*
- src/runtime4/health/*
- src/runtime4/processing/*
- src/runtime4/ui/*
- any other runtime4 modules required by the system

IMPORTANT:
All files here must remain unchanged.
They represent the "golden baseline" used for integrity comparison
and automatic module restoration.
