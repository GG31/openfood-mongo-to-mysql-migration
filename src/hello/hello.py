

class Hello:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger.get_logger(__name__)

    def say_hello(self):
        self.logger.debug('logger works')
        return 'Hello'
