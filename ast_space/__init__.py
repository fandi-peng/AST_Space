from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)

# set CSRF
app.config.from_object('config')

# database settings
app.config['MONGODB_SETTINGS'] = {'db': 'astspace'}
db = MongoEngine(app)

# register blueprints here
from ast_space.views.home import home
app.register_blueprint(home)


from .util import assets