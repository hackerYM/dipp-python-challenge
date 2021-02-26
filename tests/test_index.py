"""
Testing module for Api Index
"""
from flask import current_app
from http import HTTPStatus


def test_api_index(snapshot, client):
    """
    HAPPY: Should get the index of api server
    """
    response = client.get(current_app.config["API_BASE_PATH"])

    assert response.status_code == HTTPStatus.OK
    snapshot.assert_match(response.get_json())


def test_404_error(snapshot, client):
    """
    SAD: Should get the 404 error
    """
    response = client.get("/")

    assert response.status_code == HTTPStatus.NOT_FOUND
    snapshot.assert_match(response.get_json())


def test_405_error(snapshot, client):
    """
    SAD: Should get the 405 error
    """
    response = client.post(current_app.config["API_BASE_PATH"])

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    snapshot.assert_match(response.get_json())
