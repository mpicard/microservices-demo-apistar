from apistar import schema


class TaskDefinition(schema.String):
    max_length = 128
    default = None


class Task(schema.Object):
    properties = {
        'id': schema.Integer(default=None),
        'definition': TaskDefinition,
        'done': schema.Boolean
    }
