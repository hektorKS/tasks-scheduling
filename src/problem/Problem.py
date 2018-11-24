from Task import Task


class Problem:
    def __init__(self, lines: str, boundary: float, problem_index: int):
        self.tasks = []
        for index, line in enumerate(lines):
            self.__load_task_from_line(index, line)
        self.problem_processing_time = sum(map(lambda element: element.processing_time, self.tasks))
        self.common_due_date = int(self.problem_processing_time * boundary)
        self.starting_point = 0
        self.index = problem_index

    def __load_task_from_line(self, index: int, line: str):
        filtered_line_data = filter(lambda element: len(element) > 0, line.strip().split())
        data = list(map(lambda element: int(element), filtered_line_data))
        self.tasks.append(Task(index, data[0], data[1], data[2]))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return \
            "Problem(\n  repr: [{}],\n  tasks: {},\n  common_due_date: {},\n  starting_point: {},\n  index: {}\n)" \
            .format(
                repr(self),
                [str(task) for task in self.tasks],
                self.common_due_date,
                self.starting_point,
                self.index
            )
