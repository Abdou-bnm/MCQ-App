from enum import Enum
from datetime import datetime, timedelta
import time
from typing import Dict, Optional

class TimerState(Enum):
    """Enum representing the possible states of the timer."""
    RUNNING = "running"  # Timer is actively counting down
    PAUSED = "paused"   # Timer is temporarily halted
    STOPPED = "stopped"   # Timer is temporarily halted
    EXPIRED = "expired"  # Time has run out

class DifficultyLevel(Enum):
    """Enum representing the difficulty levels for the timer."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class DifficultyTimer:
    """
    A timer class that counts down based on the selected difficulty level 
    (easy, medium, hard). It supports pausing, resuming, and resetting the timer, 
    and can trigger custom callbacks at specific events like time ticking, warning, 
    and expiration.
    Attributes:
        difficulty (DifficultyLevel): The current difficulty level of the timer.
        time_limits (dict): A dictionary mapping each difficulty level to its corresponding time limit.
        warning_thresholds (dict): A dictionary mapping each difficulty level to its warning threshold time.
        duration (int): The total time duration for the timer in seconds.
        remaining_time (int): The remaining time on the timer in seconds.
        state (TimerState): The current state of the timer (running, paused, stopped, expired).
        start_time (datetime): The start time of the timer.
        pause_time (float): The time when the timer was paused.
        callbacks (dict): A dictionary of callback functions that are triggered during specific events.

    Methods:
        change_difficulty(new_difficulty: str): Change the difficulty level and reset the timer.
        start(): Start or resume the timer.
        pause(): Pause the timer.
        resume(): Resume the timer from a paused state.
        stop(): Stop the timer and reset the remaining time.
        reset(): Reset the timer to its initial state and start it again.
        update(): Update the timer's state and remaining time, triggering appropriate callbacks.
        add_callback(event: str, callback): Add a callback function for a specific event.
        _trigger_callbacks(event: str): Trigger all callbacks associated with an event.
        time_left: Property that returns the remaining time in seconds.
        is_running: Property that checks if the timer is currently running.
        is_warning: Property that checks if the timer is in a warning state.
        get_formatted_time(): Get the remaining time as a formatted string (MM:SS).
        get_progress_percentage(): Get the progress as a percentage of completion (0-100%).
    """
   
    # Default time limits for each difficulty (in seconds)
    DEFAULT_TIME_LIMITS = {
        DifficultyLevel.EASY: 25,
        DifficultyLevel.MEDIUM: 20,
        DifficultyLevel.HARD: 15
    }

    # Warning thresholds for each difficulty (in seconds)
    DEFAULT_WARNING_THRESHOLDS = {
        DifficultyLevel.EASY: 8,
        DifficultyLevel.MEDIUM: 12,
        DifficultyLevel.HARD: 15
    }

    def __init__(self, 
                 difficulty: str = "easy",
                 custom_time_limits: Optional[Dict] = None,
                 custom_warning_thresholds: Optional[Dict] = None):
        """
        Initialize timer with difficulty-based settings
        
        Args:
            difficulty: Difficulty level ('easy', 'medium', 'hard')
            custom_time_limits: Optional custom time limits for each difficulty
            custom_warning_thresholds: Optional custom warning thresholds
        """
        self.difficulty = DifficultyLevel(difficulty.lower())
        
        # Set time limits (use custom if provided, otherwise defaults)
        self.time_limits = custom_time_limits or self.DEFAULT_TIME_LIMITS
        self.warning_thresholds = custom_warning_thresholds or self.DEFAULT_WARNING_THRESHOLDS
        
        # Initialize timer state
        self.duration = self.time_limits[self.difficulty]
        self.warning_threshold = self.warning_thresholds[self.difficulty]
        self.remaining_time = self.duration
        self.state = TimerState.STOPPED
        self.start_time = None
        self.pause_time = None
        
        # Initialize callbacks for events
        self.callbacks = {
            'on_tick': [],
            'on_expire': [],
            'on_warning': [],
            'on_pause': [],
            'on_resume': [],
            'on_difficulty_change': []
        }
    
    def change_difficulty(self, new_difficulty: str):
        """Change difficulty level and reset timer
        Args:
            new_difficulty (str): The new difficulty level ('easy', 'medium', 'hard').
        """
        self.difficulty = DifficultyLevel(new_difficulty.lower())
        self.duration = self.time_limits[self.difficulty]
        self.warning_threshold = self.warning_thresholds[self.difficulty]
        self.reset()
        self._trigger_callbacks('on_difficulty_change')

    def start(self):
        """
        Start or resume the timer. If the timer is paused, it adjusts for the paused time.
        """
        if self.state == TimerState.PAUSED:
            elapsed_pause = time.time() - self.pause_time
            self.start_time += timedelta(seconds=elapsed_pause)
        else:
            self.start_time = datetime.now()
            self.remaining_time = self.duration
        
        self.state = TimerState.RUNNING

    def pause(self):
        """
        Pause the timer. The current time is saved so it can be resumed later.

        """
        if self.state == TimerState.RUNNING:
            self.state = TimerState.PAUSED
            self.pause_time = time.time()
            self._trigger_callbacks('on_pause')

    def resume(self):
        """Resume the timer"""
        if self.state == TimerState.PAUSED:
            self.start()
            self._trigger_callbacks('on_resume')

    def stop(self):
        """Stop the timer and reset the remaining time to its original value"""
        self.state = TimerState.STOPPED
        self.remaining_time = self.duration

    def reset(self):
        """Reset the timer to initial state"""
        self.stop()
        self.start()

    def update(self):
        """Update timer state and remaining time"""
        if self.state != TimerState.RUNNING:
            return

        elapsed = (datetime.now() - self.start_time).total_seconds()
        self.remaining_time = max(0, self.duration - elapsed)

        # Check for warning threshold
        if self.remaining_time <= self.warning_threshold:
            self._trigger_callbacks('on_warning')

        # Check for expiration
        if self.remaining_time <= 0:
            self.state = TimerState.EXPIRED
            self._trigger_callbacks('on_expire')
            return

        self._trigger_callbacks('on_tick')

    def add_callback(self, event: str, callback):
        """
        Add a callback function for a specific event.
        
        Args:
            event (str): The event to listen for (e.g., 'on_tick', 'on_warning').
            callback (function): The function to call when the event occurs.
        """
        if event in self.callbacks:
            self.callbacks[event].append(callback)

        """
        Trigger all callbacks associated with a specific event.
        
        Args:
            event (str): The event to trigger (e.g., 'on_tick', 'on_warning').
        """
        for callback in self.callbacks[event]:
            callback(self.remaining_time)
    def _trigger_callbacks(self, event: str):
        """Trigger all callbacks associated with a specific event."""
        for callback in self.callbacks.get(event, []):
            callback(self.remaining_time)
    @property
    def time_left(self) -> int:
        """Get remaining time in seconds"""
        return round(self.remaining_time)

    @property
    def is_running(self) -> bool:
        """Check if timer is currently running"""
        return self.state == TimerState.RUNNING

    @property
    def is_warning(self) -> bool:
        """Check if timer is in warning state"""
        return self.remaining_time <= self.warning_threshold

    def get_formatted_time(self) -> str:
        """
        Get the formatted time as a string (MM:SS).
        
        Returns:
            str: The remaining time formatted as MM:SS (e.g., '05:30').
        """
        minutes = int(self.remaining_time // 60)
        seconds = int(self.remaining_time % 60)
        return f"{minutes:02d}:{seconds:02d}"

    def get_progress_percentage(self) -> float:
        """
        Get the progress of the timer as a percentage (0 to 100).
        
        Returns:
            float: The progress of the timer (percentage).
        """
        return (self.remaining_time / self.duration) * 100