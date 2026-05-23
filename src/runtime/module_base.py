import logging
import time

log = logging.getLogger(__name__)


class ModuleBase:
    """
    ModuleBase 4.5
    ----------------
    - Unified lifecycle for all runtime modules
    - Deterministic structured telemetry
    - Error isolation (never crashes RuntimeEngine)
    - Health checks (health() 2.0)
    - Dependency declaration
    - Security metadata (risk, identity, capabilities)
    - Self‑Repair Layer 4.5 ready (safe-mode, degraded mode)
    - Stable structured return values for Runtime4.5
    """

    # --------------------------------------------------------
    # METADATA
    # --------------------------------------------------------
    name = "UnnamedModule"
    version = "1.0.0"
    description = "Base runtime module"
    author = "Unknown"

    # Security metadata
    risk_level = 0.0
    required_identity = None
    capabilities = []  # e.g. ["fs.read", "net.http", "exec.subprocess"]

    # Dependencies (module names)
    depends_on = []

    def __init__(self, engine):
        self.engine = engine
        self.initialized = False
        self.running = False
        self.failed = False

        # Telemetry
        self.init_time = None
        self.start_time = None
               self.stop_time = None
        self.error_count = 0

        # Self‑Repair flags
        self.safe_mode = False
        self.degraded_mode = False

    # --------------------------------------------------------
    # INTERNAL SAFE EXECUTOR
    # --------------------------------------------------------
    def _safe(self, action_name, func):
        """
        Executes a module lifecycle action safely.
        Returns structured result.
        """
        t0 = time.time()
        try:
            func()
            return {
                "status": "success",
                "module": self.name,
                "action": action_name,
                "duration": time.time() - t0,
                "module_base_version": "4.5",
            }
        except Exception as exc:
            self.failed = True
            self.error_count += 1
            log.exception("%s failed for module '%s': %s", action_name, self.name, exc)
            return {
                "status": "error",
                "module": self.name,
                "action": action_name,
                "duration": time.time() - t0,
                "exception": str(exc),
                "module_base_version": "4.5",
            }

    # --------------------------------------------------------
    # INITIALIZE
    # --------------------------------------------------------
    def initialize(self):
        """
        Prepare module resources.
        Override in subclasses.
        """
        def _do():
            log.info("Initializing module: %s", self.name)
            self.init_time = time.time()
            self.initialized = True

        return self._safe("initialize", _do)

    # --------------------------------------------------------
    # START
    # --------------------------------------------------------
    def start(self):
        """
        Start module logic.
        Override in subclasses.
        """
        if not self.initialized:
            init_res = self.initialize()
            if init_res["status"] == "error":
                return init_res

        if self.failed:
            msg = f"Module '{self.name}' cannot start (failed during init)."
            log.error(msg)
            return {
                "status": "error",
                "module": self.name,
                "action": "start",
                "message": msg,
                "module_base_version": "4.5",
            }

        def _do():
            log.info("Starting module: %s", self.name)
            self.start_time = time.time()
            self.running = True

        return self._safe("start", _do)

    # --------------------------------------------------------
    # STOP
    # --------------------------------------------------------
    def stop(self):
        """
        Stop module logic.
        Override in subclasses.
        """
        if not self.running:
            return {
                "status": "skipped",
                "module": self.name,
                "action": "stop",
                "message": "Module not running.",
                "module_base_version": "4.5",
            }

        def _do():
            log.info("Stopping module: %s", self.name)
            self.stop_time = time.time()
            self.running = False

        return self._safe("stop", _do)

    # --------------------------------------------------------
    # SHUTDOWN
    # --------------------------------------------------------
    def shutdown(self):
        """
        Cleanup module resources.
        Override in subclasses.
        """
        def _do():
            log.info("Shutting down module: %s", self.name)
            self.initialized = False

        return self._safe("shutdown", _do)

    # --------------------------------------------------------
    # HEALTH CHECK 2.0
    # --------------------------------------------------------
    def health(self):
        """
        Returns structured module health information.
        Deterministic for Runtime4.5 / Self‑Repair 4.5.
        """
        return {
            "name": self.name,
            "version": self.version,
            "running": self.running,
            "initialized": self.initialized,
            "failed": self.failed,
            "errors": self.error_count,
            "safe_mode": self.safe_mode,
            "degraded_mode": self.degraded_mode,
            "telemetry": {
                "init_time": self.init_time,
                "start_time": self.start_time,
                "stop_time": self.stop_time,
            },
            "security": {
                "risk_level": self.risk_level,
                "required_identity": self.required_identity,
                "capabilities": self.capabilities,
            },
            "depends_on": self.depends_on,
            "module_base_version": "4.5",
        }
