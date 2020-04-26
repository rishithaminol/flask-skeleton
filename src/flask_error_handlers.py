import os, traceback
from flask import render_template, request
from src.log_manager import CreateLogger
from src.core import common_response

def init_error_handler(app):
    # For DEBUGING purposes
    # If this is production, client side does no get debugging
    #  output and all the server side errors are logged into the
    #  `server.log` file.
    if os.getenv('ENV') == 'production':
        @app.errorhandler(404)
        def _404(e):
            return common_response(status=404, err_msg='Not Found')

        # http://werkzeug.pocoo.org/docs/0.14/exceptions/
        @app.errorhandler(Exception)
        def exception_handler(error):
            print("Printing traceback........")
            logger = CreateLogger(__name__, app.config.get('SERVER_LOG'))
            meth = request.method
            url = request.url
            ip_addr = request.remote_addr

            x = traceback.format_exception(type(error), error, error.__traceback__)
            a = "[Url: '%s', Method: '%s', ip_addr: '%s'] === " % (url, meth, ip_addr)
            for i in x:
                a = a + str(i)

            logger.critical(a)

            return common_response(status=500, err_msg='Internal server error')
