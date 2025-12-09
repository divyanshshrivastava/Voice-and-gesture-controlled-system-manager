# kratos_io/speech_input.py

import speech_recognition as sr
from typing import Optional
from core import config

recognizer = sr.Recognizer()


def listen_once(phrase_time_limit: Optional[float] = None) -> str:
    """
    Listens to the microphone once and returns detected speech as text.

    phrase_time_limit:
        - If None: recognizer decides when to stop (based on pause)
        - If set (e.g. 5.0): stops listening after that many seconds
    """
    with sr.Microphone() as source:
        if config.DEBUG:
            print("[Kratos] Listening for speech...")

        recognizer.adjust_for_ambient_noise(source, duration=0.3)

        audio = recognizer.listen(source, phrase_time_limit=phrase_time_limit)

    try:
        text = recognizer.recognize_google(audio)
        if config.DEBUG:
            print(f"[STT Raw]: {text}")
        return text.lower()

    except sr.UnknownValueError:
        if config.DEBUG:
            print("[STT] Could not understand audio.")
        return ""

    except sr.RequestError as e:
        print(f"[STT] Error while calling recognition service: {e}")
        return ""


def listen_for_wake_word() -> str:
    """Short listen for wake word."""
    return listen_once(phrase_time_limit=3.0)


def listen_for_command() -> str:
    """Longer listen for a full command after wake word."""
    return listen_once(phrase_time_limit=7.0)
