# pip install pyautogui


import pyautogui
import time
import random

print("Mouse mover script started. Press Ctrl+C to stop.")

try:
    while True:
        # Get the current screen size
        screen_width, screen_height = pyautogui.size()

        # Generate random coordinates within the screen boundaries
        new_x = random.randint(0, screen_width)
        new_y = random.randint(0, screen_height)

        # Move the mouse to the new random coordinates
        # The 'duration' argument makes the movement smooth
        pyautogui.moveTo(new_x, new_y, duration=0.5)

        # Wait for 60 seconds (1 minute)
        print(f"Mouse moved to ({new_x}, {new_y}). Waiting for 60 seconds...")
        time.sleep(60)

except KeyboardInterrupt:
    print("\nScript stopped by user.")
