from flask import Blueprint, jsonify, request
from main import db
from models.book import Book
from schemas.book_schema import book_schema, books_schema

books = Blueprint('books', __name__, url_prefix="/books")


@books.route("/", methods=["GET"])
def get_books():
    # get all the books from the database
    books_list = Book.query.all()
    result = books_schema.dump(books_list)
    return jsonify(result)

@books.route("/<int:id>", methods=["GET"])
def get_book(id):
    # get the book from the database by id
    book = Book.query.get(id)
    result = book_schema.dump(book)
    return jsonify(result)

@books.route("/", methods=["POST"])
def new_book():
    book_fields = book_schema.load(request.json)
    book = Book(
        title = book_fields["title"],
        genre = book_fields["genre"],
        year = book_fields["year"],
        length = book_fields["length"]
    )

    db.session.add(book)
    db.session.commit()
    return jsonify(book_schema.dump(book))

@books.route("/<int:id>", methods=["PUT"])
def update_book(id):
    #find the book in the database
    book = Book.query.get(id)
    #check if book exist in the database
    if not book:
        return {"error": "Book id not found in the database"}
    #get the book details from the request
    book_fields = book_schema.load(request.json)
    #upodate the values of the book
    book.title = book_fields["title"]
    book.genre = book_fields["genre"]
    book.length = book_fields["length"]
    book.year = book_fields["year"]

    #save changes in the database
    db.session.commit() 

    return jsonify(book_schema.dump(book))   