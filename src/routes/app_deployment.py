from flask import Blueprint, render_template, \
                   request, jsonify, session, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user

app_deployment = Blueprint('app_deployment', __name__, url_prefix='/codedeployment')

# Common response format
comm_respon = {
    'data':'',
    'message': '',
    'err_msg': '',
    'status': 200
}

@app_deployment.route('/', methods=['POST', 'GET'], strict_slashes=False)
def codedeploy():
    for key, val in request.form.items():
        print("%s:%s" % (key, val))

    return jsonify(comm_respon), comm_respon['status']
