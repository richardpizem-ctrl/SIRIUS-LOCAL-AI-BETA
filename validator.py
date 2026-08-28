# validator.py – kompatibilná validácia requestov z AUTONOMY 6.x

# Autonómia posiela rôzne typy requestov:
# - TRIAGE_FOLDER (MOVE, CLASSIFY)
# - DUPLICATE_FILE (REPORT_DUPLICATE, ARCHIVE_DUPLICATE)
# - NAVIGATION_TASK (OPEN)
# - SYSTEM_CHANGE
# - MOVE (archivácia, presun)
# Preto validator NESMIE blokovať tieto akcie.

REQUIRED_FIELDS = ["request_id", "action", "origin"]


def validate_request(req):
    errors = []

    # === Povinné polia (ale target NIE JE povinný pri MOVE, ARCHIVE, REPORT) ===
    for field in REQUIRED_FIELDS:
        if field not in req:
            errors.append(f"missing_field:{field}")

    action = req.get("action")
    payload = req.get("payload", {})

    # === Povolené akcie v SIRIUS 6.x ===
    ALLOWED_ACTIONS = [
        "MOVE",
        "NAVIGATE",
        "OPEN",
        "SYSTEM_CHANGE",
        "DELETE",
        "EXECUTE",
        "READ",
        "WRITE",
        "CLASSIFY",
        "REPORT_DUPLICATE",
        "ARCHIVE_DUPLICATE"
    ]

    if action not in ALLOWED_ACTIONS:
        errors.append(f"unknown_action:{action}")

    # === MOVE validácia (ale NEBLOKUJEME triage MOVE) ===
    if action == "MOVE":
        # Triážne návrhy majú folder/source_file, nie target
        if "source_file" not in payload:
            # ale ak je to triage folder MOVE, payload obsahuje "folder"
            if "folder" not in payload:
                errors.append("MOVE_missing_source_file")

    # === NAVIGATE / OPEN ===
    if action in ["NAVIGATE", "OPEN"]:
        # target môže byť explorer.exe, control.exe, ms-settings:
        if not req.get("target"):
            errors.append("NAVIGATE_missing_target")

    # === SYSTEM_CHANGE ===
    # autonómia posiela SYSTEM_CHANGE bez targetu, preto target NIE JE povinný
    # nič neblokujeme

    # === DUPLICITY ===
    # duplicity môžu mať payload.files, payload.hash, payload.category
    # nič neblokujeme

    return errors
