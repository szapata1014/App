from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

from app.user.views import user_blueprint
from app.book.views import book_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(book_blueprint)
