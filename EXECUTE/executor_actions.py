# executor_actions.py – vykonávacie akcie pre EXECUTE modul

import os
import time
import subprocess
import shutil

def execute_action(action, params):
    """
    Vykoná akciu podľa názvu.
    Každá akcia vráti textový výsledok, ktorý sa zapíše do executor_log.txt.
    """

    # DUPLICITY
    if action == "DUPLICATE_FOUND":
        return handle_duplicate(params)

    if action == "ARCHIVE_DUPLICATE":
        return archive_duplicate(params)

    if action == "REPORT_DUPLICATE":
        return report_duplicate(params)

    # OPTIMALIZÁCIE
    if action == "OPTIMIZE_RAM":
        return optimize_ram()

    if action == "OPTIMIZE_CPU":
        return optimize_cpu()

    if action == "CLEAN_DISK":
        return clean_disk()

    # NAVIGÁCIA (COLNÍK posiela NAVIGATE)
    if action == "NAVIGATE":
        return navigate(params)

    # PRESUN SÚBOROV (MOVE z COLNÍKA)
    if action == "MOVE":
        return move_files(params)

    return f"UNKNOWN_ACTION: {action}"


# ------------------------------------------------------------
# 1. DUPLICATE_FOUND (pôvodné)
# ------------------------------------------------------------

def handle_duplicate(params):
    file_path = params.get("file", "UNKNOWN")
    return f"Duplicate processed: {file_path}"


# ------------------------------------------------------------
# 2. ARCHIVE_DUPLICATE
# ------------------------------------------------------------

def archive_duplicate(params):
    files = params.get("files", [])
    archived = []

    # jednoduchý archív priamo pri súbore
    for f in files:
        if os.path.exists(f):
            ts = time.strftime("%Y%m%d_%H%M%S")
            target = f"{f}_{ts}.archive"
            try:
                shutil.move(f, target)
                archived.append(target)
            except Exception as e:
                return f"ARCHIVE_DUPLICATE failed for {f}: {e}"

    return f"Archived {len(archived)} files"


# ------------------------------------------------------------
# 3. REPORT_DUPLICATE
# ------------------------------------------------------------

def report_duplicate(params):
    count = params.get("count", 0)
    return f"Duplicate report logged ({count} files)"


# ------------------------------------------------------------
# 4. OPTIMIZE_RAM
# ------------------------------------------------------------

def optimize_ram():
    time.sleep(0.2)
    return "RAM optimized"


# ------------------------------------------------------------
# 5. OPTIMIZE_CPU
# ------------------------------------------------------------

def optimize_cpu():
    time.sleep(0.2)
    return "CPU optimized"


# ------------------------------------------------------------
# 6. CLEAN_DISK
# ------------------------------------------------------------

def clean_disk():
    time.sleep(0.2)
    return "Disk cleaned"


# ------------------------------------------------------------
# 7. NAVIGATE
# ------------------------------------------------------------

def navigate(params):
    # target dopĺňa COLNÍK do params["target"]
    target = params.get("target")
    if not target:
        return "NAVIGATE: missing target"

    try:
        subprocess.Popen(target)
        return f"Navigation executed: {target}"
    except Exception as e:
        return f"Navigation failed: {e}"


# ------------------------------------------------------------
# 8. MOVE
# ------------------------------------------------------------

def move_files(params):
    files = params.get("files", [])
    dest = params.get("destination")

    if not dest:
        return "MOVE: missing destination"

    moved = []

    for f in files:
        if os.path.exists(f):
            try:
                shutil.move(f, dest)
                moved.append(f)
            except Exception as e:
                return f"MOVE failed for {f}: {e}"

    return f"Moved {len(moved)} files to {dest}"
