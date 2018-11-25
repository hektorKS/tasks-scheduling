from problem.Problem import Problem
from problemsolving.entities.Entity import Entity


class Move(Entity):
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "Move(value={})".format(self.value)

    def apply_to_problem(self, problem: Problem):
        problem.starting_point += self.value
        return problem

    def recall_from_problem(self, problem: Problem):
        problem.starting_point -= self.value
        return problem

    def to_tabu(self):
        self.value = self.value * (-1)
        return self
