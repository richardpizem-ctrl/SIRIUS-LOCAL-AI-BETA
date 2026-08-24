import platform
import psutil

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
        }
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

    return info
