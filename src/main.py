import os

from ProblemsReader import ProblemsReader

BOUNDARY = 0.2


def main():
    package_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(package_dir, "../resources/sch10.txt")
    problems = ProblemsReader.read(file_path, BOUNDARY)
    for problem in problems:
        print("Processing time: " + str(problem.problem_processing_time) +
              ", Common due date: " + str(problem.common_due_date))


if __name__ == "__main__":
    main()
