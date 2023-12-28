from flask import Blueprint, render_template, \
                   request, redirect, url_for
from src.flask_login import login_user, logout_user, current_user
from src.login_manager import User
from src.core import gen_user_pass_hash, check_user_credentials

user_login = Blueprint('user_login', __name__, url_prefix='/user')

@user_login.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def sign_in():
    data = {
        'message': "",
        'login_failure': False,
        'response_code': 200
    }

    if request.method == 'POST':
        username = request.form.get('user_name')
        password = request.form.get('password')

        if username is None or password is None:
            data['message'] = "Empty fields not allowed"
            data['login_failure'] = True
            data['response_code'] = 401
            return render_template('login.html', data=data), data['response_code']

        if check_user_credentials(username, gen_user_pass_hash(password)):
            user_data = User(username)
            login_user(user=user_data)
        else:
            data['message'] = "Username or email does not exists"
            data['login_failure'] = True
            data['response_code'] = 401

    if hasattr(current_user, '_is_zombie') and current_user._is_zombie:
        logout_user()

    if current_user.is_authenticated:
        return redirect('/')

    return render_template('login.html', data=data), data['response_code']

@user_login.route('/logout', methods=['GET'], strict_slashes=False)
def sign_out():
    logout_user()

    return redirect(url_for('user_login.sign_in', _external=True))
