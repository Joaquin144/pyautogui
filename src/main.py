import os
import time
import webbrowser

from dotenv import load_dotenv

from src.logger.config import setup_logger

log = setup_logger(__name__)
load_dotenv()

log.info("Application started")

username = os.getenv("LINKEDIN_EMAIL")
log.info(f"Application running with credentials for : {username}")

webbrowser.open("https://www.google.com")
time.sleep(5)

log.error("Application stopped")
