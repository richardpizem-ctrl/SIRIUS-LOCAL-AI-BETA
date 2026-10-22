"""
SIRIUS TARGETED MINER V2.4 - Definitívny beh na 1000 relácií.
Pancierová ochrana proti zacykleniu a čisté riadenie frontu.
"""

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

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "professor"))

from gatekeeper_net import GatekeeperNet
from grammar_engine import GrammarEngine
from staging_quarantine import StagingQuarantine
from atomic_committer import AtomicCommitter

TARGET_COUNT = 1000
KG_PATH = (BASE_DIR / "autosave_kg.json").resolve()
PROFESSOR_DIR = Path(__file__).resolve().parent
QUEUE_FILE = PROFESSOR_DIR / "topic_queue.json"
VISITED_FILE = PROFESSOR_DIR / "visited_topics.json"

SCIENCE_MARKERS = (
    "fyzik", "chém", "biol", "astron", "matemat", "atóm", "jadro", "elektr", "žiaren",
    "častic", "prvok", "zlúčenin", "reakci", "energia", "hmot", "termodynam", "optik",
    "kov", "plyn", "kryštál", "bunka", "bunk", "vln", "tlak", "sila", "pole", "spektrum",
    "živoč", "stavov", "cicav", "vták", "plaz", "obojživel", "ryb", "článkonož", "hmyz",
    "mäkkýš", "drav", "bylinož", "eukaryot", "mitochondr", "fotosynt", "orgán", "sústav",
    "enzým", "bielkovin", "proteín", "nukleov", "dna", "rna", "orbitál", "kvant",
    "srdc", "pľúc", "pečeň", "obličk", "mozog", "miech", "žalúdok", "črev", "tkaniv",
    "krv", "ciev", "hemoglob", "imunit", "protilát", "antigén", "hormón", "inzul",
    "kostr", "lebk", "chrbtic", "žiabr", "plutv", "šupin", "koreň", "stonk", "list",
    "kvet", "semen", "minerál", "kremeň", "kalcit", "pyrit", "hviezda", "pulzar", "kvazar",
    "baktér", "vírus", "archea", "lymfoc", "oko", "ucho", "rohvk", "sietnic", "pankreas",
    "slezin", "prieduš", "hornin", "čadič", "žula", "vápen", "pieskov", "tekton", "litosf",
    "astenosf", "metán", "etanol", "benzén", "polymér", "elektrolýz", "zákon", "rezonan", "akustik"
)

GEO_STOP = (
    "mesto", "obec", "okres", "kraj", "rieka", "štát", "kráľ", "prezident", "narodil",
    "zomrel", "územie", "obyvateľ", "dedina", "ulica", "parlament", "strana", "politika",
    "banská", "bystrica", "bratislava", "kodaň", "dánsko", "dánsk", "nemecko", "nemeck",
    "usa", "amerika", "americk", "heidelberg", "anglick", "londýn", "leeds", "birstall",
    "pensylván", "dakot", "kanad", "holandsk", "francúzsk", "taliansk", "benátky",
    "faersk", "ázi", "európ", "liga", "klub", "hokej", "futbal", "bulls", "božie",
    "vďaka", "väčšina", "iná", "staršie", "rozlišovanie", "spojené štáty", "autor",
    "otázku", "poskytuje", "predstavu", "pôvodca", "vydavateľstvo", "zaujímava"
)

