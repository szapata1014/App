from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app import images

class AddBookForm(Form):
	title = StringField('Book Title', validators=[DataRequired()])
	isbn = StringField('ISBN', validators=[DataRequired()])
	book_image = FileField('Book Image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
