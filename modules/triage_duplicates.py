# TRIAGE DUPLICATES – SAFE VERSION
# NEHASHUJE CELÝ DISK, LEN MALÉ PRIEČINKY
# MAX 200 SÚBOROV

import os
import hashlib

class TriageDuplicates:

    def __init__(self):
        pass

    def file_hash(self, path):
        try:
            h = hashlib.sha256()
            with open(path, "rb") as f:
                while chunk := f.read(8192):
                    h.update(chunk)
            return h.hexdigest()
        except Exception:
            return None

    def scan_folder(self, path):
        duplicates = {}
        files_scanned = 0

        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    full = os.path.join(root, file)

                    # LIMIT — MAX 200 SÚBOROV
                    files_scanned += 1
                    if files_scanned > 200:
                        print("[TRIAGE_DUPLICATES] STOP — TOO MANY FILES")
                        return {}

                    h = self.file_hash(full)
                    if not h:
                        continue

                    if h not in duplicates:
                        duplicates[h] = []
                    duplicates[h].append(full)

        except Exception:
            return {}

        return duplicates

    def propose_duplicates(self, path):
        # NEPOVOLENÉ: C:\ — PRÍLIŠ VEĽKÉ
        if path == "C:\\":
            print("[TRIAGE_DUPLICATES] SKIPPED — ROOT TOO LARGE")
            return []

        duplicates = self.scan_folder(path)
        proposals = []

        for h, files in duplicates.items():
            if len(files) <= 1:
                continue

            keep = files[0]
            dups = files[1:]

            for f in dups:
                proposals.append({
                    "proposal_id": "triage-duplicate-move",
                    "action": "MOVE",
                    "target": f,
                    "payload": {
                        "destination": "C:\\SIRIUS_DUPLICATES_BIN",
                        "original": keep
                    },
                    "priority": "MEDIUM"
                })

        return proposals
