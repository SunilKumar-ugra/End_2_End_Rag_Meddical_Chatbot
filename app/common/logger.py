import logging
import os
from datetime import datetime
import sys

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    format="[%(asctime)s] - %(levelname)s \nFile    : [%(module)s] File \nLineNum : %(lineno)d - %(name)s \nMessage : %(message)s \n-----------------------",
    level=logging.INFO,
     handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger