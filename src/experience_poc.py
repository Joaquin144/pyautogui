import os
import time

import pyautogui

from src.core.extract_text_from_screenshot import extract_text_from_screenshot
from src.core.ui_helpers import scroll_until_image_section_found, scroll_until_image_section_disappears

time.sleep(4)
pyautogui.moveTo(400, 400)
experience_location = scroll_until_image_section_found("./resources/experience.png")
time.sleep(0.1)
scroll_until_image_section_disappears("./resources/experience.png")  # workaround for mismatch coordinates
experience = ""
if experience_location:
    region = (218, 230, 800, 350)
    screenshot = pyautogui.screenshot(region=region)
    experience_screenshot_path = os.path.join("/Users/zeta/coding/alpha/python_projects/emmarobot_linkedin_assignment/src/temp_screenshots/POC", "experience_screenshot.png")
    screenshot.save(experience_screenshot_path)
    extracted_text = extract_text_from_screenshot(experience_screenshot_path)
    lines = extracted_text.split('\n')
    if lines[0].strip().lower() == "experience":
        lines = lines[1:]
    if lines and "show all" in lines[-1].strip().lower():
        lines = lines[:-1]
    experience = '\n'.join(lines)