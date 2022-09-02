from main import db

class Reservation(db.Model):
    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date(), nullable=False)
    length = db.Column(db.Integer, default = 10)
    book_id = db.Column(db.Integer, db.ForeignKey("books.book_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)