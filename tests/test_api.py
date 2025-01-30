from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI template"}


def test_create_item():
    response = client.post(
        "/api/v1/items/", json={"title": "Test Item", "description": "Test Description"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Item"
