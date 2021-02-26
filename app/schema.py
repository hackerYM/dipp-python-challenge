"""
Module to handle the json parser
"""
import wrapt

from flask import request
from typing import Callable
from app.result import Response
from jsonschema import Draft7Validator


url_link_regex = r"(http|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
hex_code_regex = r"#([a-fA-F0-9]{6}|[a-fA-F0-9]{8})$"

draw_schema = {
    "type": "object",
    "properties": {
        "font_url":     {"type": "string", "pattern": url_link_regex},
        "image_url":    {"type": "string", "pattern": url_link_regex},
        "text": {
            "type": "object",
            "properties": {
                "content":      {"type": "string"},
                "text_color":   {"type": "string", "pattern": hex_code_regex},
                "border_color": {"type": "string", "pattern": hex_code_regex},
            },
            "required": ["content", "text_color", "border_color"],
        },
        "box": {
            "type": "object",
            "properties": {
                "x":        {"type": "integer", "minimum": 0, "maximum": 10000},
                "y":        {"type": "integer", "minimum": 0, "maximum": 10000},
                "width":    {"type": "integer", "minimum": 0, "maximum": 10000},
                "height":   {"type": "integer", "minimum": 0, "maximum": 10000},
            },
            "required": ["x", "y", "width", "height"],
        },
    },
    "additionalProperties": False,
}


def schema_validate(data_schema: dict):
    """
    The decorator that validating one json schema
    """
    @wrapt.decorator
    def wrapper(wrapped_func: Callable, _, args, kwargs):
        """
        Method to apply wrapt library to simply use the decorator
        """
        validator = Draft7Validator(data_schema)
        errors = sorted(validator.iter_errors(request.get_json(force=True)), key=lambda e: e.path)

        if errors:
            message = [f"{list(error.path)} / {error.message}" for error in errors]
            return Response(code=400, message=message).raise_exception()
        else:
            return wrapped_func(*args, **kwargs)

    return wrapper
