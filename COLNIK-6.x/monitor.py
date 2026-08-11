# MONITOR 6.x – WINDOWS ULTRA-SAFE VERSION (KOMPATIBILNÝ)
# Vracia CPU/RAM/DISK v presnom formáte, ktorý autonómia potrebuje

import psutil
import time

def snapshot():
    # ============================================================
    # CPU – NEBLOKUJÚCE
    # ============================================================
    cpu_total = psutil.cpu_percent(interval=None)

    cpu_info = {
        "percent": cpu_total
    }

    # ============================================================
    # RAM
    # ============================================================
    ram = psutil.virtual_memory()
    ram_info = {
        "percent": ram.percent
    }

    # ============================================================
    # DISKY – iba C:\ (hlavný systémový disk)
    # ============================================================
    try:
        disk_usage = psutil.disk_usage("C:\\")
        disk_info = {
            "percent": disk_usage.percent
        }
    except Exception:
        disk_info = {
            "percent": 0
        }

    # ============================================================
    # PROCESY – ULTRA SAFE (iba PID + názov)
    # ============================================================
    processes_info = []
    for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            processes_info.append({
                "pid": p.pid,
                "name": p.name(),
                "cpu_percent": 0,
                "memory_percent": 0
            })
        except:
            continue

    # ============================================================
    # SNAPSHOT – KOMPATIBILNÝ FORMÁT
    # ============================================================
    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),

        # 🔥 presne to, čo analyzer.py očakáva
        "system": {
            "cpu": cpu_info["percent"],
            "ram": ram_info["percent"],
            "disk": disk_info["percent"]
        },

        "processes": processes_info
    }
