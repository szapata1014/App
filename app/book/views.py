from flask import render_template, Blueprint, request, url_for, flash, redirect
from flask_login import login_required, current_user
from app.models import Book
from .forms import AddBookForm
from app import db

book_blueprint = Blueprint('book', __name__)

def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), 'info')


@book_blueprint.route('/')
def public_books():
	all_public_books = Book.query.filter_by(is_public=True)
	return render_template('public_books.html', public_books = all_public_books)

@book_blueprint.route('/books')
@login_required
def user_books():
	all_user_books = Book.query.filter_by(user_id = current_user.id)
	return render_template('user_books.html', user_books = all_user_books)

@book_blueprint.route('/add', methods=['GET', 'POST'])
def add_book():
	form = AddBookForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			new_book = Book(form.title.data, form.isbn.data, current_user.id, True)
			db.session.add(new_book)
			db.session.commit()
			flash('New book, {}, added!'.format(new_book.title), 'success')
			return redirect(url_for('book.user_books'))
		else:
			flash_errors(form)
			flash('ERROR! Book was not added.', 'error')

	return render_template('add_book.html', form=form)
