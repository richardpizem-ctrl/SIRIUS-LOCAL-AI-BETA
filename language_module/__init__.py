from .language_normalizer import LanguageNormalizer
from .language_classifier import LanguageClassifier
from .language_security import LanguageSecurity
from .language_translator import LanguageTranslator
from .language_parser import LanguageParser
from .language_output import LanguageOutput

class LanguageModule:
    def __init__(self):
        self.normalizer = LanguageNormalizer()
        self.classifier = LanguageClassifier()
        self.security = LanguageSecurity()
        self.translator = LanguageTranslator()
        self.parser = LanguageParser()
        self.output = LanguageOutput()

    def process(self, text: str) -> dict:
        """
        Kompletný jazykový pipeline pre obyčajného človeka.
        """

        # 1. Normalizácia
        normalized = self.normalizer.normalize(text)

        # 2. Kategorizácia
        category = self.classifier.classify(normalized)

        # 3. Bezpečnosť
        safe = self.security.is_safe(normalized)

        # 4. Preklad EN → SK
        translated = self.translator.translate(normalized)

        # 5. Parser
        parsed = self.parser.parse(translated)

        # 6. Výstup
        result = self.output.build(
            normalized=translated,
            category=category,
            parsed=parsed
        )

        # Pridáme bezpečnostný flag
        result["is_safe"] = safe

        return result
