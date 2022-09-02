from main import ma
from marshmallow import fields
#from schemas.author_schema import AuthorSchema

class BookSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["book_id", "title", "genre", "length", "year", "author_id", "author"]
        load_only = ['author_id']
    # Schema is defined as a String, to avoid te circular import error 
    author = fields.Nested("AuthorSchema", only=("name",))

#single book schema
book_schema = BookSchema()
#multiple_schema
books_schema = BookSchema(many=True)