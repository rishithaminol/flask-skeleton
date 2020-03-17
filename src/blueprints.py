from .routes import *

def load_blueprints(app):
    app.register_blueprint(user_login)
    app.register_blueprint(app_deployment)

    # Custom loaded blueprints should be defined here
