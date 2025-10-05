import time
from logging import exception

from src.logger.config import setup_logger
import pyautogui

log = setup_logger("ui_helpers")


def scroll_until_image_section_found(image_path: str, max_scrolls=20):
    log.info("Scroll until image section found")
    scroll_attempts = 0

    while scroll_attempts < max_scrolls:
        try:
            log.info(f"Attempt {scroll_attempts + 1} of {max_scrolls}...")

            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                log.info(f"Found the 'Image' section at {location}")
                return location
            else:
                log.info("Could not find the 'Image' section. Scrolling down...")

            # Scroll down if not found
            pyautogui.scroll(-10)
            scroll_attempts += 1
        except pyautogui.ImageNotFoundException as e:
            log.error(f"Image not found: {e}")
            pyautogui.scroll(-10)
            scroll_attempts += 1
            continue
        except Exception as e:
            log.error("Some exception occurred while scrolling.", e)
            return None

    log.info("Reached the bottom or could not find the 'Image' section.")
    return None


def scroll_until_image_section_disappears(image_path: str, max_scrolls=20):
    log.info("Scroll until image section disappears")
    scroll_attempts = 0

    while scroll_attempts < max_scrolls:
        try:
            log.info(f"Attempt {scroll_attempts + 1} of {max_scrolls}...")

            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                log.info(f"Found the 'Image' scrolling again {location}")
                pyautogui.scroll(-2)
                scroll_attempts += 1
                continue
            else:
                pyautogui.scroll(2)
                scroll_attempts += 1
                return None

        except pyautogui.ImageNotFoundException as e:
            log.error(f"Image not found: {e}")
            pyautogui.scroll(2)
            scroll_attempts += 1
            return None
        except Exception as e:
            log.error("Some exception occurred while scrolling.", e)
            return None

    log.info("Reached the bottom or could not find the 'Image' section.")
    return None


def scroll_to_top():
    log.info("Scrolling to the top...")

    # You can scroll up in small increments or do it in a loop for a more smooth experience
    for _ in range(10):  # Adjust the number of scrolls if needed
        pyautogui.scroll(200)  # Positive value scrolls up
        time.sleep(0.1)  # Small delay to simulate natural scrolling