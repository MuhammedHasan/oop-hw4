import socket
from thread import *
from controller import Controller
import re


class Server:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', 9001))
        self.controller = Controller()

    def run(self):
        self.sock.listen(5)
        while True:
            client, addr = self.sock.accept()
            start_new_thread(Server.client_process, (self, client))

    def client_process(self, client):
        data = client.recv(8024)
        res = ''
        if data[:3] == 'GET':
            res = self.controller.get()
        elif data[:4] == 'POST':
            res = self.controller.post(self.req_content(data))
        client.send(res)
        client.close()

    def req_content(self, req):
        return {
            'name': re.findall('name=?.+&', req)[0][5:-1],
            'surname': re.findall('surname=?.+', req)[0][8:]
        }

if __name__ == "__main__":
    s = Server()
    s.run()
