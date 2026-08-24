import os
import hashlib
from datetime import datetime

class DuplicateScanner:
    """
    PILIER 5 – FÁZA 1
    SCAN + HASH ENGINE
    -------------------
    - prejde všetky súbory v COLNIK-6.x
    - vytvorí index súborov
    - vypočíta SHA-256 hash
    - vráti duplicity (hash → zoznam súborov)
    """

    def __init__(self, base_path):
        self.base_path = base_path
        self.file_index = {}      # path → hash
        self.hash_map = {}        # hash → [paths]

    # ============================================================
    # HASH FILE
    # ============================================================
    def hash_file(self, file_path):
        """Vypočíta SHA-256 hash súboru."""
        try:
            sha256 = hashlib.sha256()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            return f"ERROR_HASHING: {e}"

    # ============================================================
    # SCAN FILES
    # ============================================================
    def scan_files(self):
        """
        Prejde všetky priečinky a súbory v base_path.
        Vytvorí index súborov a hash mapu.
        """
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                full_path = os.path.join(root, file)

                # vypočítaj hash
                file_hash = self.hash_file(full_path)

                # zapíš do indexu
                self.file_index[full_path] = file_hash

                # zapíš do hash mapy
                if file_hash not in self.hash_map:
                    self.hash_map[file_hash] = []
                self.hash_map[file_hash].append(full_path)

        return self.file_index

    # ============================================================
    # FIND DUPLICATES
    # ============================================================
    def find_duplicates(self):
        """
        Nájde duplicity podľa hashov.
        Vracia zoznam:
        [
            {
                "hash": "...",
                "files": ["path1", "path2"]
            }
        ]
        """
        duplicates = []

        for file_hash, paths in self.hash_map.items():
            if len(paths) > 1:
                duplicates.append({
                    "hash": file_hash,
                    "files": paths
                })

        return duplicates

    # ============================================================
    # RUN SCAN
    # ============================================================
    def run(self):
        """
        Kompletný beh FÁZY 1:
        - scan
        - hash
        - detekcia duplicít
        """
        print("[DUPLICATE_SCANNER] Spúšťam scan...")
        self.scan_files()
        duplicates = self.find_duplicates()
        print(f"[DUPLICATE_SCANNER] Nájdených duplicít: {len(duplicates)}")
        return duplicates


# ============================================================
# PRIAMY TEST (voliteľné)
# ============================================================
if __name__ == "__main__":
    scanner = DuplicateScanner(base_path="C:\\SIRIUS_ARCHIVE\\COLNIK-6.x")
    result = scanner.run()

    print("\n=== DUPLICITY ===")
    for item in result:
        print(f"\nHASH: {item['hash']}")
        for f in item["files"]:
            print(f" - {f}")
