# AUTONOMY GUARD — Alerts
# Zastaví autonómiu a vypíše presný dôvod

from kg.kg_core import KGCore
from timecore import TimeCore   # <<< TIMECORE

kg = KGCore()

class GuardAlerts:

    def __init__(self):
        # TIMECORE – PILIER 0
        self.timecore = TimeCore()
        self.timecore.runtime_start()

    def handle(self, validation):
        # validation je DICT:
        # { "status": "STOP", "problems": ["critical_repeat_id", ...] }

        status = validation.get("status", "OK")
        problems = validation.get("problems", [])

        # TIMECORE – začiatok alertu
        self.timecore.cycle_start()

        # === KG: vytvor entitu alertu ===
        alert_id = f"guard_alert_{status.lower()}"
        kg.add_entity(alert_id, {
            "type": "guard_alert",
            "status": status,
            "timestamp": self.timecore.timestamp()
        })

        # === KG: zapisuj problémy ===
        for p in problems:
            kg.add_entity(p, {"type": "guard_problem"})
            kg.add_relation(alert_id, "alert_problem", p)

        # === OK ===
        if status == "OK":
            kg.add_relation(alert_id, "decision", "OK")

            cycle_time = self.timecore.cycle_delta()
            self.timecore.cycle_end()
            kg.set_attribute(alert_id, "cycle_time", cycle_time)

            return None

        # === WARNING ===
        if status == "WARNING":
            print("\n=== AUTONOMY GUARD — WARNING ===")
            print("Upozornenia:")
            for p in problems:
                print(f"- {p}")
            print("Autonómia pokračuje.")
            print("=================================\n")

            kg.add_relation(alert_id, "decision", "WARNING")

            cycle_time = self.timecore.cycle_delta()
            self.timecore.cycle_end()
            kg.set_attribute(alert_id, "cycle_time", cycle_time)

            return None

        # === INFO ===
        if status == "INFO":
            print("\n=== AUTONOMY GUARD — INFO ===")
            print("Informácie:")
            for p in problems:
                print(f"- {p}")
            print("Autonómia pokračuje.")
            print("================================\n")

            kg.add_relation(alert_id, "decision", "INFO")

            cycle_time = self.timecore.cycle_delta()
            self.timecore.cycle_end()
            kg.set_attribute(alert_id, "cycle_time", cycle_time)

            return None

        # === STOP ===
        if status == "STOP":
            print("\n=== AUTONOMY GUARD — STOP ===")
            print("Dôvody zastavenia:")
            for p in problems:
                print(f"- {p}")
            print("Autonómia bola zastavená GUARD modulom.")
            print("========================================\n")

            # === KG: STOP relácie ===
            kg.add_relation(alert_id, "decision", "STOP")
            kg.add_relation("autonomy", "stopped_by", alert_id)

            cycle_time = self.timecore.cycle_delta()
            self.timecore.cycle_end()
            kg.set_attribute(alert_id, "cycle_time", cycle_time)

            # 🔥 AUTONÓMIA SA MUSÍ ZASTAVIŤ
            return "STOP"

        # TIMECORE – fallback
        cycle_time = self.timecore.cycle_delta()
        self.timecore.cycle_end()
        kg.set_attribute(alert_id, "cycle_time", cycle_time)

        return None
