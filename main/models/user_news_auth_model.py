from . import db
from sqlalchemy.orm import validates, relationship
from dataclasses import dataclass
from .base_model import BaseModel


@dataclass
class NewsUserAuth(BaseModel):
    id: int
    status: bool

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.BOOLEAN, default=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), unique=True)

    users = db.relationship('Users', backref=db.backref('NewsUserAuth', lazy=True))
    news = db.relationship('Sites', backref=db.backref('NewsUserAuth', lazy=True))

    @validates('link')
    def validate_site_link(self, key, link):
        if not link:
            raise AssertionError('Site link cannot be blank.')
        if Sites.query.filter(Sites.link == link).first():
            raise AssertionError('The site link {} already exists'.format(link))
        if len(link) < 2:
            raise AssertionError('Site link must be greater than 2 characters.')
        return link
