from flask import request, redirect, render_template
from flask_login import LoginManager, UserMixin, \
						login_user, \
						current_user
from .core import check_user_credentials, gen_user_pass_hash


def init_login(app):
    # flask-login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user_login_" # see methodname user_login_():

    # silly user model (create 'current_user' object)
    class User(UserMixin):
        def __init__(self, id_):
            self.malfunction = False

            try:
                x = get_user_data(id_)
                self.id = id_
                self.name = str(id_)
                self.user_id = x.user_id
                self.access_level = x.access_level
            except:
                self.malfunction = True

        def __repr__(self):
            return "%d/%s" % (self.id, self.name)

    @login_manager.user_loader
    def load_user(userid):
        x = User(userid)
        if x.malfunction:
            return None
        return x

    @app.route("/login", methods=['GET', 'POST'])
    def user_login_():
        if request.method == 'POST':
            username = request.form.get('user_name')
            password = request.form.get('user_password')

            if (username != None and password != None) \
                    and check_user_credentials(username, gen_user_pass_hash(password)):
                user = User(username)
                login_user(user)

        if current_user.is_authenticated:
            return redirect('/')

        return render_template('login.html')
