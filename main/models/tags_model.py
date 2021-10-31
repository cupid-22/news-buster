from . import db
from dataclasses import dataclass
from sqlalchemy.orm import validates


@dataclass
class Tags(db.Model):
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    @validates('name')
    def validate_tag_name(self, key, name):
        if not name:
            raise AssertionError('Tag name cannot be blank.')
        if Tags.query.filter(Tags.name == name).first():
            raise AssertionError('The tag name {} already exists'.format(name))
        if len(name) < 2:
            raise AssertionError('Tag name must be greater than 2 characters.')
        return name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    def __repr__(self):
        return f'<Tag {self.name!r}>'
