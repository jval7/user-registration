import pytest

from app import create_app, init_db


@pytest.fixture
def app():
    app = create_app()

    with app.app_context():
        init_db()

    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
