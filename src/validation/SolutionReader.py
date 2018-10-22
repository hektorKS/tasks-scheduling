class SolutionReader:

    @staticmethod
    def read(file_path: str):
        with open(file_path, 'r') as file:
            data = file.read()
        line = data.split("\n")[0]

