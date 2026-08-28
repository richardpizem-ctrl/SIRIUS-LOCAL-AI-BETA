def analyze_state(system_state):
    analysis = {}

    # CPU
    cpu = system_state.get("cpu", 0)
    if cpu < 50:
        analysis["cpu_status"] = "OK"
    elif cpu < 80:
        analysis["cpu_status"] = "HIGH"
    else:
        analysis["cpu_status"] = "CRITICAL"

    # RAM
    ram = system_state.get("ram", 0)
    if ram < 50:
        analysis["ram_status"] = "OK"
    elif ram < 80:
        analysis["ram_status"] = "HIGH"
    else:
        analysis["ram_status"] = "CRITICAL"

    # Disk
    disk = system_state.get("disk", 0)
    if disk < 70:
        analysis["disk_status"] = "OK"
    elif disk < 90:
        analysis["disk_status"] = "HIGH"
    else:
        analysis["disk_status"] = "CRITICAL"

    return analysis


def propose_action(analysis):
    # CPU
    if analysis.get("cpu_status") == "CRITICAL":
        return "INSPECT_CPU"

    # RAM
    if analysis.get("ram_status") == "CRITICAL":
        return "CLEAN_MEMORY"

    # Disk
    if analysis.get("disk_status") == "CRITICAL":
        return "DISK_CLEANUP"

    # Default
    return "NONE"
