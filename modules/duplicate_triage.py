import os
import hashlib

def hash_file(path):
    """Vytvorí hash súboru pre detekciu duplikátov."""
    try:
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
            if entry.is_file():
                file_path = entry.path
                file_hash = hash_file(file_path)

                if not file_hash:
                    continue

                if file_hash in file_hashes:
                    duplicates.append((file_path, file_hashes[file_hash]))
                else:
                    file_hashes[file_hash] = file_path

            elif entry.is_dir():
                # Prejdeme len prvú úroveň priečinka
                try:
                    for sub in os.scandir(entry.path):
                        if sub.is_file():
                            file_path = sub.path
                            file_hash = hash_file(file_path)

                            if not file_hash:
                                continue

                            if file_hash in file_hashes:
                                duplicates.append((file_path, file_hashes[file_hash]))
                            else:
                                file_hashes[file_hash] = file_path
                except PermissionError:
                    continue

    except Exception:
        return actions

    # Vytvoríme návrhy pre každý duplikát
    for dup, original in duplicates:
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
