class LanguageTranslator:
    def translate(self, text: str) -> str:
        """
        Preklad EN → SK pre obyčajného človeka.
        - neprekladá technické slová
        - neprekladá príkazy
        - neprekladá angličtinu, ak je správna
        - prekladá iba bežné frázy
        """

        # Jednoduchý slovník bežných slov
        dictionary = {
            "open": "otvor",
            "settings": "nastavenia",
            "show": "ukáž",
            "duplicates": "duplicity",
            "clean": "vyčisti",
            "disk": "disk",
            "why": "prečo",
            "slow": "pomalý",
            "computer": "počítač",
            "help": "pomôž",
            "find": "nájdi",
            "error": "chyba"
        }

        words = text.split()
        translated = []

        for w in words:
            lw = w.lower()
            if lw in dictionary:
                translated.append(dictionary[lw])
            else:
                translated.append(w)  # nechaj pôvodné slovo

        return " ".join(translated)
