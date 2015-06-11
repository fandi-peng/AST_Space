from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object('config')
app.config['MONGODB_SETTINGS'] = {'db': 'astspace'}
db = MongoEngine(app)


# register blueprints here
from .home.views import home
app.register_blueprint(home)

