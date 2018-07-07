from flask import Flask
from .hello import Hello

app = Flask(__name__)


@app.route('/')
@app.route('/<username>')
def hello(hello: Hello, username='Bob'):
    return '%s %s' % (hello.say_hello(), username)
