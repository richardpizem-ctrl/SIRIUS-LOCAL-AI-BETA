import json
import os
from pathlib import Path
import re
import sys
import time

# Vynútenie UTF-8 výstupu pre Windows konzolu
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

REQ_FILE = "C:/SIRIUS_ARCHIVE/IPC_DATA/ui_request.json"
KG_FILE = BASE_DIR / "data" / "autosave_kg.json"
if not KG_FILE.exists():
  KG_FILE = BASE_DIR / "autosave_kg.json"

PROFESSOR_DIR = Path(__file__).resolve().parent
VISITED_FILE = PROFESSOR_DIR / "visited_topics.json"
QUEUE_FILE = PROFESSOR_DIR / "topic_queue.json"

# Vedecké, materiálové a pojmové indikátory (všeobecná veda a klasické pojmy)
SCIENCE_PRIORITY_MARKERS = (
    "fyzik",
    "chém",
    "biol",
    "astron",
    "matemat",
    "geol",
    "atóm",
    "elektrón",
    "protón",
    "neutrón",
    "kvant",
    "gravitác",
    "energi",
    "hmot",
    "žiaren",
    "molekul",
    "bunk",
    "prvok",
    "zlúčenin",
    "reakci",
    "termodynam",
    "relativit",
    "planét",
    "hviezd",
    "galaxi",
    "vesmír",
    "rýchlosť",
    "tlak",
    "teplot",
    "optik",
    "magnet",
    "svetlo",
    "zvuk",
    "plyn",
    "kvapalin",
    "kov",
    "kryštál",
    "bunka",
    "organizmus",
)

# Geografický, administratívny a politický stop-filter (úplný zákaz miest, obcí a úradov)
GEO_ADMIN_BLACK_LIST = (
    "mesto",
    "obec",
    "okres",
    "kraj",
    "rieka",
    "potok",
    "primátor",
    "starosta",
    "obyvateľ",
    "rozloha",
    "banská",
    "bystrica",
    "bratislava",
    "košice",
    "zvolen",
    "nitra",
    "žilina",
    "trnava",
    "prešov",
    "štát",
    "región",
    "dedina",
    "osada",
    "ulica",
    "námestie",
    "republika",
    "politika",
    "strana",
    "voľby",
    "parlament",
    "ministerstvo",
    "úrad",
    "shire",
    "county",
    "jersey",
    "delaware",
    "indiana",
    "hampshire",
    "york",
    "ohio",
    "texas",
    "berlín",
    "stuttgart",
    "frankfurt",
    "purdue",
)


def calculate_priority(topic: str) -> int:
  """Bodovanie: Vyradenie geografie (-100), silná priorita pre vedu a pojmy (+20)."""
  t_low = topic.lower()

  # Ak téma obsahuje geografický alebo administratívny pojem, okamžite zahodiť
  if any(bad in t_low for bad in GEO_ADMIN_BLACK_LIST):
    return -100

  score = 0
  for marker in SCIENCE_PRIORITY_MARKERS:
    if marker in t_low:
      score += 20
  return score


def load_visited_topics() -> set:
  if VISITED_FILE.exists():
    try:
      with open(VISITED_FILE, "r", encoding="utf-8") as f:
        return set(json.load(f))
    except Exception:
      pass
  return set()


def save_visited_topics(visited: set):
  try:
    with open(VISITED_FILE, "w", encoding="utf-8") as f:
      json.dump(sorted(list(visited)), f, ensure_ascii=False, indent=2)
  except Exception:
    pass


def load_topic_queue() -> list:
  if QUEUE_FILE.exists():
    try:
      with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):
          return data
    except Exception:
      pass
  return []


def save_topic_queue(queue: list):
  try:
    with open(QUEUE_FILE, "w", encoding="utf-8") as f:
      json.dump(queue, f, ensure_ascii=False, indent=2)
  except Exception:
    pass


def clean_wiki_text(text: str) -> str:
  cleaned = re.sub(r"\([^)]*\)", "", text)
  cleaned = re.sub(r"\s+", " ", cleaned)
  return cleaned.strip()


def fallback_extract_facts(topic: str, text: str, grammar: GrammarEngine):
  facts = []
  clean = clean_wiki_text(text)
  sentences = re.split(r"(?<=[.!?])\s+", clean)
  patterns = grammar.PREDICATES

  for sentence in sentences:
    sentence = sentence.strip()
    if len(sentence) < 15 or len(sentence) > 220:
      continue

    match = re.search(
        rf"^{re.escape(topic)}\s+({patterns})\s+(.+)", sentence, re.IGNORECASE
    )
    if not match:
      match = re.search(
          rf"\b{re.escape(topic)}\s+({patterns})\s+([^,;.]+)",
          sentence,
          re.IGNORECASE,
      )

    if match:
      relation = match.group(1).strip().lower()
      target = match.group(2).strip(" .")

      if target.lower().endswith(
          (" z", " do", " v", " na", " a", " i", " o", " u", " s", " so", " k", " ku")
      ):
        continue

      if len(target) < 3:
        continue

      facts.append({
          "source": grammar.lemmatize_entity(topic),
          "relation": relation,
          "target": target[:90],
      })
      if len(facts) >= 3:
        break

  return facts


