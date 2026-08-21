import os

def build_folder_triage_actions(system_snapshot):
    """
    Prevod návrhu FOLDER_TRIAGE na konkrétne akcie.
    - nájde neporiadok v root priečinku
    - identifikuje priečinky s veľkým počtom súborov
    - navrhne presun, rozdelenie alebo archiváciu
    NIČ NEVYKONÁ priamo – len návrhy.
    """

    actions = []

    folder_info = system_snapshot.get("folders", {})
    root = folder_info.get("root", "C:\\")
    folders_total = folder_info.get("folders_total", 0)

    # Ak folder_scan nič nenašiel, nerobíme nič
    if folders_total == 0:
        return actions

    # Prejdeme prvú úroveň root priečinka
    try:
        for entry in os.scandir(root):
            if not entry.is_dir():
                continue

            folder_path = entry.path

            # Spočítame počet súborov v priečinku
            file_count = 0
            try:
                for sub in os.scandir(folder_path):
                    if sub.is_file():
                        file_count += 1
            except PermissionError:
                continue

            # Ak priečinok má veľa súborov → návrh na reorganizáciu
            if file_count >= 50:
                actions.append({
                    "type": "FOLDER_ACTION",
                    "action": "REORGANIZE_FOLDER",
                    "target_path": folder_path,
                    "reason": "HIGH_FILE_COUNT",
                    "metrics": {
                        "file_count": file_count
                    },
                    "strategy": "split_into_subfolders"
                })

            # Ak priečinok je prázdny → návrh na odstránenie
            if file_count == 0:
                actions.append({
                    "type": "FOLDER_ACTION",
                    "action": "DELETE_EMPTY_FOLDER",
                    "target_path": folder_path,
                    "reason": "EMPTY_FOLDER",
                    "metrics": {
                        "file_count": 0
                    }
                })

            # Návrh na archiváciu priečinkov s veľkým počtom súborov
            if file_count >= 100:
                archive_path = os.path.join(root, "SIRIUS_ARCHIVE_TEMP")
                actions.append({
                    "type": "FOLDER_ACTION",
                    "action": "MOVE_TO_ARCHIVE",
                    "target_path": folder_path,
                    "archive_path": archive_path,
                    "reason": "FOLDER_TOO_LARGE",
                    "metrics": {
                        "file_count": file_count
                    }
                })

    except Exception:
        return actions

    return actions
