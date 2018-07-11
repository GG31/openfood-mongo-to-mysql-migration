from flask import Flask


class Router:
    def __init__(self, config, logger, hello):
        self.__config = config
        self.__logger = logger.get_logger(__name__)
        self.__hello = hello

    def create_router(self):
        this = self
        app = Flask(self.__config['project']['name'])

        @app.route('/')
        @app.route('/<username>')
        def hello(username='Bob'):
            this.__logger.info('/ called')
            return '%s %s' % (this.__hello.say_hello(), username)

        return app
