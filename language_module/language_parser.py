class LanguageParser:
    def parse(self, text: str) -> dict:
        """
        Rozbije vetu na základné časti:
        - akcia (čo sa má urobiť)
        - objekt (na čo sa akcia vzťahuje)
        - stav (ak je vo vete)
        - kontext (doplnkové info)
        """

        words = text.split()
        result = {
            "action": None,
            "object": None,
            "state": None,
            "context": None
        }

        # Základné akcie pre obyčajného človeka
        actions = [
            "otvor",
            "ukáž",
            "vyčisti",
            "nájdi",
            "oprav",
            "skontroluj",
            "analyzuj",
            "prečo"
        ]

        # Akcia = prvé slovo, ak je v zozname
        if words:
            first = words[0]
            if first in actions:
                result["action"] = first

        # Objekt = druhé slovo (ak existuje)
        if len(words) > 1:
            result["object"] = words[1]

        # Stav = slová typu "pomalý", "chybný", "nefunkčný"
        states = ["pomalý", "chybný", "nefunkčný", "zaseknutý"]
        for w in words:
            if w in states:
                result["state"] = w

        # Kontext = všetko ostatné
        if len(words) > 2:
            result["context"] = " ".join(words[2:])

        return result
