from problem.Problem import Problem
from problemsolving.entities.Entity import Entity


class Swap(Entity):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "Swap(x={}, y={})".format(self.x, self.y)

    def apply_to_problem(self, problem: Problem):
        task = problem.tasks[self.x]
        problem.tasks[self.x] = problem.tasks[self.y]
        problem.tasks[self.y] = task
        return problem

    def recall_from_problem(self, problem: Problem):
        task = problem.tasks[self.x]
        problem.tasks[self.x] = problem.tasks[self.y]
        problem.tasks[self.y] = task
        return problem

    def to_tabu(self):
        return self
