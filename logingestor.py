import logging

# Configure logging
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to log messages
def log_message(level, message):
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'success':
        logging.info(message)

# Example usage
log_message('info', 'This is an informational message.')
log_message('error', 'This is an error message.')
log_message('success', 'This is a success message.')
