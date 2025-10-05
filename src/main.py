import os
from dotenv import load_dotenv

from src.core.start_linkedin_op import run_linkedin_op
from src.logger.config import setup_logger

log = setup_logger(__name__)
load_dotenv()

log.info("Application started")

username = os.getenv("LINKEDIN_EMAIL")
log.info(f"Application running with credentials for : {username}")

run_linkedin_op()

log.error("Application stopped")
