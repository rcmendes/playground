from ma import ma
from marshmallow import fields, post_dump


class BaseSchema(ma.ModelSchema):

    id = fields.String(required=True, dump_only=True)
    created_at = fields.DateTime(required=True, dump_only=True)
    updated_at = fields.DateTime(required=True, dump_only=True)
    archived_at = fields.DateTime(
        required=False, dump_only=True, load_only=True)

    @post_dump(pass_many=False)
    def remove_fiels_with_value_as_none(self, data, many, **kwargs):
        """Remove all key that the value is missing."""

        data = {k: v for k, v in data.items() if v}
        return data
