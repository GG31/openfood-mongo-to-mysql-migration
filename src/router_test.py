import pytest
from unittest.mock import MagicMock

from .router import Router
from .core import Logger
import config

test_config = config.get_config('test')


class HelloMock:
    def __init__(self, config):
        pass
    def say_hello(self):
        return 'Hi'


@pytest.fixture(autouse=True)
def client():
    hello_mock = MagicMock()
    hello_mock.say_hello = MagicMock(return_value='Hi')
    router = Router(test_config, Logger('DEBUG'), hello=hello_mock, migration=MagicMock())
    app = router.create_router()
    app.config['TESTING'] = True

    app_client = app.test_client()
    return app_client


def test_call_hello(client):
    result = client.get('/')
    assert result.data == b'Hi Bob'


def test_call_hello_with_username(client):
    result = client.get('/Alice')
    assert result.data == b'Hi Alice'



