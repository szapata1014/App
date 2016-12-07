from flask import render_template, Blueprint, request, url_for, flash, redirect, g
from flask_login import login_required, current_user
from app.models import Book, User, BookSearch
from .forms import AddBookForm, SearchBookForm, AddBookFromSearch
from app import db, images
from threading import Thread
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
from app import app, mail
MAX_SEARCH_RESULTS = 20

book_blueprint = Blueprint('book', __name__)

def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), 'info')

def send_async_email(msg):
	with app.app_context():
		mail.send(msg)

def send_email(subject, recipients, html_body):
	msg = Message(subject, recipients=recipients)
	msg.html = html_body
	thr = Thread(target=send_async_email, args=[msg])
	thr.start()	

def send_request_email(requesting_user_email, book_owner_email, book):
	confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
	confirm_url = url_for('book.confirm_request',book=book, token=confirm_serializer.dumps(requesting_user_email, salt='email-confirmation-salt'), token2=confirm_serializer.dumps(book_owner_email, salt='email-confirmation-salt'),
        _external=True)

	deny_url = url_for('book.deny_request',book=book, token=confirm_serializer.dumps(requesting_user_email, salt='email-confirmation-salt'), token2=confirm_serializer.dumps(book_owner_email, salt='email-confirmation-salt'),
        _external=True)
    
	html = render_template('email_request_book.html',requesting_user_email=requesting_user_email, book=book, confirm_url=confirm_url, deny_url=deny_url)
    
	send_email('Someone wants your book!', [book_owner_email], html)

def send_confirm_email(requesting_user_email, book_owner_email, book):
	html = render_template('email_confirm_request.html', book_owner_email=book_owner_email, book=book)
    
	send_email("There's a book coming your way!", [requesting_user_email], html)

def send_deny_email(requesting_user_email, book_owner_email, book):
	html = render_template('email_deny_request.html', book_owner_email=book_owner_email, book=book)
    
	send_email("Sorry, the book you want can't be sent.", [requesting_user_email], html)

@book_blueprint.route('/request_book/<book>/<rUser>/<bUser>', methods=['POST'])
def request_book(book, rUser, bUser):
	send_request_email(rUser, bUser, book)
	flash('Requesting book, {}!'.format(book), 'success')
	return redirect(url_for('book.user_books'))

@book_blueprint.route('/confirm_request/<book>/<token>/<token2>')
def confirm_request(book, token, token2):
	confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
	requesting_user_email = confirm_serializer.loads(token, salt='email-confirmation-salt')
	book_owner_email = confirm_serializer.loads(token2, salt='email-confirmation-salt')
	send_confirm_email(requesting_user_email, book_owner_email, book)
	return redirect(url_for('book.home'))

@book_blueprint.route('/deny_request/<book>/<token>/<token2>')
def deny_request(book,token, token2):
	confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
	requesting_user_email = confirm_serializer.loads(token, salt='email-confirmation-salt')
	book_owner_email = confirm_serializer.loads(token2, salt='email-confirmation-salt')
	send_deny_email(requesting_user_email, book_owner_email, book)
	return redirect(url_for('book.home'))	


@book_blueprint.before_request
def before_request():
    g.searchform = SearchBookForm()

@book_blueprint.route('/')
def home():
	return render_template('landingpage.html')


@book_blueprint.route('/public_books')
@login_required
def public_books():
	all_public_books = Book.query.filter_by(is_public=True)
	return render_template('public_books.html', public_books = all_public_books)

@book_blueprint.route('/books')
@login_required
def user_books():
	all_user_books = Book.query.filter_by(user_id = current_user.id)
	return render_template('user_books.html', user_books = all_user_books)

#@book_blueprint.route('/add', methods=['GET', 'POST'])
#def add_book():
#	form = AddBookForm()
#	if request.method == 'POST':
#		if form.validate_on_submit():
#			filename = images.save(request.files['book_image'])
#			url = images.url(filename)
#			new_book = Book(form.title.data, form.isbn.data, current_user.id, True, filename, url)
#			db.session.add(new_book)
#			db.session.commit()
#			flash('New book, {}, added!'.format(new_book.title), 'success')
#			return redirect(url_for('book.user_books'))
#		else:
#			flash_errors(form)
#			flash('ERROR! Book was not added.', 'error')
#
#	return render_template('add_book.html', form=form)

@book_blueprint.route('/add', methods=['GET', 'POST'])
def add_book():
	form = SearchBookForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			return redirect(url_for('book.add_results', query=form.search.data))
		else:
			flash_errors(form)
			flash('ERROR! Could not find book.', 'error')
	return render_template('add_book.html', form=form)

@book_blueprint.route('/add_results/<query>', methods=['GET', 'POST'])
def add_results(query):
	form = AddBookFromSearch()
	if request.method == 'POST':
		if form.validate_on_submit():
			new_book = Book(form.title.data, form.isbn.data, form.summary.data, current_user.id, True, True, form.img_filename.data, form.img_url.data)
			db.session.add(new_book)
			db.session.commit()
			flash('New book, {}, added!'.format(new_book.title), 'success')
			return redirect(url_for('book.user_books'))
		else:
			flash_errors(form)
			flash('ERROR! Book was not added.', 'error')
			return redirect(url_for('book.user_books'))

	else:
		results = BookSearch.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
		return render_template('add_book_results.html',
							query=query,
							results=results,
							form=form)

@book_blueprint.route('/search', methods=['POST'])
def search():
	form = SearchBookForm()
	if form.validate_on_submit():
		results = Book.query.whoosh_search(form.search.data, MAX_SEARCH_RESULTS).all()
		return render_template('public_books_search.html', user_books = results)
	else:
		flash_errors(form)
    	flash('ERROR! Could not find book.', 'error')

@book_blueprint.route('/book/<book_id>')
def book_details(book_id):
    book_with_user = db.session.query(Book, User).join(User).filter(Book.id == book_id).first()
    if book_with_user is not None:
        if book_with_user.Book.is_public:
            return render_template('book_details.html', book=book_with_user)
        else:
            if current_user.is_authenticated and book_with_user.Book.user_id == current_user.id:
                return render_template('book_details.html', book=book_with_user)
            else:
                flash('Error! Incorrect permissions to access this book.', 'error')
    else:
        flash('Error! Book does not exist.', 'error')
    return redirect(url_for('book.public_books'))
