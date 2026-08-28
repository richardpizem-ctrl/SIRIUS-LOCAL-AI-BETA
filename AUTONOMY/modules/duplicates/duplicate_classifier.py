"""
Duplicate Classifier – PILIER 5 (FÁZA 3)
----------------------------------------
Účel:
    - Rozhodnúť, či je duplicita bezpečná, kritická, systémová, modulová,
      prázdna, alebo legitímna.
    - Scanner nájde duplicity → classifier rozhodne → duplicates_module
      vytvorí správny typ návrhu.

Výstup:
    {
        "hash": "...",
        "files": [...],
        "category": "SAFE | SYSTEM | MODULE | EMPTY | KG | CRITICAL | UNKNOWN",
        "decision": "IGNORE | REPORT_ONLY | ARCHIVE | QUARANTINE",
        "reason": "text"
    }
"""

import os

class DuplicateClassifier:

    def __init__(self):
        # Kritické cesty – nikdy nemazať
        self.critical_paths = [
            "AUTONOMY",
            "core",
            "guard",
            "modules",
            "system_info",
            "SIRIUS_MODULES",
            "timecore",
            "workflow"
        ]

        # Súbory, ktoré sú legitímne prázdne
        self.empty_legit_files = [
            "__init__.py",
            "module.txt",
            "notepad"
        ]

        # KG súbory
        self.kg_files = [
            "kg_autosave.json",
            "kg_autosave_BROKEN.json",
            "kg_export.json"
        ]

    # ---------------------------------------------------------
    # Pomocné funkcie
    # ---------------------------------------------------------

    def is_empty_file(self, path):
        try:
            return os.path.getsize(path) == 0
        except:
            return False

    def is_critical_path(self, path):
        for c in self.critical_paths:
            if c.lower() in path.lower():
                return True
        return False

    def is_legit_empty(self, path):
        name = os.path.basename(path)
        return name in self.empty_legit_files

    def is_kg_file(self, path):
        name = os.path.basename(path)
        return name in self.kg_files

    # ---------------------------------------------------------
    # Hlavná klasifikácia duplicity
    # ---------------------------------------------------------

    def classify(self, hash_value, files):
        """
        Vráti kategóriu duplicity a rozhodnutie autonómie.
        """

        # 1. Prázdne súbory
        if all(self.is_empty_file(f) for f in files):
            if all(self.is_legit_empty(f) for f in files):
                return {
                    "hash": hash_value,
                    "files": files,
                    "category": "EMPTY",
                    "decision": "IGNORE",
                    "reason": "Legitímne prázdne súbory (__init__.py, module.txt)"
                }
            else:
                return {
                    "hash": hash_value,
                    "files": files,
                    "category": "EMPTY",
                    "decision": "ARCHIVE",
                    "reason": "Prázdne súbory – odporúča sa archivácia"
                }

        # 2. KG súbory
        if any(self.is_kg_file(f) for f in files):
            return {
                "hash": hash_value,
                "files": files,
                "category": "KG",
                "decision": "REPORT_ONLY",
                "reason": "KG súbory sa nikdy automaticky nemazú"
            }

        # 3. Kritické systémové cesty
        if any(self.is_critical_path(f) for f in files):
            return {
                "hash": hash_value,
                "files": files,
                "category": "CRITICAL",
                "decision": "REPORT_ONLY",
                "reason": "Duplicita v kritickom module – autonómia nesmie mazať"
            }

        # 4. Modulové duplicity
        if any("modules" in f.lower() for f in files):
            return {
                "hash": hash_value,
                "files": files,
                "category": "MODULE",
                "decision": "IGNORE",
                "reason": "Modulové duplicity sú legitímne"
            }

        # 5. Bezpečné duplicity (napr. testovacie súbory)
        # DELETE_SAFE je teraz zakázané → REPORT_ONLY
        return {
            "hash": hash_value,
            "files": files,
            "category": "SAFE",
            "decision": "REPORT_ONLY",
            "reason": "Bezpečná duplicita – ale automatické mazanie je zakázané"
        }
