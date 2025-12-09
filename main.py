# main.py

from time import sleep

from core import config
from kratos_io.speech_output import kratos_voice
from kratos_io.speech_input import listen_for_wake_word, listen_for_command
from kratos_io.wake_word import text_contains_hotword


def kratos_main_loop_simple():
    """
    Simple two-step loop:

    1) Wait for wake word ("Kratos")
    2) After wake word, listen once for a command and repeat it back

    Then go back to waiting for wake word again.
    """

    kratos_voice.say("Kratos is online. Say my name to wake me.")

    while True:
        if config.DEBUG:
            print("\n[State] Idle. Waiting for wake word...")

        # Step 1: listen for wake word
        wake_text = listen_for_wake_word()
        print(f"[Wake STT] You said: {wake_text!r}")

        if not wake_text:
            continue

        if text_contains_hotword(wake_text):
            print("[Wake] Hotword detected!")
            kratos_voice.say("Listening.")

            # Step 2: listen for a single command
            cmd_text = listen_for_command()
            print(f"[Cmd STT] You said: {cmd_text!r}")

            if cmd_text:
                kratos_voice.say(f"You said: {cmd_text}")
            else:
                kratos_voice.say("I did not catch that.")

            # Small pause before going back to idle
            sleep(0.5)

        else:
            print("[Wake] No hotword detected. Going back to idle.")


if __name__ == "__main__":
    try:
        kratos_main_loop_simple()
    except KeyboardInterrupt:
        print("\n[Kratos] Shutting down.")
