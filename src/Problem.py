from Task import Task


class Problem:
    def __init__(self, lines):
        self.tasks = []
        for line in lines:
            data = line.strip().split()
            data = list(filter(lambda x: len(x) > 0, data))
            data = list(map(lambda x: int(x), data))
            self.tasks.append(Task(data[0], data[1], data[2]))

