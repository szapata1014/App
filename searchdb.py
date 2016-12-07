from app import db
from app.models import BookSearch

db.drop_all(bind='searchdb')

db.create_all(bind='searchdb')

bookurl = 'http://localhost:5000/static/img'

book1 = BookSearch('Fifty Shades of Grey', '9781612130286','50shades.jpg', bookurl+'/50shades.jpg', summary="Fifty Shades of Grey is a 2011 erotic romance novel by British author E. L. James. It is the first instalment in the Fifty Shades trilogy that traces the deepening relationship between a college graduate, Anastasia Steele, and a young business magnate, Christian Grey.")

book2=BookSearch('Learning Python 5th Edition','9781449355739', 'learningpython.jpg', bookurl+'/learningpython.jpg' , summary="Learning Python is a tutorial book for the Python programming language, and is published by O'Reilly Media. The first (1999) and second (2003) editions were written by Mark Lutz and David Ascher, and covers Python 1.5 and 2.3, respectively. The third (2007) edition was written solely by Mark Lutz, and covers Python 2.5. The fourth (2009) and fifth (2013) editions were both written by Mark Lutz. The fourth edition covers Python 2.6 and 3.x, and the fifth edition covers Python 2.7 and Python 3.3.")

book3 = BookSearch("Harry Potter and the Sorcerer's Stone", '9780590353427','HP1.jpg', bookurl+'/HP1.jpg', summary="The first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.")

book4 = BookSearch("Harry Potter and the Prizoner of Azkaban", '9780590353452', 'HP3.jpg', bookurl+'/HP3.jpg',summary="Harry Potter is lucky to reach the age of thirteen, since he has already survived the murderous attacks of the feared Dark Lord on more than one occasion. But his hopes for a quiet term concentrating on Quidditch are dashed when a maniacal mass-murderer escapes from Azkaban, pursued by the soul-sucking Dementors who guard the prison. It's assumed that Hogwarts is the safest place for Harry to be. But is it a coincidence that he can feel eyes watching him in the dark, and should he be taking Professor Trelawney's ghoulish predictions seriously?")

book5 = BookSearch("Harry Potter and the Chamber of Secrets", "9780747560722", 'HP2.jpg', bookurl+"/HP2.jpg", summary="The Dursleys were so mean and hideous that summer that all Harry Potter wanted was to get back to the Hogwarts School for Witchcraft and Wizardry. But just as he's packing his bags, Harry receives a warning from a strange, impish creature named Dobby who says that if Harry Potter returns to Hogwarts, disaster will strike.")

book6 = BookSearch("Harry Potter and the Half-Blood Prince",'0747581088', 'HP6.jpg', bookurl+'/HP6.jpg',summary="Harry Potter and the Half-Blood Prince is the sixth and penultimate novel in the Harry Potter series, written by British author J. K. Rowling. Set during protagonist Harry Potter's sixth year at Hogwarts, the novel explores the past of Harry's nemesis, Lord Voldemort, and Harry's preparations for the final battle against Voldemort alongside his headmaster and mentor Albus Dumbledore.")

book7 = BookSearch("Harry Potter and the Goblet of Fire",'9780747560719', 'HP4.jpg', bookurl+'/HP4.jpg',summary="Harry Potter is midway through both his training as a wizard and his coming of age. Harry wants to get away from the pernicious Dursleys and go to the International Quidditch Cup with Hermione, Ron, and the Weasleys. He wants to dream about Cho Chang, his crush (and maybe do more than dream). He wants to find out about the mysterious event that supposed to take place at Hogwarts this year, an event involving two other rival schools of magic, and a competition that hasn't happened for hundreds of years. He wants to be a normal, fourteen-year-old wizard. But unfortunately for Harry Potter, he's not normal - even by wizarding standards.")

book8 = BookSearch("Harry Potter and the Order of the Phoenix",'9754247560719', 'HP5.jpg', bookurl+'/HP5.jpg',summary="Harry Potter is due to start his fifth year at Hogwarts School of Witchcraft and Wizardry. His best friends Ron and Hermione have been very secretive all summer and he is desperate to get back to school and find out what has been going on. However, what Harry discovers is far more devastating than he could ever have expected...")

book9 = BookSearch("Harry Potter and the Dealthy Hallows",'9754910460719', 'HP7.jpg', bookurl+'/HP7.jpg',summary="It's no longer safe for Harry at Hogwarts, so he and his best friends, Ron and Hermione, are on the run. Professor Dumbledore has given them clues about what they need to do to defeat the dark wizard, Lord Voldemort, once and for all, but it's up to them to figure out what these hints and suggestions really mean.")



db.session.add(book1)
db.session.add(book2)
db.session.add(book3)
db.session.add(book5)
db.session.add(book4)
db.session.add(book7)
db.session.add(book8)
db.session.add(book6)
db.session.add(book9)










db.session.commit()
