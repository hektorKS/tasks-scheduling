class Solution:
    def __init__(self, tasks: list, starting_point: int, cost: int):
        self.tasks = tasks
        self.starting_point = starting_point
        self.cost = cost

    def __str__(self):
        return "{} {} {}".format(self.cost, self.starting_point,
                                 " ".join(map(lambda task: str(task.task_id), self.tasks)))
