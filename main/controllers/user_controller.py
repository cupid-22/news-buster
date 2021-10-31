from ..models.user_model import Users


def add_user(user_details):
    user_added = Users(**user_details).save()
    return user_added


def get_all_user():
    all_users = Users.query.all()
    return all_users
