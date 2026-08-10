# AUTONOMY 6.x - autonomy_bridge.py
# Bezpečný most medzi Autonómiou a COLNÍKOM

import json
import time
import colnik_manager


def send_request_to_colnik(request_obj):
    """
    Pošle request do COLNÍK managera a vráti jeho odpoveď.
    Autonómia nikdy nevykonáva akcie – iba komunikuje.
    """

    print("\n[AUTONOMY → COLNÍK] Odosielam request:")
    print(json.dumps(request_obj, indent=2))

    response = colnik_manager.process_request(request_obj)

    print("\n[COLNÍK → AUTONOMY] Odpoveď:")
    print(json.dumps(response, indent=2))

    return response


def process_proposals(proposals_obj):
    """
    Spracuje všetky návrhy z proposer.py.
    Každý návrh sa odošle do COLNÍKA.
    """

    results = []

    for req in proposals_obj["proposals"]:
        result = send_request_to_colnik(req)
        results.append(result)

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "results": results
    }


if __name__ == "__main__":
    import proposer
    import monitor
    import analyzer

    # 1. Snapshot systému
    snap = monitor.snapshot()

    # 2. Analýza snapshotu
    analysis = analyzer.analyze(snap)

    # 3. Návrhy akcií
    proposals = proposer.propose(analysis)

    # 4. Odoslanie návrhov do COLNÍKA
    final_results = process_proposals(proposals)

    print("\n[AUTONOMY] Finálne výsledky:")
    print(json.dumps(final_results, indent=2))
