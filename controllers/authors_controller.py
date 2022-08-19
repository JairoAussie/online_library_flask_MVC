from flask import Blueprint
from main import db
from models.author import Author

authors = Blueprint('authors', __name__, url_prefix="/authors")


@authors.route("/", methods=["GET"])
def get_authors():
    # get all the books from the database
    authors_list = Author.query.all()

    return "List of authors"