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
        self.iterations = 0
        self.empty_iterations = 0
        self.max_tabu_list_size = max_tabu_list_size

    def solve(self, problem: Problem):
        self.best = copy.deepcopy(problem)
        self.best_candidate = problem
        while time.time() - self.start_time < self.processing_time and self.empty_iterations < 100:
            self.__iteration()
            self.iterations = self.iterations + 1
        return Solution(self.best, CostCounter.count(self.best))

    def __iteration(self):
        # Get neighbors and filter ones from tabu list
        _neighbours = list(filter(lambda item: item not in self.tabu_list, self.__get_neighbors(self.best_candidate)))

        # Find best neighbor
        _best_neighbour = _neighbours[0]
        _old = self.__fitness_with_change(self.best_candidate, _best_neighbour)
        for neighbour in _neighbours:
            _new = self.__fitness_with_change(self.best_candidate, neighbour)
            if _new < _old:
                _best_neighbour = neighbour
                _old = _new

        # Set new best candidate (might be worse then the one from previous iteration)
        self.best_candidate = _best_neighbour.apply_to_problem(self.best_candidate)

        # Set new best solution if appeared or increase empty iterations number
        if self.__fitness(self.best_candidate) < self.__fitness(self.best):
            self.best = copy.deepcopy(self.best_candidate)
            self.empty_iterations = 0
        else:
            self.empty_iterations = self.empty_iterations + 1

        # Add to tabu list
        self.tabu_list.append(_best_neighbour.to_tabu())

        # Control tabu list size
        if len(self.tabu_list) > self.max_tabu_list_size:
            self.tabu_list.popleft()

    def __get_neighbors(self, problem: Problem):
        _problem = problem
        neighbours = []

        # One to left
        if _problem.starting_point > 0:
            neighbours.append(Move(-1))

        # One to right
        neighbours.append(Move(1))

        # Get proper range of swapping
        range_size = 25
        tasks_number = len(_problem.tasks)
        if tasks_number > 100:
            shift = int((self.iterations % (int(tasks_number / range_size) - 1)) * range_size)
            swap_start = 1 + shift
            swap_end = swap_start + range_size
            if swap_end > tasks_number:
                swap_end = tasks_number
        else:
            swap_start = 1
            swap_end = tasks_number

        # Swapped positions
        for index in range(swap_start, swap_end):
            neighbours.append(Swap(index - 1, index))

        return neighbours

    def __fitness(self, problem: Problem):
        return CostCounter.count(problem)

    def __fitness_with_change(self, problem: Problem, entity: Entity):
        entity.apply_to_problem(problem)
        result = CostCounter.count(problem)
        entity.recall_from_problem(problem)
        return result
