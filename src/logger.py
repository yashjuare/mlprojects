import logging
import os
from datetime import datetime

# Define the log file name and path
LOG_FILE = f"{datetime.now().strftime('%m_5d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Corrected here
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)  # Corrected to use logs_dir

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

