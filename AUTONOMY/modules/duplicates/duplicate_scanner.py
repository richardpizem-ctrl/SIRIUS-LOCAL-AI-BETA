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

    SYSTEM_EMPTY_SAFE = {
        "dir",
        "python",
        "__init__.py",
        "kg_autosave_broken.json"
    }

    def __init__(self, base_path):
        self.base_path = base_path
        self.file_index = {}      # path → hash
        self.hash_map = {}        # hash → [paths]

    # ============================================================
    # HASH FILE (OPRAVENÉ – ŽIADNE CHUNKY, ŽIADNE PRÁZDNE HASHY)
    # ============================================================
    def hash_file(self, file_path):
        """Vypočíta SHA-256 hash súboru + bezpečná EMPTY logika."""
        try:
            filename = os.path.basename(file_path).lower()

            # SYSTÉMOVÉ PRÁZDNE SÚBORY – vlastný hash
            if filename in self.SYSTEM_EMPTY_SAFE:
                sha256 = hashlib.sha256()
                sha256.update(b"SIRIUS_SYSTEM_FILE")
                return sha256.hexdigest()

            # Načítanie celého súboru
            with open(file_path, "rb") as f:
                data = f.read()

            # Prázdny súbor – vlastný hash
            if len(data) == 0:
                sha256 = hashlib.sha256()
                sha256.update(b"SIRIUS_EMPTY_FILE")
                return sha256.hexdigest()

            # Reálne hashovanie dát
            sha256 = hashlib.sha256()
            sha256.update(data)
            return sha256.hexdigest()

        except Exception as e:
            return f"ERROR_HASHING: {e}"

    # ============================================================
    # SCAN FILES
    # ============================================================
    def scan_files(self):
        """Prejde všetky súbory a vytvorí hash mapu."""
        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                full_path = os.path.join(root, file)

                file_hash = self.hash_file(full_path)

                self.file_index[full_path] = file_hash

                if file_hash not in self.hash_map:
                    self.hash_map[file_hash] = []
                self.hash_map[file_hash].append(full_path)

        return self.file_index

    # ============================================================
    # FIND DUPLICATES (OPRAVENÉ – EMPTY SA NESPAJA)
    # ============================================================
    def find_duplicates(self):
        """Nájde duplicity podľa hashov."""
        duplicates = []

        empty_hash = hashlib.sha256(b"SIRIUS_EMPTY_FILE").hexdigest()
        system_hash = hashlib.sha256(b"SIRIUS_SYSTEM_FILE").hexdigest()

        for file_hash, paths in self.hash_map.items():

            # EMPTY súbory ignorovať
            if file_hash == empty_hash:
                continue

            # SYSTÉMOVÉ prázdne ignorovať
            if file_hash == system_hash:
                continue

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
        print("[DUPLICATE_SCANNER] Spúšťam scan...")
        self.scan_files()
        duplicates = self.find_duplicates()
        print(f"[DUPLICATE_SCANNER] Nájdených duplicít: {len(duplicates)}")
        return duplicates


# ============================================================
# PRIAMY TEST
# ============================================================
if __name__ == "__main__":
    scanner = DuplicateScanner(base_path="C:\\SIRIUS_ARCHIVE\\COLNIK-6.x")
    result = scanner.run()

    print("\n=== DUPLICITY ===")
    for item in result:
        print(f"\nHASH: {item['hash']}")
        for f in item["files"]:
            print(f" - {f}")
