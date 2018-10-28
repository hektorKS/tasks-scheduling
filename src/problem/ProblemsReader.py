from problem.Problem import Problem


class ProblemsReader:

    @staticmethod
    def read(file_path: str, boundary: int):
        problems = []
        with open(file_path, 'r') as file:
            data = file.read()
        lines = data.split('\n')
        counter = 0

        number_of_problems = int(lines[counter])
        counter += 1

        index = 0
        while counter < len(lines) and lines[counter] != '':
            number_of_tasks = int(lines[counter])
            counter += 1
            problems.append(Problem(lines[counter:counter + number_of_tasks], boundary, index))
            index += 1
            counter += number_of_tasks

        assert len(problems) == number_of_problems
        return problems
