import platform

import pyautogui

from src.logger.config import setup_logger

log = setup_logger('key_presses')


def focus_address_bar():
    try:
        os_name = platform.system().lower()
        if "darwin" in os_name or "mac" in os_name:
            log.debug("Attempting to focus address bar on macOS")
            pyautogui.hotkey("command", "l")
        else:
            log.debug("Attempting to focus address bar on other OS")
            pyautogui.hotkey("ctrl", "l")
    except Exception as e:
        log.error(f"Failed to focus address bar: {e}")
        raise ValueError('Failed to focus address bar')
