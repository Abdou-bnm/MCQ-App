import time
from difficulty_based_timer import DifficultyTimer
# Define test callback functions
def on_tick(remaining_time):
    print(f"Tick: {remaining_time} seconds left")

def on_expire(remaining_time):
    print(f"Timer expired! Time left: {remaining_time} seconds")

def on_warning(remaining_time):
    print(f"Warning! Only {remaining_time} seconds left")

def on_pause(remaining_time):
    print(f"Timer paused with {remaining_time} seconds remaining")

def on_resume(remaining_time):
    print(f"Timer resumed with {remaining_time} seconds remaining")

def on_difficulty_change(remaining_time):
    print(f"Difficulty changed, current remaining time: {remaining_time}")

# Initialize the DifficultyTimer with 'easy' difficulty
timer = DifficultyTimer(difficulty="easy")

# Add callback functions
timer.add_callback('on_tick', on_tick)
timer.add_callback('on_expire', on_expire)
timer.add_callback('on_warning', on_warning)
timer.add_callback('on_pause', on_pause)
timer.add_callback('on_resume', on_resume)
timer.add_callback('on_difficulty_change', on_difficulty_change)

# Start the timer
print(f"Starting the timer with {timer.difficulty.value} difficulty.")
timer.start()

# Simulate timer updates for 10 seconds
for _ in range(10):
    time.sleep(1)
    timer.update()

# Pause the timer
print("\nPausing the timer...")
timer.pause()

# Wait for 2 seconds while the timer is paused
time.sleep(2)

# Resume the timer
print("\nResuming the timer...")
timer.resume()

# Simulate timer updates for another 10 seconds
for _ in range(10):
    time.sleep(1)
    timer.update()

# Change difficulty and reset the timer
print("\nChanging difficulty to 'hard'...")
timer.change_difficulty('hard')

# Start the timer again after changing difficulty
timer.start()

# Simulate the timer running for 15 seconds
for _ in range(15):
    time.sleep(1)
    timer.update()

# Stop the timer
print("\nStopping the timer...")
timer.stop()
