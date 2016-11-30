from app import db

class Book(db.Model):
	__tablename__ = 'book'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	isbn = db.Column(db.String, nullable=False)

	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
	def __repr__(self):
		return '<title {}'.format(self.name)

class User(db.Model):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String, unique=True, nullable=False)
    	password_plaintext = db.Column(db.String, nullable=False)  # TEMPORARY - TO BE DELETED IN FAVOR OF HASHED PASSWORD
 
    	def __init__(self, email, password_plaintext):
        	self.email = email
        	self.password_plaintext = password_plaintext
 
    	def __repr__(self):
        	return '<User {0}>'.format(self.name)
