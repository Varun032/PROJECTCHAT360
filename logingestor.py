import logging

class API1:
    def __init__(self):
        self.logger = logging.getLogger('api1')
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler('log1.log')
        self.logger.addHandler(self.handler)

    def log_message(self, level, message):
        if level == 'info':
            self.logger.info(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'success':
            self.logger.info(message)

class API2:
    def __init__(self):
        self.logger = logging.getLogger('api2')
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler('log2.log')
        self.logger.addHandler(self.handler)

    def log_message(self, level, message):
        if level == 'info':
            self.logger.info(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'success':
            self.logger.info(message)

# Add more API classes as needed

# Example usage
api1 = API1()
api1.log_message('info', 'This is an informational message from API1.')

api2 = API2()
api2.log_message('error', 'This is an error message from API2.')
