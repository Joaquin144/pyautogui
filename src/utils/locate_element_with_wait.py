import time

import pyautogui

from src.logger.config import setup_logger

log = setup_logger("locate_element_with_wait")


def locate_element_with_wait(image_path: str, confidence=0.8, timeout_seconds=5, wait_time=0.5):
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        try:
            element_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if element_location:
                end_time = time.time()
                log.debug(f"Found element in {end_time - start_time} seconds for {image_path}")
                return element_location
            time.sleep(wait_time)
        except pyautogui.ImageNotFoundException as e:
            log.error(f"Image not found : {e}")
            pyautogui.scroll(-10)
            continue
    return None
