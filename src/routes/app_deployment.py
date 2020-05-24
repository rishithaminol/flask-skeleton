from flask import Blueprint, render_template, \
                   request, jsonify, session, redirect, url_for
from src.core import common_response

app_deployment = Blueprint('app_deployment', __name__, url_prefix='/codedeployment')

@app_deployment.route('/', methods=['POST', 'GET'], strict_slashes=False)
def codedeploy():
    for key, val in request.form.items():
        print("%s:%s" % (key, val))

    return common_response(data={'hello':'world'})

## 500 error producer in production environments
@app_deployment.route('/error_500', methods=['POST', 'GET'], strict_slashes=False)
def error_500():
    x = 2/0

    return common_response(data={'hello':'world'})
