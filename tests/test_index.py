"""
Testing module for Api Index
"""
from flask import current_app
from http import HTTPStatus


def test_api_index(client):
    """
    HAPPY: Should get the index of api server
    """
    response = client.get(current_app.config["API_BASE_PATH"])
    json_resp = response.get_json()

    assert response.status_code == HTTPStatus.OK
    assert json_resp["code"] == HTTPStatus.OK


def test_404_error(client):
    """
    SAD: Should get the 404 error
    """
    response = client.get("/")
    json_resp = response.get_json()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert json_resp["code"] == HTTPStatus.NOT_FOUND


def test_405_error(client):
    """
    SAD: Should get the 405 error
    """
    response = client.post(current_app.config["API_BASE_PATH"])
    json_resp = response.get_json()

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert json_resp["code"] == HTTPStatus.METHOD_NOT_ALLOWED
