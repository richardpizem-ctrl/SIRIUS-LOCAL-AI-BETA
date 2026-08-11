# SIRIUS COLNIK-6.x — Triage Duplicates Module (PRE-FINAL)
# This module detects duplicate files, folders, or KG entities.

import os

class TriageDuplicates:
    def __init__(self, base_path: str = None):
        """
        base_path je voliteľný.
        Ak nie je zadaný, automaticky sa nastaví na aktuálny COLNIK-6.x priečinok.
        """
        if base_path is None:
            base_path = os.getcwd()  # automaticky COLNIK-6.x
        self.base_path = base_path

    def list_files(self):
        """Return a list of files inside the base path."""
        try:
            return [
                f for f in os.listdir(self.base_path)
                if os.path.isfile(os.path.join(self.base_path, f))
            ]
        except Exception as e:
            return f"[TRIAGE_DUPLICATES] Error: {e}"

    def scan_for_duplicates(self):
        """
        Basic duplicate detection:
        - duplicate filenames
        - duplicate file sizes
        """
        try:
            files = self.list_files()
            seen = {}
            duplicates = []

            for f in files:
                full = os.path.join(self.base_path, f)
                size = os.path.getsize(full)

                key = (f, size)
                if key in seen:
                    duplicates.append(f)
                else:
                    seen[key] = True

            return duplicates

        except Exception as e:
            return f"[TRIAGE_DUPLICATES] Error: {e}"

    def scan(self):
        """Placeholder for scanning logic."""
        return "[TRIAGE_DUPLICATES] Scan logic not implemented yet."
