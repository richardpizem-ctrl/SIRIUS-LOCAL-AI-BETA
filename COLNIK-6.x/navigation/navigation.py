# NAVIGATION MODULE – AUTONOMY 6.x
# PILIER 3 – autonómia navigácie
# Tento modul generuje návrhy na otvorenie systémových nástrojov.
# Autonómia nikdy nesmie otvárať OS priamo.
# Všetko musí ísť cez proposer → JSON → COLNÍK → Workflow → OS.

import time
import os
import json
from timecore import TimeCore

# === AUTONOMY STATE FILE ===
AUTONOMY_STATE = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\autonomy_state.json"


def load_autonomy_state():
    """Načíta stav autonómie zo súboru autonomy_state.json."""
    if not os.path.exists(AUTONOMY_STATE):
        default_state = {
            "last_snapshot_hash": None,
            "last_navigation": [],
            "last_proposals": [],
            "last_trends": {}
        }
        with open(AUTONOMY_STATE, "w", encoding="utf-8") as f:
            json.dump(default_state, f, indent=2)
        return default_state

    try:
        with open(AUTONOMY_STATE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        default_state = {
            "last_snapshot_hash": None,
            "last_navigation": [],
            "last_proposals": [],
            "last_trends": {}
        }
        with open(AUTONOMY_STATE, "w", encoding="utf-8") as f:
            json.dump(default_state, f, indent=2)
        return default_state


class Navigation:

    def __init__(self):
        self.timecore = TimeCore()
        self.timecore.runtime_start()

    def propose_navigation(self):
        """
        Generuje návrhy navigácie (otvorenie systémových nástrojov).
        Toto je PILIER 3 – autonómia navigácie.
        Navigácia sa generuje iba ak sa systém zmenil a ešte nebola vykonaná.
        """

        # === LOAD AUTONOMY STATE ===
        state = load_autonomy_state()
        last_nav = state.get("last_navigation", [])

        # === Ak autonómia už navigáciu generovala, preskakujeme ===
        if last_nav:
            print("[NAVIGATION] Navigácia už bola generovaná – preskakujem.")
            return []

        self.timecore.cycle_start()
        proposals = []

        # ============================
        # PRIESKUMNÍK (WIN+E)
        # ============================
        proposals.append({
            "proposal_id": "nav-open_explorer",
            "module": "navigation",
            "type": "NAVIGATION_TASK",
            "action": "OPEN",
            "target": "explorer.exe",
            "payload": {"task": "OPEN_EXPLORER", "subaction": "OPEN"},
            "priority": "LOW"
        })

        # ============================
        # NASTAVENIA (WIN+I)
        # ============================
        proposals.append({
            "proposal_id": "nav-open_settings",
            "module": "navigation",
            "type": "NAVIGATION_TASK",
            "action": "OPEN",
            "target": "ms-settings:",
            "payload": {"task": "OPEN_SETTINGS", "subaction": "OPEN"},
            "priority": "LOW"
        })

        # ============================
        # OVLÁDACÍ PANEL (control.exe)
        # ============================
        proposals.append({
            "proposal_id": "nav-open_control_panel",
            "module": "navigation",
            "type": "NAVIGATION_TASK",
            "action": "OPEN",
            "target": "control.exe",
            "payload": {"task": "OPEN_CONTROL_PANEL", "subaction": "OPEN"},
            "priority": "LOW"
        })

        # ============================
        # SIEŤOVÉ PRIPOJENIA (ncpa.cpl)
        # ============================
        proposals.append({
            "proposal_id": "nav-open_network_connections",
            "module": "navigation",
            "type": "NAVIGATION_TASK",
            "action": "OPEN",
            "target": "ncpa.cpl",
            "payload": {"task": "OPEN_NETWORK_CONNECTIONS", "subaction": "OPEN"},
            "priority": "LOW"
        })

        # ============================
        # SPRÁVA DISKOV (diskmgmt.msc)
        # ============================
        proposals.append({
            "proposal_id": "nav-open_disk_management",
            "module": "navigation",
            "type": "NAVIGATION_TASK",
            "action": "OPEN",
            "target": "diskmgmt.msc",
            "payload": {"task": "OPEN_DISK_MANAGEMENT", "subaction": "OPEN"},
            "priority": "LOW"
        })

        # ============================
        # SPRÁVCA ZARIADENÍ (devmgmt.msc)
        # ============================
        proposals.append({
            "proposal_id": "nav-open_device_manager",
            "module": "navigation",
            "type": "NAVIGATION_TASK",
            "action": "OPEN",
            "target": "devmgmt.msc",
            "payload": {"task": "OPEN_DEVICE_MANAGER", "subaction": "OPEN"},
            "priority": "LOW"
        })

        # === TIMECORE END ===
        cycle_time = self.timecore.cycle_delta()
        self.timecore.cycle_end()

        # doplnenie cycle_time
        for p in proposals:
            p["cycle_time"] = cycle_time

        return proposals
