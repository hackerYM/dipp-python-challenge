"""
Testing module for building session scope
"""
import os
import pytest

from app.app import create_app


@pytest.fixture(scope="session")
def app():
    """
    Method to build the Flask application
    """
    os.environ["FLASK_ENV"] = "test"
    return create_app()


@pytest.fixture(scope="session")
def client(app):
    """
    Method to build the test client
    """
    return app.test_client()
