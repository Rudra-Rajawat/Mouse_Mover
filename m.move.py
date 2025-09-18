# pip install pyautogui

import pyautogui
import time
import random

print("Mouse mover script started. Press Ctrl+C to stop.")

try:
    while True:
        # Get the current screen size
        screen_width, screen_height = pyautogui.size()

        # Generate random coordinates, avoiding the corners
        # We use a margin of 10 pixels from the edges
        x_margin = 10
        y_margin = 10
        new_x = random.randint(x_margin, screen_width - x_margin)
        new_y = random.randint(y_margin, screen_height - y_margin)

        # Move the mouse to the new random coordinates
        pyautogui.moveTo(new_x, new_y, duration=0.5)

        # Wait for 60 seconds (1 minute)
        print(f"Mouse moved to ({new_x}, {new_y}). Waiting for 60 seconds...")
        time.sleep(60)

except KeyboardInterrupt:
    print("\nScript stopped by user.")
