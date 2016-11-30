from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)

from app.user.views import user_blueprint as user_blueprint1
from app.book.views import book_blueprint as book_blueprint1

app.register_blueprint(user_blueprint1)
app.register_blueprint(book_blueprint1)
