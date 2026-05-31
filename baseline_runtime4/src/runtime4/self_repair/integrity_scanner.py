# Runtime4 Integrity Scanner
# Phase‑5 Ready Module
# Version: 4.5.0 PRO

from __future__ import annotations


class IntegrityScanner:
    """
    SIRIUS LOCAL AI — Integrity Scanner (v4.5.0 PRO)

    Responsibilities:
        - Validate integrity_map entries deterministically
        - Detect missing or corrupted components
        - Phase‑5 ready (self-repair hooks, isolation)
        - No exception leakage
        - Works with Self‑Repair Layer and RuntimeManager45
    """

    def __init__(self, integrity_map: dict, logger=None):
        self.integrity_map = integrity_map or {}
        self.logger = logger

        self.safe_mode: bool = False
        self.degraded_mode: bool = False
        self.last_scan_ok: bool = True

        if self.logger:
            self.logger.log("[IntegrityScanner] Initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # SCAN INTEGRITY MAP
    # --------------------------------------------------------
    def scan(self) -> bool:
        """
        Perform integrity scan safely.
        Phase‑5 rules:
            - Deterministic
            - No exceptions leak
            - Safe-mode aware
        """
        try:
            if self.safe_mode:
                if self.logger:
                    self.logger.log("[IntegrityScanner] SAFE MODE → scan() blocked")
                return True

            if self.logger:
                self.logger.log("[IntegrityScanner] Scan started")

            # Integrity map must be a dict
            if not isinstance(self.integrity_map, dict):
                if self.logger:
                    self.logger.log("[IntegrityScanner] Invalid integrity_map type")
                self.last_scan_ok = False
                return False

            # Phase‑5: check each entry
            for key, value in self.integrity_map.items():
                if value is None:
                    if self.logger:
                        self.logger.log(f"[IntegrityScanner] Missing integrity entry: {key}")
                    self.last_scan_ok = False
                    continue

                if isinstance(value, dict) and "status" in value:
                    if value["status"] != "ok":
                        if self.logger:
                            self.logger.log(f"[IntegrityScanner] Integrity issue: {key} → {value}")
                        self.last_scan_ok = False

            if self.last_scan_ok:
                if self.logger:
                    self.logger.log("[IntegrityScanner] Integrity OK")
            else:
                if self.logger:
                    self.logger.log("[IntegrityScanner] Integrity scan FAILED")

            return self.last_scan_ok

        except Exception as exc:
            self.degraded_mode = True
            self.last_scan_ok = False
            if self.logger:
                self.logger.log(f"[IntegrityScanner] scan() error: {exc}")
            return False

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self):
        self.safe_mode = True
        if self.logger:
            self.logger.log("[IntegrityScanner] SAFE MODE enabled")

    def exit_safe_mode(self):
        self.safe_mode = False
        if self.logger:
            self.logger.log("[IntegrityScanner] SAFE MODE disabled")
