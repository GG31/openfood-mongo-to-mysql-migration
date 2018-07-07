import pytest
from flask_injector import FlaskInjector
from injector import singleton

from .router import app, Hello

class HelloMock:
    def __init__(self, config):
        pass
    def say_hello(self):
        return 'Hi'

@pytest.fixture(autouse=True)
def client():
    app.config['TESTING'] = True
    app_client = app.test_client()
    return app_client

def setup_function():
    def configure(binder):
        binder.bind(Hello, to=HelloMock('test'), scope=singleton)
    FlaskInjector(app=app, modules=[configure])


def test_call_hello(client):
    result = client.get('/')
    assert result.data == b'Hi Bob'

def test_call_hello_with_username(client):
    result = client.get('/Alice')
    assert result.data == b'Hi Alice'


