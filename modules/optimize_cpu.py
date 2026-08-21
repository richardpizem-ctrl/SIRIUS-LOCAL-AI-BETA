import psutil

def build_cpu_optimization_actions(system_snapshot):
    """
    Prevod návrhu OPTIMIZE_CPU na konkrétne akcie.
    - nájde procesy s vysokým CPU
    - pripraví JSON akcie pre COLNÍK / TERMINAL
    NIČ NEVYKONÁ priamo – len návrhy.
    """

    actions = []

    # Bezpečný default threshold
    cpu_threshold = 10.0  # percent

    # Skúsime použiť procesy zo snapshotu, ak sú tam
    processes = system_snapshot.get("processes", [])

    # Ak snapshot neobsahuje procesy (napr. len counts), použijeme psutil priamo
    if not processes:
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    info = proc.info
                    processes.append({
                        "pid": info['pid'],
                        "name": info['name'],
                        "cpu": info['cpu_percent']
                    })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except:
            processes = []

    # Vyberieme procesy nad prahom
    high_cpu = [
        p for p in processes
        if isinstance(p.get("cpu"), (int, float)) and p.get("cpu", 0) >= cpu_threshold
    ]

    # Zoradíme podľa CPU zostupne
    high_cpu.sort(key=lambda p: p.get("cpu", 0), reverse=True)

    # Limit – nech nerobíme chaos
    high_cpu = high_cpu[:5]

    for proc in high_cpu:
        actions.append({
            "type": "PROCESS_ACTION",
            "action": "LOWER_PRIORITY",
            "target_pid": proc["pid"],
            "target_name": proc.get("name"),
            "reason": "HIGH_CPU_USAGE",
            "metrics": {
                "cpu_percent": proc.get("cpu", 0)
            }
        })

    # Ak nič nie je nad prahom, vraciame prázdny zoznam
    return actions
