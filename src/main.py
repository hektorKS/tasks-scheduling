import os

from ProblemsReader import ProblemsReader

BOUNDARY = 0.2
FILE_PATH = "../resources/data/sch10.txt"


def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))


def main():
    package_dir = get_current_directory()
    file_path = os.path.join(package_dir, FILE_PATH)
    problems = ProblemsReader.read(file_path, BOUNDARY)
    for problem in problems:
        print("Processing time: {}, Common due date: {}"
              .format(problem.problem_processing_time, problem.common_due_date))


if __name__ == "__main__":
    main()
