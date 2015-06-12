from flask.ext.assets import Bundle, Environment
from .. import app


# a way to organize static files
bundles = {

    'base_css': Bundle(
        'css/lib/foundation.css',
        'css/lib/normalize.css',
        'css/app.css',
        filters='cssmin',
        output='gen/base.css'),

    'base_js': Bundle(
        'js/app.js',
        'js/lib/vendor/modernizr.js',
        filters='jsmin',
        output='gen/base.js',
        ),

    'bottom_js': Bundle(
        'js/lib/vendor/jquery.js',
        'js/lib/foundation.min.js',
        filters='jsmin',
        output='gen/bottom.js',
        )
}

assets = Environment(app)
assets.register(bundles)