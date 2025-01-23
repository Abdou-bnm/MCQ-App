import time
from threading import Thread

class QuizTimer:
    LEVEL_TIMES = {
        "easy": 30,    # 30 seconds
        "medium": 20,  # 20 seconds
        "hard": 10     # 10 seconds
    }

    def __init__(self, level):
        """
        Initialize the timer based on the selected level.
        """
        if level not in self.LEVEL_TIMES:
            raise ValueError("Invalid level! Choose from 'easy', 'medium', or 'hard'.")
        self.duration = self.LEVEL_TIMES[level]
        self.time_up = False  # Flag to indicate if time is up

    def start_timer(self):
        """
        Start the countdown timer in a separate thread.
        """
        self.time_up = False
        thread = Thread(target=self._countdown)
        thread.start()

    def _countdown(self):
        """
        Timer countdown logic.
        """
        time.sleep(self.duration)
        self.time_up = True

    def is_time_up(self):
        """
        Check whether the timer has expired.
        """
        return self.time_up