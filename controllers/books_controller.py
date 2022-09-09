from flask import Blueprint, jsonify, request
from main import db
from models.book import Book
from models.reservation import Reservation
from models.user import User
from schemas.book_schema import book_schema, books_schema
from schemas.reservation_schema import reservation_schema, reservations_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import date

books = Blueprint('books', __name__, url_prefix="/books")


@books.route("/", methods=["GET"])
def get_books():
    #show the content of the query string
    #print(request.query_string)
    # if we have a query string, instead of getting all the books, get the books from that searching criteria
    if request.query_string:
        #Show the values of the searching criterias
        #print(request.args.get('title'))
        #print(request.args.get('genre'))
        # get the filtered search books from the database
        if request.args.get('genre'):
            filtered_books_list = Book.query.filter_by(genre= request.args.get('genre'))
            result = books_schema.dump(filtered_books_list)
            return jsonify(result), 200
        else:
            return {"message": "No books based on that searching criteria"}
    # get all the books from the database
    books_list = Book.query.all()
    result = books_schema.dump(books_list)
    return jsonify(result), 200

@books.route("/<int:id>", methods=["GET"])
def get_book(id):
    # get the book from the database by id
    book = Book.query.get(id)
    result = book_schema.dump(book)
    return jsonify(result), 200

@books.route("/", methods=["POST"])
# a token is needed for this request
@jwt_required()
def new_book():
    # it is not enough with a token, the identity needs to be a librarian
    if get_jwt_identity() != "librarian":
        return {"error": "You don't have the permission to do this"}, 401
    book_fields = book_schema.load(request.json)
    book = Book(
        title = book_fields["title"],
        genre = book_fields["genre"],
        year = book_fields["year"],
        length = book_fields["length"],
        author_id = book_fields["author_id"]
    )

    db.session.add(book)
    db.session.commit()
    return jsonify(book_schema.dump(book)), 201

@books.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_book(id):
    # it is not enough with a token, the identity needs to be a librarian
    if get_jwt_identity() != "librarian":
        return {"error": "You don't have the permission to do this"}, 401
    #find the book in the database
    book = Book.query.get(id)
    #check if book exist in the database
    if not book:
        return {"error": "Book id not found in the database"}, 404
    #get the book details from the request
    book_fields = book_schema.load(request.json)
    #upodate the values of the book
    book.title = book_fields["title"]
    book.genre = book_fields["genre"]
    book.length = book_fields["length"]
    book.year = book_fields["year"]

    #save changes in the database
    db.session.commit() 

    return jsonify(book_schema.dump(book)), 201   

# get all reservations
@books.route("/reservations", methods=["GET"])
@jwt_required()
def get_all_reservations():
    # it is not enough with a token, the identity needs to be a librarian
    if get_jwt_identity() != "librarian":
        return {"error": "You don't have the permission to do this"}
    # get all the reservations from the database
    reservations_list = Reservation.query.all()
    result = reservations_schema.dump(reservations_list)
    return jsonify(result)
        
# post a new reservation
@books.route("<int:book_id>/reservations", methods=["POST"])
@jwt_required()
def new_reservation(book_id):
    #find the book in the database
    book = Book.query.get(book_id)
    #check if book exist in the database
    if not book:
        return {"error": "Book id not found in the database"} 
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found in the database"} 

    reservation = Reservation(
        user = user,
        book = book,
        start_date = date.today()
    )

    db.session.add(reservation)
    db.session.commit()

    return jsonify(reservation_schema.dump(reservation))
