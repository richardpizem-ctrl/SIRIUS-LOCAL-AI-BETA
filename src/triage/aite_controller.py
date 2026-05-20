# aite_controller_4_4.py
# SIRIUS LOCAL AI – Automatic Input Triage Engine (AITE) 4.4.0 PRO
# Deterministic, offline-only triage controller with safe-mode and degraded-mode support.

from typing import Dict, Any
from .input_classifier_4_4 import InputClassifier44
from .input_router_4_4 import InputRouter44
from .metadata_builder_4_4 import MetadataBuilder44


class AITEController44:
    """
    Automatic Input Triage Engine (AITE) – 4.4.0 PRO

    Responsibilities:
        - Validate input path (Phase‑5 ready)
        - Detect input type (text, image, audio, application, unknown)
        - Determine the correct target storage path
        - Generate metadata for the file
        - Provide a unified triage result for FS‑AGENT 4.4
        - Safe-mode and degraded-mode compatible
        - Deterministic, offline-only behavior

    This controller does NOT move files.
    FS‑AGENT performs the actual filesystem operations.
    """

    def __init__(self):
        self.classifier = InputClassifier44()
        self.router = InputRouter44()
        self.metadata = MetadataBuilder44()

        self.safe_mode = False
        self.degraded_mode = False

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def process(self, input_path: str) -> Dict[str, Any]:
        """
        Process an input file and return a triage package.

        Steps:
            1. Validate input path
            2. Classify input type
            3. Determine target storage path
            4. Build metadata dictionary
            5. Return unified triage result
        """

        if self.safe_mode:
            return {
                "status": "safe_mode",
                "input": input_path,
                "type": "unknown",
                "target": None,
                "metadata": {},
                "degraded_mode": self.degraded_mode,
            }

        try:
            self._validate_input(input_path)

            input_type = self.classifier.classify(input_path)
            target = self.router.route(input_type)
            meta = self.metadata.build(input_path, input_type)

            return {
                "status": "triage_complete",
                "input": input_path,
                "type": input_type,
                "target": target,
                "metadata": meta,
                "degraded_mode": self.degraded_mode,
            }

        except Exception as exc:
            self.degraded_mode = True
            return {
                "status": "error",
                "input": input_path,
                "type": "unknown",
                "target": None,
                "metadata": {},
                "exception": str(exc),
                "degraded_mode": True,
            }

    # ---------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------

    def _validate_input(self, input_path: str) -> None:
        """
        Basic validation before classification.
        Ensures the input path is usable and safe.
        Phase‑5 ready: forbidden extensions, sandbox rules, quarantine.
        """

        if not isinstance(input_path, str):
            raise TypeError("input_path must be a string")

        if input_path.strip() == "":
            raise ValueError("input_path cannot be empty")

        # Phase‑5 reserved:
        # - forbidden extensions
        # - sandbox rules
        # - path traversal protection
        # - quarantine rules
