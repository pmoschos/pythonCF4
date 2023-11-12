import logging

log_file = 'cf4.log'

# Create a filehandler for logging a file
# Default mode: 'a' which mean append
file_handler = logging.FileHandler(log_file, mode='a')

# Create a list of handlers for the logger
handlers = [file_handler]

# Name of the Logger
logger = logging.getLogger('search-app')

# Confige the root logger with the handlers list
logging.basicConfig(handlers=handlers, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

nums = [1, 2, 3, 4, 5]
num_to_find = 20

try:
    index = nums.index(num_to_find)
    print('Found!')
except ValueError as e:
    logger.error(f"{e}", exc_info=True)