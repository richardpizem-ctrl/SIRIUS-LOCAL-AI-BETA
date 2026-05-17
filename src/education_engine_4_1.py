# education_engine_4_3.py
# SIRIUS LOCAL AI – Education Engine 4.3.x
# Deterministic, safe-mode compatible explanation generator

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional


# ---------------------------------------------------------
# IDENTITY TYPES (Security Family 4.3.x)
# ---------------------------------------------------------

IdentityType = Literal["OWNER", "FAMILY", "STRANGER"]


# ---------------------------------------------------------
# FALLBACK TYPE IMPORTS (Phase‑4 safe)
# ---------------------------------------------------------

try:
    from system_health_engine_4_3 import HealthReport, HealthIssue
    from driver_manager_engine_4_3 import DriverReport, DriverIssue
    from task_manager_engine_4_3 import TaskReport, TaskIssue
    from service_manager_engine_4_3 import ServiceReport, ServiceIssue
except Exception:
    HealthReport = object  # type: ignore
    HealthIssue = object   # type: ignore
    DriverReport = object  # type: ignore
    DriverIssue = object   # type: ignore
    TaskReport = object    # type: ignore
    TaskIssue = object     # type: ignore
    ServiceReport = object # type: ignore
    ServiceIssue = object  # type: ignore


# ---------------------------------------------------------
# DATA STRUCTURES (Phase‑4)
# ---------------------------------------------------------

@dataclass
class ExplanationBlock:
    """
    One explanation block for UI or console.
    Phase‑4: deterministic, sanitized, identity-aware.
    """
    title: str
    body: str
    severity: str
    suggested_actions: List[str]


@dataclass
class EducationBundle:
    """
    Complete explanation bundle for a diagnostic report.
    """
    identity: IdentityType
    summary: str
    blocks: List[ExplanationBlock]
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ENGINE
# ---------------------------------------------------------

