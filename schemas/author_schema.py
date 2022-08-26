from main import ma

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ("author_id", "name", "country", "dob")

author_schema = AuthorSchema()
#multiple
authors_schema = AuthorSchema(many=True)