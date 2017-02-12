from src import app, facebook
from flask import render_template, url_for, request, session

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Migueldkkdjl'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True))


@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['logged_in'] = True
    session['oauth_token'] = (resp['access_token'], '')
    me = facebook.get('/me')
    return 'Logged in as id=%s name=%s redirect=%s' % \
        (me.data['id'], me.data['name'], request.args.get('next'))


@facebook.tokengetter
def get_facebook_oauth_token():
    return session.get('oauth_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('oauth_token', None)
    if session.get('oauth_token') is None:
        return "success"
    return "unsuccess"

@app.route("/logout")
def logout():
    logout = pop_login_session()
    return logout
