import time
import os
import json
from modules.detection import Detection

detector = Detection()

# ============================================================
#                CPU / RAM / DISK ANALYZERY
# ============================================================

def analyze_cpu(cpu):
    issues = []
    if cpu["percent"] > 85:
        issues.append({"type": "HIGH_CPU", "value": cpu["percent"]})
    return issues

def analyze_ram(ram):
    issues = []
    if ram["percent"] > 85:
        issues.append({"type": "HIGH_RAM", "value": ram["percent"]})
    return issues

def analyze_disk_activity(disk_delta):
    issues = []
    if disk_delta > 20_000_000:
        issues.append({"type": "DISK_ACTIVITY_CRITICAL", "severity": "critical", "value": disk_delta})
    elif disk_delta > 5_000_000:
        issues.append({"type": "DISK_ACTIVITY_HIGH", "severity": "high", "value": disk_delta})
    elif disk_delta > 500_000:
        issues.append({"type": "DISK_ACTIVITY_MEDIUM", "severity": "medium", "value": disk_delta})
    return issues

def analyze_processes(processes):
    issues = []
    for proc in processes:
        name = proc.get("name", "").lower()
        proc_issues = detector.detect_process(name)
        issues.extend(proc_issues)
    return issues

# ============================================================
#                HLAVNÁ ANALÝZA
# ============================================================

def analyze(snapshot):
    cpu_percent = snapshot["system"]["cpu"]
    ram_percent = snapshot["system"]["ram"]
    disk_delta = snapshot["system"]["disk"]

    # 🔥 TRENDY — bezpečné, nikdy nespadnú
    trends = snapshot.get("trend") or snapshot.get("trends") or {
        "cpu": "stable",
        "ram": "stable",
        "disk": "stable"
    }

    issues = []
    issues.extend(analyze_cpu({"percent": cpu_percent}))
    issues.extend(analyze_ram({"percent": ram_percent}))
    issues.extend(analyze_disk_activity(disk_delta))
    issues.extend(analyze_processes(snapshot["processes"]))

    # ============================================================
    # 🔥 PILIER 2 — DETEKCIA SÚBOROV (OPRAVENÉ)
    # ============================================================

    root_folder = None
    folders = snapshot.get("folders", {})

    if isinstance(folders, dict):
        root_folder = folders.get("root", None)

    # Ak root_folder existuje → spustíme detekciu súborov
    if root_folder and os.path.exists(root_folder):

        files = [entry.path for entry in os.scandir(root_folder) if entry.is_file()]

        # 1️⃣ DETEKCIA POŠKODENÝCH / NEÚPLNÝCH / NEBEZPEČNÝCH SÚBOROV
        for path in files:

            # CORRUPTION — pridaj len ak je problém
            corr = detector.detect_corruption(path)
            if corr and corr.get("type") != "file_ok":
                issues.append({
                    "type": "FILE_CORRUPTION",
                    "file": path,
                    "result": corr
                })

            # INCOMPLETE — pridaj len ak je problém
            inc = detector.detect_incomplete(path)
            if inc:
                issues.append({
                    "type": "FILE_INCOMPLETE",
                    "file": path,
                    "result": inc
                })

            # DANGEROUS CONTENT — pridaj len ak je problém
            dang = detector.detect_dangerous_content(path)
            if dang:
                issues.append({
                    "type": "FILE_DANGEROUS_CONTENT",
                    "file": path,
                    "result": dang
                })

        # 2️⃣ DETEKCIA DUPLICÍT A KONFLIKTOV — len ak existujú
        for i in range(len(files)):
            for j in range(i + 1, len(files)):

                dup = detector.detect_duplicate(files[i], files[j])
                if dup:
                    issues.append({
                        "type": "FILE_DUPLICATE",
                        "file1": files[i],
                        "file2": files[j],
                        "result": dup
                    })

                conf = detector.detect_conflict(files[i], files[j])
                if conf:
                    issues.append({
                        "type": "FILE_CONFLICT",
                        "file1": files[i],
                        "file2": files[j],
                        "result": conf
                    })

        # 3️⃣ DETEKCIA Z CELEJ ZLOŽKY — pridaj len reálne problémy
        folder_scan = detector.scan_folder(root_folder)
        for item in folder_scan:
            # pridaj len ak je to problém
            if item.get("type") not in ["file_ok"]:
                issues.append(item)

    # ============================================================

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "issues": issues,
        "system": {
            "cpu": cpu_percent,
            "ram": ram_percent,
            "disk": disk_delta
        },
        "trends": {
            "cpu": trends["cpu"],
            "ram": trends["ram"],
            "disk": trends["disk"]
        }
    }
