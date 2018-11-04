import itertools
import random
from random import shuffle

from problem.Problem import Problem
from problemsolving.CostCounter import CostCounter
from solution.Solution import Solution


class ProblemSolver:

    @staticmethod
    def solve(problem: Problem):
        return ProblemSolver.solve_smart(problem)

    @staticmethod
    def solve_smart(problem: Problem):
        tasks = problem.tasks
        # Sort decreasing considering (L-E)/T - cost per time unit
        tasks = sorted(
            tasks,
            key=lambda item: (item.too_late_penalty - item.too_early_penalty) / item.processing_time,
            reverse=True
        )

        # Split into two parts L and R considering CDD as split point
        time_sum = 0
        left_part = []
        right_part = []
        for task in tasks:
            time_sum += task.processing_time
            if time_sum < problem.common_due_date:
                left_part.append(task)
            else:
                right_part.append(task)

        # Sort left side by E/T - increasing cost per time unit for too early delay
        left_part = sorted(left_part, key=lambda item: item.too_early_penalty / item.processing_time)
        # Sort right side by L/T - decreasing cost per time unit for too late delay
        right_part = sorted(right_part, key=lambda item: item.too_late_penalty / item.processing_time, reverse=True)
        # Connect L and R
        problem.tasks = left_part + right_part

        # Move starting point from 0 to CDD searching for minimum cost
        costs = []
        for index in range(problem.common_due_date):
            problem.starting_point = index
            costs.append(CostCounter.count(problem))
        min_cost_index = costs.index(min(costs))
        problem.starting_point = min_cost_index

        return Solution(problem, costs[min_cost_index])

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
