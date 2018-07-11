from .router import Router
from .hello import Hello
from .core import Logger


class Assembly:
    def __init__(self, config):
        assert 'logger' in config and 'level' in config['logger'], 'expected logger.level in config'
        self.__config = config
        self.__init_connections()
        self.__init_instances()
        self.__init_router()

    def __init_instances(self):
        self.__logger = Logger(self.__config['logger']['level'])
        self.__hello = Hello(self.__config, self.__logger)
        self.__router = Router(self.__config, self.__logger, self.__hello)

    def __init_connections(self):
        pass

    def __init_router(self):
        self.__app = self.__router.create_router()
        self.__app.config['ENV'] = self.__config['flask']['environment']
        self.__app.config['DEBUG'] = self.__config['flask'].getboolean('debug')

    def start(self):
        self.__app.run()

