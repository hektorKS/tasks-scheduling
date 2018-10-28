from problemsolving.CostCounter import CostCounter
from solution.Solution import Solution


class SolutionValidator:

    @staticmethod
    def validate(solution: Solution):
        print(solution.problem)
        expected = CostCounter.count(solution.problem)
        print("Expected: {}".format(expected))
        actual = solution.cost
        print("Actual: {}".format(actual))
        return actual == expected
