from flask_injector import FlaskInjector
from injector import Module, singleton
from . import router
from .hello import Hello
from .core import Logger


class InstanceProvider(Module):
    def __init__(self, config, logger):
        # Create all your instances here
        self.__hello = Hello(config, logger)

    def configure(self, binder):
        # Bind your instances here
        binder.bind(Hello, to=self.__hello, scope=singleton)


class Assembly:
    def __init__(self, config):
        self.__config = config
        self.__logger = Logger(self.__config['logger']['level'])
        self.__init_instances()
        self.__init_router()

    def __init_instances(self):
        self.__instance_provider = InstanceProvider(self.__config, self.__logger)

    def __init_router(self):
        self.__app = router.create_router(self.__config, self.__logger)
        self.__app.config['ENV'] = self.__config['flask']['environment']
        self.__app.config['DEBUG'] = self.__config['flask'].getboolean('debug')
        FlaskInjector(app=self.__app, modules=[self.__instance_provider])

    def start(self):
        self.__app.run()

