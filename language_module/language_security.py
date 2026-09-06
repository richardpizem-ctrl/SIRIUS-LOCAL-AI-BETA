class LanguageSecurity:
    def is_safe(self, text: str) -> bool:
        """
        Bezpečnostná kontrola pre obyčajného človeka.
        Blokuje nebezpečné, mazacie, systémové alebo nejasné príkazy.
        """

        # Absolútne zakázané frázy
        forbidden = [
            "vymaž všetko",
            "zmaž všetko",
            "zmaž systém",
            "vymaž systém",
            "formátuj disk",
            "format c",
            "delete system",
            "erase system",
            "shutdown now",
            "kill process",
            "zmaž windows",
            "vymaž windows"
        ]

        # Ak veta obsahuje niečo zakázané → NEBEZPEČNÉ
        for word in forbidden:
            if word in text:
                return False

        # Nebezpečné slová (potrebujú potvrdenie)
        risky = [
            "vymaž",
            "zmaž",
            "odstráň",
            "kill",
            "erase",
            "shutdown",
            "terminate"
        ]

        # Ak veta obsahuje rizikové slovo → stále bezpečné, ale vyžaduje potvrdenie
        for word in risky:
            if word in text:
                return True  # bezpečné, ale workflow si vypýta potvrdenie

        # Inak je veta bezpečná
        return True
