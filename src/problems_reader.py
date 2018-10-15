from Problem import Problem


def read(file_path):
    problems = []
    with open(file_path, 'r') as file:
        data = file.read()
    lines = data.split('\n')
    counter = 0

    number_of_problems = int(lines[counter])
    counter += 1

    while counter < len(lines) and lines[counter] != '':
        number_of_tasks = int(lines[counter])
        counter += 1

        problems.append(Problem(lines[counter:counter + number_of_tasks]))
        counter += number_of_tasks

    assert len(problems) == number_of_problems
    return problems
