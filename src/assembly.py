from flask_injector import FlaskInjector
from injector import Module, singleton
from .router import app
from .hello import Hello


class InstanceProvider(Module):
    def __init__(self, config):
        # Create all your instances here
        self.__hello = Hello(config)

    def configure(self, binder):
        # Bind your instances here
        binder.bind(Hello, to=self.__hello, scope=singleton)

class Assembly:
    def __init__(self, config):
        self.__config = config
        self.__config_flask()

    def __config_flask(self):
        app.config['ENV'] = self.__config['flask']['environment']
        app.config['DEBUG'] = self.__config['flask'].getboolean('debug')

    def start(self):
        instance_provider = InstanceProvider(self.__config)
        FlaskInjector(app=app, modules=[instance_provider])
        app.run()

