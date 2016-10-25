from model import Model


class Controller:

    def get(self):
        return open('views/entry.html').read()

    def post(self, data):
        m = Model(data['name'], data['surname'])
        if m.validate():
            return open('views/ok.html').read()
        return open('views/notok.html').read()
