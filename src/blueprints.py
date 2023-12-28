from .routes import *

def load_blueprints(app):
    app.register_blueprint(user_login)
    app.register_blueprint(app_deployment)
    app.register_blueprint(public_web)

    # Custom loaded blueprints should be defined here
