from flask import render_template, Blueprint
from app.models import Book

book_blueprint = Blueprint('book', __name__, template_folder = 'templates')


@book_blueprint.route('/')
def index():
	all_books = Book.query.all()
	return render_template('books.html', books = all_books)
