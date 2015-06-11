from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {'db': 'astspace'}

db = MongoEngine(app)


from ast_space.home import views
