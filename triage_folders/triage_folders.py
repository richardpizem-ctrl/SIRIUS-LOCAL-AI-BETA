# SIRIUS COLNIK-6.x — Triage Folders Module (FINAL)
# PILIER 4 — TRIAZ PRIEČINKOV
# Autonómia identifikuje typ priečinka, navrhne presun, ale nikdy nekoná sama.

import os
from kg.kg_core import KGCore
from timecore import TimeCore

# === IMPORTUJ PRAVIDLÁ PILIERA 4 ===
from triage_folders.triage_folder_rules import FOLDER_TYPES, FOLDER_DESTINATIONS, TRIAGE_FOLDER_RULES

kg = KGCore()


class TriageFolders:
    def __init__(self, base_path: str = None):
        """
        base_path je voliteľný.
        Ak nie je zadaný, automaticky sa nastaví na aktuálny COLNIK-6.x priečinok.
        """
        self.timecore = TimeCore()
        self.timecore.runtime_start()

        if base_path is None:
            base_path = os.getcwd()
        self.base_path = base_path

        # === KG: pridaj root folder ako entitu ===
        kg.add_entity(self.base_path, {
            "type": "folder",
            "root": True,
            "triage_timestamp": self.timecore.timestamp()
        })

    # ============================================================
    # LIST FOLDERS
    # ============================================================
    def list_folders(self):
        """Return a list of folders inside the base path."""
        self.timecore.cycle_start()

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

            self.timecore.cycle_end()
            return folders

        except Exception as e:
            self.timecore.cycle_end()
            return f"[TRIAGE_FOLDERS] Error: {e}"

    # ============================================================
    # IDENTIFIKÁCIA TYPU PRIEČINKA
    # ============================================================
    def detect_folder_type(self, folder_name: str):
        """Zistí typ priečinka podľa názvu — už podľa PRAVIDIEL PILIERA 4."""
        for folder_type, keywords in FOLDER_TYPES.items():
            for keyword in keywords:
                if keyword.lower() == folder_name.lower():
                    return folder_type
        return "unknown"

    # ============================================================
    # TRIAZ PRIEČINKOV — HLAVNÁ LOGIKA PILIERA 4
    # ============================================================
    def triage(self):
        """
        Hlavná logika TRIAZ priečinkov.
        Autonómia identifikuje typ priečinka a navrhne presun.
        """
        self.timecore.cycle_start()
        proposals = []

        folders = self.list_folders()
        if isinstance(folders, str):
            return folders  # error

        for folder in folders:
            full_path = os.path.join(self.base_path, folder)
            folder_type = self.detect_folder_type(folder)

            # === KG: zapis typ priečinka ===
            kg.add_entity(full_path, {
                "detected_type": folder_type,
                "triage_timestamp": self.timecore.timestamp()
            })

            # === UNKNOWN → návrh na kategorizáciu ===
            if folder_type == "unknown":
                proposals.append({
                    "proposal_id": f"triage-unknown-{folder}",
                    "module": "triage_folders",
                    "type": "TRIAGE_FOLDER",
                    "action": "CLASSIFY",
                    "target": full_path,
                    "payload": {
                        "folder": folder,
                        "reason": "Unknown folder type",
                        "suggestion": "CLASSIFY_FOLDER"
                    },
                    "priority": "LOW"
                })
                continue

            # === Zisti správnu destináciu ===
            expected_destination = FOLDER_DESTINATIONS.get(folder_type)

            if expected_destination is None:
                continue

            # === Ak priečinok nie je na správnom mieste → návrh presunu ===
            correct_path = os.path.join(self.base_path, expected_destination)

            if expected_destination != "." and not full_path.startswith(correct_path):
                proposals.append({
                    "proposal_id": f"triage-move-{folder}",
                    "module": "triage_folders",
                    "type": "TRIAGE_FOLDER",
                    "action": "MOVE",
                    "target": full_path,
                    "payload": {
                        "folder": folder,
                        "detected_type": folder_type,
                        "expected_destination": correct_path,
                        "reason": "Folder is not in correct location",
                        "suggestion": "MOVE_TO_CORRECT_LOCATION"
                    },
                    "priority": "MEDIUM"
                })

        self.timecore.cycle_end()
        return proposals

    # ============================================================
    # REQUIRED FOLDERS CHECK
    # ============================================================
    def check_required_folders(self):
        """Check if required folders exist."""
        self.timecore.cycle_start()

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

        self.timecore.cycle_end()
        return missing

    # ============================================================
    # PLACEHOLDERS (NECHÁVAME PRE PILIER 5 A 6)
    # ============================================================
    def validate_structure(self):
        self.timecore.cycle_start()
        self.timecore.cycle_end()
        return "[TRIAGE_FOLDERS] Structure validation not implemented yet."

    def scan(self):
        self.timecore.cycle_start()
        self.timecore.cycle_end()
        return "[TRIAGE_FOLDERS] Scan logic not implemented yet."
