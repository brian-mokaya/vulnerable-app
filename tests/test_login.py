from fastapi.testclient import TestClient

from app.main import app


def test_login_succeeds(monkeypatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "demo://connected")

    with TestClient(app) as client:
        response = client.post(
            "/login",
            json={"username": "demo", "password": "secret"},
        )

    assert response.status_code == 200
    assert response.json() == {
        "message": "login successful",
        "user": "demo",
    }
