from flask import render_template, url_for, request, session, jsonify, Blueprint, redirect
from .forms import LoginForm, AccountsetupForm,AccountquestionairreForm


loginhandler = Blueprint('loginhandler', __name__,
                    template_folder='templates')


@loginhandler.route('/login',  methods=['GET'])
def login():
    loginform=LoginForm()
    return render_template('/account/login.html', title='login', loginform=loginform)

@loginhandler.route('/login',  methods=['POST'])
def loginpost():
    loginform=LoginForm()
    session['username']="harry"
    return redirect('/accountsetup')

@loginhandler.route('/accountsetup',  methods=['GET'])
def accountsetup():
    accountsetupform= AccountsetupForm()
    username=session['username']
    return render_template('/account/accountsetup.html', title='Account Setup', username=username, accountsetupform=accountsetupform)

@loginhandler.route('/accountsetup',  methods=['POST'])
def accountsetuppost():

    return redirect('/accountquestionairre')

@loginhandler.route('/accountquestionairre',  methods=['GET'])
def accountquestionairre():
    accountquestionairreForm=AccountquestionairreForm()
    username=session['username']
    return render_template('/account/accountquestionairre.html', title='Account Questionairre', username=username, accountquestionairreForm=accountquestionairreForm)

@loginhandler.route('/accountquestionairre',  methods=['POST'])
def accountquestionairrepost():
    return redirect('/userhomepage')
