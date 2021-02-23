"""
Module to handle the error responses
"""
from flask import make_response, jsonify, abort


class Response:
    """
    Class to handle the error responses
    """
    def __init__(self, code: int, message):

        self.code = code
        self.message = message

    def raise_exception(self):
        """
        Method to throw one Http exception immediately
        """
        json_resp = {
            "code": self.code,
            "message": self.message,
        }

        abort(make_response(jsonify(json_resp), self.code))