def get_sirius_idle_time(last_active: float) -> float:
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
  print("[SIRIUS PROFESSOR DAEMON V1.7] Klasické pojmy & Veda...")
  print("=" * 60)

  gatekeeper = GatekeeperNet()
  grammar = GrammarEngine()
  quarantine = StagingQuarantine()
  committer = AtomicCommitter()
  last_active = time.time()

  IDLE_THRESHOLD = 45
  if len(sys.argv) > 1 and sys.argv[1] == "--immediate":
    print("[PROFESSOR] Okamžitý testovací režim (--immediate, idle = 2s).")
    IDLE_THRESHOLD = 2

  # Základné vedecké a vecné pojmy (žiadna geografia ani administratíva)
  seed_topics = [
      "Atóm",
      "Elektrón",
      "Protón",
      "Neutrón",
      "Molekula",
      "Gravitácia",
      "Kvantová mechanika",
      "Periodická tabuľka",
      "Kyslík",
      "Vodík",
      "Uhlík",
      "Železo",
      "Fotosyntéza",
      "Bunka",
      "Energia",
      "Svetlo",
      "Zvuk",
      "Termodynamika",
      "Relativita",
      "Galaxia",
      "Vesmír",
      "Hmota",
      "Magnetizmus",
      "Elektrický prúd",
      "Optika",
      "Kyselina deoxyribonukleová",
  ]

  visited_topics = load_visited_topics()
  raw_queue = load_topic_queue()

  # Očista frontu: vyhodenie geografie, čísel a záporných priorít
  topic_queue = []
  seen = set()
  for item in raw_queue:
    lemma = grammar.lemmatize_entity(item)
    if (
        grammar.is_valid_topic(lemma)
        and lemma.lower() not in visited_topics
        and calculate_priority(lemma) >= 0
    ):
      if lemma.lower() not in seen:
        seen.add(lemma.lower())
        topic_queue.append(lemma)

  if not topic_queue:
    topic_queue = [t for t in seed_topics if t.lower() not in visited_topics]

  topic_queue.sort(key=calculate_priority, reverse=True)
  save_topic_queue(topic_queue)

  print(
      f"[PROFESSOR INIT] Navštívených tém: {len(visited_topics)} | Vedeckých tém"
      f" vo fronte: {len(topic_queue)}"
  )

  while True:
    try:
      idle = get_sirius_idle_time(last_active)

      if idle >= IDLE_THRESHOLD:
        print(
            f"[PROFESSOR] Sirius nečinný ({int(idle)}s). Začínam obohacovanie..."
        )

        current_batch = []
        while topic_queue and len(current_batch) < 3:
          candidate = topic_queue.pop(0)
          cand_lemma = grammar.lemmatize_entity(candidate)
          if (
              grammar.is_valid_topic(cand_lemma)
              and cand_lemma.lower() not in visited_topics
              and calculate_priority(cand_lemma) >= 0
          ):
            current_batch.append(cand_lemma)

        if not current_batch:
          print("[PROFESSOR] Front tém vyčerpaný. Resetujem na čistú vedu...")
          fresh_candidates = [
              t for t in seed_topics if t.lower() not in visited_topics
          ]
          if not fresh_candidates:
            print("[PROFESSOR] Všetky témy preskúmané. Nový cyklus.")
            visited_topics.clear()
            save_visited_topics(visited_topics)
            fresh_candidates = list(seed_topics)

          topic_queue.extend(fresh_candidates)
          topic_queue.sort(key=calculate_priority, reverse=True)
          while topic_queue and len(current_batch) < 3:
            candidate = topic_queue.pop(0)
            if candidate.lower() not in visited_topics:
              current_batch.append(candidate)

        save_topic_queue(topic_queue)

        if not current_batch:
          time.sleep(5)
          continue

        for topic in current_batch:
          if get_sirius_idle_time(last_active) == 0.0:
            print("[PROFESSOR] Preempcia: Príkaz pre Sirius prijatý, ustupujem.")
            last_active = time.time()
            topic_queue.insert(0, topic)
            save_topic_queue(topic_queue)
            break

          visited_topics.add(topic.lower())
          save_visited_topics(visited_topics)

          try:
            text = gatekeeper.fetch_wiki_extract(topic)
          except Exception as net_err:
            print(f"[PROFESSOR WARN] Chyba sťahovania '{topic}': {net_err}")
            continue

          if not text:
            continue

          # Extrakcia nových pojmov - prioritne vedecké a vecné termíny
          new_candidates = grammar.extract_candidates(text, topic)
          added_to_queue = 0
          for cand in new_candidates:
            if (
                cand.lower() not in visited_topics
                and cand not in topic_queue
                and grammar.is_valid_topic(cand)
                and calculate_priority(cand) >= 0
            ):
              topic_queue.append(cand)
              added_to_queue += 1

          if added_to_queue > 0:
            topic_queue.sort(key=calculate_priority, reverse=True)
            save_topic_queue(topic_queue)

          triplets = grammar.extract_triplets(text)
          if not triplets:
            triplets = fallback_extract_facts(topic, text, grammar)

          print(
              f"[PROFESSOR INGEST] Téma '{topic}': {len(text)} znakov ->"
              f" {len(triplets)} faktov | V čakacom rade: {len(topic_queue)}"
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
      print("\n[PROFESSOR] Ukončené používateľom. Ukladám stav...")
      save_visited_topics(visited_topics)
      save_topic_queue(topic_queue)
      break
    except Exception as e:
      print(f"[PROFESSOR ERROR] {e}")
      time.sleep(5)


if __name__ == "__main__":
  main()