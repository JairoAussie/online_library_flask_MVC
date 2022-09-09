from wsgiref import validate
from main import ma
from marshmallow.validate import Length

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "username", "email", "password")
    #add validation to password
    password = ma.String(validate=Length(min=8))
    username = ma.String(required = True)
    email = ma.String(required = True)

user_schema = UserSchema()
#multiple schema not necessary right now
#users_schema = UserSchema(many=True)