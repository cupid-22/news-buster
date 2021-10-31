from main import app
from main.controllers import user_controller, tag_controller, site_controller
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


@app.route('/add_new_site', methods=['POST', 'GET'])
def add_site():
    try:
        url = 'https://www.programmableweb.com/api/google-trends-altered'
        return jsonify(site_controller.add_site(url))
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/get_all_site', methods=['GET'])
def get_all_site():
    try:
        return jsonify(site_controller.get_all_site())
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/add_new_site_to_user', methods=['POST'])
def add_site_to_user():
    try:
        pass
    except BaseException as B:
        return B


@app.route('/add_new_tag', methods=['POST'])
def add_new_tag():
    try:
        tag_name = 'Sports'
        return jsonify(tag_controller.add_tag(tag_name))

    except AssertionError as asserted:
        return make_response(str(asserted), HTTPStatus.BAD_REQUEST)
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/get_all_tags', methods=['GET'])
def get_all_tags():
    try:
        return jsonify(tag_controller.get_all_tag())
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)
