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
