import time
import webbrowser

import pyautogui

from src.core.extract_profile_info import extract_profile_info
from src.core.handle_login import handle_login
from src.core.save_to_excel import save_to_excel
from src.logger.config import setup_logger
from src.utils import app_constants
from src.utils.key_presses import focus_address_bar

log = setup_logger(__name__)
input_file_path = './data/input/usernames.txt'


def run_linkedin_op():
    open_linkedin()
    # todo : Login into LinkedIn and wait till success
    handle_login()

    usernames = read_usernames()
    extracted_profile_data = []

    for username in usernames:
        focus_address_bar()
        search_url = generate_search_url_for_username(username)
        log.debug(f'searching : {search_url}')
        pyautogui.write(search_url)
        pyautogui.press("enter")

        profile_info = extract_profile_info(username, "info.png")
        extracted_profile_data.append(profile_info)
        time.sleep(5)

    save_to_excel(extracted_profile_data)


def open_linkedin():
    log.info("Opening LinkedIn.....")
    webbrowser.open(app_constants.website_url)
    time.sleep(2)


def read_usernames() -> list[str]:
    usernames = []
    with open(input_file_path, 'r') as file:
        for line in file:
            usernames.append(line.strip())

    return usernames


def generate_search_url_for_username(username: str) -> str:
    result_url = app_constants.base_url_search_prefix + username + "/"
    log.debug(f"generated url for : {username} is : {result_url}")
    return result_url
