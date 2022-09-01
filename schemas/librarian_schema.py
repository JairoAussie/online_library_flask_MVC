from main import ma
from marshmallow.validate import Length

class LibrarianSchema(ma.Schema):
    class Meta:
        fields = ("librarian_id", "username", "password", "name", "shift", "payrate")
    #add validation to password
    password = ma.String(validate=Length(min=8))

#just the single schema for log in purposes
librarian_schema = LibrarianSchema()
