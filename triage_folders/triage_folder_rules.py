# Triage Folder Rules (FINAL)
# Defines required folder structure for COLNIK operations.

TRIAGE_FOLDER_RULES = {
    "required": [
        "logs",
        "exports",
        "workflow",
        "kg",
        "envoy"
    ],
    "optional": [
        "backup",
        "simulator",
        "temp"
    ]
}

# === PILIER 4 — FOLDER TYPES (rozpoznanie typu priečinka) ===
FOLDER_TYPES = {
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
    "autonomy_root": ["AUTONOMY"]
}

# === PILIER 4 — DESTINATIONS (kam priečinok patrí) ===
FOLDER_DESTINATIONS = {
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
    "autonomy_root": "."
}
