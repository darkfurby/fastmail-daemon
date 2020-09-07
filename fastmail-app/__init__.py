from flask import Flask
from .config_selenium import sele_exec

app = Flask(__name__, instance_relative_config=True)
emails = []
@app.route('/')
def head():
    return 'Hello, please go to /download to download all mails.'

@app.route('/download')
def download_emails():

    emails = sele_exec()
    return "data downloaded. Now you can go see your all mails on /mailbox"

@app.route('/mailbox')
def mailbox():
    return 
    
