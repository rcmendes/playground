from marshmallow import fields
from marshmallow.validate import Email

from schemas.base import BaseSchema
from models.user import UserModel


class UserSchema(BaseSchema):
    # class Meta:
    class Meta:
        model = UserModel
        load_only = ("password",)

    email = fields.String(validate=Email())


user_schema = UserSchema()
user_list_schema = UserSchema(many=True)
