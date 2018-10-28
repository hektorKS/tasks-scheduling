import json


class ConfigLoader:
    @staticmethod
    def read():
        with open('../config.json') as file:
            data = json.load(file)
        return data
