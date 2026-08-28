# NAVIGATION RULES – AUTONOMY 6.x
# PILIER 3 – stabilizované pravidlá navigácie
# Tento modul definuje:
# - kedy sa navigácia smie spustiť
# - kedy sa navigácia musí preskočiť
# - limity návrhov
# - relevance filter
# - cooldown
# - snapshot pravidlá
# - bezpečnostné obmedzenia

NAVIGATION_RULES = {

    # ============================================================
    # WORKFLOW TRANSITIONS (pôvodné pravidlá)
    # ============================================================
    "INIT": ["ANALYZE"],
    "ANALYZE": ["VALIDATE", "REJECT"],
    "VALIDATE": ["DECIDE"],
    "DECIDE": ["WORKFLOW"],
    "WORKFLOW": ["END"],

    # ============================================================
    # NAVIGATION SAFETY RULES
    # ============================================================
    "SAFETY": {
        # Autonómia nikdy nesmie otvárať OS priamo
        "direct_os_execution": False,

        # Navigácia musí ísť cez proposer → JSON → COLNÍK → Workflow → OS
        "requires_workflow_chain": True,

        # Navigácia nesmie spúšťať nebezpečné ciele
        "blocked_targets": [
            "cmd.exe",
            "powershell.exe",
            "regedit.exe",
            "taskkill.exe",
            "shutdown.exe"
        ]
    },

    # ============================================================
    # NAVIGATION COOLDOWN
    # ============================================================
    "COOLDOWN": {
        # Navigácia sa smie spustiť raz za X sekúnd
        # Navigation.py používa 600 sekúnd (10 minút)
        "cooldown_seconds": 600
    },

    # ============================================================
    # NAVIGATION PROPOSAL LIMIT
    # ============================================================
    "LIMITS": {
        # Max počet návrhov v jednom cykle
        "max_navigation_proposals": 2,

        # Povolené navigačné úlohy
        "allowed_tasks": [
            "OPEN_EXPLORER",
            "OPEN_SETTINGS"
        ],

        # Navigácie, ktoré sa majú ignorovať
        "ignored_tasks": [
            "OPEN_CONTROL_PANEL",
            "OPEN_NETWORK_CONNECTIONS",
            "OPEN_DISK_MANAGEMENT",
            "OPEN_DEVICE_MANAGER"
        ]
    },

    # ============================================================
    # NAVIGATION RELEVANCE FILTER
    # ============================================================
    "RELEVANCE": {
        # Navigácia sa má spustiť len ak:
        # - systém má problém
        # - Guard hlási issues
        # - KG hlási issues
        # - autonómia deteguje abnormalitu
        "requires_issue": True,

        # Ak sú trendy stabilné → navigácia sa preskočí
        "skip_when_stable": True,

        # Typy problémov, ktoré aktivujú navigáciu
        "issue_types": [
            "process_danger",
            "system_anomaly",
            "kg_inconsistency",
            "config_missing"
        ]
    },

    # ============================================================
    # SNAPSHOT RULES
    # ============================================================
    "SNAPSHOT": {
        # Navigácia sa má spustiť len pri zmene snapshotu systému
        "require_snapshot_change": True,

        # Ak snapshot je rovnaký → navigácia sa preskočí
        "skip_if_same_snapshot": True
    },

    # ============================================================
    # STATE MEMORY RULES
    # ============================================================
    "STATE": {
        # Navigácia si musí pamätať posledné návrhy
        "store_last_navigation": True,

        # Navigácia si musí pamätať čas posledného spustenia
        "store_last_navigation_time": True,

        # Navigácia sa nesmie spustiť dvakrát po sebe bez cooldownu
        "prevent_repeated_navigation": True
    }
}
