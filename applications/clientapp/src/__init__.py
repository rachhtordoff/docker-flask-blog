from flask import Flask
from flask_oauthlib.client import OAuth
from . import general, userarea, loginhandler

app = Flask(__name__)
app.register_blueprint(general.general)
app.register_blueprint(userarea.userarea)
app.register_blueprint(loginhandler.loginhandler)

app.config.from_pyfile("config.py")
