import re
from typing import Dict, List

FORBIDDEN_MODAL_OPERATORS = [
    "moze", "môže", "mozu", "môžu", "mozno", "možno", "pravdepodobne",
    "udajne", "údajne", "asi", "zrejme", "might", "allegedly", "perhaps",
    "maybe", "possibly", "niekedy", "obcas", "občas"
]

NEGATION_PATTERNS = [
    r"\bnie\b", r"\bnema\b", r"\bnemá\b", r"\bnie\s+je\b",
    r"\bnie\s+su\b", r"\bnie\s+sú\b", r"\bnebol\b", r"\bnebola\b",
    r"\bnebolo\b", r"\bne\w+"
]

JUNK_SUBJECTS = {
    "nazov", "názov", "dolezite", "dôležité", "tento", "tato", "táto",
    "hlavny", "hlavný", "prvy", "prvý", "sucast", "súčasť", "ciel", "cieľ",
    "priklad", "príklad", "dovod", "dôvod", "uloha", "úloha"
}

JUNK_ENDINGS = (
    "akademických", "rôznych", "mnohých", "iných", "veľkých", "malých",
    "ktoré", "ktorá", "ktorý", "ako", "kde", "alebo", "pričom"
)

class GrammarEngine:
    def is_valid_factual_sentence(self, sentence: str) -> bool:
        clean = sentence.strip().lower()
        for mod in FORBIDDEN_MODAL_OPERATORS:
            if re.search(rf"\b{mod}\b", clean):
                return False
        for neg in NEGATION_PATTERNS:
            if re.search(neg, clean):
                return False
        return True

    def extract_triplets(self, text: str) -> List[Dict[str, str]]:
        triplets = []
        sentences = re.split(r"[.?!;]", text)
        for s in sentences:
            s_clean = s.strip()
            if not s_clean or len(s_clean) < 10 or not self.is_valid_factual_sentence(s_clean):
                continue

            m_je = re.search(r"^([A-ZÁÄČĎÉÍĽŇÓÔŔŠŤÚÝŽ][a-záäčďéíĺľňóôŕšťúýž]+)\s+(?:je|sú)\s+([a-záäčďéíĺľňóôŕšťúýž\s,]+)", s_clean)
            if m_je:
                sub = m_je.group(1).strip().lower()
                if sub in JUNK_SUBJECTS or len(sub) < 3:
                    continue

                raw_obj = m_je.group(2).split(",")[0].strip().lower()
                words = [w for w in raw_obj.split() if len(w) > 2]
                if len(words) >= 2:
                    clean_obj = " ".join(words[:4])
                    if not clean_obj.endswith(JUNK_ENDINGS):
                        triplets.append({"source": sub, "relation": "je", "target": clean_obj, "confidence": 1.0})
                continue

            m_ma = re.search(r"^([A-ZÁÄČĎÉÍĽŇÓÔŔŠŤÚÝŽ][a-záäčďéíĺľňóôŕšťúýž]+)\s+(?:má|ma)\s+([a-záäčďéíĺľňóôŕšťúýž\s,]+)", s_clean)
            if m_ma:
                sub = m_ma.group(1).strip().lower()
                if sub in JUNK_SUBJECTS or len(sub) < 3:
                    continue

                raw_obj = m_ma.group(2).split(",")[0].strip().lower()
                words = [w for w in raw_obj.split() if len(w) > 2]
                if len(words) >= 2:
                    clean_obj = " ".join(words[:4])
                    if not clean_obj.endswith(JUNK_ENDINGS):
                        triplets.append({"source": sub, "relation": "ma", "target": clean_obj, "confidence": 1.0})
                continue

        return triplets