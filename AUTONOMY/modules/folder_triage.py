import os

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
    "sirius_modules"
}

def build_folder_triage_actions(system_snapshot):
    """
    Prevod návrhu FOLDER_TRIAGE na konkrétne akcie.
    - nájde neporiadok v root priečinku
    - identifikuje priečinky s veľkým počtom súborov
    - navrhne reorganizáciu
    - NIČ NEVYKONÁ priamo – len návrhy.
    """

    actions = []

    # === DEFINITÍVNY ROOT AUTONÓMIE ===
    root = r"C:\SIRIUS_ARCHIVE\COLNIK-6.x"

    folder_info = system_snapshot.get("folders", {})
    folders_total = folder_info.get("folders_total", 0)

    # Ak folder_scan nič nenašiel, nerobíme nič
    if folders_total == 0:
        return actions

    try:
        for entry in os.scandir(root):
            if not entry.is_dir():
                continue

            folder_path = entry.path
            folder_name = os.path.basename(folder_path).lower()

            # === FIX 1: IGNORUJ SYSTÉMOVÉ PRIEČINKY ===
            if folder_name in SYSTEM_SAFE_FOLDERS:
                continue

            # === Spočítame počet súborov v priečinku ===
            file_count = 0
            try:
                for sub in os.scandir(folder_path):
                    if sub.is_file():
                        file_count += 1
            except PermissionError:
                continue

            # === FIX 2: Prázdne priečinky sa len označia, nie mažú ===
            if file_count == 0:
                actions.append({
                    "type": "FOLDER_ACTION",
                    "action": "MARK_EMPTY",
                    "target_path": folder_path,
                    "reason": "EMPTY_FOLDER",
                    "metrics": {"file_count": 0},
                    "note": "EMPTY_ONLY – no delete"
                })
                continue

            # === Veľké priečinky → návrh reorganizácie ===
            if file_count >= 50:
                actions.append({
                    "type": "FOLDER_ACTION",
                    "action": "REORGANIZE_FOLDER",
                    "target_path": folder_path,
                    "reason": "HIGH_FILE_COUNT",
                    "metrics": {"file_count": file_count},
                    "strategy": "split_into_subfolders"
                })

            # === Extrémne veľké priečinky → návrh archivácie ===
            if file_count >= 100:
                archive_path = os.path.join(root, "SIRIUS_ARCHIVE_TEMP")
                actions.append({
                    "type": "FOLDER_ACTION",
                    "action": "MOVE_TO_ARCHIVE",
                    "target_path": folder_path,
                    "archive_path": archive_path,
                    "reason": "FOLDER_TOO_LARGE",
                    "metrics": {"file_count": file_count}
                })

    except Exception:
        return actions

    return actions
