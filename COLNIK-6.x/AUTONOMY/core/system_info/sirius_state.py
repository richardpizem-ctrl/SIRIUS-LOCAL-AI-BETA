import os

def scan_sirius_state():
    """
    Ľahký SIRIUS state skener.
    Namiesto dumpovania celého projektu vráti len statusové súhrny:
    - existujúce moduly
    - existujúce konfiguračné súbory
    - stav KG
    - stav runtime
    - celkový status projektu
    """

    base = "C:\\SIRIUS_ARCHIVE\\COLNIK-6.x"

    modules = {
        "autonomy": os.path.exists(os.path.join(base, "AUTONOMY")),
        "colnik": os.path.exists(os.path.join(base, "COLNIK-6.x")),
        "workflow": os.path.exists(os.path.join(base, "workflow_engine.py")),
        "kg": os.path.exists(os.path.join(base, "autosave_kg.json")),
        "runtime": os.path.exists(os.path.join(base, "runtime_core.py"))
    }

    configs = {
        "sirius_config": os.path.exists(os.path.join(base, "sirius_config.json")),
        "kg_autosave": os.path.exists(os.path.join(base, "autosave_kg.json")),
        "modules_folder": os.path.exists(os.path.join(base, "modules"))
    }

    # KG size
    kg_path = os.path.join(base, "autosave_kg.json")
    kg_size = os.path.getsize(kg_path) if os.path.exists(kg_path) else 0

    # STATUS LOGIKA
    if not modules["runtime"]:
        status = "runtime_missing"
    elif not modules["kg"]:
        status = "kg_missing"
    elif kg_size == 0:
        status = "kg_empty"
    else:
        status = "ok"

    return {
        "modules": modules,
        "configs": configs,
        "kg_size": kg_size,
        "status": status
    }
