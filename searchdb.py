from app import db
from app.models import BookSearch

db.drop_all(bind='searchdb')

db.create_all(bind='searchdb')

bookurl = 'http://localhost:5000/static/img'

book1 = BookSearch('Fifty Shades of Grey', '9781612130286','50shades.jpg', bookurl+'/50shades.jpg', summary="Fifty Shades of Grey is a 2011 erotic romance novel by British author E. L. James. It is the first instalment in the Fifty Shades trilogy that traces the deepening relationship between a college graduate, Anastasia Steele, and a young business magnate, Christian Grey.")

book2=BookSearch('Learning Python 5th Edition','9781449355739', 'learningpython.jpg', bookurl+'/learningpython.jpg' , summary="Learning Python is a tutorial book for the Python programming language, and is published by O'Reilly Media. The first (1999) and second (2003) editions were written by Mark Lutz and David Ascher, and covers Python 1.5 and 2.3, respectively. The third (2007) edition was written solely by Mark Lutz, and covers Python 2.5. The fourth (2009) and fifth (2013) editions were both written by Mark Lutz. The fourth edition covers Python 2.6 and 3.x, and the fifth edition covers Python 2.7 and Python 3.3.")

db.session.add(book1)
db.session.add(book2)


db.session.commit()
