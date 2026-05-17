# intelligence_orchestrator_4_3.py
# SIRIUS LOCAL AI – Intelligence Orchestrator 4.3.x
# High-level, AI-aware orchestration layer (deterministic, safe-mode compatible)

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict, Any, Literal, Optional
import time

from system_health_engine_4_3 import SystemHealthEngine43, HealthIssue, HealthReport
from driver_manager_engine_4_3 import DriverManagerEngine43, DriverIssue, DriverReport
from task_manager_engine_4_3 import TaskManagerEngine43, TaskIssue, TaskReport
from service_manager_engine_4_3 import ServiceManagerEngine43, ServiceIssue, ServiceReport
from education_engine_4_3 import (
    EducationEngine43,
    EducationBundle,
    ExplanationBlock,
    IdentityType,
)
from system_agent_4_3 import (
    SystemAgent43,
    AgentAction,
    AgentResult,
    ActionType,
)


Severity = Literal["info", "warning", "critical"]


# ---------------------------------------------------------
# DATA STRUCTURES
# ---------------------------------------------------------

@dataclass
class PrioritizedItem:
    """
    Unified representation of a problem across all diagnostic domains.
    AI-aware priority model (4.3.x).
    """
    id: str
    domain: str  # "health" | "drivers" | "tasks" | "services"
    title: str
    description: str
    severity: Severity
    priority_score: int
    explanation: str
    suggested_actions: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OrchestrationPlan:
    """
    Final orchestration result:
    - prioritized issues
    - agent actions (not necessarily executed)
    - metadata
    """
    identity: IdentityType
    created_at: float
    issues: List[PrioritizedItem]
    actions: List[AgentAction]
    dry_run: bool
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ORCHESTRATOR
# ---------------------------------------------------------

