from . import db
from sqlalchemy.orm import validates
from dataclasses import dataclass
from .base_model import BaseModel


@dataclass
class Sites(BaseModel):
    link: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.TEXT, nullable=False)

    @validates('link')
    def validate_site_link(self, key, link):
        if not link:
            raise AssertionError('Site link cannot be blank.')
        if Sites.query.filter(Sites.link == link).first():
            raise AssertionError('The site link {} already exists'.format(link))
        if len(link) < 2:
            raise AssertionError('Site link must be greater than 2 characters.')
        return link

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Site {self.link!r}>'
