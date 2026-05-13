"""
Education Engine 4.1
--------------------

Vysvetľovací a komunikačný modul pre SIRIUS LOCAL AI v4.1.0.

Účel:
- prekladať technické diagnostické výstupy do zrozumiteľných vysvetlení
- generovať identity-aware odporúčania (OWNER / FAMILY / STRANGER)
- vysvetľovať riziká, dopady a bezpečné kroky
- pripravovať texty pre GUI / konzolu / VYSLANEC 4.1

Tento modul:
- NEVYKONÁVA žiadne systémové zmeny
- nerozhoduje o akciách, len ich vysvetľuje
- je čisto textový, bez prístupu k OS
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional

# Typy identít – musia sedieť so Security Family 4.0
IdentityType = Literal["OWNER", "FAMILY", "STRANGER"]

# Import typov z ostatných modulov (len type hints, aby sa to dalo prepojiť)
try:
    from system_health_engine_4_1 import HealthReport, HealthIssue
    from driver_manager_engine_4_1 import DriverReport, DriverIssue
    from task_manager_engine_4_1 import TaskReport, TaskIssue
    from service_manager_engine_4_1 import ServiceReport, ServiceIssue
except ImportError:
    # fallback pre prípad, že sa typy ešte len generujú
    HealthReport = object  # type: ignore
    HealthIssue = object  # type: ignore
    DriverReport = object  # type: ignore
    DriverIssue = object  # type: ignore
    TaskReport = object  # type: ignore
    TaskIssue = object  # type: ignore
    ServiceReport = object  # type: ignore
    ServiceIssue = object  # type: ignore


@dataclass
class ExplanationBlock:
    """
    Jeden vysvetľovací blok – vhodný na zobrazenie v GUI alebo konzole.
    """
    title: str
    body: str
    severity: str  # "info" | "warning" | "critical"
    suggested_actions: List[str]


@dataclass
class EducationBundle:
    """
    Kompletný balík vysvetlení pre danú diagnostickú sadu.
    """
    identity: IdentityType
    summary: str
    blocks: List[ExplanationBlock]


class EducationEngine41:
    """
    Education Engine 4.1

    - prekladá technické reporty do ľudských vysvetlení
    - rešpektuje identitu používateľa (OWNER / FAMILY / STRANGER)
    - nepozná GUI, len vracia štruktúry
    """

    def __init__(self) -> None:
        pass

    # -------------------------------------------------------------------------
    # PUBLIC API – VSTUPNÉ BODY
    # -------------------------------------------------------------------------

    def explain_system_health(
        self,
        identity: IdentityType,
        report: HealthReport,
    ) -> EducationBundle:
        """
        Vysvetlí System Health Report pre danú identitu.
        """
        summary = self._build_health_summary(identity, report)
        blocks: List[ExplanationBlock] = []

        for issue in report.issues:
            blocks.append(self._explain_health_issue(identity, issue))

        return EducationBundle(
            identity=identity,
            summary=summary,
            blocks=blocks,
        )

    def explain_drivers(
        self,
        identity: IdentityType,
        report: DriverReport,
    ) -> EducationBundle:
        summary = self._build_driver_summary(identity, report)
        blocks: List[ExplanationBlock] = []

        for issue in report.issues:
            blocks.append(self._explain_driver_issue(identity, issue))

        return EducationBundle(
            identity=identity,
            summary=summary,
            blocks=blocks,
        )

    def explain_tasks(
        self,
        identity: IdentityType,
        report: TaskReport,
    ) -> EducationBundle:
        summary = self._build_task_summary(identity, report)
        blocks: List[ExplanationBlock] = []

        for issue in report.issues:
            blocks.append(self._explain_task_issue(identity, issue))

        return EducationBundle(
            identity=identity,
            summary=summary,
            blocks=blocks,
        )

    def explain_services(
        self,
        identity: IdentityType,
        report: ServiceReport,
    ) -> EducationBundle:
        summary = self._build_service_summary(identity, report)
        blocks: List[ExplanationBlock] = []

        for issue in report.issues:
            blocks.append(self._explain_service_issue(identity, issue))

        return EducationBundle(
            identity=identity,
            summary=summary,
            blocks=blocks,
        )

    # -------------------------------------------------------------------------
    # SUMMARY BUILDERS
    # -------------------------------------------------------------------------

    def _build_health_summary(self, identity: IdentityType, report: HealthReport) -> str:
        base = f"Aktuálne zdravie systému je {report.health_score}/100."

        if report.health_score >= 80:
            tone = "Systém je vo všeobecnosti v dobrom stave."
        elif report.health_score >= 50:
            tone = "Systém má niekoľko problémov, ktoré môžu spôsobovať spomalenie."
        else:
            tone = "Systém je v zhoršenom stave a odporúča sa riešiť problémy čím skôr."

        if identity == "OWNER":
            extra = " Môžeme prejsť konkrétne problémy a navrhnúť bezpečné kroky."
        elif identity == "FAMILY":
            extra = " Ak chceš, môžem ti jednoducho vysvetliť, čo je najdôležitejšie vyriešiť."
        else:  # STRANGER
            extra = " Niektoré podrobné akcie môžu byť obmedzené podľa nastavení vlastníka."

        return base + " " + tone + extra

    def _build_driver_summary(self, identity: IdentityType, report: DriverReport) -> str:
        count_issues = len(report.issues)
        base = f"Nájdených bolo {count_issues} problémov súvisiacich s ovládačmi."

        if count_issues == 0:
            tone = " Ovládače momentálne nevyzerajú problematicky."
        else:
            tone = " Niektoré zariadenia nemusia fungovať správne."

        if identity == "OWNER":
            extra = " Môžeme pripraviť bezpečný plán aktualizácie alebo inštalácie ovládačov."
        elif identity == "FAMILY":
            extra = " Ak máš problém so zvukom, obrazom alebo sieťou, tieto nálezy s tým môžu súvisieť."
        else:
            extra = " Podrobné zásahy do ovládačov sú zvyčajne vyhradené pre vlastníka zariadenia."

        return base + tone + extra

    def _build_task_summary(self, identity: IdentityType, report: TaskReport) -> str:
        total = len(report.processes)
        base = f"V systéme beží približne {total} procesov."

        if not report.issues:
            tone = " Nevidím žiadne výrazné problémy s procesmi."
        else:
            tone = " Niektoré procesy môžu spôsobovať spomalenie alebo nestabilitu."

        if identity == "OWNER":
            extra = " Môžeme identifikovať konkrétne aplikácie, ktoré najviac zaťažujú systém."
        elif identity == "FAMILY":
            extra = " Ak sa ti zdá, že počítač je pomalý, môžem ti ukázať, ktoré programy to spôsobujú."
        else:
            extra = " Podrobné zásahy do procesov môžu byť obmedzené podľa nastavení vlastníka."

        return base + " " + tone + extra

    def _build_service_summary(self, identity: IdentityType, report: ServiceReport) -> str:
        total = len(report.services)
        base = f"Systémové služby: približne {total} aktívnych záznamov."

        if not report.issues:
            tone = " Služby vyzerajú byť v normálnom stave."
        else:
            tone = " Niektoré služby sú zastavené alebo nefungujú správne."

        if identity == "OWNER":
            extra = " Môžeme zvážiť bezpečný reštart vybraných služieb cez VYSLANEC 4.1."
        elif identity == "FAMILY":
            extra = " Problémy so zvukom, sieťou alebo aktualizáciami môžu súvisieť s týmito službami."
        else:
            extra = " Zmeny v službách sú zvyčajne vyhradené pre vlastníka zariadenia."

        return base + " " + tone + extra

    # -------------------------------------------------------------------------
    # ISSUE EXPLANATIONS – HEALTH
    # -------------------------------------------------------------------------

    def _explain_health_issue(
        self,
        identity: IdentityType,
        issue: HealthIssue,
    ) -> ExplanationBlock:
        # základný text z issue
        title = issue.title
        body = issue.description

        # identity-aware doplnenie
        if identity == "OWNER":
            body += " Ako vlastník môžeš tieto problémy riešiť priamo alebo cez sprievodcu."
        elif identity == "FAMILY":
            body += " Ak chceš, môžem ti to vysvetliť jednoduchšie krok za krokom."
        else:
            body += " Niektoré kroky môžu byť obmedzené podľa nastavení vlastníka."

        return ExplanationBlock(
            title=title,
            body=body,
            severity=issue.severity,
            suggested_actions=issue.suggested_actions,
        )

    # -------------------------------------------------------------------------
    # ISSUE EXPLANATIONS – DRIVERS
    # -------------------------------------------------------------------------

    def _explain_driver_issue(
        self,
        identity: IdentityType,
        issue: DriverIssue,
    ) -> ExplanationBlock:
        title = issue.title
        body = issue.description

        if identity == "OWNER":
            body += " Ovládače sú softvér, ktorý umožňuje systému komunikovať so zariadeniami (grafika, zvuk, sieť)."
        elif identity == "FAMILY":
            body += " Jednoducho povedané: počítač má problém s niektorým zariadením (napr. zvuk, obraz, internet)."
        else:
            body += " Podrobné zásahy do ovládačov sú z bezpečnostných dôvodov obmedzené."

        return ExplanationBlock(
            title=title,
            body=body,
            severity=issue.severity,
            suggested_actions=issue.suggested_actions,
        )

    # -------------------------------------------------------------------------
    # ISSUE EXPLANATIONS – TASKS
    # -------------------------------------------------------------------------

    def _explain_task_issue(
        self,
        identity: IdentityType,
        issue: TaskIssue,
    ) -> ExplanationBlock:
        title = issue.title
        body = issue.description

        if identity == "OWNER":
            body += " Procesy sú jednotlivé programy a služby, ktoré bežia na pozadí."
        elif identity == "FAMILY":
            body += " Inak povedané: niektoré programy bežia na pozadí a spomaľujú počítač."
        else:
            body += " Zásahy do bežiacich procesov môžu byť obmedzené podľa nastavení vlastníka."

        return ExplanationBlock(
            title=title,
            body=body,
            severity=issue.severity,
            suggested_actions=issue.suggested_actions,
        )

    # -------------------------------------------------------------------------
    # ISSUE EXPLANATIONS – SERVICES
    # -------------------------------------------------------------------------

    def _explain_service_issue(
        self,
        identity: IdentityType,
        issue: ServiceIssue,
    ) -> ExplanationBlock:
        title = issue.title
        body = issue.description

        if identity == "OWNER":
            body += " Služby sú systémové komponenty, ktoré zabezpečujú zvuk, sieť, aktualizácie a ďalšie funkcie."
        elif identity == "FAMILY":
            body += " Jednoducho: niektoré vnútorné časti Windows nebežia tak, ako by mali."
        else:
            body += " Zmeny v službách sú zvyčajne vyhradené pre vlastníka zariadenia."

        return ExplanationBlock(
            title=title,
            body=body,
            severity=issue.severity,
            suggested_actions=issue.suggested_actions,
        )
