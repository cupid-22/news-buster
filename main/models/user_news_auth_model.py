from . import db
from sqlalchemy.orm import validates
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

    # users = db.relationship('NewsUserAuth', backref=db.backref('Users', lazy=True))
    # news = db.relationship('Sites', backref=db.backref('NewsUserAuth', lazy=True))

    @validates('status')
    def validate_status(self, key, status):
        assert type(status) is not bool
