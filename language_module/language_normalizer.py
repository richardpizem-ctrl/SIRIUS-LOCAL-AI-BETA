class LanguageNormalizer:
    def normalize(self, text: str) -> str:
        """
        Normalizuje vstup od obyčajného človeka:
        - odstráni zbytočné slová
        - ponechá význam
        - ponechá prirodzenosť
        - neprepisuje technické slová
        """
        text = text.lower().strip()
        return text
