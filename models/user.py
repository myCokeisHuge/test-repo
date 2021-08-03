
# user created file imports
from app_code.db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):  # init is the create method, used when a new instance is created
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()  # SELECT TOP 1 * FROM __tablename__ WHERE name=name

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()  # SELECT TOP 1 * FROM __tablename__ WHERE id=id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
