from enum import Enum
from app.extensions import db
from sqlalchemy import UniqueConstraint

class UserType(Enum):
    user = "user"
    admin = "admin"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    usertype = db.Column(db.Enum(UserType), nullable=False, default=UserType.user)  # Use Enum here

    def __repr__(self):
        return f'<User {self.username}>'


class Prices(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    crop = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    price_per_kg = db.Column(db.Float, nullable=False)
    price_per_kg_retail = db.Column(db.Float, nullable=False)

    __table_args__ = (
        UniqueConstraint('crop', 'region', name='uix_crop_region'),
    )

    def __repr__(self):
        return f'<Prices {self.crop}>'
