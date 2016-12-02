from flask import render_template, Blueprint, request, url_for, flash, redirect
from flask_login import login_required, current_user
from app.models import Book, User
from .forms import AddBookForm
from app import db, images

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
	form = AddBookForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			filename = images.save(request.files['book_image'])
			url = images.url(filename)
			new_book = Book(form.title.data, form.isbn.data, current_user.id, True, filename, url)
			db.session.add(new_book)
			db.session.commit()
			flash('New book, {}, added!'.format(new_book.title), 'success')
			return redirect(url_for('book.user_books'))
		else:
			flash_errors(form)
			flash('ERROR! Book was not added.', 'error')

	return render_template('add_book.html', form=form)


@book_blueprint.route('/book/<book_id>')
def book_details(book_id):
    book_with_user = db.session.query(Book, User).join(User).filter(Book.id == book_id).first()
    if book_with_user is not None:
        if book_with_user.Book.is_public:
            return render_template('book_details.html', book=book_with_user)
        else:
            if current_user.is_authenticated and book_with_user.Book.user_id == current_user.id:
                return render_template('book_detail.html', book=book_with_user)
            else:
                flash('Error! Incorrect permissions to access this book.', 'error')
    else:
        flash('Error! Book does not exist.', 'error')
    return redirect(url_for('book.public_books'))
