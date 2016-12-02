from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)
mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

from app.models import User, Book

@login_manager.user_loader
def load_user(user_id):
	return User.query.filter(User.id == int(user_id)).first()

from app.user.views import user_blueprint as user_blueprint1
from app.book.views import book_blueprint as book_blueprint1

app.register_blueprint(user_blueprint1)
app.register_blueprint(book_blueprint1)
