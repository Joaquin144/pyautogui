import os

from src.logger.config import setup_logger
import pandas as pd

log = setup_logger(__name__)


def save_to_excel(data, path='./data/output/output.xlsx'):
    log.info("Saving data to Excel.....")
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_excel(path)
    log.info("Data saved to Excel.")
