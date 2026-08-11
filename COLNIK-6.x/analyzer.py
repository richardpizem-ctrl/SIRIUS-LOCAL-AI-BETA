# AUTONOMY 6.x – analyzer.py (KOMPATIBILNÝ S TVOJÍM MONITOROM)

import time

CPU_HIGH_THRESHOLD = 85
RAM_HIGH_THRESHOLD = 85
DISK_HIGH_THRESHOLD = 90
PROCESS_CPU_THRESHOLD = 50
PROCESS_RAM_THRESHOLD = 5


def analyze_cpu(cpu_value):
    issues = []
    if cpu_value > CPU_HIGH_THRESHOLD:
        issues.append({
            "type": "cpu_overload",
            "severity": "high",
            "value": cpu_value
        })
    return issues


def analyze_ram(ram_value):
    issues = []
    if ram_value > RAM_HIGH_THRESHOLD:
        issues.append({
            "type": "ram_overload",
            "severity": "high",
            "value": ram_value
        })
    return issues


def analyze_disk(disk_value):
    issues = []
    if disk_value > DISK_HIGH_THRESHOLD:
        issues.append({
            "type": "disk_overload",
            "severity": "high",
            "value": disk_value
        })
    return issues


def analyze_processes(processes):
    issues = []
    for p in processes:
        cpu = p.get("cpu_percent", 0)
        ram = p.get("memory_percent", 0)

        if cpu > PROCESS_CPU_THRESHOLD:
            issues.append({
                "type": "process_cpu_spike",
                "severity": "medium",
                "pid": p.get("pid"),
                "name": p.get("name", ""),
                "value": cpu
            })

        if ram > PROCESS_RAM_THRESHOLD:
            issues.append({
                "type": "process_ram_spike",
                "severity": "medium",
                "pid": p.get("pid"),
                "name": p.get("name", ""),
                "value": ram
            })

    return issues


def analyze(snapshot):
    # ============================================================
    # KOMPATIBILNÉ SO SNAPSHOT["system"]
    # ============================================================

    system = snapshot.get("system", {})

    cpu_value = system.get("cpu", 0)
    ram_value = system.get("ram", 0)
    disk_value = system.get("disk", 0)

    issues = []

    # CPU
    issues.extend(analyze_cpu(cpu_value))

    # RAM
    issues.extend(analyze_ram(ram_value))

    # DISK
    issues.extend(analyze_disk(disk_value))

    # PROCESY
    issues.extend(analyze_processes(snapshot.get("processes", [])))

    # ============================================================
    # KOMPATIBILNÝ VÝSTUP PRE AUTONÓMIU
    # ============================================================

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "issues": issues,
        "system": {
            "cpu": cpu_value,
            "ram": ram_value,
            "disk": disk_value
        }
    }
