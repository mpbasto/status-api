import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestMain:
    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy", "version": "0.1.0"}

    def test_info(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("APP_ENV", "test")
        response = client.get("/info")
        assert response.status_code == 200
        assert response.json()["app"] == "status-api"
        assert response.json()["version"] == "0.1.0"
        assert response.json()["environment"] == "test"

    def test_info_default(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.delenv("APP_ENV", raising=False)

        response = client.get("/info")

        assert response.status_code == 200
        assert response.json()["environment"] == "development"
