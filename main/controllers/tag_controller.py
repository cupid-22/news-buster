from ..models.tags_model import Tags


def add_tag(tag_name: str) -> bool:
    tag_added = Tags(tag_name).save()
    return tag_added


def get_all_tag() -> list:
    all_tag = Tags.query.all()
    return all_tag
