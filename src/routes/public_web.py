from flask import Blueprint, render_template

public_web = Blueprint('public_web', __name__, url_prefix='/')

@public_web.route('/', methods=['GET'], strict_slashes=False)
def index_():
    return render_template('index.html')
