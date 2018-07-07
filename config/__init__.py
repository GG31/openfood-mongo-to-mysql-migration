import configparser
from os import path
__dir__ = path.dirname(__file__)


def get_config(env):
    if env is None:
        env = 'default'
    file = path.join(__dir__, '%s.ini' % env)
    config = configparser.ConfigParser()
    config.read(file)
    return config
