# AUTONOMY/modules/navigation.py
# PILIER 3 – Autonómia navigácie (SIRIUS 6.x)
# Navigácia sa generuje iba raz – autonómia nikdy nesmie spamovať OS.

import os
import json
import time

# === AUTONOMY STATE FILE ===
AUTONOMY_STATE = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x\IPC_DATA\autonomy_state.json"

SUPPORTED_NAV_TASKS = {
    "OPEN_EXPLORER": "explorer.exe",
    "OPEN_SETTINGS": "ms-settings:",
    "OPEN_CONTROL_PANEL": "control.exe",
    "OPEN_NETWORK_CONNECTIONS": "ncpa.cpl",
    "OPEN_DISK_MANAGEMENT": "diskmgmt.msc",
    "OPEN_DEVICE_MANAGER": "devmgmt.msc"
}


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
        pass

    def propose_navigation(self):
        """
        Generuje návrhy navigačných úloh v štandarde SIRIUS 6.x.
        Autonómia nikdy nevykoná akciu sama – len navrhne.
        Navigácia sa generuje iba raz (ak ešte nebola vykonaná).
        """

        # === LOAD AUTONOMY STATE ===
        state = load_autonomy_state()
        last_nav = state.get("last_navigation", [])

        # === Ak autonómia už navigáciu generovala, preskakujeme ===
        if last_nav:
            print("[NAVIGATION] Navigácia už bola vykonaná – preskakujem.")
            return []

        proposals = []

        for task_key, command in SUPPORTED_NAV_TASKS.items():
            proposals.append({
                "proposal_id": f"nav-{task_key.lower()}",
                "type": "NAVIGATION_TASK",
                "action": "OPEN",
                "target": command,
                "payload": {
                    "task": task_key,
                    "subaction": "OPEN"
                },
                "priority": "LOW"
            })

        return proposals
