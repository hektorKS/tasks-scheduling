import os

from problems_reader import read


def main():
    package_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(package_dir, "../resources/sch10.txt")
    problems = read(file_path)
    print(problems)
    for problem in problems:
        sum = 0
        for task in problem.tasks:
            sum += task.processing_time
        print(sum)


if __name__ == "__main__":
    main()
