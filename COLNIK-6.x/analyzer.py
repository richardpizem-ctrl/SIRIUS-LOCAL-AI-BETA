# ANALYZER 6.x – kompatibilný s monitor.py (disková aktivita)
import time
from timecore import TimeCore   # <<< TIMECORE

# TIMECORE – PILIER 0
timecore = TimeCore()
timecore.runtime_start()

LAST_VALUES = {
    "cpu": None,
    "ram": None,
    "disk": None
}

def detect_trend(key, current):
    last = LAST_VALUES.get(key)

    if last is None:
        LAST_VALUES[key] = current
        return "stable"

    # Trend pre CPU/RAM
    if key in ["cpu", "ram"]:
        if current > last + 3:
            trend = "rising"
        elif current < last - 3:
            trend = "falling"
        else:
            trend = "stable"

    # Trend pre DISK (delta bajtov)
    else:
        if last == 0:
            trend = "stable"
        elif current > last * 1.5:
            trend = "rising"
        elif current < last * 0.5:
            trend = "falling"
        else:
            trend = "stable"

    LAST_VALUES[key] = current
    return trend


def analyze_cpu(cpu_value):
    issues = []
    if cpu_value > 85:
        issues.append({
            "type": "HIGH_CPU",
            "severity": "high",
            "value": cpu_value
        })
    return issues


def analyze_ram(ram_value):
    issues = []
    if ram_value > 85:
        issues.append({
            "type": "HIGH_RAM",
            "severity": "high",
            "value": ram_value
        })
    return issues


# 🔥 NOVÁ LOGIKA PRE DISKOVÚ AKTIVITU
def analyze_disk_activity(disk_delta):
    issues = []

    if disk_delta > 20_000_000:  # 20 MB
        issues.append({"type": "DISK_ACTIVITY_CRITICAL", "severity": "critical", "value": disk_delta})

    elif disk_delta > 5_000_000:  # 5 MB
        issues.append({"type": "DISK_ACTIVITY_HIGH", "severity": "high", "value": disk_delta})

    elif disk_delta > 500_000:  # 500 KB
        issues.append({"type": "DISK_ACTIVITY_MEDIUM", "severity": "medium", "value": disk_delta})

    return issues


def analyze_processes(processes):
    return []


def analyze(snapshot):
    # TIMECORE – začiatok analýzy
    timecore.cycle_start()

    cpu_value = snapshot["system"]["cpu"]
    ram_value = snapshot["system"]["ram"]
    disk_delta = snapshot["system"]["disk"]

    # === TRENDY ===
    cpu_trend = detect_trend("cpu", cpu_value)
    ram_trend = detect_trend("ram", ram_value)
    disk_trend = detect_trend("disk", disk_delta)

    # === ISSUES ===
    issues = []
    issues.extend(analyze_cpu(cpu_value))
    issues.extend(analyze_ram(ram_value))
    issues.extend(analyze_disk_activity(disk_delta))
    issues.extend(analyze_processes(snapshot["processes"]))

    # TIMECORE – koniec analýzy
    timecore.cycle_end()

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cycle_time": timecore.cycle_delta(),   # <<< TIMECORE METRIKA
        "issues": issues,
        "system": {
            "cpu": cpu_value,
            "ram": ram_value,
            "disk": disk_delta
        },
        "trends": {
            "cpu": cpu_trend,
            "ram": ram_trend,
            "disk": disk_trend
        }
    }
