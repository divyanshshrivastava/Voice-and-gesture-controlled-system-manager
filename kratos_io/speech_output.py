# io/speech_output.py

import pyttsx3
from core import config

class KratosVoice:
    def __init__(self):
        self.engine = pyttsx3.init()

        # Adjust voice properties
        self.engine.setProperty('rate', 165)      # speed of speech
        self.engine.setProperty('volume', 1.0)    # max volume

        # Try to set a deeper male voice (Windows usually has at least 1)
        voices = self.engine.getProperty('voices')
        for v in voices:
            if "male" in v.name.lower():
                self.engine.setProperty('voice', v.id)
                break

    def say(self, text: str):
        """Speak text out loud."""
        if config.DEBUG:
            print(f"[Kratos says]: {text}")

        self.engine.say(text)
        self.engine.runAndWait()


# Create a single shared instance
kratos_voice = KratosVoice()
