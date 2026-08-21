# AUTONOMY MODULE – NAVIGATION 6.x
# Tento modul generuje návrhy na otvorenie systémových nástrojov.
# Autonómia nikdy nesmie otvárať OS priamo.
# Všetko musí ísť cez proposer → JSON → COLNÍK → Workflow → OS.

import time
from timecore import TimeCore

class Navigation:

    def __init__(self):
        self.timecore = TimeCore()
        self.timecore.runtime_start()

    def propose_navigation(self):
        """
        Generuje návrhy navigácie (otvorenie systémových nástrojov).
        Toto je PILIER 3 – autonómia navigácie.
        """

        self.timecore.cycle_start()
        proposals = []

        # ============================
        # PRIESKUMNÍK (WIN+E)
        # ============================
        proposals.append({
            "proposal_id": f"nav-open-explorer-{time.time()}",
            "module": "navigation",
            "action": "OPEN",
            "target": "explorer.exe",
            "reason": "Otvorenie Prieskumníka",
            "priority": "LOW",
            "cycle_time": None
        })

        # ============================
        # NASTAVENIA (WIN+I)
        # ============================
        proposals.append({
            "proposal_id": f"nav-open-settings-{time.time()}",
            "module": "navigation",
            "action": "OPEN",
            "target": "ms-settings:",
            "reason": "Otvorenie Nastavení",
            "priority": "LOW",
            "cycle_time": None
        })

        # ============================
        # SPRÁVCA ÚLOH (CTRL+SHIFT+ESC)
        # ============================
        proposals.append({
            "proposal_id": f"nav-open-taskmanager-{time.time()}",
            "module": "navigation",
            "action": "OPEN",
            "target": "taskmgr.exe",
            "reason": "Otvorenie Správcu úloh",
            "priority": "LOW",
            "cycle_time": None
        })

        # ============================
        # OVLÁDACÍ PANEL (control.exe)
        # ============================
        proposals.append({
            "proposal_id": f"nav-open-controlpanel-{time.time()}",
            "module": "navigation",
            "action": "OPEN",
            "target": "control.exe",
            "reason": "Otvorenie Ovládacieho panela",
            "priority": "LOW",
            "cycle_time": None
        })

        # ============================
        # SIEŤOVÉ PRIPOJENIA (ncpa.cpl)
        # ============================
        proposals.append({
            "proposal_id": f"nav-open-network-{time.time()}",
            "module": "navigation",
            "action": "OPEN",
            "target": "ncpa.cpl",
            "reason": "Otvorenie Sieťových pripojení",
            "priority": "LOW",
            "cycle_time": None
        })

        # ============================
        # SPRÁVA DISKOV (diskmgmt.msc)
        # ============================
        proposals.append({
            "proposal_id": f"nav-open-diskmgmt-{time.time()}",
            "module": "navigation",
            "action": "OPEN",
            "target": "diskmgmt.msc",
            "reason": "Otvorenie Správy diskov",
            "priority": "LOW",
            "cycle_time": None
        })

        # ============================
        # SPRÁVCA ZARIADENÍ (devmgmt.msc)
        # ============================
        proposals.append({
            "proposal_id": f"nav-open-devicemanager-{time.time()}",
            "module": "navigation",
            "action": "OPEN",
            "target": "devmgmt.msc",
            "reason": "Otvorenie Správcu zariadení",
            "priority": "LOW",
            "cycle_time": None
        })

        # TIMECORE END
        cycle_time = self.timecore.cycle_delta()
        self.timecore.cycle_end()

        # doplnenie cycle_time
        for p in proposals:
            p["cycle_time"] = cycle_time

        return proposals
