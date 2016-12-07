from app import db
from app.models import Book, User

db.drop_all(bind='appdb')

db.create_all(bind='appdb')

admin_user = User(email='exploreyourshelf@gmail.com', password_plaintext='admin', role ='admin', credits=1)
user1 = User('sofiacamizapata@gmail.com', 'password', credits=1)
user2 = User('szapata1@stevens.edu', 'password', credits=1)

db.session.add(admin_user)
db.session.add(user1)
db.session.add(user2)

# we shouldn't need this line but for some reason we do
admin_user = User.query.filter_by(email='exploreyourshelf@gmail.com').first()
bookurl = 'http://localhost:5000/static/img'

book1 = Book('The Girl on the Train', '9789044971453', "Rachel takes the same commuter train every morning and night. Every day she rattles down the track, flashes past a stretch of cozy suburban homes, and stops at the signal that allows her to daily watch the same couple breakfasting on their deck. She's even started to feel like she knows them. Jess and Jason, she calls them. Their life as she sees it is perfect. Not unlike the life she recently lost. And then she sees something shocking. It's only a minute until the train moves on, but it's enough. Now everything's changed. Unable to keep it to herself, Rachel goes to the police. But is she really as unreliable as they say? Soon she is deeply entangled not only in the investigation but in the lives of everyone involved. Has she done more harm than good?", admin_user.id, True, True, 'girlontrain.jpg', bookurl+'/girlontrain.jpg')

book2 = Book('Fantastic Beasts and Where to Find Them', '9781408834824', "A copy of Fantastic Beasts & Where to Find Them resides in almost every wizarding household in the country. Now Muggles too have the chance to discover where the Quintaped lives, what the Puffskein eats and why it is best not to leave milk out for a Knarl.", admin_user.id, True, True, 'fantasticbeasts.jpg', bookurl+'/fantasticbeasts.jpg')

book3 = Book('The BFG', '9780142410387', "Ten-year-old Sophie is in for the adventure of a lifetime when she meets the Big Friendly Giant (Mark Rylance). Naturally scared at first, the young girl soon realizes that the 24-foot behemoth is actually quite gentle and charming. As their friendship grows, Sophie's presence attracts the unwanted attention of Bloodbottler, Fleshlumpeater and other giants. After traveling to London, Sophie and the BFG must convince Queen Victoria to help them get rid of all the bad giants once and for all.", user1.id, True, True, 'BFG.jpg', bookurl+'/BFG.jpg')


book4 = Book("Harry Potter and the Sorcerer's Stone", '9780590353427',"The first of J.K. Rowling's popular children's novels about Harry Potter, a boy who learns on his eleventh birthday that he is the orphaned son of two powerful wizards and possesses unique magical powers of his own. He is summoned from his life as an unwanted child to become a student at Hogwarts, an English boarding school for wizards. There, he meets several friends who become his closest allies and help him discover the truth about his parents' mysterious deaths.", user1.id, True, True, 'HP1.jpg', bookurl+'/HP1.jpg')

book5 = Book("You Deserve a Drink", '9780142181676', "The book details humorous anecdotes and stories of Hart's life, with a cocktail recipe accompanying each chapter.", user2.id, True, True, 'deservedrink.jpg', bookurl+'/deservedrink.jpg')

book6 = Book("Life of Pi",'0676973760',"Life of Pi is a Canadian fantasy adventure novel by Yann Martel published in 2001. The protagonist, Piscine Molitor 'Pi' Patel, an Indian boy from Pondicherry, explores issues of spirituality and practicality from an early age. He survives 227 days after a shipwreck while stranded on a lifeboat in the Pacific Ocean with a Bengal tiger named Richard Parker.",user2.id, True, True, 'LifePI.jpg', bookurl+'/LifePI.jpg')

book7 = Book("Harry Potter and the Half-Blood Prince",'0747581088',"Harry Potter and the Half-Blood Prince is the sixth and penultimate novel in the Harry Potter series, written by British author J. K. Rowling. Set during protagonist Harry Potter's sixth year at Hogwarts, the novel explores the past of Harry's nemesis, Lord Voldemort, and Harry's preparations for the final battle against Voldemort alongside his headmaster and mentor Albus Dumbledore.",user1.id, True, True, 'HP6.jpg', bookurl+'/HP6.jpg')

book8 = Book("The Great Gatsby",'9781447225928',"The Great Gatsby is a 1925 novel written by American author F. Scott Fitzgerald that follows a cast of characters living in the fictional town of West Egg on prosperous Long Island in the summer of 1922. The story primarily concerns the young and mysterious millionaire Jay Gatsby and his quixotic passion and obsession for the beautiful former debutante Daisy Buchanan. Considered to be Fitzgerald's magnum opus, The Great Gatsby explores themes of decadence, idealism, resistance to change, social upheaval, and excess, creating a portrait of the Jazz Age or the Roaring Twenties that has been described as a cautionary tale regarding the American Dream.",user2.id, True, True)

book9 = Book("War and Peace",'9780060798888',"The novel charts the history of the French invasion of Russia, and the impact of the Napoleonic era on Tsarist society, through the stories of five Russian aristocratic families. Portions of an earlier version, titled The Year 1805, were serialized in The Russian Messenger between 1865 and 1867. The novel was first published in its entirety in 1869. Newsweek in 2009 ranked it first in its Top 100 Books. In 2007, Time magazine ranked War and Peace third in its poll of the 10 greatest books of all time while Anna Karenina was ranked first.",user1.id, True, True)

book10 = Book("The Da Vinci Code",'9780552159715',"The Da Vinci Code is a 2003 mystery-detective novel by Dan Brown. It follows symbologist Robert Langdon and cryptologist Sophie Neveu Abraham after a murder in the Louvre Museum in Paris, when they become involved in a battle between the Priory of Sion and Opus Dei over the possibility of Jesus Christ having been a companion to Mary Magdalene. The title of the novel refers, among other things, to the finding of the first murder victim in the Grand Gallery of the Louvre, naked and posed similar to Leonardo da Vinci's famous drawing, the Vitruvian Man, with a cryptic message written beside his body and a pentagram drawn on his chest in his own blood.",user2.id,True,True)

book11 = Book("The Alchemist",'9780061122415',"Paulo Coelho's masterpiece tells the magical story of Santiago, an Andalusian shepherd boy who yearns to travel in search of a worldly treasure as extravagant as any ever found.The story of the treasures Santiago finds along the way teaches us, as only a few stories can, about the essential wisdom of listening to our hearts, learning to read the omens strewn along life's path, and, above all, following our dreams.",user2.id,True,True)

book12 = Book("The Catcher in the Rye",'9781476744834',"The Catcher in the Rye is a 1951 novel by J. D. Salinger. A controversial novel originally published for adults, it has since become popular with adolescent readers for its themes of teenage angst and alienation. It has been translated into almost all of the world's major languages. Around 1 million copies are sold each year with total sales of more than 65 million books.The novel's protagonist Holden Caulfield has become an icon for teenage rebellion. The novel also deals with complex issues of innocence, identity, belonging, loss, and connection.",user2.id,True,True)

db.session.add(book1)
db.session.add(book2)
db.session.add(book3)
db.session.add(book4)
db.session.add(book5)
db.session.add(book6)
db.session.add(book7)
db.session.add(book8)
db.session.add(book9)
db.session.add(book10)
db.session.add(book11)
db.session.add(book12)

db.session.commit()

