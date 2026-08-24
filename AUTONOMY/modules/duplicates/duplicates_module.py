import os
import json
from datetime import datetime

# importujeme scanner z PILIERA 5
from AUTONOMY.modules.duplicates.duplicate_scanner import DuplicateScanner


class DuplicatesModule:
    """
    AUTONOMY MODULE – PILIER 5
    --------------------------
    - volá duplicate_scanner.py
    - spracuje duplicity
    - vytvorí návrhy pre Guard
    - vráti návrhy autonómii
    """

    def __init__(self, base_path="C:\\SIRIUS_ARCHIVE\\COLNIK-6.x"):
        self.base_path = base_path
        self.scanner = DuplicateScanner(base_path)

    # ============================================================
    # GENERATE PROPOSALS
    # ============================================================
    def generate_proposals(self, duplicates):
        """
        Pre každú duplicitu vytvorí návrh pre autonómiu.
        Návrhy sú jednoduché – zatiaľ len DELETE_DUPLICATE.
        Guard neskôr rozhodne, či je akcia bezpečná.
        """

        proposals = []

        for item in duplicates:
            file_hash = item["hash"]
            files = item["files"]

            # ak sú duplicity v rovnakom priečinku → návrh DELETE
            # ak sú v rôznych priečinkoch → návrh MOVE (neskôr)
            action_type = "DELETE_DUPLICATE"

            proposal = {
                "proposal_id": f"duplicate-{file_hash}",
                "module": "duplicates",
                "type": "DUPLICATE_FILE",
                "action": action_type,
                "payload": {
                    "hash": file_hash,
                    "files": files,
                    "count": len(files),
                    "reason": "Duplicate files detected by PILIER 5"
                },
                "priority": "MEDIUM",
                "timestamp": str(datetime.now())
            }

            proposals.append(proposal)

        return proposals

    # ============================================================
    # RUN MODULE
    # ============================================================
    def run(self):
        """
        Spustí celý modul:
        - scan
        - hash
        - detekcia duplicít
        - generovanie návrhov
        """

        print("[DUPLICATES_MODULE] Spúšťam PILIER 5 – SCAN + HASH...")
        duplicates = self.scanner.run()

        print(f"[DUPLICATES_MODULE] Nájdených duplicít: {len(duplicates)}")

        proposals = self.generate_proposals(duplicates)

        print(f"[DUPLICATES_MODULE] Vytvorených návrhov: {len(proposals)}")

        return proposals


# ============================================================
# PRIAMY TEST (voliteľné)
# ============================================================
if __name__ == "__main__":
    module = DuplicatesModule()
    result = module.run()

    print("\n=== NÁVRHY AUTONÓMIE ===")
    for p in result:
        print(json.dumps(p, indent=4))
