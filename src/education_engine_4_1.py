# education_engine_4_4.py
# SIRIUS LOCAL AI – Education Engine 4.4.0 PRO
# Deterministic, safe-mode compatible explanation generator (Phase‑4/5 ready)

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal

# ---------------------------------------------------------
# IDENTITY TYPES (Security Family 4.4)
# ---------------------------------------------------------

IdentityType = Literal["OWNER", "FAMILY", "STRANGER"]

# ---------------------------------------------------------
# IMPORTS (Static, Phase‑4 safe)
# ---------------------------------------------------------

from system_health_engine_4_4 import HealthReport44, HealthIssue44
from driver_manager_engine_4_4 import DriverReport44, DriverIssue44
from task_manager_engine_4_4 import TaskReport44, TaskIssue44
from service_manager_engine_4_4 import ServiceReport44, ServiceIssue44


# ---------------------------------------------------------
# DATA STRUCTURES (Phase‑4)
# ---------------------------------------------------------

@dataclass
class ExplanationBlock44:
    """
    One explanation block for UI or console.
    Phase‑4: deterministic, sanitized, identity-aware.
    """
    title: str
    body: str
    severity: str
    suggested_actions: List[str]


@dataclass
class EducationBundle44:
    """
    Complete explanation bundle for a diagnostic report.
    """
    identity: IdentityType
    summary: str
    blocks: List[ExplanationBlock44]
    safe_mode: bool = False
    degraded_mode: bool = False


# ---------------------------------------------------------
# ENGINE
# ---------------------------------------------------------

class EducationEngine44:
    """
    Education Engine 4.4.0 PRO

    Responsibilities:
        - Convert technical reports into human-readable explanations
        - Respect identity (OWNER / FAMILY / STRANGER)
        - Provide deterministic, safe-mode compatible output
        - Provide structured fallback behavior
        - Self‑Repair 4.4 compatible
        - Phase‑5 ready (extended identity model)
    """

    def __init__(self):
        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # PUBLIC API
    # ---------------------------------------------------------

    def explain_system_health(self, identity: IdentityType, report: HealthReport44) -> EducationBundle44:
        if self.safe_mode:
            return self._bundle_safe_mode(identity)

        try:
            summary = self._build_health_summary(identity, report)
            blocks = [self._explain_health_issue(identity, issue) for issue in report.issues]

            return EducationBundle44(
                identity=identity,
                summary=summary,
                blocks=blocks,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )
        except Exception:
            self.degraded_mode = True
            return self._bundle_degraded(identity)

    def explain_drivers(self, identity: IdentityType, report: DriverReport44) -> EducationBundle44:
        if self.safe_mode:
            return self._bundle_safe_mode(identity)

        try:
            summary = self._build_driver_summary(identity, report)
            blocks = [self._explain_driver_issue(identity, issue) for issue in report.issues]

            return EducationBundle44(
                identity=identity,
                summary=summary,
                blocks=blocks,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )
        except Exception:
            self.degraded_mode = True
            return self._bundle_degraded(identity)

    def explain_tasks(self, identity: IdentityType, report: TaskReport44) -> EducationBundle44:
        if self.safe_mode:
            return self._bundle_safe_mode(identity)

        try:
            summary = self._build_task_summary(identity, report)
            blocks = [self._explain_task_issue(identity, issue) for issue in report.issues]

            return EducationBundle44(
                identity=identity,
                summary=summary,
                blocks=blocks,
                safe_mode=False,
                degraded_mode=self.degraded_mode,
            )
        except Exception:
            self.degraded_mode = True
            return self._bundle_degraded(identity)

    def explain_services(self, identity: IdentityType, report: ServiceReport44) -> EducationBundle44:
        if self.safe_mode:
            return self._bundle_safe_mode(identity)

        try:
            summary = self._build_service_summary(identity, report)
            blocks = [self._explain_service_issue(identity, issue) for issue in report.issues]

            return EducationBundle44(
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

    def _bundle_safe_mode(self, identity: IdentityType) -> EducationBundle44:
        return EducationBundle44(
            identity=identity,
            summary="Education Engine je v SAFE MODE. Diagnostické vysvetlenia sú dočasne vypnuté.",
            blocks=[],
            safe_mode=True,
            degraded_mode=False,
        )

    def _bundle_degraded(self, identity: IdentityType) -> EducationBundle44:
        return EducationBundle44(
            identity=identity,
            summary="Education Engine je v DEGRADED MODE. Niektoré vysvetlenia nemusia byť dostupné.",
            blocks=[],
            safe_mode=False,
            degraded_mode=True,
        )

    # ---------------------------------------------------------
    # SUMMARY BUILDERS (Phase‑4)
    # ---------------------------------------------------------

    def _build_health_summary(self, identity: IdentityType, report: HealthReport44) -> str:
        score = getattr(report, "health_score", 0)
        base = f"Aktuálne zdravie systému je {score}/100."

        if score >= 80:
            tone = "Systém je vo veľmi dobrom stave."
        elif score >= 50:
            tone = "Systém má niekoľko problémov, ktoré môžu spôsobovať spomalenie."
        else:
            tone = "Systém je v zhoršenom stave a odporúča sa riešiť problémy čím skôr."

        return self._identity_append(identity, base + " " + tone)

    def _build_driver_summary(self, identity: IdentityType, report: DriverReport44) -> str:
        count = len(report.issues)
        base = f"Nájdených bolo {count} problémov súvisiacich s ovládačmi."

        if count == 0:
            tone = " Ovládače momentálne nevyzerajú problematicky."
        else:
            tone = " Niektoré zariadenia nemusia fungovať správne."

        return self._identity_append(identity, base + tone)

    def _build_task_summary(self, identity: IdentityType, report: TaskReport44) -> str:
        total = len(report.processes)
        base = f"V systéme beží približne {total} procesov."

        if not report.issues:
            tone = " Nevidím žiadne výrazné problémy s procesmi."
        else:
            tone = " Niektoré procesy môžu spôsobovať spomalenie alebo nestabilitu."

        return self._identity_append(identity, base + " " + tone)

    def _build_service_summary(self, identity: IdentityType, report: ServiceReport44) -> str:
        total = len(report.services)
        base = f"Systémové služby: približne {total} aktívnych záznamov."

        if not report.issues:
            tone = " Služby vyzerajú byť v normálnom stave."
        else:
            tone = " Niektoré služby sú zastavené alebo nefungujú správne."

        return self._identity_append(identity, base + " " + tone)

    # ---------------------------------------------------------
    # ISSUE EXPLANATIONS (Phase‑4)
    # ---------------------------------------------------------

    def _explain_health_issue(self, identity: IdentityType, issue: HealthIssue44) -> ExplanationBlock44:
        body = self._identity_append(identity, issue.description)
        return ExplanationBlock44(issue.title, body, issue.severity, issue.suggested_actions)

    def _explain_driver_issue(self, identity: IdentityType, issue: DriverIssue44) -> ExplanationBlock44:
        body = self._identity_append(identity, issue.description)
        return ExplanationBlock44(issue.title, body, issue.severity, issue.suggested_actions)

    def _explain_task_issue(self, identity: IdentityType, issue: TaskIssue44) -> ExplanationBlock44:
        body = self._identity_append(identity, issue.description)
        return ExplanationBlock44(issue.title, body, issue.severity, issue.suggested_actions)

    def _explain_service_issue(self, identity: IdentityType, issue: ServiceIssue44) -> ExplanationBlock44:
        body = self._identity_append(identity, issue.description)
        return ExplanationBlock44(issue.title, body, issue.severity, issue.suggested_actions)

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
