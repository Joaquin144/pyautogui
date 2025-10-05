import time

import pyautogui

from src.logger.config import setup_logger
from src.utils.locate_element_with_wait import locate_element_with_wait

log = setup_logger("handle_login")


def handle_login_with_image():
    time.sleep(3)
    pyautogui.moveTo(600, 600)
    sso_point = locate_element_with_wait("./resources/login_sso.png")
    if sso_point is not None:
        log.info(f"Found login sso at {sso_point}")
        pyautogui.click(sso_point)
        email_sso_point = locate_element_with_wait("./resources/login_sso_email.png")
        if email_sso_point is not None:
            log.info(f"Found login sso email at {email_sso_point}")
            pyautogui.click(email_sso_point)
        else:
            log.error("unexpected state occurred")
    else:  # could be more better check
        log.info("No login sso found. Skipping login step")


def handle_login_with_coordinates():
    time.sleep(3)
    pyautogui.moveTo(600, 600)
    pyautogui.click(349, 412)
    time.sleep(2)
    pyautogui.moveTo(600, 600)
    pyautogui.click(674, 474)
    time.sleep(4)