from ..models.user_model import Users


def add_user(**user_details: object) -> bool:
    user_added = Users(**user_details).save()
    return user_added


def get_all_user() -> list:
    all_users = Users.query.all()
    return all_users


def get_user_by_category(tag) -> list:
    user_list = Users.query.filter(Users.Tag == tag).first()
    return user_list
