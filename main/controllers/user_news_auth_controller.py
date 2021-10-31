from ..models.user_news_auth_model import NewsUserAuth


def add_users_response(**response_detail: object) -> bool:
    user_news_auth_added = NewsUserAuth(**response_detail).save()
    return user_news_auth_added


def get_all_users_response() -> list:
    all_response = NewsUserAuth.query.all()
    return all_response
