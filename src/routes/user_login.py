from flask import Blueprint, render_template, \
                   request, jsonify, session, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from src.login_manager import access_privilage, User
from src.core import gen_user_pass_hash, check_user_credentials

user_login = Blueprint('user_login', __name__, url_prefix='/user')

@user_login.route('/login', methods=['POST', 'GET'], strict_slashes=False)
def sign_in():
    if request.method == 'POST':
        username = request.form.get('user_name')
        password = request.form.get('password')

        if check_user_credentials(username, gen_user_pass_hash(password)):
            user_data = User(username)
            login_user(user=user_data)

    if current_user.is_authenticated:
        return redirect('/')

    return render_template('login.html')

@user_login.route('/logout', methods=['GET'], strict_slashes=False)
def sign_out():
    logout_user()

    return redirect(url_for('user_login.sign_in', _external=True))
