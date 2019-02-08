from typing import Dict, Union

from flask_app import db
from utils import create_md5_hash


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, index=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = create_md5_hash(password)

    def verify_password(self, password) -> bool:
        return self.password == create_md5_hash(password)

    def to_json(self) -> Dict[str, Union[int, str]]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
