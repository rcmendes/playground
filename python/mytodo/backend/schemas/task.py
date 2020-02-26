from schemas.base import BaseSchema
from models.task import TaskModel


class TaskSchema(BaseSchema):
    class Meta:
        model = TaskModel
        include_fk = True
        dump_only = ("id", "agenda", )
        load_only = ("agenda",)


task_schema = TaskSchema()
task_list_schema = TaskSchema(many=True)
