# system_health_engine_4_5.py
# SIRIUS LOCAL AI – System Health Engine 4.5.0 PRO
# Deterministic, safe-mode compatible, Phase‑5 ready health diagnostics

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import List, Literal, Optional, Dict, Any

import psutil


HealthSeverity = Literal["info", "warning", "critical"]


# ---------------------------------------------------------
# DATA STRUCTURES (4.5.0 PRO)
# ---------------------------------------------------------

@dataclass
class HealthIssue45:
    id: str
    severity: HealthSeverity
    title: str
    description: str
    suggested_actions: List[str] = field(default_factory=list)
    impact: Optional[str] = None
    quick_fix: bool = False


@dataclass
class HealthReport45:
    timestamp: float
    cpu_usage: float
    ram_usage: float
    disk_usage: float
    health_score: int
    issues: List[HealthIssue45] = field(default_factory=list)
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ENGINE 4.5.0 PRO
# ---------------------------------------------------------

class SystemHealthEngine45:
    """
    System Health Engine 4.5.0 PRO

    Responsibilities:
        - Collect CPU/RAM/DISK metrics
        - Detect performance, stability and resource issues
        - Produce deterministic HealthReport45
        - Safe-mode & degraded-mode aware
        - Phase‑5 ready (extended health domains)
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def analyze(self) -> HealthReport45:
        if self.safe_mode:
            return HealthReport45(
                timestamp=time.time(),
                cpu_usage=0.0,
                ram_usage=0.0,
                disk_usage=0.0,
                health_score=100,
                issues=[],
                safe_mode=True,
                degraded_mode=False,
            )

        try:
            cpu = psutil.cpu_percent(interval=0.2)
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage("/").percent

            issues: List[HealthIssue45] = []
            score = 100

            # CPU
            if cpu > 85:
                issues.append(
                    HealthIssue45(
                        id="high_cpu",
                        severity="warning",
                        title="Vysoké vyťaženie CPU",
                        description="Procesor je dlhodobo vyťažený nad 85%.",
                        suggested_actions=["Skontrolovať procesy s vysokým CPU."],
                        impact="performance",
                        quick_fix=True,
                    )
                )
                score -= 20

            # RAM
            if ram > 90:
                issues.append(
                    HealthIssue45(
                        id="high_ram",
                        severity="warning",
                        title="Nedostatok RAM",
                        description="RAM je vyťažená nad 90%.",
                        suggested_actions=["Zatvoriť nepotrebné aplikácie."],
                        impact="performance",
                        quick_fix=True,
                    )
                )
                score -= 20

            # DISK
            if disk > 90:
                issues.append(
                    HealthIssue45(
                        id="disk_full",
                        severity="critical",
                        title="Disk je takmer plný",
                        description="Disk je zaplnený nad 90%.",
                        suggested_actions=["Odstrániť nepotrebné súbory.", "Spustiť čistenie disku."],
                        impact="system_stability",
                        quick_fix=False,
                    )
                )
                score -= 30

            # Disk cleanup suggestion
            if disk > 75:
                issues.append(
                    HealthIssue45(
                        id="disk_cleanup_recommended",
                        severity="info",
                        title="Odporúčané čistenie disku",
                        description="Disk je zaplnený nad 75%.",
                        suggested_actions=["Spustiť čistenie disku."],
                        impact="usability",
                        quick_fix=True,
                    )
                )

            # Final score clamp
            score = max(0, min(100, score))

            return HealthReport45(
                timestamp=time.time(),
                cpu_usage=cpu,
                ram_usage=ram,
                disk_usage=disk,
                health_score=score,
                issues=issues,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )

        except Exception:
            self.degraded_mode = True
            return HealthReport45(
                timestamp=time.time(),
                cpu_usage=0.0,
                ram_usage=0.0,
                disk_usage=0.0,
                health_score=0,
                issues=[],
                safe_mode=False,
                degraded_mode=True,
            )

    # ---------------------------------------------------------
    # SAFE MODE CONTROL
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
