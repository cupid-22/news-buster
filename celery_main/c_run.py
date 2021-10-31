from celery import Celery
from main.controllers.news_handler_controller import HandleSite
from main.helper.mail import Mail

celery_app = Celery('_fetch_news', broker='localhost:5672')


@celery_app.task
def mail_to_user_for_authenticity(news, category):
    # TODO match the news category to user to find mailing users
    mailing_user_list = news_handle_instance.find_user_per_category(category)
    news_details = news_handle_instance.find_news_details(news.id)  # Maybe here tags/preferences will be used
    # TODO Handle the mail user auth here so that when user confirms status can be updated via the tap
    for user in mailing_user_list:
        # TODO Need to render template here for confirmation receiving
        Mail(user.email).send_email(subject='News found for your feed', body=news_details.link)


@celery_app.task
def categorize_retrieved_news(news_url):
    news_handle_instance.categorize_retrieved_news(news_url)


@celery_app.task
def fetch_news():
    return news_handle_instance.load_news_apis()


if __name__ == '__main__':
    news_handle_instance = HandleSite()
    async_task = fetch_news.delay()
    for site in async_task:
        categorize_retrieved_news.delay(site)
        mail_to_user_for_authenticity.delay()
