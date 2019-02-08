from flask import make_response, jsonify, request, redirect, url_for

from flask_app import app
from repository import *


@app.route("/")
def home():
    return make_response(jsonify({
        "msg": "Hello"
    }), 200)


@app.route("/ping")
def ping():  # application health checker endpoint
    return "pong"


@app.route("/user", methods=["GET", "POST"])
def user_route():
    if request.method == "GET":
        users = get_all_users()
        return make_response(jsonify(
            users
        ), 200)
    elif request.method == "POST":
        if not request.is_json:
            return make_response(jsonify({
                "error": {
                    "msg": "JSON data is expected but not found"
                }
            }), 400)

        try:
            data: Dict = request.get_json()
        except Exception as ex:
            return make_response(jsonify({
                "error": {
                    "msg": str(ex)
                }
            }), 400)

        name, email, password = data.get("name"), data.get("email"), data.get("password")
        if any(item is None for item in [name, email, password]):
            return make_response(jsonify({
                "error": {
                    "msg": "name, email, password are mandatory field"
                }
            }), 400)

        user = add_new_user(name, email, password)
        if isinstance(user, Error):
            return make_response(jsonify({
                "error": {
                    "msg": user.msg
                }
            }), user.status_code)

        return make_response(jsonify(
            user.to_json()
        ), 201)


@app.route("/user/<int:id>")
def ind_user(id: int):
    user = search_user_with_id(id)
    if not user:
        return make_response(jsonify({
            "error": {
                "msg": "user not found"
            }
        }), 404)

    return make_response(jsonify(
        user.to_json()
    ), 200)


@app.route("/user/login", methods=["POST"])
def user_login():
    if request.method == "GET":
        users = get_all_users()
        return make_response(jsonify(
            users
        ), 200)
    elif request.method == "POST":
        if not request.is_json:
            return make_response(jsonify({
                "error": {
                    "msg": "JSON data is expected but not found"
                }
            }), 400)

        try:
            data: Dict = request.get_json()
        except Exception as ex:
            return make_response(jsonify({
                "error": {
                    "msg": str(ex)
                }
            }), 400)

        email, password = data.get("email"), data.get("password")
        if any(item is None for item in [email, password]):
            return make_response(jsonify({
                "error": {
                    "msg": "email, password are mandatory field"
                }
            }), 400)

        user = check_credentials(email, password)
        if not user:
            return make_response(jsonify({
                "error": {
                    "msg": "invalid email, password combination"
                }
            }), 403)

        return redirect(url_for("ind_user", id=user.id))
