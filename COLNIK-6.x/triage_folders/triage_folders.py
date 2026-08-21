# SIRIUS COLNIK-6.x — Triage Folders Module (PRE-FINAL)
# This module inspects and organizes folder structures for COLNIK validation.

import os
from kg.kg_core import KGCore
from timecore import TimeCore   # <<< TIMECORE

kg = KGCore()

class TriageFolders:
    def __init__(self, base_path: str = None):
        """
        base_path je voliteľný.
        Ak nie je zadaný, automaticky sa nastaví na aktuálny COLNIK-6.x priečinok.
        """
        self.timecore = TimeCore()     # <<< TIMECORE
        self.timecore.runtime_start()  # <<< TIMECORE

        if base_path is None:
            base_path = os.getcwd()  # automaticky COLNIK-6.x
        self.base_path = base_path

        # === KG: pridaj root folder ako entitu ===
        kg.add_entity(self.base_path, {
            "type": "folder",
            "root": True,
            "triage_timestamp": self.timecore.timestamp()
        })

    def list_folders(self):
        """Return a list of folders inside the base path."""
        self.timecore.cycle_start()   # <<< TIMECORE

        try:
            folders = [
                f for f in os.listdir(self.base_path)
                if os.path.isdir(os.path.join(self.base_path, f))
            ]

            # === KG: pridaj všetky priečinky ===
            for folder in folders:
                full_path = os.path.join(self.base_path, folder)
                kg.add_entity(full_path, {
                    "type": "folder",
                    "triage_timestamp": self.timecore.timestamp(),
                    "triage_cycle_time": self.timecore.cycle_delta()
                })
                kg.add_relation(self.base_path, "contains", full_path)

            self.timecore.cycle_end()   # <<< TIMECORE
            return folders

        except Exception as e:
            self.timecore.cycle_end()
            return f"[TRIAGE_FOLDERS] Error: {e}"

    def check_required_folders(self):
        """Check if required folders exist."""
        self.timecore.cycle_start()   # <<< TIMECORE

        from triage_folders.triage_folder_rules import TRIAGE_FOLDER_RULES

        missing = []
        for folder in TRIAGE_FOLDER_RULES["required"]:
            full_path = os.path.join(self.base_path, folder)
            if not os.path.isdir(full_path):
                missing.append(f"Missing required folder: {folder}")

            # === KG: zapisuj required folders ===
            kg.add_entity(full_path, {
                "required": True,
                "triage_timestamp": self.timecore.timestamp(),
                "triage_cycle_time": self.timecore.cycle_delta()
            })

        self.timecore.cycle_end()   # <<< TIMECORE
        return missing

    def validate_structure(self):
        """Placeholder for folder structure validation."""
        self.timecore.cycle_start()
        self.timecore.cycle_end()
        return "[TRIAGE_FOLDERS] Structure validation not implemented yet."

    def scan(self):
        """Placeholder for scanning logic."""
        self.timecore.cycle_start()
        self.timecore.cycle_end()
        return "[TRIAGE_FOLDERS] Scan logic not implemented yet."
