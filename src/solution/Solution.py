from problem.Problem import Problem


class Solution:
    def __init__(self, problem: Problem, cost: int):
        self.problem = problem
        self.cost = cost

    def __str__(self):
        return "{} {} {}".format(self.cost, self.problem.starting_point,
                                 " ".join(map(lambda task: str(task.task_id), self.problem.tasks)))

    @staticmethod
    def get_file_name_for_solution(problem: Problem, config):
        return "{}_{}_{}.txt".format(config["solving"]["file_name"].split(".")[0],
                                     problem.index, int(config["boundary"] * 10))
