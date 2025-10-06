import os
import time

import pyautogui

from src.core.extract_text_from_screenshot import extract_text_from_screenshot
from src.core.ui_helpers import scroll_until_image_section_found, scroll_until_image_section_disappears, scroll_to_top, \
    extract_first_name_prefix
from src.logger.config import setup_logger
from src.utils.locate_element_with_wait import locate_element_with_wait

log = setup_logger(__name__)


def extract_profile_info(username: str, file_name: str) -> dict:
    log.info(f"Extracting Profile Info : {username}, {file_name}")

    screenshot_dir = f"./temp_screenshots/{username}"
    os.makedirs(screenshot_dir, exist_ok=True)

    time.sleep(3)
    pyautogui.moveTo(600, 600)

    name_region = (186, 457, 464, 50)
    name_screenshot = pyautogui.screenshot(region=name_region)
    name_screenshot_path = os.path.join(screenshot_dir, "name_section_screenshot.png")
    name_screenshot.save(name_screenshot_path)
    extracted_text = extract_text_from_screenshot(name_screenshot_path)
    lines = extracted_text.split('\n')
    full_name = extract_first_name_prefix(lines[0]) if len(lines) > 0 else ""
    log.info(f"Full name for {username} is {full_name}")

    time.sleep(0.5)
    scroll_to_top()
    about_location = scroll_until_image_section_found("./resources/about.png")  # Scroll down to load the About section
    # handle_see_more()
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

    scroll_to_top()

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

    linkedin_username = username

    return {
        "name": full_name,
        "username": linkedin_username,
        "about": about,
        "experience": experience.strip()
    }

def handle_see_more():
    time.sleep(0.5)
    see_more_location = locate_element_with_wait("./resources/see_more.png", timeout_seconds=1)
    time.sleep(0.5)
    if see_more_location is not None:
        pyautogui.moveTo(600, 600)
        pyautogui.click(see_more_location)
        log.info("clicked on see more")
    else:
        log.info("see more not found")
