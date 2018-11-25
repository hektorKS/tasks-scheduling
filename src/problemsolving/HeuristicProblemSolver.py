import copy
import time
from collections import deque

from problem.Problem import Problem
from problemsolving.CostCounter import CostCounter
from problemsolving.entities.Entity import Entity
from problemsolving.entities.Move import Move
from problemsolving.entities.Swap import Swap
from solution.Solution import Solution


class HeuristicProblemSolver:

    def __init__(self, start_time: int, processing_time: int, max_tabu_list_size: int):
        self.best = None
        self.best_candidate = None
        self.tabu_list = deque([])
        self.start_time = start_time
        self.processing_time = processing_time
        self.max_tabu_list_size = max_tabu_list_size

    def solve(self, problem: Problem):
        self.best = copy.deepcopy(problem)
        self.best_candidate = problem
        self.tabu_list.append(copy.deepcopy(problem))
        while time.time() - self.start_time < self.processing_time:
            self.__iteration()
        return Solution(self.best, CostCounter.count(self.best))

    def __iteration(self):
        # Filter neighbours from tabu list
        _neighbours = list(filter(lambda item: item not in self.tabu_list, self.__get_neighbors(self.best_candidate)))

        # Filter neighbours with not better result
        _best_candidate_fitness = self.__fitness(self.best_candidate)
        # _neighbours_fitness = list(map(lambda item: self.__fitness_with_change(self.best_candidate, item), _neighbours))

        if len(_neighbours) == 0:
            return

        _best_neighbour = _neighbours[0]
        for neighbour in _neighbours:
            _old = self.__fitness_with_change(self.best_candidate, _best_neighbour)
            _new = self.__fitness_with_change(self.best_candidate, neighbour)
            if _new < _old and _new != _best_candidate_fitness:
                _best_neighbour = neighbour

        self.best_candidate = _best_neighbour.apply_to_problem(self.best_candidate)

        print("New best solution: {}".format(self.__fitness(self.best_candidate)))

        if self.__fitness(self.best_candidate) < self.__fitness(self.best):
            self.best = copy.deepcopy(self.best_candidate)

        self.tabu_list.append(_best_neighbour.to_tabu())

        if len(self.tabu_list) > self.max_tabu_list_size:
            self.tabu_list.popleft()

    def __get_neighbors(self, problem: Problem):
        _problem = problem
        neighbours = []

        # One to left
        if _problem.starting_point > 0:
            for index in range(1, _problem.starting_point + 1):
                neighbours.append(Move(index * (-1)))

        # One to right
        neighbours.append(Move(1))

        # Swapped positions
        for swap_distance in range(1):
            for index in range(swap_distance + 1, len(_problem.tasks)):
                neighbours.append(Swap(index - 1, index))

        return neighbours

    def __fitness(self, problem: Problem):
        return CostCounter.count(problem)

    def __fitness_with_change(self, problem: Problem, entity: Entity):
        entity.apply_to_problem(problem)
        result = CostCounter.count(problem)
        entity.recall_from_problem(problem)
        return result
