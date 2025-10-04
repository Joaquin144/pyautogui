import time
import webbrowser

from src.logger.config import setup_logger

log = setup_logger(__name__)

log.info("Application started")

webbrowser.open("https://www.google.com")
time.sleep(5)

log.error("Application stopped")
