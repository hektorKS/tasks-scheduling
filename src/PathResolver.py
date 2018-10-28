import os

from src import SOLUTIONS_DIRECTORY_PATH, PROBLEMS_DIRECTORY_PATH, VALIDATION_DIRECTORY_PATH


def get_problem_file_absolute_path(file_name: str):
    package_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(package_dir, PROBLEMS_DIRECTORY_PATH + file_name)


def get_solution_file_absolute_path(file_name: str):
    package_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(package_dir, SOLUTIONS_DIRECTORY_PATH + file_name)


def get_validation_absolute_file_path(file_name: str):
    package_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(package_dir, VALIDATION_DIRECTORY_PATH + file_name)
