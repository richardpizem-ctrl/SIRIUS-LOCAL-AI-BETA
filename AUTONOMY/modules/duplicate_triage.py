import os
import hashlib

# SYSTÉMOVÉ SÚBORY, KTORÉ SA MAJÚ IGNOROVAŤ
SYSTEM_SAFE_FILES = {
    "dir",
    "python",
    "__init__.py",
    "kg_autosave_broken.json",
    "kg_autosave.json",
    "colnik_out.json"
}

# SYSTÉMOVÉ PRIEČINKY, KTORÉ SA MAJÚ IGNOROVAŤ
SYSTEM_SAFE_FOLDERS = {
    "archive",
    "dir",
    "python",
    "__pycache__",
    "kg",
    "logs",
    "ipc_data",
    "modules",
    "runtime",
    "envoy",
    "execute",
    "sirius_modules",
    "triage_folders",
    "triage_duplicates"
}

def hash_file(path):
    """Vytvorí hash súboru pre detekciu duplikátov."""
    try:
        filename = os.path.basename(path).lower()

        # === FIX 1: systémové prázdne súbory sa nehashujú ===
        if filename in SYSTEM_SAFE_FILES:
            return None

        h = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None


def build_duplicate_triage_actions(system_snapshot):
    """
    Prevod návrhu DUPLICATE_TRIAGE na konkrétne akcie.
    - nájde duplikátne súbory v root priečinku
    - pripraví návrhy na odstránenie alebo archiváciu
    NIČ NEVYKONÁ priamo – len návrhy.
    """

    actions = []

    folder_info = system_snapshot.get("folders", {})
    root = folder_info.get("root", "C:\\")
    folders_total = folder_info.get("folders_total", 0)

    # Ak folder_scan nič nenašiel, nerobíme nič
    if folders_total == 0:
        return actions

    file_hashes = {}
    duplicates = []

    # Prejdeme prvú úroveň root priečinka
    try:
        for entry in os.scandir(root):

            # === FIX 2: ignoruj systémové priečinky ===
            if entry.is_dir():
                folder_name = os.path.basename(entry.path).lower()
                if folder_name in SYSTEM_SAFE_FOLDERS:
                    continue

                # Prejdeme len prvú úroveň priečinka
                try:
                    for sub in os.scandir(entry.path):
                        if sub.is_file():
                            filename = os.path.basename(sub.path).lower()

                            # === FIX 3: ignoruj systémové súbory ===
                            if filename in SYSTEM_SAFE_FILES:
                                continue

                            file_hash = hash_file(sub.path)
                            if not file_hash:
                                continue

                            if file_hash in file_hashes:
                                duplicates.append((sub.path, file_hashes[file_hash]))
                            else:
                                file_hashes[file_hash] = sub.path
                except PermissionError:
                    continue

            # === FIX 4: ignoruj systémové súbory v root-e ===
            elif entry.is_file():
                filename = os.path.basename(entry.path).lower()
                if filename in SYSTEM_SAFE_FILES:
                    continue

                file_hash = hash_file(entry.path)
                if not file_hash:
                    continue

                if file_hash in file_hashes:
                    duplicates.append((entry.path, file_hashes[file_hash]))
                else:
                    file_hashes[file_hash] = entry.path

    except Exception:
        return actions

    # === Vytvoríme návrhy pre každý duplikát ===
    for dup, original in duplicates:

        # === FIX 5: ak je originál systémový → ignorovať ===
        if os.path.basename(original).lower() in SYSTEM_SAFE_FILES:
            continue

        # === DELETE DUPLICATE ===
        actions.append({
            "type": "FILE_ACTION",
            "action": "DELETE_DUPLICATE",
            "duplicate_path": dup,
            "original_path": original,
            "reason": "DUPLICATE_FILE",
            "metrics": {
                "duplicate_of": original
            }
        })

        # === MOVE TO ARCHIVE ===
        archive_path = os.path.join(root, "SIRIUS_ARCHIVE_TEMP")

        actions.append({
            "type": "FILE_ACTION",
            "action": "MOVE_TO_ARCHIVE",
            "duplicate_path": dup,
            "archive_path": archive_path,
            "reason": "DUPLICATE_FILE_ARCHIVE",
            "metrics": {
                "duplicate_of": original
            }
        })

    return actions
