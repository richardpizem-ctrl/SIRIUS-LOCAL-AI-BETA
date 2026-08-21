# AUTONOMY GUARD — Rules
# Pravidlá zdravého behu autonómie

from kg.kg_core import KGCore
from timecore import TimeCore

kg = KGCore()

class GuardRules:

    def __init__(self):
        self.timecore = TimeCore()
        self.timecore.runtime_start()

    def validate(self, problems):
        """
        Vždy vracia DICT:
        {
            "status": "OK" | "WARNING" | "INFO" | "STOP",
            "problems": [...]
        }
        """

        # Ak GuardAnalyzer omylom pošle LIST → opravíme to
        if isinstance(problems, list) is False:
            problems = []

        # TIMECORE – začiatok rozhodovania
        self.timecore.cycle_start()

        decision_id = "guard_decision"
        kg.add_entity(decision_id, {
            "type": "guard_decision",
            "timestamp": self.timecore.timestamp()
        })

        for p in problems:
            kg.add_entity(p, {"type": "guard_problem"})
            kg.add_relation(decision_id, "has_problem", p)

        # === OK ===
        if not problems:
            kg.set_attribute(decision_id, "status", "OK")
            cycle_time = self.timecore.cycle_delta()
            self.timecore.cycle_end()
            kg.set_attribute(decision_id, "cycle_time", cycle_time)
            return {"status": "OK", "problems": []}

        # === STOP podmienky ===
        stop_conditions = {
            "critical_repeat_id",
            "critical_repeat_target",
            "critical_repeat_subaction",
            "critical_plus_cpu_rising",
            "critical_plus_ram_rising",
            "critical_plus_disk_rising"
        }

        for p in problems:
            if p in stop_conditions:
                kg.set_attribute(decision_id, "status", "STOP")
                kg.add_relation(decision_id, "decision_type", "STOP")
                cycle_time = self.timecore.cycle_delta()
                self.timecore.cycle_end()
                kg.set_attribute(decision_id, "cycle_time", cycle_time)
                return {"status": "STOP", "problems": problems}

        # === WARNING ===
        warning_conditions = {
            "too_many_proposals",
            "missing_cpu_proposal",
            "missing_disk_proposal"
        }

        for p in problems:
            if p in warning_conditions:
                kg.set_attribute(decision_id, "status", "WARNING")
                kg.add_relation(decision_id, "decision_type", "WARNING")
                cycle_time = self.timecore.cycle_delta()
                self.timecore.cycle_end()
                kg.set_attribute(decision_id, "cycle_time", cycle_time)
                return {"status": "WARNING", "problems": problems}

        # === INFO ===
        kg.set_attribute(decision_id, "status", "INFO")
        kg.add_relation(decision_id, "decision_type", "INFO")
        cycle_time = self.timecore.cycle_delta()
        self.timecore.cycle_end()
        kg.set_attribute(decision_id, "cycle_time", cycle_time)

        return {"status": "INFO", "problems": problems}
