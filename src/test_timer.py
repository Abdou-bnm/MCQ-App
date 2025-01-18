import time
import os
import sys
from Logic.difficulty_based_timer import DifficultyTimer

# Create a timer instance with the default difficulty (easy)
timer = DifficultyTimer(difficulty="easy")

# Start the timer
timer.start()
print(f"Timer started with duration: {timer.duration} seconds")

# Wait for a few seconds and update the timer
time.sleep(2)
timer.update()
print(f"Time left after 2 seconds: {timer.time_left} seconds")

# Check if the timer is running
print(f"Is timer running? {timer.is_running}")

# Pause the timer
timer.pause()
print(f"Timer paused at: {timer.time_left} seconds")

# Wait and then resume the timer
time.sleep(1)
timer.resume()
print("Timer resumed.")

# Wait until the timer reaches the warning threshold
while timer.remaining_time > timer.warning_threshold:
    time.sleep(1)
    timer.update()
    print(f"Time left: {timer.time_left} seconds")

# Verify if it's in the warning state
print(f"Is timer in warning state? {timer.is_warning}")

# Wait for the timer to expire
while timer.remaining_time > 0:
    time.sleep(1)
    timer.update()

print(f"Timer expired. Final state: {timer.state}")
