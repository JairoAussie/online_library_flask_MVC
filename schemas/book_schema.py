from main import ma

class BookSchema(ma.Schema):
    class Meta:
        #ordered = True
        fields = ["book_id", "title", "genre", "length", "year"]

#single book schema
book_schema = BookSchema()
#multiple_schema
books_schema = BookSchema(many=True)