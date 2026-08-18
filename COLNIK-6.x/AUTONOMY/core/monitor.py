import psutil
import os
import platform
import time
import json

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

    # CPU MONITOR
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

    # RAM MONITOR
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

    # DISK MONITOR – delta bajtov (aktivita)
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

        # Prvý cyklus → nemáme delta
        if self.last_disk_total is None:
            self.last_disk_total = total_used
            delta = 0
        else:
            delta = abs(total_used - self.last_disk_total)
            self.last_disk_total = total_used

        # Trendujeme delta, nie percento
        self.disk_history.append(delta)

        return delta

    # PROCESY – bezpečný režim
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

    # SIRIUS STATE – rozšírené
    def get_sirius_state(self):
        return {
            "config_exists": os.path.exists("sirius_config.json"),
            "kg_exists": os.path.exists("autosave_kg.json"),
            "kg_size": os.path.getsize("autosave_kg.json") if os.path.exists("autosave_kg.json") else 0,
            "runtime_exists": os.path.exists("runtime_core.py"),
            "modules": {
                "autonomy": os.path.exists("AUTONOMY"),
                "colnik": os.path.exists("COLNIK-6.x"),
                "workflow": os.path.exists("workflow_engine.py")
            }
        }

    # OS INFO
    def get_os_info(self):
        return {
            "platform": platform.platform(),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version()
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
        # 🔥 FOLDER SCAN – PRESNE TO, ČO ANALYZER OČAKÁVA
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
            "sirius": self.get_sirius_state(),
            "os": self.get_os_info(),

            # 🔥 TERAZ ANALYZER NEPADNE
            "folders": folders_info
        }
