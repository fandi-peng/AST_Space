from ast_space import db
import datetime

# models for the database

class Talk(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=120, required=True)
    author = db.StringField(max_length=100, required=True)
    body = db.StringField(required=True)