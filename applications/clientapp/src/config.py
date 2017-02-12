import os

DEBUG = True

OAUTH_API = os.getenv('OAUTH_API_ADDRESS',
                               'http://oauth.local')
WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ['SECRET_KEY']
