import time
import threading
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from runtime.runtime_manager import RuntimeManager


# ============================================================
# FILESYSTEM HANDLER (v4)
# ============================================================
class FSHandler(FileSystemEventHandler):
    """Filesystem event handler used by the AI Loop."""

    def __init__(self, loop):
        self.loop = loop

    def on_created(self, event):
        if not event.is_directory:
            self.loop.handle_fs_event("created", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.loop.handle_fs_event("modified", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.loop.handle_fs_event("deleted", event.src_path)


# ============================================================
# SIRIUS AI LOOP (v4.0.0)
# ============================================================
class SiriusAILoop:
    """
    SIRIUS LOCAL AI — Autonomous Runtime Loop (v4.0.0)

    Responsibilities:
    - Filesystem monitoring
    - System monitoring
    - Rule-based autonomous actions
    - RuntimeManager task dispatch
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()

        self.observer = Observer()
        self.rules = self._load_rules()

        self._running = True
        self.rm.logger.info("AI Loop initialized (v4.0.0)")

    # --------------------------------------------------------
    # RULES (v4)
    # --------------------------------------------------------
    def _load_rules(self):
        """Autonomous behavior rules (modifiable without restart)."""
        return {
            "log_auto_archive": {
                "enabled": True,
                "folder": "logs/",
                "action": "cleanup_logs"
            },
            "auto_snap_code": {
                "enabled": False,  # disabled by default in v4
                "app": "code.exe",
                "action": "snap_right"
            },
            "disk_cleanup": {
                "enabled": True,
                "threshold": 90,
                "action": "cleanup_logs",
                "folder": "logs/"
            }
        }

    # --------------------------------------------------------
    # FILESYSTEM EVENTS (v4)
    # --------------------------------------------------------
    def handle_fs_event(self, event_type, path):
        self.rm.logger.info(f"[FS] {event_type}: {path}")

        if self.rules["log_auto_archive"]["enabled"]:
            if path.endswith(".log"):
                self.rm.handle_ai_task(
                    "cleanup_logs",
                    {"folder": self.rules["log_auto_archive"]["folder"]}
                )

    # --------------------------------------------------------
    # SYSTEM MONITORING (v4)
    # --------------------------------------------------------
    def monitor_system(self):
        self.rm.logger.info("System monitor started")

        while self._running:
            try:
                disk = psutil.disk_usage("/").percent

                if self.rules["disk_cleanup"]["enabled"]:
                    if disk > self.rules["disk_cleanup"]["threshold"]:
                        self.rm.logger.warning(
                            f"[SYS] Disk usage {disk}% > threshold → cleanup"
                        )
                        self.rm.handle_ai_task(
                            "cleanup_logs",
                            {"folder": self.rules["disk_cleanup"]["folder"]}
                        )

                time.sleep(5)

            except Exception as e:
                self.rm.logger.error(f"System monitor error: {e}")
                time.sleep(2)

    # --------------------------------------------------------
    # FILESYSTEM MONITORING (v4)
    # --------------------------------------------------------
    def monitor_fs(self):
        self.rm.logger.info("Filesystem monitor started")

        try:
            handler = FSHandler(self)
            self.observer.schedule(handler, ".", recursive=True)
            self.observer.start()

        except Exception as e:
            self.rm.logger.error(f"FS monitor error: {e}")

    # --------------------------------------------------------
    # MAIN LOOP (v4)
    # --------------------------------------------------------
    def run(self):
        self.rm.logger.info("🤖 SIRIUS AI LOOP — ENTERPRISE MODE (v4.0.0)")
        self.rm.logger.info("Autonomous mode running")

        # Start FS monitoring
        threading.Thread(target=self.monitor_fs, daemon=True).start()

        # Start system monitoring
        threading.Thread(target=self.monitor_system, daemon=True).start()

        # Keep main thread alive
        try:
            while self._running:
                time.sleep(1)

        except KeyboardInterrupt:
            self.rm.logger.info("Shutdown requested (KeyboardInterrupt)")
            self.shutdown()

        except Exception as e:
            self.rm.logger.error(f"Main loop error: {e}")
            self.shutdown()

    # --------------------------------------------------------
    # CLEAN SHUTDOWN (v4)
    # --------------------------------------------------------
    def shutdown(self):
        self.rm.logger.info("Shutting down AI Loop...")

        self._running = False

        try:
            self.observer.stop()
            self.observer.join()
        except Exception:
            pass

        self.rm.logger.info("AI Loop stopped cleanly")


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    loop = SiriusAILoop()
    loop.run()
