import itertools
from typing import List

from apistar.http import Response
from apistar.schema import Boolean

from project.schema import Task, TaskDefinition


tasks = {}
counter = itertools.count(1).__next__


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def list_tasks() -> List[Task]:
    return [Task(tasks[id]) for id in tasks]


def add_task(definition: TaskDefinition) -> Response:
    if not definition:
        return Response(422, {'error': 'Task definition required.'})

    id = counter()
    tasks[id] = {
        'id': id,
        'definition': definition,
        'done': False
    }
    return Response(Task(tasks[id]), status=201)


def delete_task(task_id: int) -> Response:
    if task_id not in tasks:
        return Response({}, status=404)

    del tasks[task_id]
    return Response({}, status=204)


def patch_task(task_id: int, done: Boolean) -> Response:
    if task_id not in tasks:
        return Response({}, status=404)

    tasks[task_id]['done'] = done
    return Response(Task(tasks[task_id]), status=200)
