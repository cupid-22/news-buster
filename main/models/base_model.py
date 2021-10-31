from . import db


class BaseModel(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DATETIME, default=db.func.now())
    updated_at = db.Column(db.DATETIME, default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()
        return True
