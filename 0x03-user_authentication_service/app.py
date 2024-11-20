#!/usr/bin/env python3
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def main():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    '''
    users: a function when given a form
    will procceed to extract and save
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        is_user = AUTH.register_user(email=email, password=password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
