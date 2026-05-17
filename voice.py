# voice_4_3.py
# SIRIUS LOCAL AI – Voice Control (v4.3.x)
# Deterministic, safe-mode compatible, sandboxed voice engine

from __future__ import annotations

import speech_recognition as sr
from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter


class SiriusVoice43:
    """
    SIRIUS LOCAL AI — Voice Control (v4.3.x)

    Features:
        - Listens to microphone (sandboxed)
        - Recognizes Slovak speech
        - Sends text to NL Router 4.3
        - Safe-mode + degraded-mode support
        - Deterministic, isolated error handling
    """

    def __init__(self):
        # Runtime bootstrap
        self.runtime = RuntimeManager()
        self.safe_mode = False
        self.degraded_mode = False

        try:
            self.runtime.initialize()
        except Exception as exc:
            self.degraded_mode = True
            print(f"[VOICE] Runtime init failed: {exc}")

        # Plugins
        try:
            self.plugins = PluginLoader(self.runtime)
            self.plugins.load_plugins()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"Plugin load error: {exc}")

        # NL Router
        try:
            self.router = NaturalLanguageRouter(self.runtime, self.plugins)
            self.router.initialize()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"NL Router init error: {exc}")

        # Speech Recognition
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
        except Exception as exc:
            self.degraded_mode = True
            self.runtime.logger.error(f"Microphone init error: {exc}")

        self.runtime.logger.info("Voice engine initialized (v4.3.x)")

    # --------------------------------------------------------
    # SPEECH RECOGNITION (4.3.x)
    # --------------------------------------------------------
    def listen(self):
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
    # PROCESS COMMAND (4.3.x)
    # --------------------------------------------------------
    def process(self, text):
        """Send recognized text to NL Router 4.3."""
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
    # MAIN LOOP (4.3.x)
    # --------------------------------------------------------
    def run(self):
        """Continuous voice listening loop."""
        header = "SIRIUS Voice Control — active (v4.3.x)"
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
    def enter_safe_mode(self):
        self.safe_mode = True

    def exit_safe_mode(self):
        self.safe_mode = False


# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    voice = SiriusVoice43()
    voice.run()
