import os

# SYSTÉMOVÉ SÚBORY, KTORÉ SA MAJÚ IGNOROVAŤ
SYSTEM_EMPTY_SAFE = {
    "dir",
    "python",
    "__init__.py",
    "kg_autosave_BROKEN.json"
}

def scan_sirius_state():
    """
    Ľahký SIRIUS state skener.
    Vráti statusové súhrny:
    - existujúce moduly
    - existujúce konfiguračné súbory
    - stav KG
    - stav runtime
    - celkový status projektu
    """

    base = "C:\\SIRIUS_ARCHIVE\\COLNIK-6.x"

    # === MODULY – upravené podľa reálnej štruktúry SIRIUS 6.x ===
    modules = {
        "autonomy": os.path.isdir(os.path.join(base, "AUTONOMY")),
        "colnik": os.path.isdir(os.path.join(base, "COLNIK")),
        "workflow": os.path.isdir(os.path.join(base, "workflow")),
        "kg": os.path.exists(os.path.join(base, "kg", "kg_autosave.json")),
        "runtime": os.path.isdir(os.path.join(base, "runtime5"))
    }

    # === CONFIGS – upravené podľa reálnej štruktúry ===
    configs = {
        "sirius_config": os.path.exists(os.path.join(base, "sirius_config.json")),
        "kg_autosave": os.path.exists(os.path.join(base, "kg", "kg_autosave.json")),
        "modules_folder": os.path.isdir(os.path.join(base, "modules"))
    }

    # === KG SIZE ===
    kg_path = os.path.join(base, "kg", "kg_autosave.json")
    kg_size = os.path.getsize(kg_path) if os.path.exists(kg_path) else 0

    # === STATUS LOGIKA – rozšírená ===
    if not modules["runtime"]:
        status = "runtime_missing"

    elif not modules["kg"]:
        status = "kg_missing"

    elif kg_size == 0:
        status = "kg_empty"

    elif kg_size < 50:  # veľmi malý KG → pravdepodobne poškodený
        status = "kg_suspicious"

    else:
        status = "ok"

    # === IGNORUJ SYSTÉMOVÉ PRÁZDNE SÚBORY ===
    for safe in SYSTEM_EMPTY_SAFE:
        safe_path = os.path.join(base, safe)
        if os.path.exists(safe_path):
            # tieto súbory neovplyvňujú stav
            pass

    return {
        "modules": modules,
        "configs": configs,
        "kg_size": kg_size,
        "status": status
    }
