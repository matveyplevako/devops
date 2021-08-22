import pytest
from fastapi.testclient import TestClient

from app_python.main import app


@pytest.fixture()
def test_client():
    return TestClient(app)
