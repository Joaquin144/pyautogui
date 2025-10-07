import os
import time

import pyautogui

from src.core.extract_text_from_screenshot import extract_text_from_screenshot
from src.core.ui_helpers import extract_first_name_prefix
from src.logger.config import setup_logger



log = setup_logger("name_poc")

time.sleep(1)
pyautogui.moveTo(400, 400)
time.sleep(2)
name_region = (186, 457, 464, 50)
name_screenshot = pyautogui.screenshot(region=name_region)
name_screenshot_path = os.path.join("/Users/zeta/coding/alpha/python_projects/emmarobot_linkedin_assignment/src/temp_screenshots/POC", "name_section_screenshot.png")
name_screenshot.save(name_screenshot_path)
extracted_text = extract_text_from_screenshot(name_screenshot_path)
lines = extracted_text.split('\n')
full_name = extract_first_name_prefix(lines[0]) if len(lines) > 0 else ""
log.info(f"Full name for user is {full_name}")
