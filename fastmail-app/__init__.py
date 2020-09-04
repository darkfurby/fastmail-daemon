from flask import Flask
from . import config-selenium

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def hello():
    return 'Hello, World!'