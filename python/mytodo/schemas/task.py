from marshmallow import Schema, fields
from marshmallow.validate import Length

from ma import ma


class TaskInsertRequest(Schema):
    title = fields.String(required=True, validate=Length(min=1, max=100))
    # description = fields.String(required=False, validate=Length(max=1024))


class TaskInsertResponse(Schema):
    id = fields.String(required=True)
    title = fields.String(required=True)
    # description = fields.String(required=False)


class TaskResponse(ma.ModelSchema):
    class Meta:
        include_fk = True
        load_only = ("agenda",)
        dump_only = ("id", "agenda",)


task_insert_request = TaskInsertRequest()
task_insert_response = TaskInsertResponse()
task_response = TaskResponse()
tasks_response = TaskResponse(many=True)
