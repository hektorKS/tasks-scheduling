from Task import Task


class Problem:
    def __init__(self, lines: str, boundary: float):
        self.tasks = []
        for line in lines:
            filtered_line_data = filter(lambda element: len(element) > 0, line.strip().split())
            data = list(map(lambda element: int(element), filtered_line_data))
            self.tasks.append(Task(data[0], data[1], data[2]))
        self.problem_processing_time = sum(map(lambda element: element.processing_time, self.tasks))
        self.common_due_date = int(self.problem_processing_time * boundary)

