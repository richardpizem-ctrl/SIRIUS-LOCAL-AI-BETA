import time

def analyze_cpu(cpu):
    issues = []
    if cpu["usage_percent_total"] > 85:
        issues.append({"type": "HIGH_CPU", "value": cpu["usage_percent_total"]})
    return issues

def analyze_ram(ram):
    issues = []
    if ram["percent"] > 85:
        issues.append({"type": "HIGH_RAM", "value": ram["percent"]})
    return issues

def analyze_disks(disks):
    issues = []
    for d in disks:
        if d["percent"] > 90:
            issues.append({
                "type": "DISK_FULL",
                "value": d["percent"],
                "mount": d["mountpoint"]
            })
    return issues

def analyze_processes(processes):
    issues = []
    # RESET – procesy zatiaľ neanalyzujeme
    return issues

def analyze(snapshot):
    issues = []

    issues.extend(analyze_cpu(snapshot["cpu"]))
    issues.extend(analyze_ram(snapshot["ram"]))
    issues.extend(analyze_disks(snapshot["disks"]))
    issues.extend(analyze_processes(snapshot["processes"]))

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "issues": issues,
        "system": {
            "cpu": snapshot["cpu"]["usage_percent_total"],
            "ram": snapshot["ram"]["percent"],
            "disk": max([d["percent"] for d in snapshot["disks"]]) if snapshot["disks"] else 0
        }
    }
