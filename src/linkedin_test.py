import pyautogui
from dotenv import load_dotenv

from src.core.extract_profile_info import extract_profile_info
from src.core.handle_login import handle_login_with_image
from src.core.start_linkedin_op import generate_search_url_for_username, open_linkedin
from src.logger.config import setup_logger
from src.utils.key_presses import focus_address_bar

log = setup_logger("linkedin_test")
load_dotenv()

log.info("POC started")

# open LinkedIn
open_linkedin()

# username = "aniketkagarwal"
# username = "someetsingh"
username = "vibhu"

search_url = generate_search_url_for_username(username)
focus_address_bar()
log.debug(f'searching : {search_url}')
pyautogui.write(search_url)
pyautogui.press("enter")

log.info(extract_profile_info(username, "info.png"))

log.error("POC done")
