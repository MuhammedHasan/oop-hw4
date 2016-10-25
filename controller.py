from model import Model


class Controller:

    def get(self):
        return open('entry.html').read()

    def post(self, data):
        m = Model(data['name'], data['surname'])
        if m.validate():
            return 'Ok'
        return 'Not Ok'
