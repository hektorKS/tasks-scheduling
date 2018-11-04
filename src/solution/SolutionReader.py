import PathResolver
from problem.Problem import Problem
from problem.ProblemsReader import ProblemsReader
from solution.Solution import Solution


class SolutionReader:

    @staticmethod
    def read(file_path: str):
        with open(file_path, 'r') as file:
            data = file.readline().split(" ")
            data = list(map(lambda element: int(element), data))

        problem = SolutionReader.get_problem(file_path)

        cost = data[0]
        starting_point = data[1]
        tasks_order = data[2::]

        problem.starting_point = starting_point
        problem = SolutionReader.order_tasks(problem, tasks_order)
        return Solution(problem, cost)

    @staticmethod
    def order_tasks(problem: Problem, order: list):
        result = []
        for index in order:
            result.append(problem.tasks[index])
        problem.tasks = result
        return problem

    @staticmethod
    def get_problem(file_path: str):
        file_name_elements = file_path.split("/")[-1].split("_")
        file_name = file_name_elements[0] + ".txt"
        problem_number = int(file_name_elements[1]) - 1
        boundary = int(file_name_elements[2].split(".")[0]) / 10.0
        absolute_file_name = PathResolver.get_problem_file_absolute_path(file_name)
        return ProblemsReader.read(absolute_file_name, boundary)[problem_number]