class IntelligenceOrchestrator43:
    """
    Intelligence Orchestrator 4.3.x

    Responsibilities:
        - Run all 4.3 diagnostic engines as a single pipeline
        - Aggregate and prioritize issues across domains
        - Attach human-readable explanations from Education Engine 4.3
        - Build AI-aware, identity-aware action plans for SystemAgent43
        - Remain deterministic, offline, and fully isolated
        - Support safe-mode and degraded-mode behavior
    """

    def __init__(self, dry_run: bool = True) -> None:
        # Engines
        self.health_engine = SystemHealthEngine43()
        self.driver_engine = DriverManagerEngine43()
        self.task_engine = TaskManagerEngine43()
        self.service_engine = ServiceManagerEngine43()
        self.education_engine = EducationEngine43()
        self.agent = SystemAgent43(dry_run=dry_run)

        self.dry_run = dry_run
        self.safe_mode = False
        self.degraded_mode = False

        # Base severity weights
        self._severity_weight: Dict[Severity, int] = {
            "critical": 100,
            "warning": 50,
            "info": 10,
        }

        # Domain importance (health > drivers > tasks > services)
        self._domain_weight: Dict[str, int] = {
            "health": 30,
            "drivers": 25,
            "tasks": 15,
            "services": 10,
        }

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def build_plan(self, identity: IdentityType = "OWNER") -> OrchestrationPlan:
        """
        Run full diagnostics, build explanations, prioritize issues,
        and prepare a list of agent actions (not executed).
        Deterministic, safe-mode aware, error-safe.
        """

        if self.safe_mode:
            return OrchestrationPlan(
                identity=identity,
                created_at=time.time(),
                issues=[],
                actions=[],
                dry_run=self.dry_run,
                safe_mode=True,
                degraded_mode=False,
            )

        try:
            # 1) Run diagnostics
            health_report = self.health_engine.analyze()
            driver_report = self.driver_engine.analyze()
            task_report = self.task_engine.analyze()
            service_report = self.service_engine.analyze()

            # 2) Build explanations
            health_expl = self.education_engine.explain_system_health(identity, health_report)
            driver_expl = self.education_engine.explain_drivers(identity, driver_report)
            task_expl = self.education_engine.explain_tasks(identity, task_report)
            service_expl = self.education_engine.explain_services(identity, service_report)

            # 3) Aggregate and prioritize issues
            issues: List[PrioritizedItem] = []
            issues.extend(self._collect_health_issues(health_report, health_expl))
            issues.extend(self._collect_driver_issues(driver_report, driver_expl))
            issues.extend(self._collect_task_issues(task_report, task_expl))
            issues.extend(self._collect_service_issues(service_report, service_expl))

            # AI-aware normalization & sorting
            issues = self._normalize_and_sort_issues(issues, identity)

            # 4) Build agent actions (not executed yet)
            actions = self._build_agent_actions(
                identity=identity,
                health_report=health_report,
                driver_report=driver_report,
                task_report=task_report,
                service_report=service_report,
                issues=issues,
            )

            return OrchestrationPlan(
                identity=identity,
                created_at=time.time(),
                issues=issues,
                actions=actions,
                dry_run=self.dry_run,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )

        except Exception:
            self.degraded_mode = True
            return OrchestrationPlan(
                identity=identity,
                created_at=time.time(),
                issues=[],
                actions=[],
                dry_run=self.dry_run,
                safe_mode=False,
                degraded_mode=True,
            )

    def execute_plan(
        self,
        identity: IdentityType,
        plan: OrchestrationPlan,
        max_actions: Optional[int] = None,
    ) -> List[AgentResult]:
        """
        Optionally execute part of the plan via SystemAgent43.
        Respects identity and dry_run flag of the underlying agent.
        """
        if self.safe_mode:
            return []

        results: List[AgentResult] = []
        actions = plan.actions

        if max_actions is not None:
            actions = actions[:max_actions]

        for action in actions:
            try:
                result = self.agent.execute_action(identity, action)
                results.append(result)
            except Exception:
                self.degraded_mode = True

        return results

    # ---------------------------------------------------------
    # ISSUE COLLECTION
    # ---------------------------------------------------------

    def _collect_health_issues(
        self,
        report: HealthReport,
        bundle: EducationBundle,
    ) -> List[PrioritizedItem]:
        items: List[PrioritizedItem] = []
        blocks_by_title = {b.title: b for b in bundle.blocks}

        for issue in getattr(report, "issues", []):
            block = blocks_by_title.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, "health", issue)

            items.append(
                PrioritizedItem(
                    id=issue.id,
                    domain="health",
                    title=issue.title,
                    description=issue.description,
                    severity=issue.severity,
                    priority_score=score,
                    explanation=explanation,
                    suggested_actions=issue.suggested_actions,
                    metadata={
                        "health_score": getattr(report, "health_score", None),
                    },
                )
            )

        return items

    def _collect_driver_issues(
        self,
        report: DriverReport,
        bundle: EducationBundle,
    ) -> List[PrioritizedItem]:
        items: List[PrioritizedItem] = []
        blocks_by_title = {b.title: b for b in bundle.blocks}

        for issue in getattr(report, "issues", []):
            block = blocks_by_title.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, "drivers", issue)

            items.append(
                PrioritizedItem(
                    id=issue.id,
                    domain="drivers",
                    title=issue.title,
                    description=issue.description,
                    severity=issue.severity,
                    priority_score=score,
                    explanation=explanation,
                    suggested_actions=issue.suggested_actions,
                    metadata={
                        "related_files": getattr(issue, "related_files", []),
                        "related_devices": getattr(issue, "related_devices", []),
                    },
                )
            )

        return items

    def _collect_task_issues(
        self,
        report: TaskReport,
        bundle: EducationBundle,
    ) -> List[PrioritizedItem]:
        items: List[PrioritizedItem] = []
        blocks_by_title = {b.title: b for b in bundle.blocks}

        for issue in getattr(report, "issues", []):
            block = blocks_by_title.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, "tasks", issue)

            items.append(
                PrioritizedItem(
                    id=issue.id,
                    domain="tasks",
                    title=issue.title,
                    description=issue.description,
                    severity=issue.severity,
                    priority_score=score,
                    explanation=explanation,
                    suggested_actions=issue.suggested_actions,
                    metadata={
                        "related_pids": getattr(issue, "related_pids", []),
                    },
                )
            )

        return items

    def _collect_service_issues(
        self,
        report: ServiceReport,
        bundle: EducationBundle,
    ) -> List[PrioritizedItem]:
        items: List[PrioritizedItem] = []
        blocks_by_title = {b.title: b for b in bundle.blocks}

        for issue in getattr(report, "issues", []):
            block = blocks_by_title.get(issue.title)
            explanation = block.body if block else issue.description
            score = self._compute_priority(issue.severity, "services", issue)

            items.append(
                PrioritizedItem(
                    id=issue.id,
                    domain="services",
                    title=issue.title,
                    description=issue.description,
                    severity=issue.severity,
                    priority_score=score,
                    explanation=explanation,
                    suggested_actions=issue.suggested_actions,
                    metadata={
                        "related_services": getattr(issue, "related_services", []),
                    },
                )
            )

        return items

    # ---------------------------------------------------------
    # AI-AWARE PRIORITY MODEL
    # ---------------------------------------------------------

    def _compute_priority(
        self,
        severity: Severity,
        domain: str,
        issue: Any,
    ) -> int:
        """
        AI-aware priority model (still deterministic):

        - base severity weight
        - domain importance
        - impact hints from issue metadata (CPU, RAM, network, boot, etc.)
        - quick-win bonus for easy, low-risk fixes
        """

        base = self._severity_weight.get(severity, 10)
        domain_offset = self._domain_weight.get(domain, 0)

        impact_bonus = 0
        quick_win_bonus = 0

        # Impact hints
        impact = getattr(issue, "impact", None)
        if impact == "system_stability":
            impact_bonus += 25
        elif impact == "performance":
            impact_bonus += 15
        elif impact == "security":
            impact_bonus += 30
        elif impact == "usability":
            impact_bonus += 10

        # Quick-win hints
        if getattr(issue, "quick_fix", False):
            quick_win_bonus += 10

        return base + domain_offset + impact_bonus + quick_win_bonus

    def _normalize_and_sort_issues(
        self,
        issues: List[PrioritizedItem],
        identity: IdentityType,
    ) -> List[PrioritizedItem]:
        """
        Normalize scores and sort descending.
        Identity-aware adjustment:
        - OWNER: full priority
        - FAMILY: slightly downscale destructive domains (tasks/services)
        - STRANGER: strongly downscale everything except health info
        """

        if not issues:
            return []

        max_score = max(i.priority_score for i in issues) or 1

        adjusted: List[PrioritizedItem] = []
        for item in issues:
            score = item.priority_score / max_score * 100

            if identity == "FAMILY":
                if item.domain in ("tasks", "services"):
                    score *= 0.7
            elif identity == "STRANGER":
                if item.domain != "health":
                    score *= 0.4

            adjusted.append(
                PrioritizedItem(
                    id=item.id,
                    domain=item.domain,
                    title=item.title,
                    description=item.description,
                    severity=item.severity,
                    priority_score=int(score),
                    explanation=item.explanation,
                    suggested_actions=item.suggested_actions,
                    metadata=item.metadata,
                )
            )

        adjusted.sort(key=lambda x: x.priority_score, reverse=True)
        return adjusted

    # ---------------------------------------------------------
    # ACTION MAPPING (4.3.x)
    # ---------------------------------------------------------

    def _build_agent_actions(
        self,
        identity: IdentityType,
        health_report: HealthReport,
        driver_report: DriverReport,
        task_report: TaskReport,
        service_report: ServiceReport,
        issues: List[PrioritizedItem],
    ) -> List[AgentAction]:
        """
        Map prioritized issues to SystemAgent43 actions.
        Identity-aware and AI-aware.
        """

        actions: List[AgentAction] = []

        # DRIVER ISSUES → INSTALL DRIVER / OPEN VENDOR PAGE
        for issue in driver_report.issues:
            if issue.severity in ("warning", "critical"):
                actions.append(
                    AgentAction(
                        id=f"install_driver_{issue.id}",
                        type="INSTALL_DRIVER",
                        label="Install missing or updated driver",
                        description=issue.description,
                        identity_required="OWNER",
                        payload={
                            "related_files": getattr(issue, "related_files", []),
                            "related_devices": getattr(issue, "related_devices", []),
                        },
                    )
                )

        # TASK ISSUES → KILL PROCESS / RESTART EXPLORER
        for issue in task_report.issues:
            if getattr(issue, "id", "") == "explorer_restart_suggestion":
                actions.append(
                    AgentAction(
                        id="restart_explorer",
                        type="RESTART_EXPLORER",
                        label="Restart Windows Explorer",
                        description=issue.description,
                        identity_required="OWNER",
                        payload={},
                    )
                )

            if getattr(issue, "id", "") in ("high_cpu_processes", "high_ram_processes"):
                for pid in getattr(issue, "related_pids", []):
                    actions.append(
                        AgentAction(
                            id=f"kill_process_{pid}",
                            type="KILL_PROCESS",
                            label=f"Terminate process {pid}",
                            description=issue.description,
                            identity_required="OWNER",
                            payload={"pid": pid},
                        )
                    )

        # SERVICE ISSUES → RESTART SERVICE
        for issue in service_report.issues:
            for svc in getattr(issue, "related_services", []):
                actions.append(
                    AgentAction(
                        id=f"restart_service_{svc}",
                        type="RESTART_SERVICE",
                        label=f"Restart service {svc}",
                        description=issue.description,
                        identity_required="OWNER",
                        payload={"service_name": svc},
                    )
                )

        # HEALTH ISSUES → HIGH-LEVEL ACTIONS (e.g., CLEANUP, OPTIMIZE)
        for issue in health_report.issues:
            if getattr(issue, "id", "") == "disk_cleanup_recommended":
                actions.append(
                    AgentAction(
                        id="run_disk_cleanup",
                        type="RUN_DISK_CLEANUP",
                        label="Run disk cleanup",
                        description=issue.description,
                        identity_required="OWNER",
                        payload={},
                    )
                )

        return actions

    # ---------------------------------------------------------
    # SAFE-MODE CONTROL
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
