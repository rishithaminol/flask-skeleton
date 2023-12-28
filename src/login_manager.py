from flask import request, redirect
from src.flask_login import LoginManager, UserMixin, \
						current_user, login_required
from functools import wraps
from src.core import get_user_data, common_response
from src.menu_nav import al_separation
from src.log_manager import CreateLogger
log_ = CreateLogger(__name__, './login_manager.log')

# silly user model (create 'current_user' object)
class User(UserMixin):
    def __init__(self, id_, session_id=None):
        self.malfunction = False
        self._is_authenticated = True
        self._is_zombie = False

        x = get_user_data(id_, session_id)
        if x:
            self.id = id_
            self.name = str(id_)
            self.access_level = x[3]
            self.id_user = x[0] # User's id number according to the database
            self.session_id = x[4]
            self.expire = x[5]
        else:
            self.malfunction = True
            self._is_authenticated = False

            # Still active session even if database end the session
            if len(session_id) > 0 or len(id_) > 0:
                self._is_zombie = True
            log_.warning("Session handling mis alignment")

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
    login_manager.session_protection = "none"

    @login_manager.user_loader
    def load_user(userid, session_id):
        x = User(userid, session_id)

        if x._is_zombie:
            return x

        if x.malfunction:
            return None
        return x

    @login_manager.unauthorized_handler
    def unauth_handler():
        return redirect('/user/login')
