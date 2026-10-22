import re
import sys
from typing import Dict, List

# Vynútenie UTF-8 výstupu pre Windows konzolu
if sys.platform == "win32":
  try:
    sys.stdout.reconfigure(encoding="utf-8")
  except Exception:
    pass

# Jazykovo špecifické dáta
FORBIDDEN_MODAL_OPERATORS = {
    "sk": [
        "moze",
        "môže",
        "mozu",
        "môžu",
        "mozno",
        "možno",
        "pravdepodobne",
        "udajne",
        "údajne",
        "asi",
        "zrejme",
        "niekedy",
        "obcas",
        "občas",
    ],
    "en": [
        "might",
        "may",
        "could",
        "can",
        "allegedly",
        "perhaps",
        "maybe",
        "possibly",
        "sometimes",
        "often",
    ],
}

NEGATION_PATTERNS = {
    "sk": [
        r"\bnie\b",
        r"\bnema\b",
        r"\bnemá\b",
        r"\bnie\s+je\b",
        r"\bnie\s+su\b",
        r"\bnie\s+sú\b",
        r"\bnebol\b",
        r"\bnebola\b",
        r"\bnebolo\b",
        r"\bne\w+",
    ],
    "en": [
        r"\bnot\b",
        r"\bno\b",
        r"\bnever\b",
        r"\bisn't\b",
        r"\baren't\b",
        r"\bwasn't\b",
        r"\bweren't\b",
        r"\bdon't\b",
        r"\bdoesn't\b",
        r"\bdidn't\b",
    ],
}

SAV_STOPWORDS = {
    "sk": {
        "nazov",
        "názov",
        "dolezite",
        "dôležité",
        "tento",
        "tato",
        "táto",
        "toto",
        "tieto",
        "títo",
        "hlavny",
        "hlavný",
        "hlavná",
        "prvy",
        "prvý",
        "prvá",
        "druhý",
        "druhá",
        "tretí",
        "sucast",
        "súčasť",
        "ciel",
        "cieľ",
        "priklad",
        "príklad",
        "dovod",
        "dôvod",
        "uloha",
        "úloha",
        "jeho",
        "jej",
        "ich",
        "náš",
        "váš",
        "môj",
        "tvoj",
        "svoj",
        "podľa",
        "medzi",
        "preto",
        "napriek",
        "okrem",
        "počas",
        "kvôli",
        "všetky",
        "všetci",
        "každý",
        "každá",
        "niektoré",
        "mnohé",
        "iný",
        "iná",
        "ďalší",
        "ďalšie",
        "slovenská",
        "slovensko",
        "napríklad",
        "priemerná",
        "priemerný",
        "celková",
        "celkový",
        "veľká",
        "veľký",
        "malá",
        "malý",
        "nový",
        "starý",
        "významný",
        "známy",
        "často",
        "veľmi",
        "najmä",
        "avšak",
        "pretože",
        "keďže",
        "pričom",
    },
    "en": {
        "name",
        "important",
        "this",
        "that",
        "these",
        "those",
        "main",
        "first",
        "second",
        "third",
        "part",
        "goal",
        "example",
        "reason",
        "task",
        "his",
        "her",
        "its",
        "their",
        "our",
        "your",
        "my",
        "according",
        "between",
        "therefore",
        "despite",
        "except",
        "during",
        "all",
        "every",
        "each",
        "some",
        "many",
        "other",
        "another",
        "example",
        "average",
        "total",
        "large",
        "small",
        "new",
        "old",
        "significant",
        "known",
        "often",
        "very",
        "mainly",
        "however",
        "because",
        "while",
    },
}

JUNK_ENDINGS = {
    "sk": (
        "akademických",
        "rôznych",
        "mnohých",
        "iných",
        "veľkých",
        "malých",
        "najstarších",
        "ktoré",
        "ktorá",
        "ktorý",
        "ako",
        "kde",
        "alebo",
        "pričom",
        " z",
        " do",
        " v",
        " na",
        " a",
        " i",
        " o",
        " u",
        " s",
        " so",
        " k",
        " ku",
    ),
    "en": (
        "various",
        "many",
        "other",
        "large",
        "small",
        "which",
        "that",
        "who",
        "as",
        "where",
        "or",
        "while",
        " of",
        " to",
        " in",
        " on",
        " and",
        " or",
        " with",
        " by",
        " for",
        " from",
    ),
}

