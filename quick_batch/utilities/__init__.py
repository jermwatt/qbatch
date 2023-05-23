import os
import sys
import logging

# path to this file's directory and parent directory
file_path = os.path.abspath(__file__)
base_directory = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))

# add to path
sys.path.append(base_directory)

# define paths to each app dockerfile location
processor_path = os.path.join(base_directory, 'quick_batch', 'processor_app')
queue_path = os.path.join(base_directory, 'quick_batch', 'queue_app')


# instantiate progress logger 
from utilities.progress_logger import LogExceptions, Logger
log_exceptions = LogExceptions()

# instantiate logger
logpath = '/Users/wattjer/Desktop/quick_batch/tests/test_data/log_data/logs.txt'

# delete log file if it exists
if os.path.exists(logpath):
    os.remove(logpath)

# instantiate log_exceptions decorator
logger = Logger(logpath)

# Open the log file
logger.open_log()

# Redirect sys.stdout to the logger
sys.stdout = logger
