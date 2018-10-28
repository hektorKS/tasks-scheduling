from solution.Solution import Solution


class SolutionWriter:
    @staticmethod
    def write(file_name: str, solution: Solution):
        with open(file_name, 'w') as file:
            file.write(str(solution))
