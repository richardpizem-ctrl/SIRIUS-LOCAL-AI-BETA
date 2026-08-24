import time
from timecore import TimeCore   # <<< TIMECORE

# ============================================================
# TIMECORE – PILIER 0
# ============================================================

timecore = TimeCore()
timecore.runtime_start()

# Cooldown tabuľka (sekundy)
COOLDOWN = {
    "OPTIMIZE_CPU": 45,
    "OPTIMIZE_RAM": 45,
    "CLEAN_DISK": 60
}

LAST_EXECUTED = {
    "OPTIMIZE_CPU": 0,
    "OPTIMIZE_RAM": 0,
    "CLEAN_DISK": 0
}


def is_on_cooldown(action: str) -> bool:
    last = LAST_EXECUTED.get(action, 0)
    cd = COOLDOWN.get(action, 30)
    return (time.time() - last) < cd


def mark_executed(action: str) -> None:
    LAST_EXECUTED[action] = time.time()


# ============================================================
#                   🔥 GUARD LAYER – OPRAVENÝ 🔥
# ============================================================

SAFE_ACTIONS = {
    "OPTIMIZE_CPU",
    "OPTIMIZE_RAM",
    "CLEAN_DISK",

    "REPORT_CORRUPTED_FILE",
    "REPORT_DANGEROUS_FILE",
    "QUARANTINE",
    "KILL",

    "DELETE_EMPTY_FOLDER",
    "REORGANIZE_FOLDER",
    "MOVE_TO_ARCHIVE",

    "DELETE_DUPLICATE",

    # NAVIGÁCIA
    "NAVIGATE"
}

# 🔥 MAPOVANIE AUTONÓMNYCH AKCIÍ NA COLNÍK AKCIE
ACTION_MAP = {
    "OPTIMIZE_CPU": "SYSTEM_CHANGE",
    "OPTIMIZE_RAM": "SYSTEM_CHANGE",
    "CLEAN_DISK": "SYSTEM_CHANGE",

    "REPORT_CORRUPTED_FILE": "SYSTEM_CHANGE",
    "REPORT_DANGEROUS_FILE": "SYSTEM_CHANGE",

    "DELETE_EMPTY_FOLDER": "DELETE",
    "DELETE_DUPLICATE": "DELETE",

    "MOVE_TO_ARCHIVE": "MOVE",
    "REORGANIZE_FOLDER": "MOVE",

    "KILL": "EXECUTE",
    "QUARANTINE": "SYSTEM_CHANGE",

    # NAVIGÁCIA → spúšťanie systémových nástrojov
    "NAVIGATE": "EXECUTE"
}


def guard_check(proposals, system_snapshot):
    """
    GUARD kontrola návrhov autonómie.
    """

    system = system_snapshot.get("system", {})
    cpu = system.get("cpu", 0)
    ram = system.get("ram", 0)
    disk = system.get("disk", 0)

    # Kritický stav systému → GLOBAL STOP
    if cpu >= 100 and ram >= 95 and disk >= 80_000_000:
        return "STOP"

    for p in proposals:

        if not isinstance(p, dict):
            return "STOP_AUTONOMY"

        if "proposal_id" not in p or "action" not in p or "target" not in p:
            return "STOP_AUTONOMY"

        if p["action"] not in SAFE_ACTIONS:
            return "STOP_AUTONOMY"

        if not isinstance(p["target"], str):
            return "STOP_AUTONOMY"

    return "OK"


# ============================================================
#                   🔥 AUTONÓMIA + GUARD + TIMECORE 🔥
# ============================================================

