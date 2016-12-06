from app import db
from app.models import Book, User

db.drop_all(bind='appdb')

db.create_all(bind='appdb')

admin_user = User(email='exploreyourshelf@gmail.com', password_plaintext='admin', role ='admin')
user1 = User('sofiacamizapata@gmail.com', 'password')
user2 = User('szapata1@stevens.edu', 'password')

db.session.add(admin_user)
db.session.add(user1)
db.session.add(user2)

# we shouldn't need this line but for some reason we do
admin_user = User.query.filter_by(email='exploreyourshelf@gmail.com').first()

book1 = Book('The Girl on the Train', '9789044971453', admin_user.id, False)
book2 = Book('Fantastic Beasts and Where to Find Them', '9781408834824', admin_user.id, True)
book3 = Book('The BFG', '9780142410387', user1.id, True)

db.session.add(book1)
db.session.add(book2)
db.session.add(book3)

db.session.commit()

