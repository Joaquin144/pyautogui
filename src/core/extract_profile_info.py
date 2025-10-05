import os
import time

import pyautogui

from src.core.extract_text_from_screenshot import extract_text_from_screenshot
from src.core.ui_helpers import scroll_until_image_section_found, scroll_until_image_section_disappears
from src.logger.config import setup_logger

log = setup_logger(__name__)


def extract_profile_info(username: str, file_name: str) -> dict:
    log.info(f"Extracting Profile Info : {username}, {file_name}")

    screenshot_dir = f"./temp_screenshots/{username}"
    os.makedirs(screenshot_dir, exist_ok=True)

    time.sleep(3)
    pyautogui.moveTo(600, 600)
    about_location = scroll_until_image_section_found("./resources/about.png")  # Scroll down to load the About section
    scroll_until_image_section_disappears("./resources/about.png")
    about = ""
    if about_location:
        # region = (about_location[0] - 100, about_location[1] - 50, about_location[0] + 600, about_location[1] + 250)
        # left, top, width, height
        region = (220, 230, 780, 150)
        screenshot = pyautogui.screenshot(region=region)
        about_screenshot_path = os.path.join(screenshot_dir, "about_screenshot.png")
        screenshot.save(about_screenshot_path)
        extracted_text = extract_text_from_screenshot(about_screenshot_path)
        lines = extracted_text.split('\n')
        if lines[0].strip().lower() == "about":
            lines = lines[1:]
        if lines and "see more" in lines[-1].strip().lower():
            lines = lines[:-1]
        about = '\n'.join(lines)

    experience = ""
    pyautogui.moveTo(600, 600)
    experience_location = scroll_until_image_section_found("./resources/experience.png")
    scroll_until_image_section_disappears("./resources/experience.png") # workaround for mismatch coordinates
    if experience_location:
        region = (218, 230, 800, 350)
        screenshot = pyautogui.screenshot(region=region)
        experience_screenshot_path = os.path.join(screenshot_dir, "experience_screenshot.png")
        screenshot.save(experience_screenshot_path)
        extracted_text = extract_text_from_screenshot(experience_screenshot_path)
        lines = extracted_text.split('\n')
        if lines[0].strip().lower() == "experience":
            lines = lines[1:]
        if lines and "show all" in lines[-1].strip().lower():
            lines = lines[:-1]
        experience = '\n'.join(lines)

    name = username

    return {
        "username": name,
        "about": about,
        "experience": experience.strip()
    }
