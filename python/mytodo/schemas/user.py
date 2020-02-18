from marshmallow import Schema, fields
from marshmallow.validate import Length


class RegisterUserRequest(Schema):
    username = fields.Str(required=True, validate=Length(min=4, max=80))
    password = fields.Str(required=True, validate=Length(max=255))


class RegisterUserResponse(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)


class UserResponse(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)


register_user_request = RegisterUserRequest()
register_user_response = RegisterUserResponse()
user_response = UserResponse()
users_response = UserResponse(many=True)
