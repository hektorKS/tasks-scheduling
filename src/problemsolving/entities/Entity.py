from abc import abstractmethod

from problem.Problem import Problem


class Entity:
    @abstractmethod
    def apply_to_problem(self, problem: Problem): raise NotImplementedError

    @abstractmethod
    def recall_from_problem(self, problem: Problem): raise NotImplementedError

    @abstractmethod
    def to_tabu(self): raise NotImplementedError
