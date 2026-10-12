import json
import os
from pathlib import Path
import re
import sys
import time

# Vynutenie UTF-8 vystupu pre Windows terminal
if sys.platform == "win32":
  try:
    sys.stdout.reconfigure(encoding="utf-8")
  except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "professor"))

from atomic_committer import AtomicCommitter
from gatekeeper_net import GatekeeperNet
from grammar_engine import GrammarEngine
from staging_quarantine import StagingQuarantine

# Profesor sleduje aktivitu Sirius Orchestratora cez IPC subor
REQ_FILE = "C:/SIRIUS_ARCHIVE/IPC_DATA/ui_request.json"
KG_FILE = BASE_DIR / "data" / "autosave_kg.json"
if not KG_FILE.exists():
  KG_FILE = BASE_DIR / "autosave_kg.json"


def repair_existing_knowledge_graph(kg_path: Path):
  """SPÄTNÁ OPRAVA: Prejde existujúci autosave_kg.json a vyčistí chybné / odseknuté relácie."""
  if not kg_path.exists():
    return

  try:
    with open(kg_path, "r", encoding="utf-8") as f:
      data = json.load(f)

    relations = data.get("relations", [])
    if not relations:
      return

    cleaned_relations = []
    removed_count = 0
    invalid_endings = (
        " z",
        " do",
        " v",
        " na",
        " a",
        " i",
        " k",
        " so",
        " vo",
        " najstarších",
        " akademických",
    )

    for r in relations:
      src = str(r.get("source", "")).strip()
      rel = str(r.get("relation", "")).strip()
      tgt = str(r.get("target", "")).strip()

      is_valid = True
      if not src or not rel or not tgt:
        is_valid = False
      elif tgt.lower().endswith(invalid_endings):
        is_valid = False
      elif len(tgt) < 2:
        is_valid = False

      if is_valid:
        cleaned_relations.append(r)
      else:
        removed_count += 1

    if removed_count > 0:
      data["relations"] = cleaned_relations
      temp_path = kg_path.with_suffix(".tmp")
      with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
      temp_path.replace(kg_path)
      print(
          f"[REPAIR ENGINE] Spätne opravený graf: Odstránených {removed_count}"
          " chybných/neúplných faktov."
      )
    else:
      print(
          "[REPAIR ENGINE] Kontrola integrity grafu: Žiadne chybné väzby"
          " nenájdené."
      )

  except Exception as e:
    print(f"[REPAIR ENGINE WARNING] Nepodarilo sa skontrolovať starý graf: {e}")


def fallback_extract_facts(topic: str, text: str):
  """Doplnkový záchyt pre prípady, kedy GrammarEngine minie vetu."""
  facts = []
  sentences = re.split(r"(?<=[.!?])\s+", text)
  patterns = [
      r"\bje\b",
      r"\bsú\b",
      r"\bpredstavuje\b",
      r"\bpatrí medzi\b",
      r"\btvorí\b",
  ]

  for sentence in sentences:
    sentence = sentence.strip()
    if len(sentence) < 15 or len(sentence) > 200:
      continue

    for pred in patterns:
      match = re.search(
          rf"^{re.escape(topic)}\s+({pred})\s+(.+)", sentence, re.IGNORECASE
      )
      if match:
        relation = match.group(1).strip()
        target = match.group(2).strip(" .")

        if target.lower().endswith(
            (" z", " do", " v", " na", " a", " i", " o", " u")
        ):
          continue

        facts.append({
            "source": topic,
            "relation": relation,
            "target": target[:90],
        })
        break

  return facts


def get_sirius_idle_time(last_active: float) -> float:
  # Kontrola iba zivych poziadaviek nie starsich ako 30 sekund
  if os.path.exists(REQ_FILE):
    try:
      mtime = os.path.getmtime(REQ_FILE)
      if time.time() - mtime < 30:
        return 0.0
    except Exception:
      pass
  return time.time() - last_active


def main():
  print("=" * 60)
  print("[SIRIUS PROFESSOR DAEMON V1.2] Satelitny proces spusteny...")
  print("=" * 60)

  # 1. Spätná kontrola grafu
  repair_existing_knowledge_graph(KG_FILE)

  gatekeeper = GatekeeperNet()
  grammar = GrammarEngine()
  quarantine = StagingQuarantine()
  committer = AtomicCommitter()
  last_active = time.time()

  IDLE_THRESHOLD = 45

  if len(sys.argv) > 1 and sys.argv[1] == "--immediate":
    print("[PROFESSOR] Okamzity testovaci rezim (--immediate, idle = 2s).")
    IDLE_THRESHOLD = 2

  seed_topics = [
      "Jupiter",
      "Atóm",
      "Elektrón",
      "Gravitácia",
      "Kyslík",
      "Vodík",
      "Zem",
      "Slnko",
      "Bunka",
      "Galaxia",
      "Mars",
      "Fotosyntéza",
      "Molekula",
      "Voda",
      "Železo",
      "Mesiac",
      "Neutrón",
      "Fyzika",
      "Chémia",
      "Biológia",
      "Astronómia",
      "Matematika",
  ]
  topic_queue = list(seed_topics)

  while True:
    try:
      idle = get_sirius_idle_time(last_active)

      if idle >= IDLE_THRESHOLD:
        print(
            f"[PROFESSOR] Sirius necinny ({int(idle)}s). Zacinam obohacovanie..."
        )

        current_batch = []
        for _ in range(3):
          if not topic_queue:
            topic_queue = list(seed_topics)
          current_batch.append(topic_queue.pop(0))

        for topic in current_batch:
          if get_sirius_idle_time(last_active) == 0.0:
            print(
                "[PROFESSOR] Preempcia: Prikaz pre Sirius prijaty, ustupujem."
            )
            last_active = time.time()
            break

          try:
            text = gatekeeper.fetch_wiki_extract(topic)
          except Exception as net_err:
            print(
                f"[PROFESSOR WARN] Chyba pri stahovani temy '{topic}': {net_err}"
            )
            continue

          if not text:
            continue

          triplets = grammar.extract_triplets(text)
          if not triplets:
            triplets = fallback_extract_facts(topic, text)

          print(
              f"[PROFESSOR INGEST] Téma '{topic}': {len(text)} znakov textu ->"
              f" {len(triplets)} faktov"
          )

          for t in triplets:
            quarantine.stage_triplet(
                t["source"], t["relation"], t["target"], "sk.wikipedia.org"
            )

        promotable = quarantine.get_promotable_triplets()
        if promotable:
          committer.commit_triplets(promotable)

        time.sleep(30)
      else:
        time.sleep(2)

    except KeyboardInterrupt:
      print("\n[PROFESSOR] Ukoncene pouzivatelom.")
      break
    except Exception as e:
      print(f"[PROFESSOR ERROR] {e}")
      time.sleep(5)


if __name__ == "__main__":
  main()