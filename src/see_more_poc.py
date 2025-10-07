import time

from src.core.extract_profile_info import handle_see_more
from src.logger.config import setup_logger

log = setup_logger("see_more_poc")

time.sleep(4)
handle_see_more()

# import pyautogui
#
# screen_width, screen_height = pyautogui.size()
# print("Screen resolution:", screen_width, screen_height)
#
# img = pyautogui.screenshot()
# print("Screenshot size:", img.size)

