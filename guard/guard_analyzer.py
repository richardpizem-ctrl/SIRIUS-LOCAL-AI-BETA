# AUTONOMY GUARD — Analyzer
# Vyhodnocuje správanie autonómie

from kg.kg_core import KGCore
from timecore import TimeCore   # <<< TIMECORE

kg = KGCore()

class GuardAnalyzer:

    def __init__(self):
        # História návrhov podľa ID
        self.proposal_history = {}

        # História návrhov podľa targetu
        self.target_history = {}

        # História návrhov podľa subaction
        self.subaction_history = {}

        # TIMECORE – PILIER 0
        self.timecore = TimeCore()
        self.timecore.runtime_start()

        # === KG: registrácia modulu ===
        kg.add_entity("guard_analyzer", {"type": "module"})
        kg.add_relation("guard_analyzer", "initialized", "autonomy_guard")

    def analyze(self, monitor_snapshot):
        # TIMECORE – začiatok analýzy
        self.timecore.cycle_start()

        problems = []

        proposals = monitor_snapshot.get("proposals", [])
        trends = monitor_snapshot.get("trends", {})
        system = monitor_snapshot.get("system", {})

        # === KG: vytvor snapshot analýzy ===
        analysis_id = f"guard_analysis_cycle_{monitor_snapshot.get('cycle', 0)}"
        kg.add_entity(analysis_id, {
            "type": "guard_analysis",
            "cycle": monitor_snapshot.get("cycle", 0)
        })
        kg.add_relation("guard_analyzer", "performed_analysis", analysis_id)

        # === 1. Príliš veľa návrhov ===
        if len(proposals) > 5:
            problems.append("too_many_proposals")
            kg.add_entity("too_many_proposals", {"type": "guard_problem"})
            kg.add_relation(analysis_id, "detected_problem", "too_many_proposals")

        # === 2. Žiadne návrhy pri rising trendoch ===
        if len(proposals) == 0:
            if trends.get("cpu") == "rising":
                problems.append("missing_cpu_proposal")
                kg.add_entity("missing_cpu_proposal", {"type": "guard_problem"})
                kg.add_relation(analysis_id, "detected_problem", "missing_cpu_proposal")

            if trends.get("disk") == "rising":
                problems.append("missing_disk_proposal")
                kg.add_entity("missing_disk_proposal", {"type": "guard_problem"})
                kg.add_relation(analysis_id, "detected_problem", "missing_disk_proposal")

        # === 3. CRITICAL návrh (ID) — okamžitý STOP ===
        for p in proposals:
            pid = p.get("proposal_id")
            priority = p.get("priority", "NORMAL")

            if pid not in self.proposal_history:
                self.proposal_history[pid] = 0

            self.proposal_history[pid] += 1

            if priority == "CRITICAL":
                problems.append("critical_repeat_id")
                kg.add_entity("critical_repeat_id", {"type": "guard_problem"})
                kg.add_relation(analysis_id, "detected_problem", "critical_repeat_id")
                if pid:
                    kg.add_relation("critical_repeat_id", "caused_by", pid)

        # === 4. CRITICAL target — okamžitý STOP ===
        for p in proposals:
            target = p.get("target")
            priority = p.get("priority", "NORMAL")

            if target not in self.target_history:
                self.target_history[target] = 0

            self.target_history[target] += 1

            if priority == "CRITICAL":
                problems.append("critical_repeat_target")
                kg.add_entity("critical_repeat_target", {"type": "guard_problem"})
                kg.add_relation(analysis_id, "detected_problem", "critical_repeat_target")
                if target:
                    kg.add_relation("critical_repeat_target", "caused_by", target)

        # === 5. CRITICAL subaction — okamžitý STOP ===
        for p in proposals:
            sub = p.get("payload", {}).get("subaction")
            priority = p.get("priority", "NORMAL")

            if sub not in self.subaction_history:
                self.subaction_history[sub] = 0

            self.subaction_history[sub] += 1

            if priority == "CRITICAL":
                problems.append("critical_repeat_subaction")
                kg.add_entity("critical_repeat_subaction", {"type": "guard_problem"})
                kg.add_relation(analysis_id, "detected_problem", "critical_repeat_subaction")
                if sub:
                    kg.add_relation("critical_repeat_subaction", "caused_by", sub)

        # === 6. CRITICAL + rising trend — okamžitý STOP ===
        for p in proposals:
            if p.get("priority") == "CRITICAL":
                pid = p.get("proposal_id")

                if trends.get("cpu") == "rising":
                    problems.append("critical_plus_cpu_rising")
                    kg.add_entity("critical_plus_cpu_rising", {"type": "guard_problem"})
                    kg.add_relation(analysis_id, "detected_problem", "critical_plus_cpu_rising")
                    if pid:
                        kg.add_relation("critical_plus_cpu_rising", "caused_by", pid)

                if trends.get("ram") == "rising":
                    problems.append("critical_plus_ram_rising")
                    kg.add_entity("critical_plus_ram_rising", {"type": "guard_problem"})
                    kg.add_relation(analysis_id, "detected_problem", "critical_plus_ram_rising")
                    if pid:
                        kg.add_relation("critical_plus_ram_rising", "caused_by", pid)

                if trends.get("disk") == "rising":
                    problems.append("critical_plus_disk_rising")
                    kg.add_entity("critical_plus_disk_rising", {"type": "guard_problem"})
                    kg.add_relation(analysis_id, "detected_problem", "critical_plus_disk_rising")
                    if pid:
                        kg.add_relation("critical_plus_disk_rising", "caused_by", pid)

        # TIMECORE – koniec analýzy
        self.timecore.cycle_end()
        cycle_time = self.timecore.cycle_delta()

        # === KG: zapis cycle_time ===
        kg.set_attribute(analysis_id, "cycle_time", cycle_time)

        return problems
