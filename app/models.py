from app import db, app
from sqlalchemy.ext.hybrid import hybrid_method
from datetime import datetime

import sys
if sys.version_info >= (3,0):
	enable_search = False
else:
	enable_search = True
	import flask_whooshalchemy as whooshalchemy

class Book(db.Model):
	__tablename__ = 'book'
	__bind_key__ = 'appdb'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	isbn = db.Column(db.String, nullable=False)
	is_public = db.Column(db.Boolean, nullable=False)
	image_filename = db.Column(db.String, default=None, nullable=True)
	image_url = db.Column(db.String, default=None, nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, title, isbn, user_id, is_public, image_filename=None, image_url=None):
		self.title = title
		self.isbn = isbn
		self.is_public = is_public
		self.image_filename = image_filename
		self.image_url = image_url
 		self.user_id = user_id

	def __repr__(self):
		return '<title {}'.format(self.name)

class User(db.Model):
	__tablename__ = 'users'
	__bind_key__ = 'appdb'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String, unique=True, nullable=False)
    	password_plaintext = db.Column(db.String, nullable=False)
 	authenticated = db.Column(db.Boolean, default=False)
	email_confirmation_sent_on = db.Column(db.DateTime, nullable=True)
    	email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
       	email_confirmed_on = db.Column(db.DateTime, nullable=True)
	registered_on = db.Column(db.DateTime, nullable=True)
	last_logged_in = db.Column(db.DateTime, nullable=True)
	current_logged_in = db.Column(db.DateTime, nullable=True)
	role = db.Column(db.String, default = 'user')
	books = db.relationship('Book', backref='user', lazy='dynamic')

    	def __init__(self, email, password_plaintext, email_confirmation_sent_on=None, role = 'user'):
        	self.email = email
        	self.password_plaintext = password_plaintext
		self.authenticated = False
		self.email_confirmation_sent_on = email_confirmation_sent_on
        	self.email_confirmed = False
        	self.email_confirmed_on = None
		self.registered_on = datetime.now()
        	self.last_logged_in = None
        	self.current_logged_in = datetime.now()
		self.role = role

	@hybrid_method
    	def is_correct_password(self, plaintext_password):
        	return self.password_plaintext == plaintext_password
 
    	@property
    	def is_authenticated(self):
        	"""Return True if the user is authenticated."""
        	return self.authenticated
 
   	@property
    	def is_active(self):
        	"""Always True, as all users are active."""
        	return True
 
    	@property
    	def is_anonymous(self):
        	"""Always False, as anonymous users aren't supported."""
        	return False
 
    	def get_id(self):
        	"""Return the email address to satisfy Flask-Login's requirements."""
        	"""Requires use of Python 3"""
        	return str(self.id)
	
	def __repr__(self):
        	return '<User {0}>'.format(self.name)


class BookSearch(db.Model):
	__tablename__ = 'booksearch'
	__bind_key__ = 'searchdb'
	__searchable__ = ['title', 'isbn']

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	isbn = db.Column(db.String, nullable=False)
	image_filename = db.Column(db.String, default=None, nullable=True)
	image_url = db.Column(db.String, default=None, nullable=True)
	summary = db.Column(db.String, default=None,nullable=True)

	def __init__(self, title, isbn, image_filename=None, image_url=None, summary=None):
		self.title = title
		self.isbn = isbn
		self.image_filename = image_filename
		self.image_url = image_url
		self.summary = summary

	def __repr__(self):
		return '<title {}'.format(self.title)

if enable_search:
	whooshalchemy.whoosh_index(app, BookSearch)