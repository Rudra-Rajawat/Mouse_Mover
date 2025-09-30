# pip install pyautogui

import pyautogui
import time
import random


pyautogui.FAILSAFE = False
print("M mover script started. Press Ctrl+C to stop.")

try:
    while True:
        # Get the current screen size
        screen_width, screen_height = pyautogui.size()

        new_x = random.randint(0, screen_width  )
        new_y = random.randint(0, screen_height )

        # Move the m to the new random coordinates
        pyautogui.moveTo(new_x, new_y, duration=0.5)

        # Wait for 60 seconds (1 minute)
        # print(f"M moved to ({new_x}, {new_y}). Waiting for 10 seconds...")
        time.sleep(60)

except KeyboardInterrupt:
    print("\nScript stopped by user.")
