from marshmallow import Schema, fields


class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(
        validate=fields.Length(min=6, max=12), required=True)


login_schema = LoginSchema()
