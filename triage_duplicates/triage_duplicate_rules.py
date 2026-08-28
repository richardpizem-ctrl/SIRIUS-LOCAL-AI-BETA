# Triage Duplicate Rules (PRE-FINAL)
# Defines how duplicates should be detected and handled.

TRIAGE_DUPLICATE_RULES = {
    "file_extensions_to_check": [
        ".json",
        ".txt",
        ".log",
        ".py"
    ],
    "duplicate_handling": {
        "keep_first": True,
        "log_duplicates": True,
        "auto_delete": False
    }
}

