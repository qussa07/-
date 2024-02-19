import io
import logging
from json import dumps
from time import sleep

from flask import Flask
from multiprocessing import Process
from contextlib import contextmanager, redirect_stdout

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = [
        {"receipt": "king`s fried egg", "egg": 3, "salt": 1},
        {"receipt": "fried egg", "egg": 2, "salt": 1},
        {"receipt": "fried egg with cheese", "egg": 2, "cheese": 2, "salt": 1},
        {"receipt": "omelette", "egg": 2, "salt": 1, "milk": 1},
        {"receipt": "omelette with cheese", "egg": 2, "cheese": 2, "salt": 1, "milk": 2},
        {"receipt": "omelette with cheese and bacon", "egg": 2, "cheese": 2, "bacon": 1, "salt": 1, "milk": 1}
    ]

    server = Server('127.0.0.1', 5000, data)
    with server.run():
        while (row := input('Введите "stop" для завершения работы сервера: ')) != 'stop':
            ...
