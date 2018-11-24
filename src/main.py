import time

import PathResolver
from config.ConfigLoader import ConfigLoader
from problem.ProblemsReader import ProblemsReader
from problemsolving.HeuristicProblemSolver import HeuristicProblemSolver
from problemsolving.ProblemSolver import ProblemSolver
from solution.Solution import Solution
from solution.SolutionReader import SolutionReader
from solution.SolutionWriter import SolutionWriter
from validation.SolutionValidator import SolutionValidator


def solving(config):
    # read problems from file
    file_name = config["solving"]["file_name"]
    problems_file_path = PathResolver.get_problem_file_absolute_path(file_name)
    problems = ProblemsReader.read(problems_file_path, config["boundary"])
    # solve problem
    for index in config["solving"]["problems"]:
        problem = problems[index - 1]
        start_time = time.time()
        solution = ProblemSolver.solve(problem)
        # Heuristic solving
        if config["solving"]["use_heuristic"]:
            processing_time = config["heuristic"]["processing_time"]
            max_tabu_list_size = config["heuristic"]["max_tabu_list_size"]
            heuristic_problem_solver = HeuristicProblemSolver(start_time, processing_time, max_tabu_list_size)
            solution = heuristic_problem_solver.solve(solution.problem)
        print("Processing time[{}]: {}s".format(index, round(time.time() - start_time, 5)))
        # save solution
        solution_file_name = Solution.get_file_name_for_solution(problem, config)
        solution_file_path = PathResolver.get_solution_file_absolute_path(solution_file_name)
        SolutionWriter.write(solution_file_path, solution)


def validation(config):
    # validate solution
    file_name = config["validation"]["file_name"]
    solution_file_path = PathResolver.get_validation_absolute_file_path(file_name)
    solution = SolutionReader.read(solution_file_path)
    validation_result = SolutionValidator.validate(solution)
    print("Validation result for solution[{}]: {}".format(file_name, validation_result))


def main():
    # read config
    config = ConfigLoader.read()
    solving(config)
    # validation(config)


if __name__ == "__main__":
    main()
