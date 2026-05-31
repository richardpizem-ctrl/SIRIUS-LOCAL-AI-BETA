# Runtime4 Recovery Protocol
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class RecoveryProtocol:
    """
    SIRIUS LOCAL AI — Recovery Protocol (v4.5.0 PRO)

    Responsibilities:
        - Coordinate integrity scanning and module rebuilding
        - Deterministic, safe-mode compatible recovery workflow
        - Phase‑5 ready (self-repair orchestration, isolation)
        - No exception leakage
        - Works with IntegrityScanner, ModuleRebuilder, FallbackManager
    """

    def __init__(self, integrity_map, baseline_store, logger):
        self.integrity_map = integrity_map or {}
        self.baseline_store = baseline_store or {}
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.last_recovery_ok: bool = True

        if self.logger:
            self.logger.log("[RecoveryProtocol] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # EXECUTE RECOVERY WORKFLOW
    # --------------------------------------------------------
    def execute(self) -> bool:
        """
        Execute the full recovery protocol.
        Phase‑5 rules:
            - Deterministic
            - No exceptions leak
            - Safe-mode aware
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[RecoveryProtocol] SAFE MODE → execute() blocked")
                return False

            if self.logger:
                self.logger.log("[RecoveryProtocol] Recovery started")

            # Validate integrity_map
            if not isinstance(self.integrity_map, dict):
                return self._fail("Invalid integrity_map format")

            # Validate baseline_store
            if not isinstance(self.baseline_store, dict):
                return self._fail("Invalid baseline_store format")

            # Phase‑5: detect corrupted modules
            corrupted = self._detect_corruption()

            if not corrupted:
                if self.logger:
                    self.logger.log("[RecoveryProtocol] No corruption detected → OK")
                return True

            # Phase‑5: rebuild corrupted modules
            self._rebuild_modules(corrupted)

            if self.last_recovery_ok:
                if self.logger:
                    self.logger.log("[RecoveryProtocol] Recovery completed successfully")
            else:
                if self.logger:
                    self.logger.log("[RecoveryProtocol] Recovery completed with errors")

            return self.last_recovery_ok

        except Exception as exc:
            self.degraded_mode = True
            self.last_recovery_ok = False
            if self.logger:
                self.logger.log(f"[RecoveryProtocol] execute() error: {exc}")
            return False

    # --------------------------------------------------------
    # DETECT CORRUPTED MODULES
    # --------------------------------------------------------
    def _detect_corruption(self) -> list[str]:
        """Return list of corrupted or missing modules."""
        corrupted = []

        for module_name, entry in self.integrity_map.items():
            if entry is None:
                corrupted.append(module_name)
                if self.logger:
                    self.logger.log(f"[RecoveryProtocol] Missing integrity entry: {module_name}")
                continue

            if isinstance(entry, dict) and entry.get("status") != "ok":
                corrupted.append(module_name)
                if self.logger:
                    self.logger.log(f"[RecoveryProtocol] Corrupted module: {module_name}")

        return corrupted

    # --------------------------------------------------------
    # REBUILD CORRUPTED MODULES
    # --------------------------------------------------------
    def _rebuild_modules(self, modules: list[str]):
        """Rebuild the given modules using baseline_store."""
        for module_name in modules:
            if module_name not in self.baseline_store:
                self._fail(f"No baseline available for: {module_name}")
                continue

            baseline_content = self.baseline_store[module_name]

            try:
                with open(module_name, "w", encoding="utf-8") as f:
                    f.write(baseline_content)

                if self.logger:
                    self.logger.log(f"[RecoveryProtocol] Restored module: {module_name}")

            except Exception as exc:
                self._fail(f"Failed to restore {module_name}: {exc}")

    # --------------------------------------------------------
    # INTERNAL FAILURE HANDLER
    # --------------------------------------------------------
    def _fail(self, message: str) -> bool:
        """Mark recovery as failed and log the issue."""
        self.last_recovery_ok = False
        if self.logger:
            self.logger.log(f"[RecoveryProtocol] ERROR: {message}")
        return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[RecoveryProtocol] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[RecoveryProtocol] SAFE MODE disabled")
