import pytest
from app import init_app


@pytest.fixture(scope="module")
def test_client():
    flask_app = init_app()
    return flask_app.test_client()
