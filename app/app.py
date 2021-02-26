"""
Module for managing Flask app's init functions
"""
import os
import logging
import colorlog

from time import time
from http import HTTPStatus
from flask import Flask, request, jsonify, abort, g
from flask.helpers import locked_cached_property

from config.config import ConfigName, get_config
from app.controllers.index import bp_index
from app.controllers.image import bp_image

from werkzeug.exceptions import default_exceptions


class MyFlask(Flask):
    """
    Class for Flask application with custom function
    """
    @locked_cached_property
    def logger(self):
        """
        Method to use the logging formatter for colored output
        """
        logging.getLogger("werkzeug").setLevel(logging.CRITICAL)  # disable the original logging

        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(asctime)s - [%(levelname)s] %(message)s"))

        super().logger.handlers = [handler]
        super().logger.setLevel(logging.DEBUG)

        if self.debug:
            super().logger.setLevel(logging.INFO)

        if self.testing:
            super().logger.setLevel(logging.CRITICAL)

        return super().logger


def create_app():
    """
    Method to init and set up the Flask application
    """
    flask_app = MyFlask(import_name="dipp_app")

    _init_config(flask_app)
    _setup_context(flask_app)

    _register_blueprint(flask_app)
    _register_api_error(flask_app)

    return flask_app


def _init_config(app):
    """
    Method to initialize the configuration
    """
    env = os.getenv("FLASK_ENV", ConfigName.DEV.value)
    app.config.from_object(get_config(env))


def _setup_context(app):
    """
    Method to set up the context in the Flask application
    """
    @app.before_request
    def _log_requests_info():
        """
        Method to logging the client requests info
        """
        if request.method == "OPTIONS":
            return

        g.start = time()
        req_size = int(request.headers.get("Content-Length", 0)) / 1024
        app.logger.info(f'-- "{request.method} {request.path}" - {request.remote_addr} - {req_size:.2f} kb --')

        if request.data and not request.is_json:
            abort(HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

        app.logger.debug(request.json)

    @app.after_request
    def _log_response_info(response):
        """
        Method to logging the server response info
        """
        if request.method == "OPTIONS":
            return response

        app.logger.debug(response.json)
        app.logger.info(f'-- "{request.method} {request.path}" - {response.status} - {time() - g.start:.2f} sec --')

        return response


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
