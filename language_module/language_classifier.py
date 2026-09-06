class LanguageClassifier:
    def classify(self, text: str) -> str:
        """
        Kategorizuje vetu od obyčajného človeka:
        - rozlíši otázku
        - rozlíši príkaz
        - rozlíši žiadosť
        - rozlíši problém
        - rozlíši diagnostiku
        """

        # Otázka (končí otáznikom alebo začína 'prečo', 'ako', 'kedy', 'čo')
        if text.endswith("?") or text.startswith(("prečo", "ako", "kedy", "čo")):
            return "question"

        # Príkaz (začína slovesom: otvor, ukáž, vyčisti, nájdi, oprav)
        if text.startswith(("otvor", "ukáž", "vyčisti", "nájdi", "oprav")):
            return "command"

        # Problém (obsahuje slová: nefunguje, nejde, je pomalý, chyba)
        if any(word in text for word in ["nefunguje", "nejde", "pomalý", "chyba"]):
            return "problem"

        # Žiadosť (obsahuje slová: prosím, mohol by si, vieš mi)
        if any(word in text for word in ["prosím", "mohol by si", "vieš mi"]):
            return "request"

        # Diagnostika (obsahuje slová: diagnostika, skontroluj, analyzuj)
        if any(word in text for word in ["diagnostika", "skontroluj", "analyzuj"]):
            return "diagnostic"

        # Default fallback
        return "unknown"
