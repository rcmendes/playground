from marshmallow import Schema, fields


class RegisterUserDTORequest(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class RegisterUserDTOResponse(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
