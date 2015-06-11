from ast_space import db
import datetime


class Post(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.StringField(max_length=100, required=True)
    body = db.StringField(required=True)