DIRECT_LEMMAS = {
    "sk": {
        "zeme": "Zem",
        "zemou": "Zem",
        "zemi": "Zem",
        "mesiaca": "Mesiac",
        "mesiacom": "Mesiac",
        "mesiaci": "Mesiac",
        "mesiace": "Mesiac",
        "slnka": "Slnko",
        "slnku": "Slnko",
        "slnkom": "Slnko",
        "atómu": "Atóm",
        "atómom": "Atóm",
        "atómy": "Atóm",
        "elektrónu": "Elektrón",
        "elektrónom": "Elektrón",
        "elektróny": "Elektrón",
        "neutrónu": "Neutrón",
        "neutrónom": "Neutrón",
        "neutróny": "Neutrón",
        "jadra": "Jadro",
        "jadru": "Jadro",
        "jadrom": "Jadro",
        "bunky": "Bunka",
        "bunke": "Bunka",
        "bunkou": "Bunka",
        "gravitácie": "Gravitácia",
        "gravitáciou": "Gravitácia",
        "vody": "Voda",
        "vode": "Voda",
        "vodou": "Voda",
    },
    "en": {},
}


class GrammarEngine:

  def __init__(self, default_lang="sk"):
    self.default_lang = default_lang.lower()
    if self.default_lang not in ["sk", "en"]:
      self.default_lang = "sk"

  def _get_predicates(self, lang: str) -> str:
    if lang == "en":
      return (
          r"is|are|has|have|contains|contain|consists of|forms|represents|belongs"
          r" to|includes"
      )
    return (
        r"je|sú|má|ma|predstavuje|predstavujú|pozostáva|pozostávajú|patrí|patria|"
        r"tvorí|tvoria|slúži|vzniká|obsahuje|zahŕňa"
    )

  def is_valid_factual_sentence(self, sentence: str, lang: str = None) -> bool:
    l = lang or self.default_lang
    clean = sentence.strip().lower()
    for mod in FORBIDDEN_MODAL_OPERATORS.get(l, FORBIDDEN_MODAL_OPERATORS["sk"]):
      if re.search(rf"\b{mod}\b", clean):
        return False
    for neg in NEGATION_PATTERNS.get(l, NEGATION_PATTERNS["sk"]):
      if re.search(neg, clean):
        return False
    return True

  def lemmatize_word(self, word: str, lang: str = None) -> str:
    l = lang or self.default_lang
    w_low = word.lower().strip()
    direct = DIRECT_LEMMAS.get(l, {})
    if w_low in direct:
      return direct[w_low]

    if l == "sk" and len(w_low) > 4:
      if w_low.endswith("om"):
        return word[:-2]
      if w_low.endswith("ou"):
        return word[:-2] + "a"
      if w_low.endswith("och") or w_low.endswith("ami"):
        return word[:-3]
    elif l == "en":
      # Základné anglické ošetrenie množného čísla (-ies -> -y, -s)
      if w_low.endswith("ies") and len(w_low) > 4:
        return word[:-3] + "y"
      if w_low.endswith("s") and not w_low.endswith("ss") and len(w_low) > 3:
        return word[:-1]

    return word

  def lemmatize_entity(self, entity: str, lang: str = None) -> str:
    l = lang or self.default_lang
    words = entity.strip().split()
    if not words:
      return ""

    stopwords = SAV_STOPWORDS.get(l, SAV_STOPWORDS["sk"])
    if len(words) == 2 and words[0][0].isupper() and words[1][0].isupper():
      if words[0].lower() in stopwords:
        return ""
      return f"{words[0]} {self.lemmatize_word(words[1], l)}"

    cleaned = [self.lemmatize_word(w, l) for w in words]
    res = " ".join(cleaned)
    return res[0].upper() + res[1:] if res else ""

  def is_valid_topic(self, topic: str, lang: str = None) -> bool:
    l = lang or self.default_lang
    t_clean = topic.strip()
    t_low = t_clean.lower()

    if len(t_clean) < 3:
      return False

    stopwords = SAV_STOPWORDS.get(l, SAV_STOPWORDS["sk"])
    if t_low in stopwords:
      return False

    parts = t_low.split()
    if parts and parts[0] in stopwords:
      return False

    if re.search(r"\d", t_clean):
      return False

    return True

  def extract_candidates(
      self, text: str, current_topic: str, lang: str = None
  ) -> List[str]:
    l = lang or self.default_lang
    candidates = []

    # Regulárny výraz pre výber veľkých písmen
    multi_matches = re.findall(
        r"\b([A-ZÀ-ž][a-zà-ž]{2,}\s+[A-ZÀ-ž][a-zà-ž]{2,})\b", text
    )
    stopwords = SAV_STOPWORDS.get(l, SAV_STOPWORDS["sk"])

    for m in multi_matches:
      first, second = m.split()
      if first.lower() in stopwords or second.lower() in stopwords:
        continue
      lemma_m = self.lemmatize_entity(m, l)
      if (
          self.is_valid_topic(lemma_m, l)
          and lemma_m.lower() != current_topic.lower()
      ):
        candidates.append(lemma_m)

    single_matches = re.findall(r"\b[A-ZÀ-ž][a-zà-ž]{2,}\b", text)
    for s in single_matches:
      lemma_s = self.lemmatize_entity(s, l)
      if (
          self.is_valid_topic(lemma_s, l)
          and lemma_s.lower() != current_topic.lower()
      ):
        candidates.append(lemma_s)

    seen = set()
    result = []
    for c in candidates:
      c_low = c.lower()
      if c_low not in seen:
        seen.add(c_low)
        result.append(c)

    return result[:10]

  def extract_triplets(self, text: str, lang: str = None) -> List[Dict[str, str]]:
    l = lang or self.default_lang
    triplets = []
    clean = re.sub(r"\([^)]*\)", "", text)
    clean = re.sub(r"\s+", " ", clean).strip()

    sentences = re.split(r"[.?!;]", clean)
    predicates_str = self._get_predicates(l)
    junk = JUNK_ENDINGS.get(l, JUNK_ENDINGS["sk"])

    for s in sentences:
      s_clean = s.strip()
      if (
          not s_clean
          or len(s_clean) < 10
          or not self.is_valid_factual_sentence(s_clean, l)
      ):
        continue

      pattern = (
          r"^([A-ZÀ-ž][a-zà-ž]+(?:\s+[A-ZÀ-ž][a-zà-ž]+)?)\s+("
          + predicates_str
          + r")\s+([^,;.]+)"
      )
      match = re.search(pattern, s_clean, re.IGNORECASE)

      if match:
        raw_sub = match.group(1).strip()
        rel = match.group(2).strip().lower()
        raw_obj = match.group(3).strip()

        sub_clean = self.lemmatize_entity(raw_sub, l)
        if not self.is_valid_topic(sub_clean, l):
          continue

        words = [w for w in raw_obj.split() if len(w) > 2]
        if len(words) >= 2:
          clean_obj = " ".join(words[:6]).lower()
          if clean_obj.endswith(junk):
            continue

          if l == "sk":
            if rel in ("sú", "je"):
              rel_norm = "je"
            elif rel in ("má", "ma"):
              rel_norm = "ma"
            else:
              rel_norm = rel
          else:
            if rel in ("are", "is"):
              rel_norm = "is"
            elif rel in ("have", "has"):
              rel_norm = "has"
            else:
              rel_norm = rel

          triplets.append({
              "source": sub_clean.lower(),
              "relation": rel_norm,
              "target": clean_obj,
              "confidence": 1.0,
          })

    return triplets