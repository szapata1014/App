from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class AddBookForm(Form):
	title = StringField('Book Title', validators=[DataRequired()])
	isbn = StringField('ISBN', validators=[DataRequired()])

