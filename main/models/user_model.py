from . import db
from dataclasses import dataclass
from sqlalchemy.orm import validates
import re
from .base_model import BaseModel


@dataclass
class Users(BaseModel):
    name: str
    email: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # users = db.relationship("NewsUserAuth", backref=db.backref('Users', lazy=True))

    @validates('name')
    def validate_user_name(self, key, name):
        if not name:
            raise AssertionError('User name cannot be blank.')
        if Users.query.filter(Users.name == name).first():
            raise AssertionError('The name {} already exists'.format(name))
        if len(name) < 2:
            raise AssertionError('Name must be greater than 2 characters.')
        return name

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('Email cannot be blank.')
        if not re.search("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email):
            raise AssertionError(f"{email} is not a Valid Email Id")
        if Users.query.filter(Users.email == email).first():
            raise AssertionError(f'User with this {email} email already exists.')
        return email
