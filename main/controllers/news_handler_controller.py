from .site_controller import get_all_site
from .user_controller import get_user_by_category
from ..models.news_model import News


class HandleSite:
    def __init__(self, pre_defined_sites=None):
        self.site_urls = []
        if pre_defined_sites:
            self.site_urls.extend(pre_defined_sites)

    def load_news_apis(self):
        all_sites = get_all_site()
        self.site_urls.extend(all_sites)

    @staticmethod
    def find_news_details(news_id):
        news_details = News.query.filter(id=news_id).first()
        return news_details

    @staticmethod
    def find_user_per_category(categories):
        news_details = get_user_by_category(categories)
        return news_details

    def categorize_retrieved_news(self, news_url):
        return News.query.filter(url=news_url)
