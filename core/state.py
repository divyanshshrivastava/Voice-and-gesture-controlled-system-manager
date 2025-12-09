# core/state.py

"""
Holds the global state for Kratos.

This is where we remember:
- which mode Kratos is in (command vs dictation)
- whether he's currently listening for commands
- whether only the owner's voice is allowed
- when the last activity happened (for timeout logic)
"""

from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import Optional


class Mode(Enum):
    """Kratos' high-level operating modes."""
    COMMAND = "command"    # Normal command mode: "minimize", "open chrome" etc.
    DICTATION = "dictation"  # Typing whatever you say into the active window


@dataclass
class AppState:
    """
    Represents the current state of Kratos.

    This is a single object we can pass around, so all parts of the system
    (orchestrator, input, skills) see the same up-to-date state.
    """

    mode: Mode = Mode.COMMAND

    # Is Kratos actively listening for commands right now
    # (after you've said "Kratos")?
    listening: bool = False

    # When was the last time Kratos processed a command or heard you say something
    # relevant while listening?
    last_activity: Optional[datetime] = None

    # Security-related flags (for the "only my voice" behaviour)
    owner_lock_enabled: bool = True        # if True, only the owner is allowed
    allow_other_speakers: bool = False     # if True, others can give commands too

    def set_mode(self, new_mode: Mode) -> None:
        """Change Kratos' mode (e.g., COMMAND -> DICTATION)."""
        self.mode = new_mode
        self.mark_activity()

    def start_listening(self) -> None:
        """Put Kratos into active listening state."""
        self.listening = True
        self.mark_activity()

    def stop_listening(self) -> None:
        """Stop active listening (back to idle)."""
        self.listening = False

    def mark_activity(self) -> None:
        """Record that something just happened (used for timeout checks)."""
        self.last_activity = datetime.now()

    def should_timeout(self, timeout_seconds: int) -> bool:
        """
        Returns True if Kratos has been listening for longer than
        'timeout_seconds' since the last activity.
        """
        if not self.listening:
            return False

        if self.last_activity is None:
            return False

        delta = datetime.now() - self.last_activity
        return delta.total_seconds() > timeout_seconds


# Create a single, shared AppState instance for the whole app.
# Other modules can import this as:
#   from core.state import app_state
app_state = AppState()
