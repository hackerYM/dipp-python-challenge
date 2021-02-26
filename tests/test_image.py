"""
Testing module for Api Image
"""
import pytest

from flask import current_app
from http import HTTPStatus


@pytest.fixture
def req_data():
    """
    Method to build the request data
    """
    return {
        "font_url": "https://storage.googleapis.com/dipp-massimo-development-fonts/4f2cf2b6b99d96ca.ttf",
        "image_url": "https://storage.googleapis.com/dipp-massimo-development-images/1f1282fef735f349.jpg",
        "text": {
            "content": "Dipp inc, thinking out of how to draw a text on the box.",
            "text_color": "#000000",
            "border_color": "#000000"
        },
        "box": {
            "x": 40,
            "y": 100,
            "width": 500,
            "height": 500
        }
    }


def test_api_image_with_square_box(snapshot, client, req_data):
    """
    HAPPY: Should draw a text box with a square box
    """
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.OK
    snapshot.assert_match(response.get_json()["splits"])


def test_api_image_with_vertical_rectangle(snapshot, client, req_data):
    """
    HAPPY: Should draw a text box with a vertical rectangle box
    """
    req_data["box"]["width"] = 100
    req_data["box"]["height"] = 1000
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.OK
    snapshot.assert_match(response.get_json()["splits"])


def test_api_image_with_horizontal_rectangle(snapshot, client, req_data):
    """
    HAPPY: Should draw a text box with a horizontal rectangle box
    """
    req_data["box"]["width"] = 1000
    req_data["box"]["height"] = 100
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.OK
    snapshot.assert_match(response.get_json()["splits"])


def test_api_image_with_super_long_content(snapshot, client, req_data):
    """
    HAPPY: Should draw a text box with a super long content
    """
    req_data["text"]["content"] = "draw the text box with a super long content " * 10
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.OK
    snapshot.assert_match(response.get_json()["splits"])


def test_400_by_small_box(snapshot, client, req_data):
    """
    SAD: Should get the 400 error by the small box size
    """
    req_data["box"]["width"] = 10
    req_data["box"]["height"] = 10
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    snapshot.assert_match(response.get_json())


def test_400_by_wrong_width(snapshot, client, req_data):
    """
    SAD: Should get the 400 error by the wrong width
    """
    req_data["box"]["width"] = -100
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    snapshot.assert_match(response.get_json())


def test_400_by_wrong_height(snapshot, client, req_data):
    """
    SAD: Should get the 400 error by the wrong height
    """
    req_data["box"]["height"] = -100
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    snapshot.assert_match(response.get_json())


def test_400_by_wrong_text_color(snapshot, client, req_data):
    """
    SAD: Should get the 400 error by the wrong text color
    """
    req_data["text"]["text_color"] = "no-hex-code"
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    snapshot.assert_match(response.get_json())


def test_400_by_wrong_image_url(snapshot, client, req_data):
    """
    SAD: Should get the 400 error by the wrong image url
    """
    req_data["image_url"] = "no-image-url"
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    snapshot.assert_match(response.get_json())


def test_400_by_ghost_image_url(snapshot, client, req_data):
    """
    SAD: Should get the 400 error by the ghost image url
    """
    req_data["image_url"] = "https://storage.googleapis.com/dipp-massimo-development-images/no-found.jpg"
    response = client.post(f"{current_app.config['API_BASE_PATH']}draw", json=req_data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    snapshot.assert_match(response.get_json())
