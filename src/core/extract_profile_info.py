import os
import time

import pyautogui

from src.core.extract_text_from_screenshot import extract_text_from_screenshot
from src.core.ui_helpers import scroll_until_image_section_found, scroll_until_image_section_disappears, scroll_to_top, \
    extract_first_name_prefix, get_end_of_about_region
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
    pyautogui.moveTo(400, 400)
    about_location = scroll_until_image_section_found("./resources/about.png")  # Scroll down to load the About section
    time.sleep(0.1)
    scroll_until_image_section_disappears("./resources/about.png")
    about = ""
    if about_location:
        # left, top, width, height
        handle_see_more()
        end_of_about_location = get_end_of_about_region()
        if end_of_about_location:
            region = (220, 220, 780, int(end_of_about_location.y / 2) - 220 - 10)
        else:
            region = (220, 220, 780, 500)  # About section is very big
        screenshot = pyautogui.screenshot(region=region)
        about_screenshot_path = os.path.join(screenshot_dir, "about_screenshot.png")
        screenshot.save(about_screenshot_path)
        extracted_text = extract_text_from_screenshot(about_screenshot_path)
        lines = extracted_text.split('\n')
        if lines[0].strip().lower() == "about":
            lines = lines[1:]
        about = '\n'.join(lines)

    scroll_to_top()

    experience = ""
    pyautogui.moveTo(600, 600)
    experience_location = scroll_until_image_section_found("./resources/experience.png")
    scroll_until_image_section_disappears("./resources/experience.png")  # workaround for mismatch coordinates
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
    see_more_location = locate_element_with_wait("./resources/see_more.png", timeout_seconds=1, confidence=0.85)
    time.sleep(0.3)
    if see_more_location is not None:
        log.info(f"SeeMore : {see_more_location}")
        x = int(see_more_location.x / 2)
        y = int(see_more_location.y / 2)
        pyautogui.moveTo(x, y)
        time.sleep(0.2)
        pyautogui.click(x, y)
        time.sleep(0.2)
        log.info("clicked on see more")
    else:
        log.info("see more not found")
