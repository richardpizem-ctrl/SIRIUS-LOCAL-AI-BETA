import os

def build_disk_cleanup_actions(system_snapshot):
    """
    Prevod návrhu DISK_CLEANUP na konkrétne akcie.
    - nájde najväčšie priečinky v root
    - pripraví návrhy na presun alebo vyčistenie
    NIČ NEVYKONÁ priamo – len návrhy.
    """

    actions = []

    folder_info = system_snapshot.get("folders", {})
    root = folder_info.get("root", "C:\\")
    folders_total = folder_info.get("folders_total", 0)
    total_size = folder_info.get("total_size", 0)
    largest = folder_info.get("largest_folder", {})

    # Ak folder_scan nič nenašiel, nerobíme nič
    if folders_total == 0 or not largest.get("path"):
        return actions

    largest_path = largest["path"]
    largest_size = largest["size"]

    # Ak je priečinok väčší ako 50 MB → návrh na cleanup
    size_threshold = 50 * 1024 * 1024  # 50 MB

    if largest_size >= size_threshold:
        actions.append({
            "type": "FOLDER_ACTION",
            "action": "CLEAN_FOLDER",
            "target_path": largest_path,
            "reason": "LARGE_FOLDER",
            "metrics": {
                "folder_size_bytes": largest_size,
                "total_root_size": total_size
            }
        })

    # Návrh na presun veľkých priečinkov do archívu
    archive_path = os.path.join(root, "SIRIUS_ARCHIVE_TEMP")

    actions.append({
        "type": "FOLDER_ACTION",
        "action": "MOVE_TO_ARCHIVE",
        "target_path": largest_path,
        "archive_path": archive_path,
        "reason": "DISK_OPTIMIZATION",
        "metrics": {
            "folder_size_bytes": largest_size
        }
    })

    return actions
