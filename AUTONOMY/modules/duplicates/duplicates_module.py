import os
import json
from datetime import datetime

# importujeme scanner z PILIERA 5
from AUTONOMY.modules.duplicates.duplicate_scanner import DuplicateScanner

# importujeme nový classifier (FÁZA 3)
from AUTONOMY.modules.duplicates.duplicate_classifier import DuplicateClassifier


class DuplicatesModule:
    """
    AUTONOMY MODULE – PILIER 5
    --------------------------
    - volá duplicate_scanner.py
    - spracuje duplicity
    - klasifikuje duplicity (FÁZA 3)
    - vytvorí bezpečné návrhy pre Guard
    - vráti návrhy autonómii
    """

    def __init__(self, base_path="C:\\SIRIUS_ARCHIVE\\COLNIK-6.x"):
        self.base_path = base_path
        self.scanner = DuplicateScanner(base_path)
        self.classifier = DuplicateClassifier()   # ← nový classifier

    # ============================================================
    # GENERATE PROPOSALS (už s classifierom)
    # ============================================================
    def generate_proposals(self, duplicates):
        """
        Pre každú duplicitu vytvorí návrh pre autonómiu.
        Teraz už podľa classifiera (FÁZA 3).
        """

        proposals = []

        for item in duplicates:
            file_hash = item["hash"]
            files = item["files"]

            # ----------------------------------------------------
            # 1. Klasifikácia duplicity
            # ----------------------------------------------------
            classification = self.classifier.classify(file_hash, files)

            category = classification["category"]
            decision = classification["decision"]
            reason = classification["reason"]

            # ----------------------------------------------------
            # 2. Mapovanie rozhodnutia classifiera na autonómiu
            # ----------------------------------------------------
            # DELETE_SAFE je teraz zablokované → REPORT_ONLY
            if decision == "DELETE_SAFE":
                decision = "REPORT_ONLY"

            action_map = {
                "IGNORE": "IGNORE_DUPLICATE",
                "DELETE_SAFE": "DELETE_DUPLICATE_SAFE",   # už sa nepoužije
                "ARCHIVE": "ARCHIVE_DUPLICATE",
                "QUARANTINE": "QUARANTINE_DUPLICATE",
                "REPORT_ONLY": "REPORT_DUPLICATE"
            }

            action_type = action_map.get(decision, "REPORT_DUPLICATE")

            # ----------------------------------------------------
            # 3. Vytvorenie návrhu
            # ----------------------------------------------------
            proposal = {
                "proposal_id": f"duplicate-{file_hash}",
                "module": "duplicates",
                "type": "DUPLICATE_FILE",
                "action": action_type,
                "payload": {
                    "hash": file_hash,
                    "files": files,
                    "count": len(files),
                    "category": category,
                    "decision": decision,
                    "reason": reason
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
        - klasifikácia duplicít (FÁZA 3)
        - generovanie bezpečných návrhov
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
