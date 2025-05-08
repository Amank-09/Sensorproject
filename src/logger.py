# Logging is imp to track events that are happening while any project/software runs
# This helps in debugging and monitoring application behavior

import logging
import os
from datetime import datetime
 
log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs",log_file) # joins current working directory,logs & log_file together.

os.makedirs(logs_path, exist_ok = True)

log_file_path = os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # time in seconds, line no. ka data, name ka data in seconds, levelname in seconds and message in s.
    level = logging.INFO # from this level keep track of all the logging
)