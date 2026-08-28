# PILIER 1 – Autonómia poznania PC
# Hlavný orchestrátor system_info

from .hardware_scan import scan_hardware
from .os_scan import scan_os
from .folder_scan import scan_folders
from .sirius_state import scan_sirius_state

# SYSTÉMOVÉ SÚBORY, KTORÉ SA MAJÚ IGNOROVAŤ V ANALÝZE
SYSTEM_EMPTY_SAFE = {
    "dir",
    "python",
    "__init__.py",
    "kg_autosave_BROKEN.json"
}

def filter_analysis(data):
    """
    Odstráni falošné FILE_CORRUPTION / EMPTY_FILE / DUPLICATE
    pre systémové prázdne súbory.
    """
    if "issues" not in data:
        return data

    filtered = []
    for issue in data["issues"]:
        # ak je to súbor, zober len názov
        filename = None
        if "file" in issue:
            filename = issue["file"].split("\\")[-1].lower()
        if "path" in issue:
            filename = issue["path"].split("\\")[-1].lower()
        if "file1" in issue:
            filename = issue["file1"].split("\\")[-1].lower()

        # ignoruj DIR / PYTHON / __init__.py / kg_autosave_BROKEN.json
        if filename in SYSTEM_EMPTY_SAFE:
            continue

        filtered.append(issue)

    data["issues"] = filtered
    return data


def collect_system_info():
    """
    Spojí všetky skenery do jedného balíka informácií.
    + aplikuje filter na falošné EMPTY_FILE / FILE_CORRUPTION
    """
    hardware = scan_hardware()
    os_info = scan_os()
    folders = scan_folders()
    sirius = scan_sirius_state()

    # aplikuj filter na OS analýzu
    os_info = filter_analysis(os_info)

    return {
        "hardware": hardware,
        "os": os_info,
        "folders": folders,
        "sirius": sirius
    }
