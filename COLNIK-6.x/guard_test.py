# GUARD TEST SIMULATOR – SIRIUS 6.x (VERZIA 2.1)
# STOP AUTONOMY už NEUKONČÍ simuláciu – pokračujeme ďalej.

import time

class FakeMonitor:
    def __init__(self):
        self.scenario_step = 0

    def next_snapshot(self):
        self.scenario_step += 1

        if self.scenario_step in (1, 2):
            return {"system": {"cpu": 10.0, "ram": 40.0, "disk": 100_000},
                    "trend": {"cpu": "stable", "ram": "stable", "disk": "stable"}}

        if self.scenario_step == 3:
            return {"system": {"cpu": 95.0, "ram": 70.0, "disk": 5_000_000},
                    "trend": {"cpu": "rising", "ram": "rising", "disk": "rising"}}

        if self.scenario_step == 4:
            return {"system": {"cpu": 30.0, "ram": 50.0, "disk": 200_000},
                    "trend": {"cpu": "stable", "ram": "stable", "disk": "stable"}}

        if self.scenario_step == 5:
            return {"system": {"cpu": 20.0, "ram": 50.0, "disk": 25_000_000},
                    "trend": {"cpu": "stable", "ram": "stable", "disk": "rising"}}

        if self.scenario_step == 6:
            return {"system": {"cpu": 20.0, "ram": 50.0, "disk": 25_000_000},
                    "trend": {"cpu": "stable", "ram": "stable", "disk": "rising"}}

        if self.scenario_step == 7:
            return {"system": {"cpu": 90.0, "ram": 90.0, "disk": 50_000_000},
                    "trend": {"cpu": "rising", "ram": "rising", "disk": "rising"}}

        if self.scenario_step == 8:
            return {"system": {"cpu": 15.0, "ram": 45.0, "disk": 200_000},
                    "trend": {"cpu": "falling", "ram": "stable", "disk": "falling"}}

        if self.scenario_step == 9:
            return {"system": {"cpu": 15.0, "ram": 45.0, "disk": 200_000},
                    "trend": {"cpu": "falling", "ram": "stable", "disk": "falling"}}

        if self.scenario_step == 10:
            return {"system": {"cpu": 100.0, "ram": 99.0, "disk": 100_000_000},
                    "trend": {"cpu": "rising", "ram": "rising", "disk": "rising"}}

        return {"system": {"cpu": 10.0, "ram": 40.0, "disk": 100_000},
                "trend": {"cpu": "stable", "ram": "stable", "disk": "stable"}}


class FakeAutonomy:
    def generate_proposals(self, snapshot, step):
        system = snapshot["system"]
        proposals = []

        if step in (1, 2):
            return proposals

        if step == 3:
            proposals.append({
                "proposal_id": "cpu-opt",
                "action": "OPTIMIZE_CPU",
                "target": "SYSTEM",
                "payload": {"cpu": system["cpu"]},
                "priority": "HIGH"
            })
            return proposals

        if step == 4:
            proposals.append({
                "proposal_id": "invalid-1",
                "action": "CLEAN_DISK",
                "target": "SYSTEM",
                "payload": {},
                "priority": "MEDIUM"
            })
            return proposals

        if step == 5:
            proposals.append({
                "proposal_id": "bad-target",
                "action": "CLEAN_DISK",
                "target": "USER",
                "payload": {"disk": system["disk"]},
                "priority": "MEDIUM"
            })
            return proposals

        if step == 6:
            proposals.append({
                "proposal_id": "unknown-action",
                "action": "FLY_TO_MOON",
                "target": "SYSTEM",
                "payload": {"disk": system["disk"]},
                "priority": "MEDIUM"
            })
            return proposals

        if step == 7:
            proposals.append("THIS_IS_NOT_A_DICT")
            return proposals

        if step == 8:
            proposals.append({
                "proposal_id": "nonsense",
                "action": "CLEAN_DISK",
                "target": "SYSTEM",
                "payload": {"cpu": 999},
                "priority": "MEDIUM"
            })
            return proposals

        if step == 9:
            return proposals

        if step == 10:
            proposals.append({
                "proposal_id": "disk-clean",
                "action": "CLEAN_DISK",
                "target": "SYSTEM",
                "payload": {"disk": system["disk"]},
                "priority": "HIGH"
            })
            return proposals

        return proposals


