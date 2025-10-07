import os
import time

import pyautogui

from src.core.extract_profile_info import handle_see_more
from src.core.extract_text_from_screenshot import extract_text_from_screenshot
from src.core.ui_helpers import scroll_until_image_section_found, scroll_until_image_section_disappears, \
    get_end_of_about_region
from src.logger.config import setup_logger

log = setup_logger("about_poc")

time.sleep(4)
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
    about_screenshot_path = os.path.join(
        "/Users/zeta/coding/alpha/python_projects/emmarobot_linkedin_assignment/src/temp_screenshots/POC",
        "about_screenshot.png")
    screenshot.save(about_screenshot_path)
    extracted_text = extract_text_from_screenshot(about_screenshot_path)
    lines = extracted_text.split('\n')
    if lines[0].strip().lower() == "about":
        lines = lines[1:]
    about = '\n'.join(lines)

    log.info(f"about is : {about}")
else:
    log.info("no about found")
