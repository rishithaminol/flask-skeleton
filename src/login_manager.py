from flask import request, redirect, render_template, _request_ctx_stack, jsonify
from flask_login import LoginManager, UserMixin, \
						login_user, \
						current_user, login_required
from functools import wraps
from .core import check_user_credentials, gen_user_pass_hash, get_user_data, common_response
from .menu_nav import al_separation

# silly user model (create 'current_user' object)
class User(UserMixin):
    def __init__(self, id_):
        self.malfunction = False
        self._is_authenticated = True

        try:
            x = get_user_data(id_)
            self.id = id_
            self.name = str(id_)
            self.access_level = x.access_level
            self.id_user = x.id_ # User's id number according to the database
        except:
            self.malfunction = True
            self._is_authenticated = False

        if self.malfunction:
            print("====== Malfunction occured =====")

    @property
    def is_authenticated(self):
        return self._is_authenticated

    def __repr__(self):
        return "%d/%s" % (self.id, self.name)

# This function restricts spcific users based on specific rules
# if the given user meets the specific requirements, this continues
#    execution otherwise stops execution
def access_privilage(func):
    @wraps(func)
    @login_required
    def decorated_view(*args, **kwargs):
        found_ = False
        for i in al_separation:
            if  ((current_user.access_level in i['access_levels']) or (-1 in i['access_levels'])) \
                 and (i['endpoint'] == request.endpoint):
                found_ = True
                break

        if found_:
            return func(*args, **kwargs)
        else:
            return common_response(status=401, err_msg='Access level unauthorized')

    return decorated_view

def init_login(app):
    # flask-login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user_login.sign_in" # see methodname user_login_():

    @login_manager.user_loader
    def load_user(userid):
        x = User(userid)
        if x.malfunction:
            return None
        return x
