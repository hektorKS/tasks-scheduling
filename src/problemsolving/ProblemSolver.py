import random
from random import shuffle

import itertools

from problem.Problem import Problem
from problemsolving.CostCounter import CostCounter
from solution.Solution import Solution


class ProblemSolver:

    @staticmethod
    def solve(problem: Problem):
        return ProblemSolver.solve_random(problem)

    @staticmethod
    def solve_simple(problem: Problem):
        cost = CostCounter.count(problem)
        return Solution(problem, cost)

    @staticmethod
    def solve_with_permutations(problem: Problem):
        tasks_permutations = list(itertools.permutations(range(len(problem.tasks))))
        tasks_costs = []
        for permutation in tasks_permutations:
            problem = ProblemSolver.order_tasks(problem, permutation)
            tasks_costs.append(CostCounter.count(problem))
        min_cost_index = tasks_costs.index(min(tasks_costs))
        optimal_problem = ProblemSolver.order_tasks(problem, tasks_permutations[min_cost_index])
        optimal_cost = tasks_costs[min_cost_index]
        return Solution(optimal_problem, optimal_cost)

    @staticmethod
    def solve_random(problem: Problem):
        shuffle(problem.tasks)
        problem.starting_point = random.randrange(0, 10)
        cost = CostCounter.count(problem)
        return Solution(problem, cost)

    @staticmethod
    def order_tasks(problem: Problem, order: list):
        result = []
        for index in order:
            result.append(problem.tasks[index])
        problem.tasks = result
        return problem
