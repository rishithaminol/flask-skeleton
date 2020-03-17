import os

from flask import Flask, render_template, send_from_directory
from .login_manager import init_login, access_privilage
from .db import db_session
from .routes import user_login, app_deployment


def create_app(test_config=None):
    real_path = os.path.realpath(__file__)
    template_dir = os.path.join(os.path.dirname(real_path), 'templates')
    assets_dir = os.path.join(os.path.dirname(real_path), 'public')
    base_dir = os.path.dirname(real_path) # src - directory

    # create and configure the app
    app = Flask(__name__, template_folder=template_dir,
                            instance_path=base_dir)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    init_login(app)

    # Register all routes before return
    # a simple page that says hello
    @app.route('/')
    @access_privilage
    def index():
        return render_template('index.html')

    @app.route('/public/<path:filepath>')
    def public(filepath):
        return send_from_directory(assets_dir, filepath)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    # Register all database interaction configs before return
    
    return app
