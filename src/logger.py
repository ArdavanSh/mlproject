import logging
import os
from datetime import datetime

# Create a log filename with the current date
log_filename = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, log_filename)

# Set up logging configuration
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


