from celery import Celery
from main.controllers.news_handler_controller import HandleSite

celery_app = Celery('_fetch_news',
                    broker='localhost:5672')


@celery_app.task
def fetch_news():
    news_handle_instance = HandleSite()
    news_handle_instance.load_news_apis()
    print(news_handle_instance.site_urls)


if __name__ == '__main__':
    fetch_news()
