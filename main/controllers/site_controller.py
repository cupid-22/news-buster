from ..models.site_model import Sites


def add_site(site_name):
    site_added = Sites(link=site_name).save()
    return site_added


def get_all_site():
    all_tag = Sites.query.all()
    return all_tag
