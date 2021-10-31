from . import db
from sqlalchemy.orm import validates, relationship
from dataclasses import dataclass
from .base_model import BaseModel


@dataclass
class Sites(BaseModel):
    link: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    link = db.Column(db.TEXT, nullable=False)

    # news_sites = db.relationship("News", backref=db.backref('Sites', lazy=True))

    @validates('link')
    def validate_site_link(self, key, link):
        if not link:
            raise AssertionError('Site link cannot be blank.')
        if Sites.query.filter(Sites.link == link).first():
            raise AssertionError('The site link {} already exists'.format(link))
        if len(link) < 2:
            raise AssertionError('Site link must be greater than 2 characters.')
        return link

    def __repr__(self):
        return f'<Site {self.link!r}>'
