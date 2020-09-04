from flask import Flask
from .config_selenium import sele_exec

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def hello():
    return 'Hello, World!'