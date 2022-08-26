from flask import Blueprint, jsonify, request
from main import db
from models.author import Author
from schemas.author_schema import author_schema, authors_schema

authors = Blueprint('authors', __name__, url_prefix="/authors")


@authors.route("/", methods=["GET"])
def get_authors():
    # get all the books from the database
    authors_list = Author.query.all()
    result = authors_schema.dump(authors_list)
    return jsonify(result)

@authors.route("/<int:id>", methods=["GET"])
def get_author(id):
    #search author by id (primary key)
    author = Author.query.get(id)
    #get a list of authors filtering by the given criteria. first will return the first match instead of a returning a list
    #author = Author.query.filter_by(author_id=id).first()
    #check if we found an author
    if not author:
        return {"error": "author id not found"}

    #serialise the result in a single author schema
    result = author_schema.dump(author)
    return jsonify(result) 

#POST an author
@authors.route("/", methods=["POST"])
def create_author():
    #get the values from the request and load them with the single schema
    author_fields = author_schema.load(request.json)
    #create a new Author object
    author = Author(
        name = author_fields["name"],
        country= author_fields["country"],
        dob= author_fields["dob"]
    )

    db.session.add(author)
    #store in the database and save the changes
    db.session.commit()

    return jsonify(author_schema.dump(author))

#DELETE and author
@authors.route("/<int:id>", methods=["DELETE"])
def delete_author(id):
    #search author by id (primary key)
    author = Author.query.get(id)
    #get a list of authors filtering by the given criteria. first will return the first match instead of a returning a list
    #author = Author.query.filter_by(author_id=id).first()
    #check if we found an author
    if not author:
        return {"error": "author id not found"}

    # delete the author from the database
    db.session.delete(author)
    #save the changes in the database
    db.session.commit()

    return {"message": "Author removed successfully"}