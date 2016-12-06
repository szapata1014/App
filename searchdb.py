from app import db
from app.models import BookSearch

db.drop_all(bind='searchdb')

db.create_all(bind='searchdb')

book1 = BookSearch('The Girl on the Train', '9789044971453', image_url="{{ url_for('static', filename='img/GirlOnTheTrain') }}", summary="Rachel takes the same commuter train every morning and night. Every day she rattles down the track, flashes past a stretch of cozy suburban homes, and stops at the signal that allows her to daily watch the same couple breakfasting on their deck. She's even started to feel like she knows them. Jess and Jason, she calls them. Their life as she sees it is perfect. Not unlike the life she recently lost. And then she sees something shocking. It's only a minute until the train moves on, but it's enough. Now everything's changed. Unable to keep it to herself, Rachel goes to the police. But is she really as unreliable as they say? Soon she is deeply entangled not only in the investigation but in the lives of everyone involved. Has she done more harm than good?")
book2 = BookSearch('Fantastic Beasts and Where to Find Them', '9781408834824', image_url="https://images.gr-assets.com/books/1303738520l/41899.jpg", summary="A copy of Fantastic Beasts & Where to Find Them resides in almost every wizarding household in the country. Now Muggles too have the chance to discover where the Quintaped lives, what the Puffskein eats and why it is best not to leave milk out for a Knarl.")
book3 = BookSearch('The BFG', '9780142410387', image_url='https://upload.wikimedia.org/wikipedia/en/b/b2/The_BFG_%28Dahl_novel_-_cover_art%29.jpg', summary="Ten-year-old Sophie is in for the adventure of a lifetime when she meets the Big Friendly Giant (Mark Rylance). Naturally scared at first, the young girl soon realizes that the 24-foot behemoth is actually quite gentle and charming. As their friendship grows, Sophie's presence attracts the unwanted attention of Bloodbottler, Fleshlumpeater and other giants. After traveling to London, Sophie and the BFG must convince Queen Victoria to help them get rid of all the bad giants once and for all.")
book4 = BookSearch("Harry Potter and the Sorcerer's Stone", '9780590353427',image_url='http://freeaudiobookguide.com/wp-content/uploads/2015/08/harry-potter-and-the-sorcerers-stone-free-audiobook-download.jpg', summary="The first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.")

db.session.add(book1)
db.session.add(book2)
db.session.add(book3)
db.session.add(book4)


db.session.commit()