class Guard:
    def __init__(self):
        self.repetition_counter = {}
        self.autonomy_stopped = False
        self.global_stopped = False

    def check_proposals(self, proposals, snapshot, step):
        if self.global_stopped:
            print(f"[GUARD] GLOBAL STOP already active → step {step}")
            return "STOP"

        if step in (1, 2):
            print(f"[GUARD] Normal step {step} → OK")
            return "OK"

        if any(type(p) != dict for p in proposals):
            print(f"[GUARD] MALFORMED PROPOSAL at step {step} → STOP AUTONOMY")
            self.autonomy_stopped = True
            return "STOP_AUTONOMY"

        for p in proposals:

            if p.get("proposal_id") == "invalid-1":
                print(f"[GUARD] INVALID PROPOSAL at step {step} → STOP AUTONOMY")
                self.autonomy_stopped = True
                return "STOP_AUTONOMY"

            if p.get("target") not in ("SYSTEM", "USER_APP"):
                print(f"[GUARD] INVALID TARGET at step {step} → STOP AUTONOMY")
                self.autonomy_stopped = True
                return "STOP_AUTONOMY"

            if p.get("action") not in ("OPTIMIZE_CPU", "OPTIMIZE_RAM", "CLEAN_DISK"):
                print(f"[GUARD] UNKNOWN ACTION at step {step} → STOP AUTONOMY")
                self.autonomy_stopped = True
                return "STOP_AUTONOMY"

            if "disk" not in p.get("payload", {}) and p["action"] == "CLEAN_DISK":
                print(f"[GUARD] INVALID PAYLOAD at step {step} → STOP AUTONOMY")
                self.autonomy_stopped = True
                return "STOP_AUTONOMY"

            pid = p["proposal_id"]
            self.repetition_counter[pid] = self.repetition_counter.get(pid, 0) + 1

            if self.repetition_counter[pid] >= 3:
                print(f"[GUARD] REPETITION of {pid} at step {step} → STOP AUTONOMY")
                self.autonomy_stopped = True
                return "STOP_AUTONOMY"

        system = snapshot["system"]
        if system["cpu"] >= 100.0 and system["ram"] >= 95.0 and system["disk"] >= 80_000_000:
            print(f"[GUARD] CRITICAL SYSTEM STATE at step {step} → GLOBAL STOP")
            self.global_stopped = True
            return "STOP"

        if step == 9 and not proposals:
            print(f"[GUARD] System recovered at step {step} → OK")
            return "OK"

        print(f"[GUARD] Step {step} → MONITORING")
        return "MONITORING"


def run_guard_simulation():
    monitor = FakeMonitor()
    autonomy = FakeAutonomy()
    guard = Guard()

    print("=== GUARD TEST SIMULATOR START ===")

    for step in range(1, 11):
        snapshot = monitor.next_snapshot()
        proposals = autonomy.generate_proposals(snapshot, step)
        status = guard.check_proposals(proposals, snapshot, step)

        print(f"\n[STEP {step}]")
        print("SYSTEM:", snapshot["system"])
        print("TREND:", snapshot["trend"])
        print("PROPOSALS:", proposals)
        print("GUARD STATUS:", status)
        print("-" * 40)

        if status == "STOP":
            print("=== GLOBAL STOP → SIMULATION TERMINATED ===")
            break

        time.sleep(0.5)

    print("=== GUARD TEST SIMULATOR END ===")


if __name__ == "__main__":
    run_guard_simulation()
