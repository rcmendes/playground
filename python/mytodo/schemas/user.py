from marshmallow import Schema, fields
from marshmallow.validate import Length


class RegisterUserRequest(Schema):
    username = fields.String(required=True, validate=Length(min=4, max=80))
    password = fields.String(required=True, validate=Length(max=255))


class RegisterUserResponse(Schema):
    id = fields.String(required=True)
    username = fields.String(required=True)


class UserResponse(Schema):
    id = fields.String(required=True)
    username = fields.String(required=True)


register_user_request = RegisterUserRequest()
register_user_response = RegisterUserResponse()
user_response = UserResponse()
users_response = UserResponse(many=True)
