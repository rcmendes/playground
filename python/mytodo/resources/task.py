from flask_restful import Resource
from models.task import TaskModel
from schemas.task import task_insert_request, task_insert_response, task_response, tasks_response


class Task(Resource):
    @classmethod
    def get(cls, task_id: int = None):
        if task_id:
            task = TaskModel.find_by_id(task_id)
            if not task:
                return {"message": "Task not found"}, 200

            return task_response.dump(task), 200

        tasks = TaskModel.fetch_all()
        return tasks_response.dump(tasks), 200
