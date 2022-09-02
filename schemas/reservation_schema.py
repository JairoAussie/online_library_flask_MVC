from main import ma
from marshmallow import fields
from schemas.book_schema import BookSchema
from schemas.user_schema import UserSchema

class ReservationSchema(ma.Schema):
    class Meta:
        ordered=True
        fields = ('reservation_id', "user", "book","start_date","length", "book_id", "user_id",)
        load_only = ("book_id", "user_id")
    user = fields.Nested(UserSchema, only=("username",))
    book = fields.Nested(BookSchema, only=("title",))
reservation_schema = ReservationSchema()
reservations_schema = ReservationSchema(many=True)