def generate_proposals(analysis):
    """
    Generovanie návrhov autonómie na základe analýzy systému + issues.
    """

    # TIMECORE – začiatok generovania návrhov
    timecore.cycle_start()

    proposals = []

    system = analysis.get("system", {})
    trends = analysis.get("trends", {})
    issues = analysis.get("issues", [])

    cpu_val = system.get("cpu", 0)
    ram_val = system.get("ram", 0)
    disk_val = system.get("disk", 0)

    cpu_trend = trends.get("cpu", "stable")
    ram_trend = trends.get("ram", "stable")
    disk_trend = trends.get("disk", "stable")

    # ============================
    # CPU OPTIMIZATION
    # ============================
    if cpu_val > 50 or cpu_trend == "rising":
        if not is_on_cooldown("OPTIMIZE_CPU"):
            proposals.append({
                "proposal_id": "cpu-opt",
                "action": "OPTIMIZE_CPU",
                "target": "SYSTEM",
                "payload": {"cpu": cpu_val},
                "priority": "HIGH" if cpu_val > 80 else "NORMAL",
                "cycle_time": None
            })
            mark_executed("OPTIMIZE_CPU")

    # ============================
    # RAM OPTIMIZATION
    # ============================
    if ram_val > 75 or ram_trend == "rising":
        if not is_on_cooldown("OPTIMIZE_RAM"):
            proposals.append({
                "proposal_id": "ram-opt",
                "action": "OPTIMIZE_RAM",
                "target": "SYSTEM",
                "payload": {"ram": ram_val},
                "priority": "HIGH" if ram_val > 85 else "NORMAL",
                "cycle_time": None
            })
            mark_executed("OPTIMIZE_RAM")

    # ============================
    # DISK CLEAN
    # ============================
    if disk_val > 10_000_000 or disk_trend == "rising":
        if not is_on_cooldown("CLEAN_DISK"):
            proposals.append({
                "proposal_id": "disk-clean",
                "action": "CLEAN_DISK",
                "target": "SYSTEM",
                "payload": {"disk": disk_val},
                "priority": "HIGH" if disk_val > 20_000_000 else "NORMAL",
                "cycle_time": None
            })
            mark_executed("CLEAN_DISK")

    # ============================================================
    # 🔥 2. PILIER – DETECTION ISSUES → PROPOSALS
    # ============================================================

    for issue in issues:

        # ------------------------------
        # POŠKODENÉ SÚBORY
        # ------------------------------
        if issue.get("type") == "FILE_CORRUPTION_CHECK":
            proposals.append({
                "proposal_id": f"corrupt-{issue['file']}",
                "action": "REPORT_CORRUPTED_FILE",
                "target": issue["file"],
                "payload": {"result": issue["result"]},
                "priority": "HIGH",
                "cycle_time": None
            })

        # ------------------------------
        # NEÚPLNÉ SÚBORY
        # ------------------------------
        if issue.get("type") == "FILE_INCOMPLETE_CHECK":
            proposals.append({
                "proposal_id": f"incomplete-{issue['file']}",
                "action": "REPORT_CORRUPTED_FILE",
                "target": issue["file"],
                "payload": {"result": issue["result"]},
                "priority": "HIGH",
                "cycle_time": None
            })

        # ------------------------------
        # NEBEZPEČNÝ OBSAH
        # ------------------------------
        if issue.get("type") == "FILE_DANGEROUS_CONTENT_CHECK":
            proposals.append({
                "proposal_id": f"danger-{issue['file']}",
                "action": "REPORT_DANGEROUS_FILE",
                "target": issue["file"],
                "payload": {"result": issue["result"]},
                "priority": "CRITICAL",
                "cycle_time": None
            })

        # ------------------------------
        # DUPLICITY
        # ------------------------------
        if issue.get("type") == "FILE_DUPLICATE_CHECK":
            proposals.append({
                "proposal_id": f"duplicate-{issue['file1']}-{issue['file2']}",
                "action": "DELETE_DUPLICATE",
                "target": issue["file1"],
                "payload": {"duplicate_of": issue["file2"]},
                "priority": "NORMAL",
                "cycle_time": None
            })

        # ------------------------------
        # KONFLIKTY
        # ------------------------------
        if issue.get("type") == "FILE_CONFLICT_CHECK":
            proposals.append({
                "proposal_id": f"conflict-{issue['file1']}-{issue['file2']}",
                "action": "MOVE_TO_ARCHIVE",
                "target": issue["file1"],
                "payload": {"conflict_with": issue["file2"]},
                "priority": "NORMAL",
                "cycle_time": None
            })

        # ------------------------------
        # NEBEZPEČNÝ PROCES
        # ------------------------------
        if issue.get("type") == "process_danger":

            # 🔥 TVRDÁ OPRAVA — IGNORUJ KILL NA SYSTÉMOVÝ PROCES
            if issue.get("process", "").lower() == "wmiregistrationservice.exe":
                print("[GUARD] IGNORUJEM KILL návrh na systémový proces wmiregistrationservice.exe")
                continue

            proposals.append({
                "proposal_id": "proc-danger-01",
                "action": "KILL",
                "target": issue["process"],
                "payload": {"reason": issue["reason"]},
                "priority": "CRITICAL",
                "cycle_time": None
            })

    # ============================================================
    # ODSTRÁNENIE DUPLICÍT
    # ============================================================

    unique = []
    seen_ids = set()

    for p in proposals:
        pid = p.get("proposal_id")
        if pid not in seen_ids:
            unique.append(p)
            seen_ids.add(pid)

    # ============================================================
    # 🔥 GUARD KONTROLA
    # ============================================================

    guard_status = guard_check(unique, analysis)

    if guard_status == "STOP":
        print("[GUARD] GLOBAL STOP – kritický stav systému")
        timecore.cycle_end()
        return []

    if guard_status == "STOP_AUTONOMY":
        print("[GUARD] STOP AUTONOMY – návrhy zablokované")
        timecore.cycle_end()
        return []

    # TIMECORE – koniec generovania návrhov
    cycle_time = timecore.cycle_delta()
    timecore.cycle_end()

    # doplnenie cycle_time do návrhov
    for p in unique:
        p["cycle_time"] = cycle_time

    return unique
