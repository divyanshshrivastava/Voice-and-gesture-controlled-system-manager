# core/orchestrator.py

"""
Orchestrator for Kratos.

Takes recognized text (after wake word), parses it into an Intent,
and decides what to do (for now: just voice confirmations + mode changes).
"""

from core.state import app_state, Mode
from core import config
from kratos_io.speech_output import kratos_voice
from nlu.intents import Intent
from nlu.parser import parse_intent


def handle_command_text(text: str) -> None:
    """
    Process a single command string.

    For now, this:
      - parses the intent
      - updates state for dictation-related commands
      - speaks back what it understood
    """
    raw = text.strip()
    t = raw.lower()

    if not t:
        if config.DEBUG:
            print("[Orchestrator] Empty command text.")
        kratos_voice.say("I did not catch that.")
        return

    if config.DEBUG:
        print(f"[Orchestrator] Received command text: {raw!r}")

    intent = parse_intent(t)
    if config.DEBUG:
        print(f"[Orchestrator] Parsed intent: {intent}")

    # Handle known intents
    if intent == Intent.START_DICTATION:
        app_state.set_mode(Mode.DICTATION)
        kratos_voice.say("Dictation mode enabled. I will type what you say.")
        return

    if intent == Intent.STOP_DICTATION:
        app_state.set_mode(Mode.COMMAND)
        kratos_voice.say("Dictation mode disabled. Back to command mode.")
        return

    if intent == Intent.MINIMIZE_WINDOW:
        # Later we'll call a real system_control.minimize() here
        kratos_voice.say("I would minimize the current window now.")
        return

    if intent == Intent.MAXIMIZE_WINDOW:
        kratos_voice.say("I would maximize the current window now.")
        return

    if intent == Intent.CLOSE_WINDOW:
        kratos_voice.say("I would close the current window now.")
        return

    # Fallback for UNKNOWN
    kratos_voice.say(f"You said: {raw}. I am not sure what to do with that yet.")
