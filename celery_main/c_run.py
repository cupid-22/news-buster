from celery import Celery
from main.controllers.news_handler_controller import HandleSite

celery_app = Celery('_fetch_news', broker='localhost:5672')

news_handle_instance = HandleSite()


@celery_app.task
def mail_to_user_for_authenticity():
    pass


@celery_app.task
def categorize_retrieved_news():
    pass


@celery_app.task
def fetch_news():
    news_handle_instance.load_news_apis()


if __name__ == '__main__':
    async_task = fetch_news()
    if async_task == 'SUCCESS':
        categorize_retrieved_news.delay()
