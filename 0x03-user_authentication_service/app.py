#!/usr/bin/env python3
from auth import Auth
from flask import Flask, jsonify, request, abort


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def main():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """
    Endpoint to register a new user.

    - Accepts email and password from form data.
    - If the email is already registered, return an error.
    - Otherwise, register the user and return a success message.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        is_user = AUTH.register_user(email=email, password=password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(401)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
