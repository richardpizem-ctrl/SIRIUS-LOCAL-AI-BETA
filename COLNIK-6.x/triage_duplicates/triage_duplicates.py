# SIRIUS COLNIK-6.x — Triage Duplicates Module (FINAL + TIMECORE)
# This module detects duplicate files, folders, or KG entities.

import os
from timecore import TimeCore   # <<< TIMECORE

class TriageDuplicates:
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

    def list_files(self):
        """Return a list of files inside the base path."""
        self.timecore.cycle_start()   # <<< TIMECORE START

        try:
            files = [
                f for f in os.listdir(self.base_path)
                if os.path.isfile(os.path.join(self.base_path, f))
            ]

            self.timecore.cycle_end()   # <<< TIMECORE END

            return {
                "status": "OK",
                "files": files,
                "cycle_time": self.timecore.cycle_delta()
            }

        except Exception as e:
            self.timecore.cycle_end()
            return {
                "status": "ERROR",
                "message": str(e),
                "cycle_time": self.timecore.cycle_delta()
            }

    def scan_for_duplicates(self):
        """
        Basic duplicate detection:
        - duplicate filenames
        - duplicate file sizes
        """

        self.timecore.cycle_start()   # <<< TIMECORE START

        try:
            result = self.list_files()
            if result["status"] != "OK":
                self.timecore.cycle_end()
                return {
                    "status": "ERROR",
                    "message": result["message"],
                    "cycle_time": self.timecore.cycle_delta()
                }

            files = result["files"]
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

            self.timecore.cycle_end()

            return {
                "status": "OK",
                "duplicates": duplicates,
                "cycle_time": self.timecore.cycle_delta()
            }

        except Exception as e:
            self.timecore.cycle_end()
            return {
                "status": "ERROR",
                "message": str(e),
                "cycle_time": self.timecore.cycle_delta()
            }

    def scan(self):
        """Placeholder for scanning logic."""
        self.timecore.cycle_start()
        self.timecore.cycle_end()
        return {
            "status": "NOT_IMPLEMENTED",
            "message": "Scan logic not implemented yet.",
            "cycle_time": self.timecore.cycle_delta()
        }
