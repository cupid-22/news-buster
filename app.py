from flask import Flask
from celery import Celery

flask_app = Flask(__name__)
celery_app = Celery()


@flask_app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    flask_app.run()
