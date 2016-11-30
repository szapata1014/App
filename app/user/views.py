from flask import render_template, Blueprint

user_blueprint = Blueprint('user', __name__, template_forlder='templates')

@user_blueprint.route('/login')
def login():
	return render_template('login.html')
