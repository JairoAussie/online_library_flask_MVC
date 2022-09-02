from main import db

class Book(db.Model):
    __tablename__="books"
    book_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    genre = db.Column(db.String())
    length = db.Column(db.Integer())
    year = db.Column(db.Integer())
    author_id = db.Column(db.Integer, db.ForeignKey("authors.author_id"))
    reservations = db.relationship(
        "Reservation",
        backref = "book",
        cascade="all, delete"
    )