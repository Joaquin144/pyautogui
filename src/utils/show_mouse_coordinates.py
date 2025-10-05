import pyautogui
import time

from src.logger.config import setup_logger

log = setup_logger("show_mouse_coordinates")


def show_mouse_coordinates():
    try:
        while True:
            # Get the current mouse position
            x, y = pyautogui.position()
            log.info(f"Mouse Position: X = {x}, Y = {y}")
            time.sleep(0.1)  # Refresh every 0.1 seconds
    except KeyboardInterrupt:
        print("\nExited by user.")


# Call the function to start showing the mouse position
show_mouse_coordinates()
