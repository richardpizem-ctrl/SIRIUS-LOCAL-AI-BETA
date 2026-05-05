from .input_classifier import InputClassifier
from .input_router import InputRouter
from .metadata_builder import MetadataBuilder


class AITEController:
    """
    Automatic Input Triage Engine (AITE)

    Responsibilities:
        - Detect input type (text, image, audio, application, unknown)
        - Determine the correct target storage path
        - Generate metadata for the file
        - Provide a unified triage result for FS-AGENT

    This controller does NOT move files.
    FS-AGENT performs the actual filesystem operations.
    """

    def __init__(self):
        self.classifier = InputClassifier()
        self.router = InputRouter()
        self.metadata = MetadataBuilder()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def process(self, input_path: str) -> dict:
        """
        Process an input file and return a triage package.

        Steps:
            1. Validate input path
            2. Classify input type
            3. Determine target storage path
            4. Build metadata dictionary
            5. Return unified triage result

        FS-AGENT will later:
            - move the file
            - rename if needed
            - apply metadata
        """

        self._validate_input(input_path)

        input_type = self.classifier.classify(input_path)
        target = self.router.route(input_type)
        meta = self.metadata.build(input_path, input_type)

        return {
            "input": input_path,
            "type": input_type,
            "target": target,
            "metadata": meta,
            "status": "triage_complete"
        }

    # ---------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------

    def _validate_input(self, input_path: str) -> None:
        """
        Basic validation before classification.
        Ensures the input path is usable and safe.
        """

        if not isinstance(input_path, str):
            raise TypeError("input_path must be a string")

        if input_path.strip() == "":
            raise ValueError("input_path cannot be empty")

        # Additional safety checks for future versions:
        # - forbidden extensions
        # - sandbox rules
        # - path traversal protection
        # - quarantine rules
        # (Phase 5)
