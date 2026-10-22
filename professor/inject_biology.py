"""
SIRIUS QUEUE INJECTOR - BIOLÓGIA & ZOOLOGICKÁ TAXONÓMIA
Okamžité vloženie 20 kľúčových biologických entít do topic_queue.json.
"""

import json
from pathlib import Path

QUEUE_FILE = Path("topic_queue.json").resolve()

# 20 kľúčových vedeckých pojmov z biológie a ríše živočíchov
BIOLOGY_SEEDS = [
    "Živočíchy",
    "Stavovce",
    "Bezstavovce",
    "Cicavce",
    "Vtáky",
    "Plazy",
    "Obojživelníky",
    "Ryby",
    "Článkonožce",
    "Hmyz",
    "Mäkkýše",
    "Dravce",
    "Bylinožravce",
    "Eukaryota",
    "Bunkové jadro",
    "Mitochondria",
    "Fotosyntéza",
    "Nervová sústava",
    "Cievna sústava",
    "Dýchacia sústava"
]


def inject_topics():
    queue = []
    if QUEUE_FILE.exists():
        try:
            with open(QUEUE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    queue = data
        except Exception as e:
            print(f"[WARN] Nepodarilo sa načítať pôvodný front: {e}")

    # Normalizácia existujúcich tém pre kontrolu duplicít
    existing_lower = {t.strip().lower() for t in queue}

    added = []
    # Nové biologické témy zaradíme na začiatok, aby ich miner spracoval prednostne
    for topic in reversed(BIOLOGY_SEEDS):
        if topic.strip().lower() not in existing_lower:
            queue.insert(0, topic.strip())
            added.append(topic.strip())

    try:
        with open(QUEUE_FILE, "w", encoding="utf-8") as f:
            json.dump(queue, f, ensure_ascii=False, indent=2)
        print("=" * 60)
        print(f"[INJECT OK] Úspešne vložených {len(added)} nových biologických tém.")
        print(f"[STATUS] Celkový počet tém v čakacom rade: {len(queue)}")
        print("=" * 60)
        if added:
            print("Pridané témy:")
            for item in reversed(added):
                print(f"  • {item}")
    except Exception as e:
        print(f"[ERROR] Zápis do {QUEUE_FILE.name} zlyhal: {e}")


if __name__ == "__main__":
    inject_topics()