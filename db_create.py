from app import db
from app.models import Book

db.drop_all()

db.create_all()

book1 = Book('The Girl on the Train', '9789044971453')
book2 = Book('Fantastic Beasts and Where to Find Them', '9781408834824')
book3 = Book('The BFG', '9780142410387')
db.session.add(book1)
db.session.add(book2)
db.session.add(book3)

db.session.commit()

