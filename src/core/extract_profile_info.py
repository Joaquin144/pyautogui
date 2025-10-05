import os
import time

import pyautogui

from src.core.extract_text_from_screenshot import extract_text_from_screenshot
from src.logger.config import setup_logger

log = setup_logger(__name__)


def extract_profile_info(username: str, file_name: str) -> dict:
    log.info(f"Extracting Profile Info : {username}, {file_name}")

    screenshot_dir = f"./temp_screenshots/{username}"
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_path = os.path.join(screenshot_dir, file_name)

    time.sleep(3)
    pyautogui.moveTo(600, 600)  # Move to neutral position
    pyautogui.scroll(-1000)  # Scroll down to load About section
    time.sleep(2)

    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    log.info(f"Screenshot saved at : {screenshot_path}")

    extracted_text = extract_text_from_screenshot(screenshot_path)
    log.debug(f"OCR Text:\n{extracted_text}")

    name = username
    about = ""
    experience = ""

    for line in extracted_text.splitlines():
        if "subscribers" in line.lower():
            experience += line.strip() + " "
        elif "videos" in line.lower():
            experience += line.strip()
        elif not about and len(line.strip()) > 30:
            about = line.strip()

    return {
        "username": name,
        "about": about,
        "experience": experience.strip()
    }
