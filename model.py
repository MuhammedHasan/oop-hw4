import json


class Model:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def validate(self):
        data = json.load(open('names.txt'))
        return data['name'] == self.name and data['surname'] == self.surname
