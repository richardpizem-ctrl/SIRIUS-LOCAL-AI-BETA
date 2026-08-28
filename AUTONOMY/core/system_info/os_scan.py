import platform
import psutil

# SYSTÉMOVÉ SÚBORY, KTORÉ SA MAJÚ IGNOROVAŤ V ANALÝZE
SYSTEM_EMPTY_SAFE = {
    "dir",
    "python",
    "__init__.py",
    "kg_autosave_BROKEN.json"
}

def scan_os():
    """
    Ľahký OS skener.
    Namiesto dumpovania všetkých služieb/procesov vráti len statusové súhrny.
    """
    info = {
        "os_version": platform.platform(),
        "build": platform.version(),
        "services": {
            "total": 0,
            "running": 0,
            "stopped": 0
        },
        "processes": {
            "total": 0
        },
        # 🔥 PRIDANÉ: issues pole, aby sme mohli filtrovať falošné hlášky
        "issues": []
    }

    # === PROCESY – len počet, nie celý zoznam ===
    try:
        count = 0
        for _ in psutil.process_iter(['pid']):
            count += 1
        info["processes"]["total"] = count
    except:
        info["processes"]["total"] = 0

    # === SLUŽBY – len počty, nie celý zoznam ===
    try:
        total = 0
        running = 0
        stopped = 0

        for svc in psutil.win_service_iter():
            try:
                s = svc.as_dict()
                total += 1
                status = s.get("status")
                if status == "running":
                    running += 1
                else:
                    stopped += 1
            except:
                continue

        info["services"]["total"] = total
        info["services"]["running"] = running
        info["services"]["stopped"] = stopped
    except:
        info["services"]["total"] = 0
        info["services"]["running"] = 0
        info["services"]["stopped"] = 0

    # === 🔥 FILTER: odstrániť falošné FILE_CORRUPTION / EMPTY_FILE ===
    filtered_issues = []
    for issue in info.get("issues", []):
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

        filtered_issues.append(issue)

    info["issues"] = filtered_issues

    return info
