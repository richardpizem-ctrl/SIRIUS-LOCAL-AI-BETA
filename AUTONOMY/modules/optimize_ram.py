import psutil

def build_ram_optimization_actions(system_snapshot):
    """
    Prevod návrhu OPTIMIZE_RAM na konkrétne akcie.
    - nájde procesy s vysokou RAM
    - pripraví JSON akcie pre COLNÍK / TERMINAL
    NIČ NEVYKONÁ priamo – len návrhy.
    """

    actions = []

    # Bezpečný default threshold
    ram_threshold = 5.0  # percent RAM

    # Skúsime použiť procesy zo snapshotu, ak sú tam
    processes = system_snapshot.get("processes", [])

    # Ak snapshot neobsahuje procesy (napr. len counts), použijeme psutil priamo
    if not processes:
        try:
            for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
                try:
                    info = proc.info
                    processes.append({
                        "pid": info['pid'],
                        "name": info['name'],
                        "ram": info['memory_percent']
                    })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except:
            processes = []

    # Vyberieme procesy nad prahom
    high_ram = [
        p for p in processes
        if isinstance(p.get("ram"), (int, float)) and p.get("ram", 0) >= ram_threshold
    ]

    # Zoradíme podľa RAM zostupne
    high_ram.sort(key=lambda p: p.get("ram", 0), reverse=True)

    # Limit – nech nerobíme chaos
    high_ram = high_ram[:5]

    for proc in high_ram:
        actions.append({
            "type": "PROCESS_ACTION",
            "action": "TERMINATE_PROCESS",
            "target_pid": proc["pid"],
            "target_name": proc.get("name"),
            "reason": "HIGH_RAM_USAGE",
            "metrics": {
                "ram_percent": proc.get("ram", 0)
            }
        })

    # Ak nič nie je nad prahom, vraciame prázdny zoznam
    return actions
