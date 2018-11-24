import copy
import time
from collections import deque

from problem.Problem import Problem
from problemsolving.CostCounter import CostCounter
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
        self.tabu_list.append(self.best_candidate)
        while time.time() - self.start_time < self.processing_time:
            self.__iteration()
        return Solution(self.best, CostCounter.count(self.best))

    def __iteration(self):
        _neighbours = list(filter(lambda item: item not in self.tabu_list, self.__get_neighbors(self.best_candidate)))
        _neighbours_fitness = list(map(lambda item: self.__fitness(item), _neighbours))

        _new_best_candidate = _neighbours[0]
        for candidate in _neighbours:
            if self.__fitness(candidate) < self.__fitness(_new_best_candidate):
                _new_best_candidate = candidate

        self.best_candidate = _new_best_candidate

        # print("New best: {}".format(self.best_candidate))
        print("New best solution: {}".format(CostCounter.count(self.best_candidate)))

        if self.__fitness(self.best_candidate) < self.__fitness(self.best):
            self.best = copy.deepcopy(self.best_candidate)

        self.tabu_list.append(self.best_candidate)

        if len(self.tabu_list) > self.max_tabu_list_size:
            self.tabu_list.popleft()

    def __get_neighbors(self, problem: Problem):
        _problem = problem
        neighbours = []

        # One to left
        if _problem.starting_point > 0:
            neighbour = copy.deepcopy(_problem)
            neighbour.starting_point = neighbour.starting_point - 1
            neighbours.append(neighbour)

        # One to right
        neighbour = copy.deepcopy(_problem)
        neighbour.starting_point = neighbour.starting_point + 1
        neighbours.append(neighbour)

        # Swapped positions
        for swap_distance in range(1):
            for index in range(swap_distance + 1, len(_problem.tasks)):
                neighbours.append(self.__copy_with_swapped_positions(_problem, index - 1, index))

        return neighbours

    def __copy_with_swapped_positions(self, problem: Problem, position_x: int, position_y: int):
        problem_copy = copy.deepcopy(problem)
        task = problem_copy.tasks[position_x]
        problem_copy.tasks[position_x] = problem_copy.tasks[position_y]
        problem_copy.tasks[position_y] = task
        return problem_copy

    def __fitness(self, problem: Problem):
        return CostCounter.count(problem)
