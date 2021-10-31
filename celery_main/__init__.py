from celery import Celery
from main import app

celery_app = Celery('_fetch_news',
                    broker=app.config.get('RABBIT_MQ'),
                    backend=app.config.get('DB_URI')
                    )


@celery_app.task
def fetch_news():
    print('Working')