class EducationEngine43:
    """
    Education Engine 4.3.x

    Responsibilities:
        - Convert technical reports into human-readable explanations
        - Respect identity (OWNER / FAMILY / STRANGER)
        - Provide deterministic, safe-mode compatible output
        - Provide structured fallback behavior
        - Self‑Repair 4.4 ready
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def explain_system_health(self, identity: IdentityType, report: HealthReport) -> EducationBundle:
        if self.safe_mode:
            return self._bundle_safe_mode(identity)

        try:
            summary = self._build_health_summary(identity, report)
            blocks = [self._explain_health_issue(identity, issue) for issue in report.issues]

            return EducationBundle(
                identity=identity,
                summary=summary,
                blocks=blocks,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )
        except Exception:
            self.degraded_mode = True
            return self._bundle_degraded(identity)

    def explain_drivers(self, identity: IdentityType, report: DriverReport) -> EducationBundle:
        if self.safe_mode:
            return self._bundle_safe_mode(identity)

        try:
            summary = self._build_driver_summary(identity, report)
            blocks = [self._explain_driver_issue(identity, issue) for issue in report.issues]

            return EducationBundle(
                identity=identity,
                summary=summary,
                blocks=blocks,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )
        except Exception:
            self.degraded_mode = True
            return self._bundle_degraded(identity)

    def explain_tasks(self, identity: IdentityType, report: TaskReport) -> EducationBundle:
        if self.safe_mode:
            return self._bundle_safe_mode(identity)

        try:
            summary = self._build_task_summary(identity, report)
            blocks = [self._explain_task_issue(identity, issue) for issue in report.issues]

            return EducationBundle(
                identity=identity,
                summary=summary,
                blocks=blocks,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )
        except Exception:
            self.degraded_mode = True
            return self._bundle_degraded(identity)

    def explain_services(self, identity: IdentityType, report: ServiceReport) -> EducationBundle:
        if self.safe_mode:
            return self._bundle_safe_mode(identity)

        try:
            summary = self._build_service_summary(identity, report)
            blocks = [self._explain_service_issue(identity, issue) for issue in report.issues]

            return EducationBundle(
                identity=identity,
                summary=summary,
                blocks=blocks,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )
        except Exception:
            self.degraded_mode = True
            return self._bundle_degraded(identity)

    # ---------------------------------------------------------
    # SAFE-MODE / DEGRADED-MODE BUNDLES
    # ---------------------------------------------------------

    def _bundle_safe_mode(self, identity: IdentityType) -> EducationBundle:
        return EducationBundle(
            identity=identity,
            summary="Education Engine je v SAFE MODE. Diagnostické vysvetlenia sú dočasne vypnuté.",
            blocks=[],
            safe_mode=True,
            degraded_mode=False,
        )

    def _bundle_degraded(self, identity: IdentityType) -> EducationBundle:
        return EducationBundle(
            identity=identity,
            summary="Education Engine je v DEGRADED MODE. Niektoré vysvetlenia nemusia byť dostupné.",
            blocks=[],
            safe_mode=False,
            degraded_mode=True,
        )

    # ---------------------------------------------------------
    # SUMMARY BUILDERS (Phase‑4)
    # ---------------------------------------------------------

    def _build_health_summary(self, identity: IdentityType, report: HealthReport) -> str:
        score = getattr(report, "health_score", 0)
        base = f"Aktuálne zdravie systému je {score}/100."

        if score >= 80:
            tone = "Systém je vo veľmi dobrom stave."
        elif score >= 50:
            tone = "Systém má niekoľko problémov, ktoré môžu spôsobovať spomalenie."
        else:
            tone = "Systém je v zhoršenom stave a odporúča sa riešiť problémy čím skôr."

        return self._identity_append(identity, base + " " + tone)

    def _build_driver_summary(self, identity: IdentityType, report: DriverReport) -> str:
        count = len(getattr(report, "issues", []))
        base = f"Nájdených bolo {count} problémov súvisiacich s ovládačmi."

        if count == 0:
            tone = " Ovládače momentálne nevyzerajú problematicky."
        else:
            tone = " Niektoré zariadenia nemusia fungovať správne."

        return self._identity_append(identity, base + tone)

    def _build_task_summary(self, identity: IdentityType, report: TaskReport) -> str:
        total = len(getattr(report, "processes", []))
        base = f"V systéme beží približne {total} procesov."

        if not getattr(report, "issues", []):
            tone = " Nevidím žiadne výrazné problémy s procesmi."
        else:
            tone = " Niektoré procesy môžu spôsobovať spomalenie alebo nestabilitu."

        return self._identity_append(identity, base + " " + tone)

    def _build_service_summary(self, identity: IdentityType, report: ServiceReport) -> str:
        total = len(getattr(report, "services", []))
        base = f"Systémové služby: približne {total} aktívnych záznamov."

        if not getattr(report, "issues", []):
            tone = " Služby vyzerajú byť v normálnom stave."
        else:
            tone = " Niektoré služby sú zastavené alebo nefungujú správne."

        return self._identity_append(identity, base + " " + tone)

    # ---------------------------------------------------------
    # ISSUE EXPLANATIONS (Phase‑4)
    # ---------------------------------------------------------

    def _explain_health_issue(self, identity: IdentityType, issue: HealthIssue) -> ExplanationBlock:
        body = self._identity_append(identity, issue.description)
        return ExplanationBlock(issue.title, body, issue.severity, issue.suggested_actions)

    def _explain_driver_issue(self, identity: IdentityType, issue: DriverIssue) -> ExplanationBlock:
        body = self._identity_append(identity, issue.description)
        return ExplanationBlock(issue.title, body, issue.severity, issue.suggested_actions)

    def _explain_task_issue(self, identity: IdentityType, issue: TaskIssue) -> ExplanationBlock:
        body = self._identity_append(identity, issue.description)
        return ExplanationBlock(issue.title, body, issue.severity, issue.suggested_actions)

    def _explain_service_issue(self, identity: IdentityType, issue: ServiceIssue) -> ExplanationBlock:
        body = self._identity_append(identity, issue.description)
        return ExplanationBlock(issue.title, body, issue.severity, issue.suggested_actions)

    # ---------------------------------------------------------
    # IDENTITY-AWARE TEXT APPENDER
    # ---------------------------------------------------------

    def _identity_append(self, identity: IdentityType, text: str) -> str:
        if identity == "OWNER":
            return text + " Ako vlastník môžeš tieto problémy riešiť priamo alebo cez sprievodcu."
        if identity == "FAMILY":
            return text + " Ak chceš, môžem ti to vysvetliť jednoduchšie krok za krokom."
        return text + " Niektoré kroky môžu byť obmedzené podľa nastavení vlastníka."

    # ---------------------------------------------------------
    # SAFE-MODE CONTROL
    # ---------------------------------------------------------

    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False
