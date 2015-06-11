from flask.ext.assets import Bundle, Environment
from .. import app

bundles = {

    'base_js': Bundle(
        'js/home.js',
        output='gen/home.js'),

    'base_css': Bundle(
        'css/lib/foundation.css',
        'css/home.css',
        output='gen/home.css')

}

assets = Environment(app)

assets.register(bundles)