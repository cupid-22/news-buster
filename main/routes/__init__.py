from flask import render_template, make_response
from main import app
from http import HTTPStatus


@app.route('/')
def show_the_default_page():
    try:
        return make_response(render_template('SETDEFAULT.html'), HTTPStatus.OK)
    except BaseException as B:
        return B


@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found(*args):
    """Page not found."""
    return make_response(render_template("HTTP404.html"), HTTPStatus.NOT_FOUND)


@app.errorhandler(HTTPStatus.BAD_REQUEST)
def bad_request(*args):
    """Bad request."""
    return make_response(render_template("HTTP400.html"), HTTPStatus.BAD_REQUEST)


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def server_error(*args):
    """Internal server error."""
    return make_response(render_template("HTTP500.html"), HTTPStatus.INTERNAL_SERVER_ERROR)


from .configurable import *
