# TRIAGE FOLDERS – AUTONOMY 6.x (SUPER-FINAL FIXED)
# Identifikácia priečinkov + návrhy reorganizácie
# Opravené: case-insensitive porovnávanie, žiadne falošné MOVE pre ARCHIVE vs archive

import os

class TriageFolders:

    def __init__(self, base_path=None):
        # === DEFINITÍVNA OPRAVA ROOTU ===
        if base_path is None:
            base_path = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x"

        self.base_path = base_path

    def classify_folder(self, path):
        try:
            items = os.listdir(path)
        except Exception:
            return "unknown"

        if not items:
            return "empty"

        file_count = len([
            f for f in items
            if os.path.isfile(os.path.join(path, f))
        ])
        folder_count = len([
            f for f in items
            if os.path.isdir(os.path.join(path, f))
        ])

        if file_count > 100:
            return "heavy"

        if folder_count > 20:
            return "complex"

        return "normal"

    def propose_triage(self, path):
        folder_type = self.classify_folder(path)
        proposals = []

        # === CASE-INSENSITIVE FIX ===
        # ARCHIVE == archive == Archive == ArChIvE
        folder_name = os.path.basename(path)
        folder_lower = folder_name.lower()

        # === ARCHIVE folder must NEVER generate MOVE ===
        if folder_lower == "archive":
            return proposals

        # === EMPTY FOLDER ===
        if folder_type == "empty":
            proposals.append({
                "proposal_id": "triage-delete-folder",
                "action": "DELETE",
                "target": path,
                "payload": {"reason": "empty_folder"},
                "priority": "LOW"
            })

        # === HEAVY FOLDER ===
        if folder_type == "heavy":
            proposals.append({
                "proposal_id": "triage-move-heavy",
                "action": "MOVE",
                "target": path,
                "payload": {
                    "destination": os.path.join(self.base_path, "ARCHIVE_HEAVY")
                },
                "priority": "MEDIUM"
            })

        # === COMPLEX FOLDER ===
        if folder_type == "complex":
            proposals.append({
                "proposal_id": "triage-reorg-complex",
                "action": "REORGANIZE",
                "target": path,
                "payload": {"strategy": "split_subfolders"},
                "priority": "MEDIUM"
            })

        return proposals
