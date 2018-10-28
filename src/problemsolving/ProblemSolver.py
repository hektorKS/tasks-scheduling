import itertools
from random import shuffle

from problem.Problem import Problem
from problemsolving.CostCounter import CostCounter
from solution.Solution import Solution


class ProblemSolver:

    @staticmethod
    def solve_with_permutations(problem: Problem):
        # tasks_permutations = list(itertools.permutations(range(len(problem.tasks))))
        tasks_permutations = [[4, 0, 6, 1, 5, 7, 8, 2, 3, 9]]
        tasks_costs = []
        for permutation in tasks_permutations:
            print(permutation)
            problem = ProblemSolver.order_tasks(problem, permutation)
            tasks_costs.append(CostCounter.count(problem))

        min_cost_index = tasks_costs.index(min(tasks_costs))
        optimal_problem = ProblemSolver.order_tasks(problem, tasks_permutations[min_cost_index])
        optimal_cost = tasks_costs[min_cost_index]
        return Solution(optimal_problem, optimal_cost)

    @staticmethod
    def solve_random(problem: Problem):
        shuffle(problem.tasks)
        cost = CostCounter.count(problem)
        return Solution(problem, cost)

    @staticmethod
    def order_tasks(problem: Problem, order: list):
        result = []
        for index in order:
            result.append(problem.tasks[index])
        problem.tasks = result
        return problem
