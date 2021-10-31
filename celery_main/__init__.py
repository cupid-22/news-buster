from celery import Celery
from main import app
from time import sleep

celery_app = Celery('_fetch_news',
                    broker=app.config.get('RABBIT_MQ'),
                    backend=app.config.get('DB_URI')
                    )


@celery_app.task
def fetch_news():
    sleep(5)
    return 'Working'

