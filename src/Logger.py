import logging
import os
from datetime import datetime

# Directory for logs
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Ensure the directory exists

# Filename for the log
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Setting up basic configuration for logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s",  # Removed %(names)s
    level=logging.INFO,
)


