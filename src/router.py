from flask import Flask
from .hello import Hello


def create_router(config, logger):
    app = Flask(config['project']['name'])
    logger = logger.get_logger(__name__)

    @app.route('/')
    @app.route('/<username>')
    def hello(hello: Hello, username='Bob'):
        logger.info('/ called')
        return '%s %s' % (hello.say_hello(), username)
    return app
