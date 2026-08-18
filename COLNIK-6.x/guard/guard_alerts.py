# AUTONOMY GUARD — Alerts
# Zastaví autonómiu a vypíše presný dôvod

class GuardAlerts:

    def handle(self, validation):
        if validation["status"] == "OK":
            return None

        print("\n=== AUTONOMY GUARD — STOP ===")
        print("Dôvody:")
        for p in validation["problems"]:
            print(f"- {p}")
        print("==============================\n")

        return "STOP"
