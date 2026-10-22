import json
from pathlib import Path
import re
import sys
import time

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path("C:/SIRIUS_ARCHIVE/SIRIUS-LOCAL-AI-5.6.2")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "professor"))

from gatekeeper_net import GatekeeperNet
from grammar_engine import GrammarEngine
from staging_quarantine import StagingQuarantine
from atomic_committer import AtomicCommitter

TARGET_COUNT = 1000
KG_PATH = BASE_DIR / "autosave_kg_en.json"
QUEUE_FILE = BASE_DIR / "professor" / "topic_queue_en.json"
VISITED_FILE = BASE_DIR / "professor" / "visited_topics_en.json"

BACKUP_TOPICS = [
    "Quantum computing", "Supermassive black hole", "Dark flow", 
    "Moscovium", "Americium", "String theory", "Loop quantum gravity", 
    "Cosmic microwave background", "Neutrino oscillation", "Particle accelerator", 
    "Hadron collider", "Supercritical fluid", "Plasma physics", 
    "Magnetohydrodynamics", "Superfluidity", "Quantum cryptography", 
    "Topological insulator", "Graphene lattice", "Astrophysical jet", "Magnetar"
]

GEO_STOP = (
    "city", "town", "county", "state", "river", "country", "king", "president", "born",
    "died", "territory", "population", "village", "street", "parliament", "party", "politics",
    "london", "berlin", "paris", "new york", "america", "england", "europe", "asia"
)

def main():
    print("=" * 60)
    print("[SIRIUS MINER EN V3.3] Ostrý beh s automatickou zálohou")
    print("=" * 60)

    gatekeeper = GatekeeperNet(default_lang="en")
    grammar = GrammarEngine(default_lang="en")
    quarantine = StagingQuarantine()
    committer = AtomicCommitter(kg_path=KG_PATH)

    current = 0
    if KG_PATH.exists():
        try:
            with open(KG_PATH, "r", encoding="utf-8-sig") as f:
                d = json.load(f)
            current = len(d.get("relations", []))
        except Exception:
            pass
    print(f"[START] Aktuálny stav anglického grafu: {current} / {TARGET_COUNT}")

    visited = set()
    if VISITED_FILE.exists():
        try:
            with open(VISITED_FILE, "r", encoding="utf-8-sig") as f:
                visited = set(json.load(f))
        except Exception:
            pass

    queue = []
    if QUEUE_FILE.exists():
        try:
            with open(QUEUE_FILE, "r", encoding="utf-8-sig") as f:
                queue = json.load(f)
        except Exception:
            pass

    # Ak je front prázdny, automaticky ho naplníme záložnými témami
    if not queue:
        queue = list(BACKUP_TOPICS)
        print(f"[FRONT] Súbor bol prázdny, automaticky doplnených {len(queue)} záložných tém.")
    else:
        print(f"[FRONT] Načítaných {len(queue)} tém zo súboru.")

    while current < TARGET_COUNT:
        if not queue:
            print("\n[MINER] Čakací rad je prázdny. Končíme beh.")
            break

        topic = queue.pop(0)
        
        with open(QUEUE_FILE, "w", encoding="utf-8") as f:
            json.dump(queue, f, ensure_ascii=False, indent=2)

        topic_clean = grammar.lemmatize_entity(topic, lang="en")
        if topic_clean.lower() in visited:
            continue
            
        visited.add(topic_clean.lower())
        with open(VISITED_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(list(visited)), f, ensure_ascii=False, indent=2)

        print(f"\n[MINER] Sťahujem: {topic_clean} | Vo fronte: {len(queue)}")

        try:
            text = gatekeeper.fetch_wiki_extract(topic_clean, lang="en")
        except Exception as e:
            print(f"[CHYBA SIETE]: {e}")
            time.sleep(1)
            continue

        if not text:
            continue

        triplets = grammar.extract_triplets(text, lang="en")
        if not triplets:
            clean = re.sub(r"\([^)]*\)", "", text)
            sentences = re.split(r"(?<=[.!?])\s+", clean)
            for sentence in sentences:
                s = sentence.strip()
                if 15 <= len(s) <= 200:
                    m = re.search(rf"\b{re.escape(topic_clean)}\s+(is|are|has|have|contains)\s+([^,;.]+)", s, re.IGNORECASE)
                    if m:
                        triplets.append({
                            "source": topic_clean,
                            "relation": m.group(1).strip().lower(),
                            "target": m.group(2).strip(" .")[:90]
                        })
                        break

        clean_triplets = []
        for t in triplets:
            if not any(g in t["source"].lower() or g in t["target"].lower() for g in GEO_STOP):
                clean_triplets.append(t)

        if clean_triplets:
            for t in clean_triplets:
                quarantine.stage_triplet(t["source"], t["relation"], t["target"], "en.wikipedia.org")
            committer.commit_triplets(quarantine.get_promotable_triplets())
            
            with open(KG_PATH, "r", encoding="utf-8-sig") as f:
                d = json.load(f)
            current = len(d.get("relations", []))
            print(f"[COMMIT] Uložené. Nový stav: {current} relácií")

        time.sleep(1.0)

    print("\n[HOTOVO] Hotové.")

if __name__ == "__main__":
    main()