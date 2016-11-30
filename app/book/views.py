from flask import render_template, Blueprint, request, url_for, flash, redirect
from app.models import Book
from .forms import AddBookForm
from app import db

book_blueprint = Blueprint('book', __name__, template_folder = 'templates')

def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), 'info')


@book_blueprint.route('/')
def index():
	all_books = Book.query.all()
	return render_template('books.html', books = all_books)

@book_blueprint.route('/add', methods=['GET', 'POST'])
def add_book():
	form = AddBookForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			new_book = Book(form.title.data, form.isbn.data)
			db.session.add(new_book)
			db.session.commit()
			flash('New book, {}, added!'.format(new_book.title), 'success')
			return redirect(url_for('book.index'))
		else:
			flash_errors(form)
			flash('ERROR! Book was not added.', 'error')

	return render_template('add_book.html', form=form)
