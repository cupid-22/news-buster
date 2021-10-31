from main import app
from main.controllers import user_controller, tag_controller, site_controller, user_news_auth_controller
from flask import make_response, jsonify, request
from http import HTTPStatus


@app.route('/get_all_user', methods=['GET'])
def get_all_user():
    try:
        return jsonify(user_controller.get_all_user())
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/add_new_user', methods=['POST'])
def add_user():
    try:
        request_data = request.get_json()
        name = request_data.get('name')
        email = request_data.get('email')

        return jsonify(user_controller.add_user(name=name, email=email))

    except AssertionError as asserted:
        return make_response(str(asserted), HTTPStatus.BAD_REQUEST)
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/add_new_site', methods=['POST'])
def add_site():
    try:
        request_data = request.get_json()
        url = request_data.get('url')
        return jsonify(site_controller.add_site(url))

    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/get_all_site', methods=['GET'])
def get_all_site():
    try:
        return jsonify(site_controller.get_all_site())
    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)


@app.route('/add_new_tag', methods=['POST'])
def add_new_tag():
    try:
        request_data = request.get_json()
        tag_name = request_data.get('tag_name')
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


@app.route('/user/mail/<int:n_mail_id>/mail_approval/<bool:is_authentic>', methods=['GET'])
def get_all_tags(n_mail_id, is_authentic):
    try:
        return jsonify(user_news_auth_controller.add_users_response(id=n_mail_id, status=is_authentic))

    except BaseException as B:
        return make_response(str(B), HTTPStatus.INTERNAL_SERVER_ERROR)
