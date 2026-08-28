# Triage Folder Rules (SUPER-FINAL)
# Defines required folder structure and classification rules for COLNIK operations.
# PILIER 4 — TRIAZ PRIEČINKOV

TRIAGE_FOLDER_RULES = {
    "required": [
        "logs",
        "exports",
        "workflow",
        "kg",
        "envoy",
        "modules",
        "runtime",
        "configs",
        "backups"
    ],
    "optional": [
        "backup",
        "simulator",
        "temp",
        "__pycache__",
        "archive"
    ]
}

# ============================================================
# FOLDER TYPES — ROZPOZNANIE TYPU PRIEČINKA
# ============================================================

FOLDER_TYPES = {
    # ROOT PROJECT
    "sirius_root": ["COLNIK", "COLNIK-6.x"],
    "simulator": ["COLNIK_SIMULATOR"],
    "exports": ["exports"],

    # AUTONOMY TRIAGE MODULES
    "autonomy_triage": ["triage_duplicates", "triage_folders"],

    # AUTONOMY STRUCTURE
    "autonomy_core": ["core"],
    "autonomy_guard": ["guard"],
    "autonomy_modules": ["modules"],
    "autonomy_ipc": ["IPC_DATA", "ipc_data"],
    "autonomy_logs": ["logs"],
    "autonomy_cache": ["__pycache__"],
    "autonomy_runtime": ["runtime", "runtime5", "runtime5.x"],
    "autonomy_detection": ["detection"],
    "autonomy_workflow": ["workflow"],
    "autonomy_envoy": ["envoy"],
    "autonomy_navigation": ["navigation"],
    "autonomy_timecore": ["timecore"],
    "autonomy_kg": ["kg"],
    "autonomy_terminal": ["terminal_assistant", "terminal"],
    "autonomy_config": ["config", "configs"],
    "autonomy_backup": ["backup", "backups"],
    "autonomy_archive": ["archive"],
    "autonomy_root": ["AUTONOMY"],

    # SIRIUS MODULES
    "sirius_modules": ["SIRIUS_MODULES"],

    # GENERAL SYSTEM FOLDERS
    "system_temp": ["temp", "tmp"],
    "system_logs": ["logs"],
    "system_configs": ["configs"],
    "system_runtime": ["runtime"],
    "system_backups": ["backups"],
    "system_archive": ["archive"]
}

# ============================================================
# DESTINATIONS — KAM PRIEČINOK PATRÍ
# ============================================================

FOLDER_DESTINATIONS = {
    # ROOT PROJECT
    "sirius_root": ".",
    "simulator": "simulator",
    "exports": "exports",

    # AUTONOMY TRIAGE MODULES
    "autonomy_triage": "triage",

    # AUTONOMY STRUCTURE
    "autonomy_core": "core",
    "autonomy_guard": "guard",
    "autonomy_modules": "modules",
    "autonomy_ipc": "IPC_DATA",
    "autonomy_logs": "logs",
    "autonomy_cache": "__pycache__",
    "autonomy_runtime": "runtime",
    "autonomy_detection": "detection",
    "autonomy_workflow": "workflow",
    "autonomy_envoy": "envoy",
    "autonomy_navigation": "navigation",
    "autonomy_timecore": "timecore",
    "autonomy_kg": "kg",
    "autonomy_terminal": "terminal_assistant",
    "autonomy_config": "config",
    "autonomy_backup": "backups",
    "autonomy_archive": "archive",
    "autonomy_root": ".",

    # SIRIUS MODULES
    "sirius_modules": "SIRIUS_MODULES",

    # GENERAL SYSTEM FOLDERS
    "system_temp": "temp",
    "system_logs": "logs",
    "system_configs": "configs",
    "system_runtime": "runtime",
    "system_backups": "backups",
    "system_archive": "archive"
}
