import os

def scan_folders(root="C:\\"):
    """
    Ľahký folder-scan.
    Namiesto dumpovania celého disku vráti len statusové súhrny:
    - počet priečinkov
    - počet súborov
    - celková veľkosť
    - najväčší priečinok (názov + veľkosť)
    """

    result = {
        "root": root,
        "folders_total": 0,
        "files_total": 0,
        "total_size": 0,
        "largest_folder": {
            "path": None,
            "size": 0
        }
    }

    # Prejdeme len prvú úroveň (root), nie celý disk
    try:
        for entry in os.scandir(root):
            if entry.is_dir():
                result["folders_total"] += 1

                folder_size = 0
                try:
                    for sub in os.scandir(entry.path):
                        if sub.is_file():
                            folder_size += os.path.getsize(sub.path)
                            result["files_total"] += 1
                except PermissionError:
                    continue

                result["total_size"] += folder_size

                if folder_size > result["largest_folder"]["size"]:
                    result["largest_folder"]["size"] = folder_size
                    result["largest_folder"]["path"] = entry.path

            elif entry.is_file():
                result["files_total"] += 1
                try:
                    size = os.path.getsize(entry.path)
                    result["total_size"] += size
                except:
                    continue

    except Exception:
        return result

    return result
