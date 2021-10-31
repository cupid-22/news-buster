from ..models.site_model import Sites


def add_site(site_link: str) -> bool:
    site_added = Sites(link=site_link).save()
    return site_added


def get_all_site() -> list:
    all_sites = Sites.query.all()
    return all_sites
