import psutil

def scan_hardware():
    """
    Reálna implementácia hardvérového skeneru.
    Získava CPU, RAM a disky cez psutil.
    """
    info = {
        "cpu": {
            "cores": psutil.cpu_count(logical=False),
            "threads": psutil.cpu_count(logical=True),
            "frequency": psutil.cpu_freq().current if psutil.cpu_freq() else None,
            "usage": psutil.cpu_percent(interval=0.1)
        },
        "ram": {
            "total": psutil.virtual_memory().total,
            "used": psutil.virtual_memory().used,
            "percent": psutil.virtual_memory().percent
        },
        "disks": []
    }

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            info["disks"].append({
                "device": part.device,
                "mount": part.mountpoint,
                "fstype": part.fstype,
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": usage.percent
            })
        except PermissionError:
            continue

    return info
