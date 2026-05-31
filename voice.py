# voice_4_5.py
# SIRIUS LOCAL AI – Voice Control (v4.5.0 PRO)
# Deterministic, safe-mode compatible, sandboxed voice engine (Phase‑5 ready)

from __future__ import annotations

import speech_recognition as sr
from runtime.runtime_manager_4_5 import RuntimeManager45
from runtime.plugin_loader_4_5 import PluginLoader45
from runtime.nl_router_4_5 import NaturalLanguageRouter45


class SiriusVoice45:
    """
    SIRIUS LOCAL AI — Voice Control (v4.5.0 PRO)

    Features:
        - Listens to microphone (sandboxed)
        - Recognizes Slovak speech
        - Sends text to NL Router 4.5
        - Safe-mode + degraded-mode support
        - Deterministic, isolated error handling
        - Phase‑5 ready
    """

    def __init__(self):
        self.safe_mode: bool = False
        self.degraded_mode: bool = False

        # ----------------------------------------------------
        # Runtime bootstrap
        # ----------------------------------------------------
        try:
            self.runtime = RuntimeManager45()
            self.runtime.initialize()
        except Exception as exc:
            self.degraded_mode = True
            print(f"[VOICE] Runtime init failed: {exc}")
            raise

        # ----------------------------------------------------
        # Plugins
        # ----------------------------------------------------
        try:
            self.plugins = PluginLoader45(self.runtime)
            self.plugins.load_all()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"[VOICE] Plugin load error: {exc}")

        # ----------------------------------------------------
        # NL Router
        # ----------------------------------------------------
        try:
            self.router = NaturalLanguageRouter45(self.runtime, self.plugins)
            self.router.initialize()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"[VOICE] NL Router init error: {exc}")

        # ----------------------------------------------------
        # Speech Recognition
        # ----------------------------------------------------
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"[VOICE] Microphone init error: {exc}")

        self.runtime.logger.info("Voice engine initialized (v4.5.0 PRO)")

    # --------------------------------------------------------
    # SPEECH RECOGNITION (4.5.0 PRO)
    # --------------------------------------------------------
    def listen(self) -> str | None:
        """Listen to microphone and return recognized text."""
        if self.safe_mode:
            return None

        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio, language="sk-SK")
            self.runtime.logger.info(f"[VOICE] Recognized: {text}")
            return text

        except sr.UnknownValueError:
            self.runtime.logger.warning("[VOICE] Could not understand speech")
            return None

        except sr.RequestError as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[VOICE] Speech recognition service error: {e}")
            return None

        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[VOICE] Unexpected error: {e}")
            return None

    # --------------------------------------------------------
    # PROCESS COMMAND (4.5.0 PRO)
    # --------------------------------------------------------
    def process(self, text: str | None) -> None:
        """Send recognized text to NL Router 4.5."""
        if not text:
            return

        if self.safe_mode:
            self.runtime.logger.warning("[VOICE] NL routing blocked: SAFE MODE")
            return

        try:
            result = self.router.route(text)
            self.runtime.logger.info(f"[VOICE] NL result: {result}")
        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[VOICE] NL processing error: {e}")

    # --------------------------------------------------------
    # MAIN LOOP (4.5.0 PRO)
    # --------------------------------------------------------
    def run(self) -> None:
        """Continuous voice listening loop."""
        header = "SIRIUS Voice Control — active (v4.5.0 PRO)"
        if self.safe_mode:
            header += " [SAFE MODE]"
        elif self.degraded_mode:
            header += " [DEGRADED MODE]"

        self.runtime.logger.info(header)
        self.runtime.logger.info("Listening for commands...")

        try:
            while True:
                text = self.listen()
                self.process(text)

        except KeyboardInterrupt:
            self.runtime.logger.info("[VOICE] Shutdown requested (KeyboardInterrupt)")

        except Exception as e:
            self.degraded_mode = True
            self.runtime.logger.error(f"[VOICE] Main loop error: {e}")

    # --------------------------------------------------------
    # SAFE-MODE CONTROL
    # --------------------------------------------------------
    def enter_safe_mode(self) -> None:
        self.safe_mode = True

    def exit_safe_mode(self) -> None:
        self.safe_mode = False


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    voice = SiriusVoice45()
    voice.run()
