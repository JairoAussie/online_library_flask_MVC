from main import ma
from marshmallow import fields

from schemas.book_schema import BookSchema

class AuthorSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("author_id", "name", "country", "dob", "books")
    books = fields.List(fields.Nested(BookSchema, only=("title","genre", "year"))) #exclude=("author",)) to avoid recursive calls between schemas

author_schema = AuthorSchema()
#multiple
authors_schema = AuthorSchema(many=True)