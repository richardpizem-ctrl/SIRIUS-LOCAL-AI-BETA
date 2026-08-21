# PILIER 1 – Autonómia poznania PC
# Hlavný orchestrátor system_info

from .hardware_scan import scan_hardware
from .os_scan import scan_os
from .folder_scan import scan_folders
from .sirius_state import scan_sirius_state

def collect_system_info():
    """
    Spojí všetky skenery do jedného balíka informácií.
    """
    return {
        "hardware": scan_hardware(),
        "os": scan_os(),
        "folders": scan_folders(),
        "sirius": scan_sirius_state()
    }
