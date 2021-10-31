from main import app
from main.controllers import user_controller
from flask import make_response, jsonify, request
from http import HTTPStatus


@app.route('/get_all_user', methods=['GET'])
def get_all_user():
    try:
        return jsonify(user_controller.get_all_user())
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/add_new_user', methods=['POST', 'GET'])
def add_user():
    try:
        user_object = {
            "name": "G_M",
            "email": "email1@email.com",
        }
        return jsonify(user_controller.add_user(user_object))
    except AssertionError as asserted:
        return make_response(str(asserted), HTTPStatus.BAD_REQUEST)
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/add_new_site', methods=['POST'])
def add_site():
    try:
        pass
    except BaseException as B:
        return B


@app.route('/add_new_site_to_user', methods=['POST'])
def add_site_to_user():
    try:
        pass
    except BaseException as B:
        return B
