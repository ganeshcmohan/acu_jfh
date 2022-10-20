from db import db
from typing import List
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash



class UserModel(db.Model):
    """This model has only read access"""

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False, unique=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class AcuReportModel(db.Model):
    __tablename__ = "acureport"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    search_keyword = db.Column(db.String(80), nullable=True)
    address = db.Column(db.String(200), nullable=True)


    def __init__(self, search_keyword, address):
        self.search_keyword = search_keyword
        self.address = address


    def __repr__(self):
        return "OrderModel(search_keyword=%s, address=%s)" % (
            self.search_keyword,
            self.address,
        )

    def json(self):
        return {
            "order_id": self.order_id,
            "search_keyword": self.search_keyword,
            "address": self.address
        }

    @classmethod
    def find_by_id(cls, _id) -> "AcuReportModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["AcuReportModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
