# NAVIGATION MODULE – AUTONOMY 6.x
# PILIER 3 – autonómia navigácie
# Tento modul generuje návrhy na otvorenie systémových nástrojov.
# Autonómia nikdy nesmie otvárať OS priamo.
# Všetko musí ísť cez proposer → JSON → COLNÍK → Workflow → OS.

import time
import os
import json
from datetime import datetime
from timecore import TimeCore

# === AUTONOMY STATE FILE ===
AUTONOMY_STATE = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\autonomy_state.json"


def load_autonomy_state():
    """Načíta stav autonómie zo súboru autonomy_state.json."""
    if not os.path.exists(AUTONOMY_STATE):
        default_state = {
            "last_snapshot_hash": None,
            "last_navigation": [],
            "last_navigation_time": None,
            "last_proposals": [],
            "last_trends": {},
            "analysis_issues": []
        }
        with open(AUTONOMY_STATE, "w", encoding="utf-8") as f:
            json.dump(default_state, f, indent=2)
        return default_state

    try:
        with open(AUTONOMY_STATE, "r", encoding="utf-8") as f:
            state = json.load(f)
    except:
        state = {
            "last_snapshot_hash": None,
            "last_navigation": [],
            "last_navigation_time": None,
            "last_proposals": [],
            "last_trends": {},
            "analysis_issues": []
        }

    # doplnenie chýbajúcich kľúčov
    if "last_navigation_time" not in state:
        state["last_navigation_time"] = None
    if "analysis_issues" not in state:
        state["analysis_issues"] = []
    if "last_trends" not in state:
        state["last_trends"] = {}

    return state


def save_autonomy_state(state):
    """Uloží stav autonómie do súboru autonomy_state.json."""
    try:
        with open(AUTONOMY_STATE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except:
        print("[NAVIGATION] Chyba pri ukladaní autonomy_state.json")


class Navigation:

    def __init__(self):
        self.timecore = TimeCore()
        self.timecore.runtime_start()
        # cooldown v sekundách (napr. 10 minút)
        self.navigation_cooldown_seconds = 600

    def _cooldown_active(self, state):
        """Skontroluje, či je navigácia v cooldown režime."""
        last_time = state.get("last_navigation_time")
        if not last_time:
            return False

        try:
            last_dt = datetime.fromisoformat(last_time)
        except:
            return False

        now = datetime.utcnow()
        delta = (now - last_dt).total_seconds()
        return delta < self.navigation_cooldown_seconds

    def _trends_stable(self, state):
        """Skontroluje, či sú trendy stabilné (CPU/RAM/disk)."""
        trends = state.get("last_trends", {})
        if not trends:
            return False

        cpu = trends.get("cpu")
        ram = trends.get("ram")
        disk = trends.get("disk")

        return cpu == "stable" and ram == "stable" and disk == "stable"

    def _has_issues(self, state):
        """Zistí, či analýza hlási problémy (process_danger, atď.)."""
        issues = state.get("analysis_issues", [])
        return bool(issues)

    def propose_navigation(self):
        """
        Generuje návrhy navigácie (otvorenie systémových nástrojov).
        Toto je PILIER 3 – autonómia navigácie.

        Stabilizácia:
        - navigácia sa negeneruje v každom cykle (cooldown)
        - navigácia sa negeneruje, ak sú trendy stabilné a nie sú problémy
        - limit návrhov (max 2 – explorer + settings)
        """

        state = load_autonomy_state()
        last_nav = state.get("last_navigation", [])

        # === COOL DOWN: ak už navigácia prebehla nedávno, preskoč ===
        if self._cooldown_active(state):
            print("[NAVIGATION] Navigácia v cooldown režime – preskakujem.")
            return []

        # === Ak už bola navigácia generovaná v minulosti a systém je stabilný, preskoč ===
        if last_nav and self._trends_stable(state) and not self._has_issues(state):
            print("[NAVIGATION] Navigácia už bola generovaná a systém je stabilný – preskakujem.")
            return []

        # === Ak sú trendy stabilné a nie sú žiadne issues, navigáciu netreba ===
        if self._trends_stable(state) and not self._has_issues(state):
            print("[NAVIGATION] Systém je stabilný, žiadne problémy – navigáciu negenerujem.")
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

        # === LIMIT NÁVRHOV – max 2 (explorer + settings) ===
        proposals = proposals[:2]

        # === TIMECORE END ===
        cycle_time = self.timecore.cycle_delta()
        self.timecore.cycle_end()

        for p in proposals:
            p["cycle_time"] = cycle_time

        # === UPDATE AUTONOMY STATE ===
        state["last_navigation"] = [p["proposal_id"] for p in proposals]
        state["last_navigation_time"] = datetime.utcnow().isoformat()
        save_autonomy_state(state)

        print(f"[NAVIGATION] Navigačné návrhy vygenerované (count={len(proposals)}).")
        return proposals
