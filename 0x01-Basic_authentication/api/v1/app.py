#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

'''
This is used as a check to know what class
of authetication should be run
'''
if os.getenv("AUTH_TYPE") == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()

if os.getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before_request():
    '''
    The before_request: This is a function that aims
    to intercept all incoming request to the server
    it's main role is to alter what has been specfied
    by the programmer before further processing
    Args: None
    Returns: None
    '''
    if auth is None:
        return
    isPart = auth.require_auth(
        request.path, [
            '/api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/'])
    if isPart is False:
        return
    isAuthorized = auth.authorization_header(request)
    if isAuthorized is None:
        abort(401)
    isCurrentUser = auth.current_user(request)
    if isCurrentUser is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """unauthorized error handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """forbidde error handler
    """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
