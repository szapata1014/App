from flask_wtf import Form
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from wtforms_components import read_only
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images

class AddBookForm(Form):
	title = StringField('Book Title', validators=[DataRequired()])
	isbn = StringField('ISBN', validators=[DataRequired()])
	book_image = FileField('Book Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])

class SearchBookForm(Form):
	search = StringField('Search for a Book', validators=[DataRequired()])

class AddBookFromSearch(Form):
	title = HiddenField( validators=[DataRequired()])
	isbn = HiddenField( validators=[DataRequired()])
	#book_image = HiddenField( validators=[FileRequired()])
	#summary = HiddenField( validators=[DataRequired()])