from flask import Blueprint
from main import db
from main import bcrypt
from models.author import Author
from models.book import Book
from models.user import User
from models.librarian import Librarian
from datetime import date


db_commands = Blueprint("db", __name__)

@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all models in the physical DB
    db.create_all()
    print('Tables created')

@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables
    db.drop_all()
    print('Tables dropped')

@db_commands.cli.command('seed')
def seed_db():

    librarian1 = Librarian(
        username = "sam",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8"),
        name = "Sam the librarian"
    )

    db.session.add(librarian1)  
    
    user1 = User(
        username = "jairo",
        email = "jairo@email.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8")
    )

    db.session.add(user1)   

    user2 = User(
        username = "pang",
        email = "pang@email.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf-8")
    )

    db.session.add(user2)  
    author1 = Author(
        name = "Haruki Murakami",
        country = "Japan",
        dob = date(day = 12, month = 1,year = 1949 )
    )

    db.session.add(author1)

    author2 = Author(
        name = "Margaret Atwood",
        country = "Canada",
        dob = date(day = 18, month = 11,year = 1939 )
    )

    db.session.add(author2)

    author3 = Author(
        name = "Tom Clancy",
        country = "USA",
        dob = date(day = 12, month = 4,year = 1947 )
    )

    db.session.add(author3)

    book1 = Book(
        title = "1Q84",
        genre = "Novel",
        year = 2009,
        length = 928
    )
    db.session.add(book1)

    book2 = Book(
        title = "Norwegian Wood",
        genre = "Novel",
        year = 1995,
        length = 296
    )
    db.session.add(book2)

    book3 = Book(
        title = "Alias Grace",
        genre = "Fiction",
        year = 1996,
        length = 470
    )
    db.session.add(book3)

    book4 = Book(
        title = "The Handmaid's Tale",
        genre = "Science Fiction",
        year = 1985,
        length = 311
    )
    db.session.add(book4)

    book5 = Book(
        title = "The Hand of the Red October",
        genre = "Fiction",
        year = 1984,
        length = 387
    )
    db.session.add(book5)

    db.session.commit()
    print("tables seeded")