from . import db
from flask_login import UserMixin

# class Image(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     img_src = db.Column(db.Text)
#     type = db.Column(db.Integer, primary_key=True)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    Nickname = db.Column(db.String(150))
    