# ai_loop_4_5.py
# SIRIUS LOCAL AI – Autonomous Runtime Loop 4.5.0 PRO
# Deterministic, safe‑mode compatible, sandboxed AI loop (Phase‑5 ready)

from __future__ import annotations

import time
import threading
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from runtime.runtime_manager_4_5 import RuntimeManager45


# ============================================================
# FILESYSTEM HANDLER (4.5.0 PRO)
# ============================================================
class FSHandler45(FileSystemEventHandler):
    """Filesystem event handler used by the AI Loop 4.5."""

    def __init__(self, loop: "SiriusAILoop45"):
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
# SIRIUS AI LOOP (4.5.0 PRO)
# ============================================================
class SiriusAILoop45:
    """
    SIRIUS LOCAL AI — Autonomous Runtime Loop (4.5.0 PRO)

    Responsibilities:
        - Filesystem monitoring (sandboxed)
        - System monitoring (safe, deterministic)
        - Rule-based autonomous actions
        - RuntimeManager45 task dispatch
        - Safe-mode + degraded-mode support
        - Phase‑5 / Self‑Repair 4.5 ready
    """

    def __init__(self):
        # Runtime bootstrap
        try:
            self.rm = RuntimeManager45()
            self.rm.initialize()
        except Exception as exc:
            print(f"[AI LOOP] Runtime init failed: {exc}")
            raise

        self.observer = Observer()
        self.rules = self._load_rules()

        self.safe_mode = False
        self.degraded_mode = False
        self._running = True

        self.rm.logger.info("AI Loop initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # RULES (4.5.0 PRO)
    # --------------------------------------------------------
    def _load_rules(self):
        """
        Autonomous behavior rules.
        Phase‑5: deterministic, AI-aware, safe-mode compatible.
        """
        return {
            "log_auto_archive": {
                "enabled": True,
                "folder": "logs/",
                "action": "cleanup_logs",
                "impact": "maintenance",
            },
            "disk_cleanup": {
                "enabled": True,
                "threshold": 90,
                "action": "cleanup_logs",
                "folder": "logs/",
                "impact": "stability",
            },
            "fs_watchdog": {
                "enabled": True,
                "impact": "monitoring",
            },
        }

    # --------------------------------------------------------
    # FILESYSTEM EVENTS (4.5.0 PRO)
    # --------------------------------------------------------
    def handle_fs_event(self, event_type: str, path: str) -> None:
        if self.safe_mode:
            return

        try:
            self.rm.logger.info(f"[FS] {event_type}: {path}")

            rule = self.rules.get("log_auto_archive")
            if rule and rule["enabled"] and path.endswith(".log"):
                self.rm.handle_ai_task(
                    rule["action"],
                    {"folder": rule["folder"]},
                )

        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"FS event error: {e}")

    # --------------------------------------------------------
    # SYSTEM MONITORING (4.5.0 PRO)
    # --------------------------------------------------------
    def monitor_system(self) -> None:
        self.rm.logger.info("System monitor started")

        while self._running:
            try:
                if self.safe_mode:
                    time.sleep(2)
                    continue

                disk = psutil.disk_usage("/").percent

                rule = self.rules.get("disk_cleanup")
                if rule and rule["enabled"] and disk > rule["threshold"]:
                    self.rm.logger.warning(
                        f"[SYS] Disk usage {disk}% > threshold → cleanup"
                    )
                    self.rm.handle_ai_task(
                        rule["action"],
                        {"folder": rule["folder"]},
                    )

                time.sleep(5)

            except Exception as e:
                self.degraded_mode = True
                self.rm.logger.error(f"System monitor error: {e}")
                time.sleep(2)

    # --------------------------------------------------------
    # FILESYSTEM MONITORING (4.5.0 PRO)
    # --------------------------------------------------------
    def monitor_fs(self) -> None:
        self.rm.logger.info("Filesystem monitor started")

        if not self.rules["fs_watchdog"]["enabled"]:
            return

        try:
            handler = FSHandler45(self)
            self.observer.schedule(handler, ".", recursive=True)
            self.observer.start()

        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"FS monitor error: {e}")

    # --------------------------------------------------------
    # MAIN LOOP (4.5.0 PRO)
    # --------------------------------------------------------
    def run(self) -> None:
        header = "🤖 SIRIUS AI LOOP — ENTERPRISE MODE (v4.5.0 PRO)"
        if self.safe_mode:
            header += " [SAFE MODE]"
        elif self.degraded_mode:
            header += " [DEGRADED MODE]"

        self.rm.logger.info(header)
        self.rm.logger.info("Autonomous mode running")

        threading.Thread(target=self.monitor_fs, daemon=True).start()
        threading.Thread(target=self.monitor_system, daemon=True).start()

        try:
            while self._running:
                time.sleep(1)

        except KeyboardInterrupt:
            self.rm.logger.info("Shutdown requested (KeyboardInterrupt)")
            self.shutdown()

        except Exception as e:
            self.degraded_mode = True
            self.rm.logger.error(f"Main loop error: {e}")
            self.shutdown()

    # --------------------------------------------------------
    # CLEAN SHUTDOWN (4.5.0 PRO)
    # --------------------------------------------------------
    def shutdown(self) -> None:
        self.rm.logger.info("Shutting down AI Loop...")

        self._running = False

        try:
            self.observer.stop()
            self.observer.join()
        except Exception:
            pass

        self.rm.logger.info("AI Loop stopped cleanly")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self) -> None:
        self.safe_mode = True

    def exit_safe_mode(self) -> None:
        self.safe_mode = False


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    loop = SiriusAILoop45()
    loop.run()
