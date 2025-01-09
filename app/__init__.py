import logging
import os,sys
from datetime import datetime
dir_path = os.path.join(os.getcwd(),"logs")
os.makedirs(dir_path, exist_ok=True)
logger = logging.getLogger("DataSyncLogger")

logger.setLevel(logging.INFO)
date_str = datetime.now().strftime('%Y%m%d')
log_filename = os.path.join(dir_path, f"{date_str}_one-drive-to-db.log")
file_handler = logging.FileHandler(log_filename, mode='a')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

def log_uncaught_exception(exc_type, exc_value, exc_tb):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_tb)
    else:
        logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_tb))

sys.excepthook = log_uncaught_exception