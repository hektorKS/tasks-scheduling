import os

from Problem import Problem
from ProblemResolver import ProblemResolver
from ProblemsReader import ProblemsReader

BOUNDARY = 0.2
FILE_PATH = "../resources/data/sch10.txt"
SOLUTIONS_FOLDER_PATH = "../resources/solutions/{}_{}_{}.txt"


def get_solution_file_name_for_problem(problem: Problem):
    file_name = FILE_PATH.split("/")[-1].split(".")[0]
    return SOLUTIONS_FOLDER_PATH.format(file_name, problem.index, int(BOUNDARY * 10))


def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))


def main():
    package_dir = get_current_directory()
    file_path = os.path.join(package_dir, FILE_PATH)
    problems = ProblemsReader.read(file_path, BOUNDARY)
    for problem in problems:
        print("Index: {}, Processing time: {}, Common due date: {}"
              .format(problem.index, problem.problem_processing_time, problem.common_due_date))

    for problem in problems:
        file_name = get_solution_file_name_for_problem(problem)
        with open(file_name, 'w') as file:
            file.write(str(ProblemResolver.resolve(problem)))


if __name__ == "__main__":
    main()
