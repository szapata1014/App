
from flask import render_template, Blueprint

book_blueprint = Blueprint('book', __name__, template_folder = 'templates')


@book_blueprint.route('/')
def index():
	return render_template('index.html')
