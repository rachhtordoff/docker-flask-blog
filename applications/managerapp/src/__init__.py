from flask import Flask
from flask_oauthlib.client import OAuth

app = Flask(__name__)


SECRET_KEY = 'development key'
DEBUG = True
FACEBOOK_APP_ID = '1239932412696644'
FACEBOOK_APP_SECRET = 'be4160f4485e2e1a9cb3e226cf801f3b'

app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()


facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)
from src import views
