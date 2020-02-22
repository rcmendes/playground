from models.user import UserModel
from ma import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        dump_only = ("id",)
        load_only = ("password",)


user_schema = UserSchema()
user_list_schema = UserSchema(many=True)
