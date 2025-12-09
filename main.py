# main.py

from time import sleep

from core import config
from core.state import app_state, Mode

from kratos_io.speech_output import kratos_voice
from kratos_io.speech_input import listen_once


def demo_state_flow():
    print("=== Kratos demo start ===")
    print(f"Initial mode: {app_state.mode}")
    print(f"Initially listening? {app_state.listening}")

    # Simulate saying "Kratos"
    print("\n[Simulating: you say 'Kratos']")
    app_state.start_listening()
    print(f"Listening? {app_state.listening}")
    print(f"Last activity: {app_state.last_activity}")

    # Simulate switching to dictation mode
    print("\n[Simulating: you say 'start dictation']")
    app_state.set_mode(Mode.DICTATION)
    print(f"Current mode: {app_state.mode}")

    # Wait a bit to test timeout logic
    print(f"\nWaiting for {config.LISTEN_TIMEOUT_SECONDS + 2} seconds to test timeout...")
    sleep(config.LISTEN_TIMEOUT_SECONDS + 2)

    if app_state.should_timeout(config.LISTEN_TIMEOUT_SECONDS):
        print("Timeout reached. Kratos should stop listening now.")
        app_state.stop_listening()

    print(f"Listening after timeout? {app_state.listening}")
    print("=== Kratos demo end ===")

if __name__ == "__main__":
    demo_state_flow()
    print("\nTesting Kratos voice…")
    kratos_voice.say("Kratos is online.")

    print(f"You said: {text}")
    kratos_voice.say(f"You said {text}")
