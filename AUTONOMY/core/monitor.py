import psutil
import os
import platform
import time
import json
import subprocess

from AUTONOMY.core.trend_utils import compute_trend


class SystemMonitor:
    def __init__(self):
        self.timestamp = None

        # História pre trendovanie
        self.cpu_history = []
        self.ram_history = []
        self.disk_history = []

        # Disk delta – posledná hodnota
        self.last_disk_total = None

    # ============================================================
    # CPU MONITOR
    # ============================================================
    def get_cpu(self):
        try:
            percent = psutil.cpu_percent(interval=0.2)
            self.cpu_history.append(percent)

            return {
                "percent": percent,
                "count": psutil.cpu_count(logical=True),
                "freq": psutil.cpu_freq().current if psutil.cpu_freq() else 0
            }
        except Exception:
            return {"percent": 0, "count": 0, "freq": 0}

    # ============================================================
    # RAM MONITOR
    # ============================================================
    def get_ram(self):
        try:
            mem = psutil.virtual_memory()
            self.ram_history.append(mem.percent)

            return {
                "total": mem.total,
                "available": mem.available,
                "used": mem.used,
                "percent": mem.percent
            }
        except:
            return {"total": 0, "available": 0, "used": 0, "percent": 0}

    # ============================================================
    # DISK MONITOR – delta bajtov (aktivita)
    # ============================================================
    def get_disk_activity(self):
        total_used = 0

        try:
            for part in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(part.mountpoint)
                    total_used += usage.used
                except PermissionError:
                    continue
        except:
            return 0

        if self.last_disk_total is None:
            self.last_disk_total = total_used
            delta = 0
        else:
            delta = abs(total_used - self.last_disk_total)
            self.last_disk_total = total_used

        self.disk_history.append(delta)
        return delta

    # ============================================================
    # PROCESY – bezpečný režim
    # ============================================================
    def get_processes(self):
        process_list = []
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    info = proc.info
                    process_list.append({
                        "pid": info['pid'],
                        "name": info['name'],
                        "cpu": info['cpu_percent'],
                        "ram": info['memory_percent']
                    })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except:
            return []
        return process_list[:25]

    # ============================================================
    # GPU – doplnené (PILIER 1)
    # ============================================================
    def get_gpu(self):
        gpu_info = {
            "name": None,
            "memory_total": None,
            "memory_used": None
        }

        try:
            result = subprocess.check_output(
                ["wmic", "path", "win32_VideoController", "get", "Name"],
                stderr=subprocess.DEVNULL,
                stdin=subprocess.DEVNULL,
                text=True
            )
            lines = [l.strip() for l in result.splitlines() if l.strip()]
            if len(lines) > 1:
                gpu_info["name"] = lines[1]
        except Exception:
            pass

        return gpu_info

    # ============================================================
    # SLUŽBY – doplnené (PILIER 1)
    # ============================================================
    def get_services_info(self):
        services_total = 0
        running = 0
        stopped = 0

        try:
            for svc in psutil.win_service_iter():
                services_total += 1
                try:
                    status = svc.status()
                    if status == "running":
                        running += 1
                    else:
                        stopped += 1
                except Exception:
                    continue
        except Exception:
            pass

        return {
            "total": services_total,
            "running": running,
            "stopped": stopped
        }

    # ============================================================
    # OS INFO – rozšírené o služby
    # ============================================================
    def get_os_info(self):
        return {
            "platform": platform.platform(),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "services": self.get_services_info()
        }

    # ============================================================
    # SIRIUS STATE – doplnené ENVOY + SELFREPAIR + configs
    # ============================================================
    def get_sirius_state(self):
        sirius_root = "C:\\SIRIUS_ARCHIVE\\COLNIK-6.x"

        envoy_exists = os.path.exists(os.path.join(sirius_root, "ENVOY"))
        selfrepair_exists = os.path.exists(os.path.join(sirius_root, "SELFREPAIR"))

        sirius_config = os.path.join(sirius_root, "sirius_config.json")
        kg_autosave = os.path.join(sirius_root, "KG", "autosave_kg.json")

        return {
            "config_exists": os.path.exists(sirius_config),
            "kg_exists": os.path.exists(kg_autosave),
            "kg_size": os.path.getsize(kg_autosave) if os.path.exists(kg_autosave) else 0,
            "runtime_exists": os.path.exists(os.path.join(sirius_root, "runtime_core.py")),

            "modules": {
                "autonomy": os.path.exists(os.path.join(sirius_root, "AUTONOMY")),
                "colnik": os.path.exists(os.path.join(sirius_root, "COLNIK-6.x")),
                "workflow": os.path.exists(os.path.join(sirius_root, "workflow_engine.py")),
                "envoy": envoy_exists,
                "selfrepair": selfrepair_exists
            },

            "configs": {
                "sirius_config": os.path.exists(sirius_config),
                "kg_autosave": os.path.exists(kg_autosave),
                "modules_folder": os.path.exists(os.path.join(sirius_root, "modules"))
            }
        }

    # SNAPSHOT – kompletný stav systému + TRENDY
    def snapshot(self):
        self.timestamp = time.time()

        cpu_data = self.get_cpu()
        ram_data = self.get_ram()
        disk_delta = self.get_disk_activity()

        cpu_trend = compute_trend(self.cpu_history)
        ram_trend = compute_trend(self.ram_history)
        disk_trend = compute_trend(self.disk_history)

        # ============================================================
        # FOLDER SCAN – nechávam presne ako máš
        # ============================================================

        root = "C:\\SIRIUS_ARCHIVE"
        folders_total = 0
        files_total = 0
        total_size = 0
        largest_folder = {"path": root, "size": 0}

        try:
            for entry in os.scandir(root):
                if entry.is_dir():
                    folders_total += 1
                    size = 0
                    try:
                        for sub in os.scandir(entry.path):
                            if sub.is_file():
                                files_total += 1
                                file_size = os.path.getsize(sub.path)
                                size += file_size
                                total_size += file_size
                    except:
                        pass

                    if size > largest_folder["size"]:
                        largest_folder = {"path": entry.path, "size": size}

                elif entry.is_file():
                    files_total += 1
                    total_size += os.path.getsize(entry.path)

        except Exception:
            pass

        folders_info = {
            "root": root,
            "folders_total": folders_total,
            "files_total": files_total,
            "total_size": total_size,
            "largest_folder": largest_folder
        }

        # ============================================================

        return {
            "timestamp": self.timestamp,

            "system": {
                "cpu": cpu_data["percent"],
                "ram": ram_data["percent"],
                "disk": disk_delta
            },

            "trend": {
                "cpu": cpu_trend,
                "ram": ram_trend,
                "disk": disk_trend
            },

            "processes": self.get_processes(),
            "gpu": self.get_gpu(),
            "sirius": self.get_sirius_state(),
            "os": self.get_os_info(),
            "folders": folders_info
        }
