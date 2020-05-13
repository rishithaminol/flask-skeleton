"""
* User sanitization mecanisms
* User input validation mechanisms
* Authentication mechanisms (token based, etc..)
* In the future please log all the malicious events with X-Request-Id then logging systems can track.
* This security module catches X-Request-Id header and logs it in malicious incidents (In the future)
"""

from functools import wraps
from flask import request, abort
from src.core import common_response

"""
Perform request validation on the fly without making python flask
views complex.
"""
def request_manipulator(max_length=2048):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cl = request.content_length
            if cl is None:
                return common_response(status=413, err_msg='Missing body content')
            if cl is not None and cl > max_length:
                return common_response(status=413, err_msg='Maximum request body length {}'.format(max_length))
            return f(*args, **kwargs)
        return wrapper
    return decorator
