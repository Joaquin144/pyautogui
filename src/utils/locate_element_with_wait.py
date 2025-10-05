import time

import pyautogui

from src.logger.config import setup_logger

log = setup_logger(__name__)


def locate_element_with_wait(image_path: str, confidence=0.8, timeout_seconds=10, wait_time=0.5):
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        element_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if element_location:
            end_time = time.time()
            log.debug(f"Found element in {end_time - start_time} seconds for {image_path}")
            return element_location
        time.sleep(wait_time)
    return None
