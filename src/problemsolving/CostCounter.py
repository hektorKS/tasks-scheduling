from problem.Problem import Problem


class CostCounter:

    @staticmethod
    def count(problem: Problem):
        cost = 0
        actual_point_in_time = problem.starting_point
        for task in problem.tasks:
            task_end_point = actual_point_in_time + task.processing_time
            # Too late cost
            if task_end_point > problem.common_due_date:
                cost += (task_end_point - problem.common_due_date) * task.too_late_penalty
            # Too early cost
            if task_end_point < problem.common_due_date:
                cost += (problem.common_due_date - task_end_point) * task.too_early_penalty
            actual_point_in_time += task.processing_time
        return cost