# Garantovaný zoznam čerstvých vedeckých tém na prekročenie 1000 relácií
MASSIVE_BACKUP_TOPICS = [
    "Tachyon", "Wormhole", "Baryónová hmotnosť", "Kvantový počítač", "Supergravitácia",
    "Kozmické žiarenie", "Zodiakálne svetlo", "Stellarová evolúcia", "Planetary nebula", "Röntgenové žiarenie",
    "Gama záblesk", "Kvantová elektrodynamika", "Kvantová chromodynamika", "Standardný model", "Higgs bosonský",
    "Leptón", "Hadrón", "Bozón W", "Bozón Z", "Gravitón",
    "Solárna konstanta", "Heliopauza", "Intersteliárne medium", "Protoplanetárny disk", "Vesmírny prach",
    "Metabolická dráha", "ATP syntáza", "Fotosystém I", "Fotosystém II", "Ribozým",
    "Teloméra", "Telomeráza", "Epigenetika", "Metylácia DNA", "Histón",
    "Transkripcia", "Translácia", "Ribozóm", "Transferová RNA", "Messengerová RNA",
    "Imunoglobulín", "Komplementárny systém", "Makrofág", "Neutrofil", "Eozinofil",
    "Bazofil", "Dendritická bunka", "Apoptóza", "Nekróza", "Mitóza",
    "Meióza", "Crossing-over", "Mutácia", "Genóm", "Proteóm",
    "Lipozóm", "Micela", "Membránový potenciál", "Akčný potenciál", "Ionový kanál",
    "Konektor", "Glutamát", "Dopamín", "Serotonín", "Acetylcholín",
    "GABA", "Endorfín", "Myelínová pošva", "Ranvierov zárez", "Gliová bunka",
    "Astrocyt", "Mikroglia", "Oligodendrocyt", "Schwannova bunka", "Krvno-mozgová bariéra"
, 'Betón', 'Železobetón', 'Cement', 'Maltová zmes', 'Tehla', 'Tvárnica', 'Sadrokartón', 'Tepelná izolácia', 'Hydroizolácia', 'Krov', 'Krytina', 'Základová doska', 'Poter', 'Omietka', 'Fasáda', 'Lešenie', 'Debnenie', 'Armatúra', 'Kladivo', 'Skrutkovač', 'Kliešte', 'Vodováha', 'Uhlová brúska', 'Vŕtačka', 'Priamočiara píla', 'Okružná píla', 'Zváračka', 'Transformátor', 'Elektromotor', 'Istič', 'Prúdový chránič', 'Multimeter', 'Rezistor', 'Kondenzátor', 'Dióda', 'Tranzistor', 'Akumulátor', 'Ozubené koleso', 'Ložisko', 'Hriadeľ', 'Kľukový hriadeľ', 'Piest', 'Ojnica', 'Zotrvačník', 'Ventil', 'Čerpadlo', 'Kompresor', 'Hydraulika', 'Pneumatika', 'Tlakomer', 'Termostat', 'Výmenník tepla', 'Radiátor', 'Kotol', 'Klimatizácia', 'Solárny panel', 'Tepelné čerpadlo', 'Potrubie', 'Sifón', 'Kanalizácia', 'Hliník', 'Meď', 'Železo', 'Zlato', 'Striebro', 'Platina', 'Zinok', 'Olovo', 'Cín', 'Nikel', 'Chróm', 'Titán', 'Volfrám', 'Uhlík', 'Vodík', 'Kyslík', 'Dusík', 'Sírnik', 'Kyselina sírová', 'Kyselina chlorovodíková', 'Hydroxid sodný', 'Kremeň', 'Živec', 'Sľuda', 'Kalcit', 'Sadrovec', 'Diamant', 'Grafit', 'Magnetit', 'Hematit', 'Rýchlosť', 'Zrýchlenie', 'Hmotnosť', 'Sila', 'Tlak', 'Teplota', 'Hustota', 'Objem', 'Energia', 'Výkon', 'Elektrický prúd', 'Elektrické napätie', 'Elektrický odpor', 'Magnetické pole', 'Frekvencia', 'Vlnová dĺžka', 'Galaxia', 'Hviezda', 'Planéta', 'Kométa', 'Bryndza', 'Oštiepok', 'Parenica', 'Korbáčik', 'Žinčica', 'Kyslé mlieko', 'Tvaroh', 'Maslo', 'Syr', 'Smotana', 'Klobása', 'Jaternica', 'Slanina', 'Oškvarky', 'Bravčová masť', 'Halušky', 'Pirohy', 'Lokša', 'Zemiaková placka', 'Kapustnica', 'Fazuľová polievka', 'Guláš', 'Demikát', 'Držková polievka', 'Chlieb', 'Rožok', 'Vianočka', 'Bábovka', 'Štrúdľa', 'Parené buchty', 'Trdelník', 'Medovník', 'Kvasnice', 'Múka', 'Krupica', 'Stočný med', 'Cukor', 'Soľ', 'Ocot', 'Horčica', 'Kyslá kapusta', 'Kvasená uhorka', 'Pivo', 'Víno', 'Medovina', 'Slivovica', 'Borovička', 'Hriatô', 'Káva', 'Čaj', 'Ligurček', 'Majoránka', 'Rasca', 'Bobkový list', 'Čierne korenie', 'Mletá paprika', 'Cesnak', 'Cibuľa', 'Chren', 'Kôpor']


