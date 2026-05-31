# Runtime4 Orchestrator
# RuntimeManager45 PRO
# Version: 4.5.0 PRO

from __future__ import annotations

from runtime4.system_health.health_monitor import HealthMonitor
from runtime4.self_repair.self_repair_engine import SelfRepairEngine
from runtime4.services.service_registry import ServiceRegistry
from runtime4.services.service_manager import ServiceManager
from runtime4.task_manager.task_scheduler import TaskScheduler
from runtime4.task_manager.task_queue import TaskQueue
from runtime4.task_manager.task_manager import TaskManager


class RuntimeManager45:
    """
    SIRIUS LOCAL AI — Runtime Manager 4.5 PRO

    Orchestrates:
        - System health checks
        - Self‑repair cycles
        - Service lifecycle
        - Task scheduling & execution
        - Global safe-mode / degraded-mode

    Public API:
        - start_runtime()
        - tick()
        - shutdown()
        - status()
    """

    def __init__(
        self,
        health_monitor: HealthMonitor,
        self_repair_engine: SelfRepairEngine,
        service_registry: ServiceRegistry,
        service_manager: ServiceManager,
        task_scheduler: TaskScheduler,
        task_queue: TaskQueue,
        task_manager: TaskManager,
        logger,
    ):
        self.health_monitor = health_monitor
        self.self_repair_engine = self_repair_engine
        self.service_registry = service_registry
        self.service_manager = service_manager
        self.task_scheduler = task_scheduler
        self.task_queue = task_queue
        self.task_manager = task_manager
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.running: bool = False

        self.logger.log("[RuntimeManager45] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # LIFECYCLE
    # --------------------------------------------------------
    def start_runtime(self) -> bool:
        try:
            self.logger.log("[RuntimeManager45] Starting runtime")

            # Start all registered services
            for name in self.service_registry.list():
                self.service_manager.start(name)

            self.running = True
            self.logger.log("[RuntimeManager45] Runtime started")
            return True

        except Exception as exc:
            self.degraded_mode = True
            self.logger.log(f"[RuntimeManager45] start_runtime() error: {exc}")
            return False

    def shutdown(self) -> bool:
        try:
            self.logger.log("[RuntimeManager45] Shutting down runtime")

            for name in self.service_registry.list():
                self.service_manager.stop(name)

            self.running = False
            self.logger.log("[RuntimeManager45] Runtime stopped")
            return True

        except Exception as exc:
            self.degraded_mode = True
            self.logger.log(f"[RuntimeManager45] shutdown() error: {exc}")
            return False

    # --------------------------------------------------------
    # MAIN TICK
    # --------------------------------------------------------
    def tick(self):
        """
        One orchestrator step.
        Order:
            1) health check
            2) self‑repair if needed
            3) task execution
        """
        if not self.running:
            return

        try:
            # 1) Health check
            ok = self.health_monitor.check()
            if not ok:
                self.logger.log("[RuntimeManager45] Health issue detected → triggering self‑repair")
                self._run_self_repair()

            # 2) Run next task
            self.task_manager.run_next()

        except Exception as exc:
            self.degraded_mode = True
            self.logger.log(f"[RuntimeManager45] tick() error: {exc}")

    # --------------------------------------------------------
    # SELF‑REPAIR
    # --------------------------------------------------------
    def _run_self_repair(self):
        try:
            stable = self.self_repair_engine.run_cycle()
            if not stable:
                self.degraded_mode = True
                self.logger.log("[RuntimeManager45] Self‑repair ended in degraded mode")
        except Exception as exc:
            self.degraded_mode = True
            self.logger.log(f"[RuntimeManager45] _run_self_repair() error: {exc}")

    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------
    def status(self) -> dict:
        try:
            health = self.health_monitor.status()
            return {
                "running": self.running,
                "safe_mode": self.safe_mode,
                "degraded_mode": self.degraded_mode,
                "health": health,
            }
        except Exception as exc:
            self.degraded_mode = True
            self.logger.log(f"[RuntimeManager45] status() error: {exc}")
            return {
                "running": self.running,
                "safe_mode": self.safe_mode,
                "degraded_mode": True,
                "health": {"ok": False, "issue": "internal_error"},
            }

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        self.logger.log("[RuntimeManager45] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        self.logger.log("[RuntimeManager45] SAFE MODE disabled")
