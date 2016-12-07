from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
from wtforms_components import read_only
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images

class AddBookForm(FlaskForm):
	title = StringField('Book Title', validators=[DataRequired()])
	isbn = StringField('ISBN', validators=[DataRequired()])
	summary = StringField('Summary', validators=[DataRequired()])
	book_image = FileField('Book Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])

class SearchBookForm(FlaskForm):
	search = StringField('Search for a Book', validators=[DataRequired()])

class AddBookFromSearch(FlaskForm):
	title = HiddenField( validators=[DataRequired()])
	isbn = HiddenField( validators=[DataRequired()])
	img_filename = HiddenField( validators=[DataRequired()])
	img_url = HiddenField( validators=[DataRequired()])
	summary = HiddenField( validators=[DataRequired()])
