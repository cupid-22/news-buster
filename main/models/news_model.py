from . import db
from dataclasses import dataclass
from sqlalchemy.orm import validates

from .base_model import BaseModel


@dataclass
class News(BaseModel):
    name: str
    title: str
    body: str
    url: str
    site_id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=True)
    url = db.Column(db.String(120), unique=True, nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), unique=True)

    site = db.relationship('Sites', backref=db.backref('News', lazy=True))
    news = db.relationship("News", backref=db.backref('NewsUserAuth', lazy=True))

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise AssertionError('News title cannot be blank.')
        return title

    @validates('link')
    def validate_site_link(self, key, link):
        if not link:
            raise AssertionError('News link cannot be blank.')
        if News.query.filter(News.link == link).first():
            raise AssertionError('The news link {} already exists'.format(link))
        if len(link) < 2:
            raise AssertionError('News link must be greater than 2 characters.')
        return link

    #
    # @validates('body')
    # def validate_email(self, key, body):
    #     if not body:
    #         raise AssertionError('Body cannot be blank.')
    #     return body

    def __repr__(self):
        return f'<News {self.name!r}>'
