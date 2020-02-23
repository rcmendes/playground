from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from models.task import TaskModel
from schemas.task import task_schema, task_list_schema


class Task(Resource):
    @classmethod
    @jwt_required
    def get(cls, task_id: str = None):
        if task_id:
            task = TaskModel.find_by_id(task_id)
            if not task:
                return {"message": "Task not found"}, 404

            return task_schema.dump(task), 200

        tasks = TaskModel.fetch_all()
        return task_list_schema.dump(tasks), 200

    @classmethod
    @jwt_required
    def post(cls):
        task_json = request.get_json()

        task = task_schema.load(task_json)

        task.save()

        return task_schema.dump(task), 201

    @classmethod
    @jwt_required
    def put(cls, task_id: str):
        task_json = request.get_json()
        taskSchema = task_schema.load(task_json)
        task = TaskModel.find_by_id(taskSchema["id"])
        if not task:
            return {"message": "Task <id={}> not found ".format(task_id)}, 404
