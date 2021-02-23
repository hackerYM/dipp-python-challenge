"""
Module for managing Flask app's init functions
"""
import os
from http import HTTPStatus
from flask import Flask, jsonify

from config.config import ConfigName, get_config
from app.controllers.index import bp_index
from app.controllers.image import bp_image

from werkzeug.exceptions import default_exceptions


def create_app():
    """
    Method to init and set up the Flask application
    """
    flask_app = Flask(import_name="dipp_app")

    _init_config(flask_app)
    _register_blueprint(flask_app)
    _register_api_error(flask_app)

    return flask_app


def _init_config(app):
    """
    Method to initialize the configuration
    """
    env = os.getenv("FLASK_ENV", ConfigName.DEV.value)
    app.config.from_object(get_config(env))


def _register_blueprint(app):
    """
    Method to register the blueprint
    """
    prefix = app.config["API_BASE_PATH"]

    app.register_blueprint(bp_index, url_prefix=prefix)
    app.register_blueprint(bp_image, url_prefix=prefix)


def _register_api_error(app):
    """
    Method to register the api error
    """
    def _custom_http_error(error):
        """
        Method to build the custom format of http error
        """
        messages = {v: v.description for v in HTTPStatus.__members__.values()}
        json_response = {
            "code": error.code,
            "message": messages[error.code],
        }

        return jsonify(json_response), error.code

    for exc in default_exceptions:
        app.register_error_handler(exc, _custom_http_error)
