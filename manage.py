from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth

from closure_service.closure_views import closure_app
from minimal_cover_service.minimal_cover_views import minimal_cover_app
from common_utils.http_util import *

app = Flask(__name__)
auth = HTTPBasicAuth()
app.register_blueprint(closure_app)
app.register_blueprint(minimal_cover_app)


@app.route('/')
def hello_world():
    return render_template("API3.html")


@auth.error_handler
def unauthorized():
    message = "Unauthorized access"
    return common_result(401, False, message, None)


@app.errorhandler(404)
def not_service(error):
    message = "NOT FOUND"
    print(error)
    return common_result(404, False, message, None)


@app.errorhandler(400)
def input_err(error):
    message = "Invalid data!"
    print(error)
    return common_result(400, False, message, None)


@app.errorhandler(500)
def intern_err(error):
    message = "Internal error!"
    return common_result(500, False, message, None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
