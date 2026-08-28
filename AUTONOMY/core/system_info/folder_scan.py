import os

# SYSTÉMOVÉ SÚBORY, KTORÉ SA MAJÚ IGNOROVAŤ
SYSTEM_EMPTY_SAFE = {
    "dir",
    "python",
    "__init__.py",
    "kg_autosave_BROKEN.json"
}

def scan_folders(root=r"C:\SIRIUS_ARCHIVE\COLNIK-6.x"):
    result = {
        "root": root,
        "folders_total": 0,
        "files_total": 0,
        "total_size": 0,
        "largest_folder": {
            "path": None,
            "size": 0
        },
        "required_folders": {
            "modules": os.path.isdir(os.path.join(root, "modules")),
            "runtime": os.path.isdir(os.path.join(root, "runtime")),
            "configs": os.path.isdir(os.path.join(root, "configs")),
            "backups": os.path.isdir(os.path.join(root, "backups"))
        }
    }

    try:
        for entry in os.scandir(root):
            if entry.is_dir():
                result["folders_total"] += 1

                folder_size = 0
                try:
                    for sub in os.scandir(entry.path):

                        # === IGNORUJ SYSTÉMOVÉ PRÁZDNE SÚBORY ===
                        if sub.is_file():
                            filename = os.path.basename(sub.path).lower()
                            if filename in SYSTEM_EMPTY_SAFE:
                                continue

                            folder_size += os.path.getsize(sub.path)
                            result["files_total"] += 1

                except PermissionError:
                    continue

                result["total_size"] += folder_size

                if folder_size > result["largest_folder"]["size"]:
                    result["largest_folder"]["size"] = folder_size
                    result["largest_folder"]["path"] = entry.path

            elif entry.is_file():
                filename = os.path.basename(entry.path).lower()

                # === IGNORUJ SYSTÉMOVÉ PRÁZDNE SÚBORY ===
                if filename in SYSTEM_EMPTY_SAFE:
                    continue

                result["files_total"] += 1
                try:
                    size = os.path.getsize(entry.path)
                    result["total_size"] += size
                except:
                    continue

    except Exception:
        return result

    return result
