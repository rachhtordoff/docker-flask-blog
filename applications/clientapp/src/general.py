from flask import render_template, url_for, request, session, jsonify, Blueprint

general = Blueprint('general', __name__,
                    template_folder='templates')


@general.route('/')
@general.route('/website')
def website():

    return render_template('index.html',
                           title='Home')
