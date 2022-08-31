from main import db

class Librarian(db.Model):
    __tablename__ = "librarians"

    librarian_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    shift = db.Column(db.String(), default = "Weekdays mornings")
    payrate = db.Column(db.Float(), default = 30.0)