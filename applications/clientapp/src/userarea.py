from flask import render_template, url_for, request, session, jsonify, Blueprint

userarea = Blueprint('userarea', __name__,
                    template_folder='templates')

@userarea.route('/userhomepage',  methods=['GET'])
def userhomepage():
    username=session['username']
    return render_template('/user/userhomepage.html', title='Homepage', username=username)
