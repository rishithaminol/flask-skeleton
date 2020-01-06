import os

from flask import Flask, render_template
from .login_manager import init_login
from .db import db_session


def create_app(test_config=None):
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    # assets_dir = os.path.join(__file__, 'public')

    # create and configure the app
    app = Flask(__name__, template_folder=template_dir,
                            instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    init_login(app)

    # Register all routes before return
    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('welcome.html')

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    # Register all database interaction configs before return
    
    return app
