import psutil
import platform
import time

class SystemMonitor:

    def __init__(self):
        pass

    # -----------------------------
    # SAFE CPU / RAM / DISK
    # -----------------------------
    def safe_system(self):
        try:
            cpu = psutil.cpu_percent(interval=0.1)
        except:
            cpu = 0.0

        try:
            ram = psutil.virtual_memory().percent
        except:
            ram = 0.0

        try:
            disk = psutil.disk_usage("C:\\").percent
        except:
            disk = 0.0

        return {
            "cpu": cpu,
            "ram": ram,
            "disk": disk
        }

    # -----------------------------
    # SAFE PROCESS LIST
    # -----------------------------
    def safe_process_list(self):
        processes = []
        for proc in psutil.process_iter(["pid", "name"]):
            try:
                processes.append({
                    "pid": proc.pid,
                    "name": proc.info["name"]
                })
            except:
                continue
        return processes

    # -----------------------------
    # SAFE FOLDER META (NO SCAN)
    # -----------------------------
    def safe_folder_meta(self):
        # IBA META – ŽIADNE os.walk, ŽIADNE getsize
        try:
            root = "C:\\"
            folders = len(next(os.walk(root))[1])
            files = len(next(os.walk(root))[2])
        except:
            folders = 0
            files = 0

        return {
            "root": "C:\\",
            "folders_total": folders,
            "files_total": files,
            "total_size": 0,
            "largest_folder": {
                "path": "C:\\Windows",
                "size": 0
            }
        }

    # -----------------------------
    # MAIN SNAPSHOT
    # -----------------------------
    def snapshot(self):
        system_info = self.safe_system()
        processes = self.safe_process_list()
        folders = self.safe_folder_meta()

        return {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "system": system_info,
            "processes": processes,
            "folders": folders
        }