def get_current_count() -> int:
    if not KG_PATH.exists():
        return 0
    try:
        with open(KG_PATH, "r", encoding="utf-8") as f:
            d = json.load(f)
        return len(d.get("relations", []))
    except Exception:
        return 0


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
                if isinstance(data, list) and data:
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


def main():
    print("=" * 60)
    print(f"[SIRIUS MINER V2.4] Definitívny beh na {TARGET_COUNT} relácií")
    print("=" * 60)

    gatekeeper = GatekeeperNet()
    grammar = GrammarEngine()
    quarantine = StagingQuarantine()
    committer = AtomicCommitter()

    current = get_current_count()
    print(f"[START] Aktuálny stav grafu: {current} / {TARGET_COUNT}")

    visited = load_visited_topics()
    
    # Vygenerujeme čerstvý front striktne len z tých tém, ktoré ešte neboli navštívené
    queue = [t for t in MASSIVE_BACKUP_TOPICS if t.lower() not in visited]
    save_topic_queue(queue)

    print(f"[FRONT] Pripravených {len(queue)} čistých tém v čakacom rade.")

    while current < TARGET_COUNT:
        if not queue:
            print("\n[MINER] Čakací rad je prázdny. Ukončujem beh.")
            break

        topic = queue.pop(0)
        save_topic_queue(queue)

        topic_clean = grammar.lemmatize_entity(topic)
        if topic_clean.lower() in visited:
            continue
            
        visited.add(topic_clean.lower())
        save_visited_topics(visited)

        print(f"\n[MINER] Sťahujem ({current}/{TARGET_COUNT}): {topic_clean} | Vo fronte: {len(queue)}")

        try:
            text = gatekeeper.fetch_wiki_extract(topic_clean)
        except Exception as e:
            print(f"[CHYBA SIETE] {topic_clean}: {e}")
            time.sleep(1)
            continue

        if not text:
            continue

        triplets = grammar.extract_triplets(text)
        if not triplets:
            # Fallback extrakcia
            clean = re.sub(r"\([^)]*\)", "", text)
            sentences = re.split(r"(?<=[.!?])\s+", clean)
            pred_regex = r"(je|sú|má|majú|obsahuje|obsahujú|pozostáva|tvorí|predstavuje|patrí medzi)"
            for sentence in sentences:
                s = sentence.strip()
                if len(s) < 15 or len(s) > 200:
                    continue
                m = re.search(rf"\b{re.escape(topic_clean)}\s+{pred_regex}\s+([^,;.]+)", s, re.IGNORECASE)
                if m:
                    rel = m.group(1).strip().lower()
                    tgt = m.group(2).strip(" .")[:90]
                    if len(tgt) >= 3 and not any(g in tgt.lower() for g in GEO_STOP):
                        triplets.append({
                            "source": topic_clean,
                            "relation": rel,
                            "target": tgt
                        })
                        break

        clean_triplets = []
        for t in triplets:
            s_low = t["source"].lower()
            tgt_low = t["target"].lower()
            if not any(g in s_low or g in tgt_low for g in GEO_STOP):
                clean_triplets.append(t)

        if clean_triplets:
            for t in clean_triplets:
                quarantine.stage_triplet(t["source"], t["relation"], t["target"], "sk.wikipedia.org")
            committer.commit_triplets(quarantine.get_promotable_triplets())
            current = get_current_count()
            print(f"[COMMIT] Uložené. Nový stav: {current} relácií (Cieľ: {TARGET_COUNT})")

        time.sleep(1.0)

    print("\n" + "=" * 60)
    print(f"[HOTOVO] Konečný stav slovenskej vetvy: {current} relácií.")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[MINER] Prerušené používateľom. Stav je bezpečne uložený.")