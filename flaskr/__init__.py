import os

from flask import Flask
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
from flaskr.config import Config

db=SQLAlchemy()

def create_app(config_class = Config, test_config=False):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)

    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'




    return app