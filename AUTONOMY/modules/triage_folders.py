# TRIAGE FOLDERS – AUTONOMY 6.x
# Identifikácia priečinkov + návrhy reorganizácie

import os

class TriageFolders:

    def __init__(self):
        pass

    def classify_folder(self, path):
        """
        Jednoduchá klasifikácia priečinka podľa obsahu.
        """
        try:
            items = os.listdir(path)
        except Exception:
            return "unknown"

        if not items:
            return "empty"

        file_count = len([f for f in items if os.path.isfile(os.path.join(path, f))])
        folder_count = len([f for f in items if os.path.isdir(os.path.join(path, f))])

        if file_count > 100:
            return "heavy"

        if folder_count > 20:
            return "complex"

        return "normal"

    def propose_triage(self, path):
        """
        Generuje návrhy reorganizácie priečinka.
        """
        folder_type = self.classify_folder(path)
        proposals = []

        # === EMPTY FOLDER → DELETE ===
        if folder_type == "empty":
            proposals.append({
                "proposal_id": "triage-delete-folder",
                "action": "DELETE",
                "target": path,
                "payload": {"reason": "empty_folder"},
                "priority": "LOW"
            })

        # === HEAVY FOLDER → MOVE ===
        if folder_type == "heavy":
            proposals.append({
                "proposal_id": "triage-move-heavy",
                "action": "MOVE",
                "target": path,
                "payload": {"destination": "C:\\ARCHIVE_HEAVY"},
                "priority": "MEDIUM"
            })

        # === COMPLEX FOLDER → REORGANIZE ===
        if folder_type == "complex":
            proposals.append({
                "proposal_id": "triage-reorg-complex",
                "action": "REORGANIZE",
                "target": path,
                "payload": {"strategy": "split_subfolders"},
                "priority": "MEDIUM"
            })

        return proposals
