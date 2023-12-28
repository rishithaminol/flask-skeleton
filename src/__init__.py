import os

from flask import Flask, send_from_directory, request
from src.login_manager import init_login
from src.db import db_session
from src.flask_error_handlers import init_error_handler


def create_app(test_config=None):
    real_path = os.path.realpath(__file__)
    template_dir = os.path.join(os.path.dirname(real_path), 'templates')
    assets_dir = os.path.join(os.path.dirname(real_path), 'public')
    base_dir = os.path.dirname(real_path) # src - directory

    # create and configure the app
    app = Flask(__name__, template_folder=template_dir,
                            instance_path=base_dir,
                            static_folder=None)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    init_login(app)

    @app.route('/robots.txt', methods=['GET'])
    @app.route('/sitemap.xml', methods=['GET'])
    def seo():
        print(request.path[1:])
        return send_from_directory(assets_dir, request.path[1:])

    @app.route('/public/<path:filepath>')
    def public(filepath):
        return send_from_directory(assets_dir, filepath)

    @app.after_request
    def fake_response_headers(response):
        # Fake response headers
        response.headers["Server"] = "Microsoft-IIS/8.5"
        response.headers["X-AspNet-Version"] = "4.0.30319"
        response.headers["X-Powered-By"] = "ASP.NET"
        return response

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    # Flask error handlers section
    init_error_handler(app)

    # Register all database interaction configs before return
    
    return app
