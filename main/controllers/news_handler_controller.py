from ..models.site_model import Sites


class HandleSite:
    def __init__(self, pre_defined_sites=None):
        self.site_urls = []
        if pre_defined_sites:
            self.site_urls.extend(pre_defined_sites)

    def load_news_apis(self):
        all_sites = Sites.query.all()
        self.site_urls.extend(all_sites)

    def categorize_retrieved_news(self):
        all_sites = Sites.query.all()
        self.site_urls.extend(all_sites)
